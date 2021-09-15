from googleapiclient.discovery import build
from dotenv import load_dotenv
import os


videos = []


load_dotenv()
YT_API_KEY = os.getenv('YOUTUBE_API_KEY')

youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

nextPageToken = None


while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId='PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p',
        maxResults=50,
        pageToken=nextPageToken,
    )
    playlist_response = pl_request.execute()


    video_ids = []
    for item in playlist_response['items']:
        video_ids.append(item['contentDetails']['videoId'])

    video_request = youtube.videos().list(
        part='statistics',
        id=','.join(video_ids)
    )
    video_response = video_request.execute()

    for item in video_response['items']:
        video_views = item['statistics']['viewCount']
        
        video_id = item['id']
        yt_link = f'https://youtu.be/{video_id}'
        

        videos.append(
            {
                'views': int(video_views),
                'url': yt_link,
            }
        )

    nextPageToken = playlist_response.get('nextPageToken')

    if not nextPageToken:
        break

       
videos.sort(key=lambda vid: vid['views'], reverse=True) # highest view first

for video in videos[:10]: # this [:10] slicing will return top 10 vids instead of the total o/p
    print(video['url'], video['views'])

print(len(videos))    

