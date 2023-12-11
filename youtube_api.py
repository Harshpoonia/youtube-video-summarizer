from googleapiclient.discovery import build

API_KEY = 'YOUR_API_KEY'

def get_video_details(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(
        part='snippet',
        id=video_id
    )
    response = request.execute()
    return response['items'][0] if response['items'] else None
