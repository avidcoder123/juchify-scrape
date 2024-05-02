import requests
import json

def getPage(page):
    res = requests.get(f"https://juchify.com/api/v1/channel/3?returnContentOnly=true&restriction=&order=popularity:desc&paginate=simple&perPage=50&query=&page={page}")
    return json.loads(res.text)

print(getPage(1))