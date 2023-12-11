import streamlit as st
from youtube_api import get_video_details
from text_summarization import summarize_text
from text_to_speech import text_to_speech, translate_text

def extract_video_id(link):
    # Extract video ID from the YouTube link
    # Example: https://www.youtube.com/watch?v=VIDEO_ID
    parts = link.split("?v=jV1vkHv4zq8")
    if len(parts) > 1:
        video_id = parts[1].split("&")[0]
        return video_id
    return None

def main():
    st.title("YouTube Video Summarizer")

    # Link external CSS file
    st.markdown(
        """
        <link href="styles.css" rel="stylesheet">
        """,
        unsafe_allow_html=True
    )

    st.markdown("<p class='title'>YouTube Video Summarizer</p>", unsafe_allow_html=True)

    youtube_link = st.text_input("Enter YouTube video link:", key='youtube_link', class='text-input')
    video_id = extract_video_id(youtube_link)

    target_language = st.selectbox("Select Target Language", ["English", "Spanish", "French"], key='target_language')

    if st.button("Summarize and Convert to Speech", class='button'):
        if youtube_link:
            # Fetch video transcript or content from YouTube API
            video_content = get_video_details(video_id)  # Replace with actual fetched data from YouTube API

            # Summarize the video content
            summary = summarize_text(video_content)

            # Translate summarized text to the selected language
            translated_summary = translate_text(summary, target_language.lower())

            # Convert translated text to speech in English
            text_to_speech(translated_summary)

            st.success("Summarization and Conversion completed. Click below to listen.")
            st.audio("output.mp3", format='audio/mp3')

        else:
            st.warning("Please enter a YouTube video link.")

if __name__ == "__main__":
    main()
