from googleapiclient.discovery import build
import re

# Your API key obtained from Google Cloud Console
API_KEY = "<YOUR_API_KEY>"

# Function to extract video ID from the YouTube link
def extract_video_id(link):
    pattern = r"(?<=v=)[\w-]+|(?<=youtu.be/)[\w-]+"
    match = re.search(pattern, link)
    if match:
        return match.group()
    else:
        return None

# Function to fetch video details based on the video ID
def fetch_video_details(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    return response

# Example usage
if __name__ == "__main__":
    youtube_link = "YOUR_YOUTUBE_VIDEO_LINK_HERE"
    video_id = extract_video_id(youtube_link)
    if video_id:
        video_details = fetch_video_details(video_id)
        print(video_details)
    else:
        print("Invalid YouTube link provided.")
