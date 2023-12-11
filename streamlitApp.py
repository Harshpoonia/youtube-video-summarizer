import streamlit as st
from googleapiclient.discovery import build
from transformers import pipeline
from gtts import gTTS
import os

# YouTube API Key - Replace with your API key
API_KEY = "AIzaSyBS0Xeh4p4J1mPCOFK_FsIIP-jfZu6teIU"

# Function to extract video ID from the YouTube link
def extract_video_id(link):
    # Your code to extract video ID
    # ...

# Function to fetch video details based on the video ID
def fetch_video_details(video_id):
    # Your code to fetch video details
    # ...

# Function to summarize text
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary_text = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    return summary_text

# Function to convert text to speech and save as an MP3 file
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")

# Streamlit app
def main():
    st.title("YouTube Video Summarizer & Speech Generator")

    youtube_link = st.text_input("Enter YouTube video link:")

    if st.button("Generate Speech"):
        if youtube_link:
            video_id = extract_video_id(youtube_link)
            if video_id:
                video_details = fetch_video_details(video_id)
                video_text = video_details['items'][0]['snippet']['description']  # Adjust this to get the relevant text

                # Summarize text
                summary = summarize_text(video_text)

                # Convert summary to speech and save as MP3
                text_to_speech(summary)
                
                st.audio("output.mp3", format='audio/mp3')
            else:
                st.write("Invalid YouTube link provided.")
        else:
            st.write("Please enter a YouTube video link.")

if __name__ == "__main__":
    main()
