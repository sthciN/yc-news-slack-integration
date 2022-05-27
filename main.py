from send_message import yc_news_send_message
from dotenv import find_dotenv, load_dotenv


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

if __name__ == '__main__':
    yc_news_send_message()