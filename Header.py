import json
with open("insulin1.json", "rb") as f:
    data = json.load(f)
    
for key, value in data.items():
    print(key, value)
