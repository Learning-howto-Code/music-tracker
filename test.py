import json
start= "2026-07-26 16:03"
end = "2026-07-26 17:00"
def search(start, end):
    

    with open("history.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return "History log seems to be empty"
    for data in data:
        if data["Date"]>= start and data["Date"] <= end:
            print(data)
search(start, end)  
