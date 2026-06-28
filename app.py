import streamlit as st
from modules.transcript import get_transcript
from modules.learning_service import LearningService
from utils.markdown_parser import parse_learning_content
from modules.quiz_service import QuizService

# -----------------------------
# Page Configuration (must be first Streamlit call)
# -----------------------------
st.set_page_config(
    page_title="YouTube AI Learning Assistant",
    page_icon="🎥",
    layout="wide"
)

# -----------------------------
# Session State Initialization
# -----------------------------
if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

if "transcript_data" not in st.session_state:
    st.session_state.transcript_data = None

if "sections" not in st.session_state:
    st.session_state.sections = None

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = None

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📚 Navigation")
st.sidebar.info(
    """
    **Version:** 2.0

    AI-powered learning assistant for YouTube videos.
    """
)

# -----------------------------
# Main Title
# -----------------------------
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

# -----------------------------
# Analyze Button Handler
# -----------------------------
if analyze:
    if not youtube_url:
        st.warning("⚠️ Please enter a YouTube URL.")
    else:
        try:
            learning_service = LearningService()
            quiz_service = QuizService()

            with st.status("🔄 Analyzing your video...", expanded=True) as status:

                st.write("📡 Fetching transcript from YouTube...")
                transcript_data = get_transcript(youtube_url)
                st.write("✅ Transcript fetched successfully!")

                st.write("🧠 Generating AI learning content...")
                learning_content = learning_service.generate_learning_content(transcript_data)
                st.write("✅ Learning content generated!")

                st.write("📝 Parsing sections (summary, key points, notes)...")
                sections = parse_learning_content(learning_content)
                st.write("✅ Sections parsed!")

                st.write("❓ Building quiz questions...")
                quiz_questions = quiz_service.generate_quiz(transcript_data)
                st.write("✅ Quiz ready!")

                status.update(label="✅ Analysis complete!", state="complete", expanded=False)

            # Reset quiz state on new analysis
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.answered = False

            # Save to session state
            st.session_state.transcript_data = transcript_data
            st.session_state.sections = sections
            st.session_state.quiz_questions = quiz_questions
            st.session_state.analysis_complete = True

            st.success("✅ Video analyzed successfully! Transcript extracted and AI summary generated.")

        except Exception as e:
            error_message = str(e)

            if "Subtitles are disabled" in error_message:
                st.error("❌ This video doesn't have captions available. Please choose another video.")
            elif "Invalid YouTube URL" in error_message:
                st.error("❌ Please enter a valid YouTube URL.")
            else:
                st.error("⚠️ Unable to fetch transcript. Please try another video.")
                with st.expander("Developer Details"):
                    st.code(error_message)

# -----------------------------
# Results Display (persists across reruns via session state)
# -----------------------------
if st.session_state.analysis_complete:
    transcript_data = st.session_state.transcript_data
    sections = st.session_state.sections
    quiz_questions = st.session_state.quiz_questions

    language = transcript_data.language.replace(" (auto-generated)", "")

    col1, col2, col3 = st.columns(3)
    col1.metric("📝 Words", f"{transcript_data.word_count:,}")
    col2.metric("🌐 Language", language)
    col3.metric("📖 Reading Time", f"{transcript_data.estimated_reading_time} min")

    col4, col5 = st.columns(2)
    col4.metric("🔤 Characters", f"{transcript_data.character_count:,}")

    transcript_type = (
        "Auto Generated" if "auto" in transcript_data.language.lower() else "Manual"
    )
    col5.metric("📄 Transcript", transcript_type)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📄 Transcript",
        "📝 Summary",
        "📌 Key Points",
        "📚 Study Notes",
        "🧠 Concepts",
        "❓ Quiz",
    ])

    with tab1:
        st.text_area("Transcript", transcript_data.transcript, height=450)

    with tab2:
        st.markdown(sections.get("Executive Summary", "Not available."))

    with tab3:
        st.markdown(sections.get("Key Points", "Not available."))

    with tab4:
        st.markdown(sections.get("Study Notes", "Not available."))

    with tab5:
        st.markdown(sections.get("Important Concepts", "Not available."))

    with tab6:
        st.subheader("📝 AI Generated Quiz")

        if st.session_state.quiz_index >= len(quiz_questions):
            st.success("🎉 Quiz Completed!")
            st.metric("Final Score", f"{st.session_state.quiz_score}/{len(quiz_questions)}")
            percentage = (st.session_state.quiz_score / len(quiz_questions)) * 100
            st.metric("Percentage", f"{percentage:.1f}%")

            if st.button("Restart Quiz"):
                st.session_state.quiz_index = 0
                st.session_state.quiz_score = 0
                st.session_state.answered = False
                st.rerun()

        else:
            progress = st.session_state.quiz_index / len(quiz_questions)
            st.progress(progress)

            question = quiz_questions[st.session_state.quiz_index]

            st.markdown(f"### Question {st.session_state.quiz_index + 1} of {len(quiz_questions)}")
            st.write(question.question)

            selected = st.radio(
                "Choose your answer",
                question.options,
                key=f"q_{st.session_state.quiz_index}"
            )

            if not st.session_state.answered:
                if st.button("Submit Answer"):
                    st.session_state.answered = True
                    if selected == question.answer:
                        st.session_state.quiz_score += 1
                        st.success("✅ Correct!")
                    else:
                        st.error(f"❌ Incorrect.\n\nCorrect Answer: {question.answer}")
                    st.info(question.explanation)
            else:
                st.info(question.explanation)

                if st.button("Next Question"):
                    st.session_state.quiz_index += 1
                    st.session_state.answered = False
                    st.rerun()