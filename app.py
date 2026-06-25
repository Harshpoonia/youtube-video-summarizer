import streamlit as st

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
        st.success("Video URL received successfully.")
        st.write("Transcript extraction will be implemented next.")
    else:
        st.warning("Please enter a YouTube video URL.")