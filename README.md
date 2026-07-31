# Summary
Noted is a python backend that keeps track of all the music played on your mac, across spotify, apple music, youtube, and other brower based streamers, using Apple's media controls. Using raw json, your data is 100% yours forever, stored on your computer, and never stored on the cloud. Noted also runs a MCP server that allows for data integration with llm's, allowing your music data to be used in countless ways, from visualization of trends to my favorite featre; Music recomendations that understand your tastes better than anyone, and aren't tainted by preserving spotify's bottom line. And of course under an MIT license, the source code is fully open source for modification and improvement. 

# Features
Apart from plain data logging, Noted's MCP server allows your favorite llm to inteligently query your data intead loading 10's of thousands of tokens, giving you better results and saving you tokens. 
# Supported apps

- Spotify
- Apple Music
- Web browsers(though they are not enabled by default to keep videos out of your data)
- Make a pr/ issue if you want something else added!

# Motive
As someone that listens to toooons of music, I fouund that spotify was feeding me the same 50 songs over and over and I know I'm not the only one. I dislike/ have little experience making frontends though, as I have a impossible time making them look good at all, and also wanted to expirement with creating my own mcp servers, after using many premade ones. 

# Tech stack
- To get the actual now playing data from my mac, I used the nowplaying-cli, a great cli that exposes appl'es music controls
- For better genre classification and indexing, I used an llm from openrouter using the ai.hackclub.com wrapper for free usage. Any llm provider would work here though. 
- For the MCP server, I used FastMCP, as it seemed like a solid simple option for my very simple server.
- For the llm to connect to the server, I went with claude, as I have claude pro.

# Install
* Please note that due to the core architechture of this project, it fundementally only works on macs.  
1. Clone the repo "git clone https://github.com/Learning-howto-Code/noted"


# AI statement
Claude was consulted for explaining errors, asking how to do things, and general educational assitance, though all of the code is hand written by me. This readme was properly formatted with claude to, though every single word is mine. 
