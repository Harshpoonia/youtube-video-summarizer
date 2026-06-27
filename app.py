import streamlit as st
from modules.transcript import get_transcript
from modules.learning_service import LearningService
from utils.markdown_parser import parse_learning_content
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

        try:
            with st.spinner("Fetching transcript..."):
                transcript_data = get_transcript(youtube_url)

            learning_service = LearningService()

            with st.spinner("🤖 Gemini is analyzing the transcript..."):
                learning_content = learning_service.generate_learning_content(transcript_data)
                

            sections = parse_learning_content(learning_content)
            

            st.success("✅ Video analyzed successfully! Transcript extracted and AI summary generated.")
            
            language = transcript_data.language.replace(
                " (auto-generated)",
                ""
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "📝 Words",
                f"{transcript_data.word_count:,}"
            )

            col2.metric(
                "🌐 Language",
                language
            )

            col3.metric(
                "📖 Reading Time",
                f"{transcript_data.estimated_reading_time} min"
            )

            col4, col5 = st.columns(2)

            col4.metric(
                "🔤 Characters",
                f"{transcript_data.character_count:,}"
            )

            transcript_type = (
                "Auto Generated"
                if "auto" in transcript_data.language.lower()
                else "Manual"
            )

            col5.metric(
                "📄 Transcript",
                transcript_type
            )
            
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📄 Transcript", 
                "📝 Summary", 
                "📌 Key Points", 
                "📚 Study Notes",
                "🧠 Concepts"
                ])

            with tab1:
                st.text_area(
                    "Transcript",
                    transcript_data.transcript,
                    height=450
                )

            with tab2:
                st.markdown(
                    sections.get(
                        "Executive Summary",
                        "Not available.")
                )
            
            with tab3:
                st.markdown(
                    sections.get(
                        "Key Points",
                        "Not available."  ) 
                )    
            
            with tab4:
                st.markdown(
                    sections.get(
                        "Study Notes",
                        "Not available."
                    )
                )

            with tab5:
                st.markdown(
                    sections.get(
                        "Important Concepts",
                        "Not available."
                    )
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

    else:

        st.warning("⚠️ Please enter a YouTube URL.")