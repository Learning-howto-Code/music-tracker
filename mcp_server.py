from time import time
from pathlib import Path    
from mcp.server.fastmcp import FastMCP
import json
from datetime import date, datetime
from typing import Annotated, Literal
from pydantic import Field
from collections import Counter

history_file =  Path(__file__).parent / "history.json"
mcp = FastMCP("Music Tracker")
@mcp.tool()
def search_in_range(# searches logs for all songs within a specified date range
    start: Annotated[date, Field(description="Start of the lookup window, ISO 8601 (YYYY-MM-DD). Inclusive.")],
    end: Annotated[date, Field(description="End of the lookup window, ISO 8601 (YYYY-MM-DD). Inclusive.")],
) -> list[dict]:
    """Return every listening-history entry played between start and end, inclusive."""
    global entry
    if end < start:
        raise ValueError("end must be on or after start")
    try:
        with open(history_file, "r") as f:
        
            data = json.load(f)
    except json.JSONDecodeError:
            return "History log seems to be empty"
    matches = []
    for entry in data:
        temp = datetime.fromisoformat(entry["Date"]).date()
        if temp >= start and temp <= end:      
            matches.append(entry)
    return matches 
def most_popular_songs(
    start: Annotated[date, Field(description="Start of the lookup window, ISO 8601 (YYYY-MM-DD). Inclusive.")],
    end: Annotated[date, Field(description="End of the lookup window, ISO 8601 (YYYY-MM-DD). Inclusive.")],     
    threshold: Annotated[int, Field(description="Maximum number of songs to be returned in ranked order of times played. Leave blank to return all songs in ranked order")]=1000000000000
):
     matches, entry = search_in_range(start, end)
     print(entry)
     counts = Counter(entry["Title"] for entry in matches)
     print(threshold)
     top_songs = counts.most_common(threshold)
     return top_songs





if __name__ == "__main__":
    mcp.run()
