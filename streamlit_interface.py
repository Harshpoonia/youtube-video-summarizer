import streamlit as st
from youtube_api import get_video_details

def extract_video_id(link):
    # Extract video ID from the YouTube link
    # Example: https://www.youtube.com/watch?v=VIDEO_ID
    parts = link.split("?v=")
    if len(parts) > 1:
        video_id = parts[1].split("&")[0]
        return video_id
    return None

def main():
    st.title("YouTube Video Summarizer")

    youtube_link = st.text_input("Enter YouTube video link:")
    video_id = extract_video_id( https://www.youtube.com/watch?v=jV1vkHv4zq8)
   
   

    if st.button("Fetch Video Details"):
        if youtube_link:
            details = get_video_details(video_id)
            if details:
                st.success("Video Details Fetched:")
                st.write("Title:", details['snippet']['title'])
                st.write("Channel:", details['snippet']['channelTitle'])
                st.write("Description:", details['snippet']['description'])
                # Add more video details as needed
            else:
                st.error("No details found for the given video.")
        else:
            st.warning("Please enter a YouTube video link.")

if __name__ == "__main__":
    main()
