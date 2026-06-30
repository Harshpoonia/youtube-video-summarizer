"""
app.py

Streamlit UI for the YouTube AI Learning Assistant.

Responsible ONLY for:
- Rendering UI
- Managing Streamlit session state
- Calling services (modules/)
- Displaying results

This file must never contain AI prompt logic or Gemini response
parsing — that all lives in modules/ and utils/.
"""

import streamlit as st

from config import settings
from modules.ai_service import AIService, AIServiceError
from modules.flashcard_service import FlashcardService
from modules.learning_service import LearningService
from modules.quiz_service import QuizService
from modules.transcript import TranscriptError, fetch_transcript

st.set_page_config(
    page_title=settings.app_title,
    page_icon="🎓",
    layout="wide",
)


# ---------------------------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------------------------

def init_session_state() -> None:
    defaults = {
        "analysis_complete": False,
        "transcript_data": None,
        "learning_content": None,
        "quiz_questions": None,
        "quiz_index": 0,
        "quiz_score": 0,
        "answered": False,
        "selected_option": None,
        "flashcards": None,
        "flashcard_index": 0,
        "flashcard_flipped": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_for_new_video() -> None:
    st.session_state.analysis_complete = False
    st.session_state.transcript_data = None
    st.session_state.learning_content = None
    st.session_state.quiz_questions = None
    st.session_state.quiz_index = 0
    st.session_state.quiz_score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.flashcards = None
    st.session_state.flashcard_index = 0
    st.session_state.flashcard_flipped = False


# ---------------------------------------------------------------------------
# Service Instantiation (cached so we don't reconnect every rerun)
# ---------------------------------------------------------------------------

@st.cache_resource
def get_ai_service() -> AIService:
    return AIService()


def get_learning_service() -> LearningService:
    return LearningService(ai_service=get_ai_service())


def get_quiz_service() -> QuizService:
    return QuizService(ai_service=get_ai_service())


def get_flashcard_service() -> FlashcardService:
    return FlashcardService(ai_service=get_ai_service())


# ---------------------------------------------------------------------------
# Pipeline: Extraction + Generation (runs once, then cached in session state)
# ---------------------------------------------------------------------------

def run_pipeline(youtube_url: str, num_quiz_questions: int, num_flashcards: int) -> None:
    progress = st.progress(0, text="Starting…")

    try:
        progress.progress(10, text="Fetching transcript…")
        transcript_data = fetch_transcript(youtube_url)
        st.session_state.transcript_data = transcript_data

        progress.progress(40, text="Generating learning content with Gemini…")
        learning_content = get_learning_service().generate_learning_content(transcript_data)
        st.session_state.learning_content = learning_content

        progress.progress(70, text="Generating quiz questions…")
        quiz_questions = get_quiz_service().generate_quiz(
            transcript_data, num_questions=num_quiz_questions
        )
        st.session_state.quiz_questions = quiz_questions

        progress.progress(90, text="Generating flashcards…")
        flashcards = get_flashcard_service().generate_flashcards(
            transcript_data, num_cards=num_flashcards
        )
        st.session_state.flashcards = flashcards

        progress.progress(100, text="Done!")
        st.session_state.analysis_complete = True

    except TranscriptError as exc:
        progress.empty()
        _render_error_card(
            "Transcript Error",
            str(exc),
            "Please verify the YouTube URL and try again.",
        )
    except (AIServiceError, ValueError) as exc:
        progress.empty()
        title, help_text = _classify_ai_error(exc)
        _render_error_card(title, str(exc), help_text)
    except Exception as exc:  # noqa: BLE001 - last line of defense for the UI
        progress.empty()
        _render_error_card(
            "Unexpected Error",
            str(exc),
            "Please retry or check the app logs for more details.",
        )


def _classify_ai_error(exc: AIServiceError | ValueError) -> tuple[str, str]:
    if isinstance(exc, AIServiceError):
        if getattr(exc, "code", None) == "quota_exhausted":
            return (
                "Gemini Quota Exhausted",
                "Your Gemini quota has been exceeded. Check API limits or switch plans."
                " If you continue to see this, wait a few minutes and retry.",
            )
        if getattr(exc, "code", None) == "unauthenticated":
            return (
                "Gemini Authentication Error",
                "Authentication to Gemini failed. Check your GEMINI_API_KEY, .env file,"
                " and ensure your credentials are correctly configured.",
            )
        if getattr(exc, "code", None) == "rate_limited":
            return (
                "Gemini Rate Limited",
                "Gemini is temporarily rate-limiting requests. Retry after a short wait.",
            )
        if getattr(exc, "code", None) == "empty_response":
            return (
                "Gemini Returned No Content",
                "We received an empty response from Gemini. Please retry the request.",
            )
    return (
        "AI Generation Error",
        "There was a problem generating content. Try again or check your Gemini configuration.",
    )


def _render_error_card(title: str, message: str, help_text: str) -> None:
    with st.container():
        st.error(f"**{title}**")
        st.write(message)
        st.info(help_text)


# ---------------------------------------------------------------------------
# Section Renderers
# ---------------------------------------------------------------------------

def render_sidebar() -> tuple[str, int, int]:
    with st.sidebar:
        st.header("⚙️ Settings")
        num_quiz_questions = st.slider("Number of quiz questions", 3, 15, 5)
        num_flashcards = st.slider("Number of flashcards", 5, 20, 10)
        st.divider()
        st.caption(f"Model: `{settings.gemini_model}`")
    return num_quiz_questions, num_flashcards


def render_input_section(num_quiz_questions: int, num_flashcards: int) -> None:
    st.title(f"🎓 {settings.app_title}")
    st.write("Turn any educational YouTube video into structured study material, a quiz, and flashcards.")

    youtube_url = st.text_input("YouTube video URL", placeholder="https://www.youtube.com/watch?v=...")

    if st.button("Analyze Video", type="primary", disabled=not youtube_url):
        reset_for_new_video()
        run_pipeline(youtube_url, num_quiz_questions, num_flashcards)


def render_transcript_summary() -> None:
    transcript_data = st.session_state.transcript_data
    if not transcript_data:
        return
    with st.expander("📄 Transcript Info"):
        st.write(f"**Video ID:** {transcript_data.video_id}")
        st.write(f"**Language:** {transcript_data.language}")
        st.write(f"**Word count:** {transcript_data.word_count:,}")


def render_learning_content() -> None:
    content = st.session_state.learning_content
    if not content:
        return

    st.header("📘 Learning Content")
    tabs = st.tabs(["Executive Summary", "Key Points", "Study Notes", "Important Concepts"])

    with tabs[0]:
        st.markdown(content.executive_summary)
    with tabs[1]:
        st.markdown(content.key_points)
    with tabs[2]:
        st.markdown(content.study_notes)
    with tabs[3]:
        st.markdown(content.important_concepts)


def render_quiz() -> None:
    questions = st.session_state.quiz_questions
    if not questions:
        return

    st.header("📝 Quiz")
    index = st.session_state.quiz_index

    if index >= len(questions):
        st.success(f"Quiz complete! Score: {st.session_state.quiz_score} / {len(questions)}")
        if st.button("Restart Quiz"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.answered = False
            st.session_state.selected_option = None
            st.rerun()
        return

    question = questions[index]
    st.progress((index) / len(questions), text=f"Question {index + 1} of {len(questions)}")
    st.subheader(question.question)

    selected = st.radio(
        "Choose an answer:",
        question.options,
        index=None,
        key=f"quiz_radio_{index}",
        disabled=st.session_state.answered,
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Submit Answer", disabled=st.session_state.answered or selected is None):
            st.session_state.answered = True
            st.session_state.selected_option = selected
            if question.is_correct(selected):
                st.session_state.quiz_score += 1
            st.rerun()

    if st.session_state.answered:
        if question.is_correct(st.session_state.selected_option):
            st.success("Correct! ✅")
        else:
            st.error(f"Incorrect. The correct answer is: **{question.correct_answer}**")
        st.info(question.explanation)

        with col2:
            if st.button("Next Question →"):
                st.session_state.quiz_index += 1
                st.session_state.answered = False
                st.session_state.selected_option = None
                st.rerun()


def render_flashcards() -> None:
    cards = st.session_state.flashcards
    if not cards:
        return

    st.header("🗂️ Flashcards")
    index = st.session_state.flashcard_index
    total = len(cards)

    if index >= total:
        index = 0
        st.session_state.flashcard_index = 0

    card = cards[index]
    st.caption(f"Card {index + 1} of {total} · Topic: {card.topic}" + (f" · {card.difficulty}" if card.difficulty else ""))

    face_text = card.back if st.session_state.flashcard_flipped else card.front
    st.markdown(
        f"""
        <div style="
            border: 2px solid #4A4A4A;
            border-radius: 16px;
            padding: 3rem 2rem;
            text-align: center;
            font-size: 1.3rem;
            min-height: 160px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: rgba(127,127,127,0.08);
        ">
            {face_text}
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("⬅️ Previous", disabled=index == 0):
            st.session_state.flashcard_index -= 1
            st.session_state.flashcard_flipped = False
            st.rerun()
    with col2:
        if st.button("🔄 Flip"):
            st.session_state.flashcard_flipped = not st.session_state.flashcard_flipped
            st.rerun()
    with col3:
        if st.button("Next ➡️", disabled=index >= total - 1):
            st.session_state.flashcard_index += 1
            st.session_state.flashcard_flipped = False
            st.rerun()
    with col4:
        if st.button("🔀 Shuffle"):
            import random

            random.shuffle(st.session_state.flashcards)
            st.session_state.flashcard_index = 0
            st.session_state.flashcard_flipped = False
            st.rerun()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    init_session_state()
    num_quiz_questions, num_flashcards = render_sidebar()
    render_input_section(num_quiz_questions, num_flashcards)

    if st.session_state.analysis_complete:
        st.divider()
        render_transcript_summary()
        render_learning_content()
        st.divider()
        render_quiz()
        st.divider()
        render_flashcards()


if __name__ == "__main__":
    main()