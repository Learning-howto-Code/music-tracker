import subprocess

def now_playing_music():
    script = '''
    tell application "Spotify"
        if player state is playing then
            return (name of current track) & " — " & (artist of current track)
        end if
    end tell
    '''
    return subprocess.run(["osascript", "-e", script],
                          capture_output=True, text=True).stdout.strip()

print(now_playing_music())
