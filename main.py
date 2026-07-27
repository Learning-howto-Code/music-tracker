"""
Plan:
Get song title and artist, query spotify and apple music
Parse output, input into json
loop every 5 seconds, only log on change
"""
from math import inf
import os
import subprocess
from dotenv import load_dotenv # type: ignore
import json
import time
from openrouter import OpenRouter
from pathlib import Path
history_file =  Path(__file__).parent / "history.json"
load_dotenv()
model = 'inclusionai/ling-3.0-flash:free'

def get_song():
    info = subprocess.run(["nowplaying-cli", "get", "artist", "title", "MediaType", "duration"], capture_output=True, text=True)
    song_dict= info.stdout.strip().split("\n")
    song_dict= dict(zip(["artist", "title", "MediaType", "duration"], song_dict))
    print(song_dict)
    print(song_dict["artist"])
    return song_dict

song_dict = get_song()
def get_song_info(song_dict):

    HCAI = os.getenv("HCAI")
    print("loaded api key")
    client = OpenRouter(
        api_key=HCAI,
        server_url="https://ai.hackclub.com/proxy/v1",
    )
    print("sent response")
    response = client.chat.send(
        model=model,
        messages=[
            {"role": "system", "content": f"You describe the vibe of a song in 8-12 words. Output a comma-separated list of descriptors covering genre, mood, texture, and setting. Do not write a full sentence. Go beyond one-word labels like \"pop\" or \"rock\" — be specific and evocative. If you don't know the song, infer from the artist's typical style. Output only the descriptors. No preamble, no quotes, no trailing period. If you don't know the song, DO NOT GUESS UNDER ANY CIRCUMSTANCES, instead say genre unknown  The song you are describing is {song_dict['title']} by {song_dict['artist']}."},
        ],
        stream=False,
    )
    print(f"message was You describe the vibe of a song in 8-12 words. Output a comma-separated list of descriptors covering genre, mood, texture, and setting. Do not write a full sentence. Go beyond one-word labels like \"pop\" or \"rock\" — be specific and evocative. If you don't know the song, infer from the artist's typical style. Output only the descriptors. No preamble, no quotes, no trailing period.  The song you are describing is {song_dict['title']} by {song_dict['artist']}.")
    print("sent response")
    response = response.choices[0].message.content
    print("got response")
    print(response)
    return response
def log_song(song_dict, response, elapsed_time):
    global current
    with open(history_file, "r")as f:
        try:
            old = json.load(f)
        except json.JSONDecodeError:
            old = []
    if (song_dict["duration"]) == 'null':
        duration = 0
    else:
        duration= float(song_dict["duration"])
    m,s = divmod(int(duration), 60)
    duration = f"{m}:{s:02d}"

    current={
        "Artist": song_dict["artist"],
        "Title": song_dict["title"],
        "Duration": duration,
        "Description": response,
        "Date": time.strftime("%Y-%m-%d %H:%M:", time.localtime()),
        "Played song for(seconds)": elapsed_time
    }


    old.append(current)
    with open(history_file, "w") as i:
        json.dump(old, i, indent=4) 
    # print(info)
current_song=None
old_song= None
elapsed_time = 0
old_song_dict = song_dict
while True:
    song_dict = get_song()
    print(f"got song, song is {song_dict['title']}")
    current_song = song_dict["title"]

    if current_song != old_song or current_song == None:  #When the current song changes, we want to log
        response = get_song_info(song_dict)
        print(f"got response, response is {response}")
        
        log_song(old_song_dict, response, elapsed_time)
        old_song_dict = song_dict
        print("logged song")
        elapsed_time = 0
    elif current_song == old_song:
        print("no change, not logging")
        print(f"current song: {current_song}, old song: {old_song}")
    old_song = current_song
    elapsed_time += 5
    time.sleep(5)
        
