import json

from models.quiz_model import QuizQuestion


def parse_quiz(json_text: str) -> list[QuizQuestion]:
    """
    Convert Gemini JSON response into QuizQuestion objects.
    """

    try:
        data = json.loads(json_text)

        questions = []

        for item in data:

            questions.append(
                QuizQuestion(
                    question=item["question"],
                    options=item["options"],
                    answer=item["answer"],
                    explanation=item["explanation"],
                )
            )

        return questions

    except Exception as e:
        raise RuntimeError(
            f"Failed to parse quiz JSON:\n{e}"
        )