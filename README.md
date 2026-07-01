# 🎥 YouTube AI Learning Assistant

> **Transform any YouTube video into an interactive AI-powered learning experience.**

The **YouTube AI Learning Assistant** is an AI-powered educational application that converts YouTube videos into structured learning resources using **Google Gemini AI**. Instead of simply summarizing videos, the application generates comprehensive study material including executive summaries, study notes, quizzes, and AI-generated flashcards.

Originally developed as a **YouTube Video Summarizer**, the project has evolved into a modular learning platform following modern software engineering principles.

---

# ✨ Features

## 📺 Transcript Extraction

* Extract transcripts from YouTube videos
* Supports manual and auto-generated captions
* Automatic language detection
* Transcript analytics

---

## 📊 Transcript Analytics

Automatically generates:

* 📝 Word Count
* 🔤 Character Count
* 🌐 Language Detection
* 📖 Estimated Reading Time

---

## 🤖 AI Learning Content

Using Google Gemini, the application generates:

* 📝 Executive Summary
* 📌 Key Points
* 📚 Study Notes
* 🧠 Important Concepts

---

## ❓ Interactive AI Quiz

Test your understanding with AI-generated quizzes.

Features include:

* Multiple Choice Questions
* One Question at a Time
* Instant Feedback
* Answer Explanations
* Progress Tracking
* Final Score
* Session State Support

---

## 🗂️ AI Flashcards

Generate interactive revision flashcards.

Features include:

* Front & Back Cards
* AI-generated Concepts
* Sequential Navigation
* Interactive Learning Experience

---

## 🏗️ Modern Architecture

* Modular Service-Oriented Design
* Centralized Configuration
* Prompt Engineering
* Markdown Parsing
* JSON Parsing
* Session State Management
* Reusable Services
* Scalable Project Structure

---

# 🏛️ Architecture

```text
                    Streamlit UI
                         │
                         ▼
                 Session State Manager
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Transcript        LearningService   FlashcardService
     │                    │                │
     ▼                    ▼                ▼
Transcript Model     QuizService      AIService
                          │                │
                          └──────┬─────────┘
                                 ▼
                          Google Gemini API
                                 │
               ┌─────────────────┼────────────────┐
               ▼                 ▼                ▼
        Markdown Parser     Quiz Parser     Flashcard Parser
               │                 │                │
               └─────────────────┴────────────────┘
                                 ▼
                        Streamlit Dashboard
```

---

# 📂 Project Structure

```text
youtube-ai-learning-assistant/

│── app.py
│── config.py
│── requirements.txt
│── README.md
│── PROJECT_ROADMAP.md

├── modules/
│   ├── ai_service.py
│   ├── learning_service.py
│   ├── quiz_service.py
│   ├── flashcard_service.py
│   └── transcript.py
│
├── models/
│   ├── transcript_model.py
│   ├── quiz_model.py
│   └── flashcard_model.py
│
├── prompts/
│   ├── learning_prompt.txt
│   ├── quiz_prompt.txt
│   └── flashcard_prompt.txt
│
├── utils/
│   ├── markdown_parser.py
│   ├── quiz_parser.py
│   ├── flashcard_parser.py
│   └── prompt_loader.py
│
├── assets/
└── tests/
```

---

# ⚙️ Tech Stack

| Category        | Technology             |
| --------------- | ---------------------- |
| Language        | Python                 |
| Frontend        | Streamlit              |
| AI              | Google Gemini          |
| Transcript API  | youtube-transcript-api |
| Configuration   | python-dotenv          |
| Version Control | Git & GitHub           |

---

# 🚀 Installation

```bash
git clone https://github.com/<your-username>/youtube-ai-learning-assistant.git

cd youtube-ai-learning-assistant

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.0-flash
```

Run the application:

```bash
streamlit run app.py
```

---

# 📈 Project Evolution

| Version | Major Improvements                       |
| ------- | ---------------------------------------- |
| v1.0    | YouTube Video Summarizer                 |
| v2.0    | AI Learning Content                      |
| v2.1    | Interactive Quiz                         |
| v2.2    | Flashcards + Major Architecture Refactor |

---

# ✅ Completed Features

* Transcript Extraction
* Transcript Analytics
* Executive Summary
* Key Points
* Study Notes
* Important Concepts
* Interactive Quiz
* AI Flashcards
* Session State Management
* AI Service Layer
* Prompt Management
* Markdown Parsing
* JSON Parsing
* Modular Architecture

---

# 🚧 Upcoming Features

* 💬 Chat with Video
* 📄 PDF Export
* 🔊 Text-to-Speech
* 🌍 Multi-language Support
* ⏱️ Timestamp Navigation
* 📈 Learning Progress
* 🤖 AI Tutor Mode

See **PROJECT_ROADMAP.md** for the complete roadmap.

---

# 👨‍💻 Author

**Harsh Poonia**

MCA Student | AI • Machine Learning • Data Analytics

This project demonstrates the use of **Generative AI**, **modular software architecture**, **prompt engineering**, and **interactive educational applications** to transform YouTube videos into structured learning experiences.

If you found this project useful, consider giving it a ⭐ on GitHub.
