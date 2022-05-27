import logging
import os

import requests

from item import get_story_by_id
from top_stories import get_top_story_ids
    
logger = logging.getLogger(__name__)

# ID of channel you want to post message to
channel_id = "C03H3V4M2Q3"


def yc_news_send_message():
    try:
        story = []
        top_story_ids = get_top_story_ids(top=1)

        for item_id in top_story_ids:
            story.append(get_story_by_id(item_id))
        
        # Only top 1 
        story = story[0]
        text = story['text'][:400] + '      ' if story['text'] else ''
        text = story['title'] + '\n' + text + '\n' + 'Read More At:   ' + story['url']
        url = os.environ.get('YC_NEWS_SEND_WEBHOOK_URL')
        body = {'text': text}
        requests.post(url, json=body)
        
        return None

    except Exception as e:
        print(f"Error??: {e}")
        