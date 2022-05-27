import json
import requests

def get_top_story_ids(top=10):
    result = []
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    r = requests.get(url)
    
    if r:
        r = r.text
        r = json.loads(r)
        # Top x
        result = r[:top]

    return result