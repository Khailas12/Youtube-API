from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()
YT_API_KEY = os.getenv('YOUTUBE_API_KEY')

youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()
print(response)