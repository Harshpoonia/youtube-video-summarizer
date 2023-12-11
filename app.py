import streamlit as st
from youtube_util import get_video_id
from text_summarization import summarize_text
from text_to_speech import text_to_speech

# Your YouTube API Key and other functions...

def main():
    st.title("YouTube Video Summarizer")

    st.markdown("<p class='title'>YouTube Video Summarizer</p>", unsafe_allow_html=True)

    youtube_link = st.text_input("Enter YouTube video link:", key='youtube_link')
    video_id = get_video_id(youtube_link) if youtube_link else None

    if st.button("Summarize and Convert to Speech"):
        if video_id:
            transcript = get_transcript(video_id)
            if transcript:
                # Summarize the fetched transcript
                summary = summarize_text(transcript)

                # Convert summarized text to speech in English
                text_to_speech(summary)

                st.success("Summarization and Conversion completed. Click below to listen.")
                st.audio("output.mp3", format='audio/mp3')
            else:
                st.warning("Transcript not found for this video.")
        else:
            st.warning("Please enter a valid YouTube video link.")

if __name__ == "__main__":
    main()
