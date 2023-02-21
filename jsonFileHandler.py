from fileinput import filename
import json
def readJsonFile():
    data = ""
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
print(readJsonFile)