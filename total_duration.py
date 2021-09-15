from googleapiclient.discovery import build
from dotenv import load_dotenv
from datetime import timedelta
import timeit
import re    # regular expression
import os


def analyzing_time():
    start = timeit.default_timer()
    print(f"Analyzing playlist in: {str(start)} Seconds")
    
    
def main():
    load_dotenv()
    YT_API_KEY = os.getenv('YOUTUBE_API_KEY')


    youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

    nextPageToken = None         

    hours_pattern = re.compile(r'(\d+)H')  # H = hours
    minutes_pattern = re.compile(r'(\d+)M') #\d -> digit
    seconds_pattern = re.compile(r'(\d+)S')

    total_seconds = 0


    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId="PLPN21ZkIRg_oQAFzLalMk4H9nFB32ipHG",
            maxResults=50, 
            pageToken=nextPageToken
        )
        analyzing_time()

        playlist_response = pl_request.execute()

        video_ids = []
        for item in playlist_response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        video_request = youtube.videos().list(
            part='contentDetails', 
            id=','.join(video_ids) 
        )
        video_response = video_request.execute()

        for item in video_response['items']:
            duration = item['contentDetails']['duration']
            
            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = seconds_pattern.search(duration)
            
            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0
            
            video_seconds = timedelta(
                hours = hours,
                minutes = minutes,
                seconds = seconds
            )
            vid_secs = video_seconds.total_seconds()
            
            total_seconds += vid_secs
        
        
        nextPageToken = playlist_response.get('nextPageToken')
        
        if not nextPageToken:
            break

    total_seconds = int(total_seconds)


    # The divmod() is part of python's standard library which takes two numbers as parameters and gives the quotient and remainder of their division as a tupl
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    print(f"\nTotal Time: {hours}H {minutes}M {seconds}S")
    print(f"\nTotal Time: {hours}:{minutes}:{seconds}")