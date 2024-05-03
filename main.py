import requests
import json
import re

# def getPage(page):
#     res = requests.get(f"https://juchify.com/api/v1/channel/3?returnContentOnly=true&restriction=&order=popularity:desc&paginate=simple&perPage=50&query=&page={page}")
#     return json.loads(res.text)

def getSongById(id):
    res = requests.get(f"https://juchify.com/api/v1/tracks/{id}?loader=trackPage")
    return json.loads(res.text)

# songsList = getPage(2)["pagination"]["data"]
# data = getSongById(songsList[0]["id"])
# print(data["src"])
id = 1
song = getSongById(id)
name = song["track"]["name"].replace(" ", "-").lower()
res = requests.get(f"https://juchify.com/track/{id}/{name}").text

print(res)

#TODO: Extract song src from track's page