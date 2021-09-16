from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle
import os


# pickle -> Used to save python objects in a file as bytes and load em back into python using that file.


def auth_user():
    credentials = None
    if os.path.exists("token.pickle"):
        print('Loading credentials from file') # loads from token.pickle file if it exists
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)
    # token.pickle -> it stores the user's credentials from prior succesful logins


    # this will refresh the token or login if there's no valid credentials
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing acess token')
            credentials.refresh(Request())

        else:
            print('Fetching new tokens')
            flow = InstalledAppFlow.from_client_secrets_file(
                r"Yt-Playlist-time-totalizer/OAuth_to_user_accounts/client_secrets.json",
                scopes=["https://www.googleapis.com/auth/youtube.readonly"]
            )   # acessing the json file with secret API keys
    # acc to the link on scopes, it's to View your YouTube account and there are many.


            # print(credentials.to_json())
                
            # consent gives a refresh token while running
            flow.run_local_server(port=8080, prompr='consent',authorization_prompt_message='')

            credentials = flow.credentials

            # save the credentials for next run
            with open("token.pickle", "wb") as f:
                print('saving credentials')
                # The dump() method is used when the Python objects have to be stored in a file. Allows you to convert a python object into JSON
                pickle.dump(credentials, f)


    youtube = build('youtube', 'v3', credentials=credentials)
    request = youtube.playlistItems().list(
    part='status, contentDetails',
    playlistId='PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_'
    )

    response = request.execute()

    for item in response['items']:
        video_id = (item['contentDetails']['videoId'])
        yt_link = f'https://youtu.be/{video_id}'
        print(yt_link)


    # https://developers.google.com/youtube/v3/guides/auth/installed-apps