import streamlit as st
from modules.transcript import get_transcript

# Page Configuration
st.set_page_config(
    page_title="YouTube AI Learning Assistant",
    page_icon="🎥",
    layout="wide"
)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.info(
    """
    **Version:** 2.0

    AI-powered learning assistant for YouTube videos.
    """
)

# Main Title
st.title("🎥 YouTube AI Learning Assistant")

st.markdown(
    """
Turn any YouTube video into an interactive learning experience.

### Features (Coming Soon)
- 📄 Transcript Extraction
- 📝 AI Summary
- 📌 Key Points
- 🔊 Text-to-Speech
- 📄 PDF Notes
- 🤖 AI Chat with Video
"""
)

st.divider()

youtube_url = st.text_input(
    "🔗 Enter YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

analyze = st.button("🚀 Analyze Video", use_container_width=True)

if analyze:

    if youtube_url:

        with st.spinner("Fetching transcript..."):

            try:

                transcript = get_transcript(youtube_url)

                st.success("Transcript extracted successfully!")

                st.subheader("📄 Video Transcript")

                st.text_area(
                    label="Transcript",
                    value=transcript,
                    height=400
                )

            except Exception as e:

                error_message = str(e)

                if "Subtitles are disabled" in error_message:

                    st.error(
                        "❌ This video doesn't have captions available. Please choose another video."
                    )

                elif "Invalid YouTube URL" in error_message:

                    st.error(
                        "❌ Please enter a valid YouTube URL."
                    )

                else:

                    st.error(
                        "⚠️ Unable to fetch transcript. Please try another video."
                    )

                    with st.expander("Developer Details"):

                        st.code(error_message)