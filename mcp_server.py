from time import time
from pathlib import Path    
from mcp.server.fastmcp import FastMCP
import json
from datetime import date
from typing import Annotated, Literal
from pydantic import Field

history_file =  Path(__file__).parent / "history.json"
mcp = FastMCP("Music Tracker")
@mcp.tool()
def search_in_range(
    start: Annotated[date, Field(description="Start of the lookup window, ISO 8601 (YYYY-MM-DD). Inclusive.")],
    end: Annotated[date, Field(description="End of the lookup window, ISO 8601 (YYYY-MM-DD). Inclusive.")],
) -> list[dict]:
    """Return every listening-history entry played between start and end, inclusive."""
    if end < start:
        raise ValueError("end must be on or after start")
    try:
        with open(history_file, "r") as f:
        
            data = json.load(f)
    except json.JSONDecodeError:
            return "History log seems to be empty"
    for data in data:
        if data["Date"]>= start and data["Date"] <= end:
            return data
if __name__ == "__main__":
    mcp.run()
