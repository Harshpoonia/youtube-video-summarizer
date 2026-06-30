from models.transcript import TranscriptData
from modules.quiz_service import QuizService

dummy = TranscriptData(
    video_id="1",
    transcript="""
Python is an interpreted programming language.
It is widely used in AI and Data Science.
""",
    language="English",
    word_count=20,
    character_count=120,
    estimated_reading_time=1,
)

quiz = QuizService()

questions = quiz.generate_quiz(dummy)

for q in questions:

    print()

    print(q.question)

    print(q.options)

    print(q.answer)

    print(q.explanation)