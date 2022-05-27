import json
import requests

def get_story_by_id(item_id):
    result = {}
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(item_id)
    r = requests.get(url)
    
    if r:
        r = r.text
        r = json.loads(r)
        # Top 1
        result = {'by': r['by'], 'text': r.get('text'), 'title': r['title'], 'url': r['url']}
    
    return result