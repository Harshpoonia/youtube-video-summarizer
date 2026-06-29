# 🎥 YouTube AI Learning Assistant

> **Transform any YouTube video into structured learning material using Google Gemini AI.**

The **YouTube AI Learning Assistant** is an AI-powered educational application that converts YouTube videos into organized study resources. By combining YouTube transcript extraction with Google's Gemini AI, the application generates comprehensive learning material including summaries, study notes, important concepts, and interactive quizzes.

Originally developed as a **YouTube Video Summarizer** for my BCA Minor Project, this application has been redesigned and expanded into a modular AI-powered learning platform as part of my MCA journey.

---

# 🚀 Features

## 📺 YouTube Transcript Extraction

* Extract transcripts directly from YouTube videos
* Supports manually created and auto-generated captions
* Automatic transcript language detection
* Handles unavailable transcripts gracefully

---

## 📊 Transcript Analytics Dashboard

Automatically generates useful transcript statistics:

* 📝 Word Count
* 🔤 Character Count
* 🌐 Language Detection
* 📖 Estimated Reading Time

---

## 🤖 AI Learning Content

Generate structured educational material using **Google Gemini**.

### 📝 Executive Summary

A concise overview of the video's main ideas.

### 📌 Key Points

Quick bullet-point revision notes.

### 📚 Study Notes

Detailed explanations suitable for revision and learning.

### 🧠 Important Concepts

Important concepts extracted from the transcript with brief explanations.

---

## ❓ Interactive AI Quiz

Test your understanding of the video with automatically generated quizzes.

Features include:

* AI-generated MCQs
* Four options per question
* One question at a time
* Instant answer feedback
* Explanation for each answer
* Progress tracking
* Final score and percentage

---

## 🖥️ Modern User Interface

* Clean Streamlit interface
* Multi-tab learning experience
* Interactive quiz interface
* Persistent application state using Session State

---

# 🏗️ System Architecture

```text
                          User
                            │
                            ▼
                    Streamlit Interface
                            │
                            ▼
                  YouTube Transcript API
                            │
                            ▼
                   Transcript Data Model
                            │
            ┌───────────────┴────────────────┐
            ▼                                ▼
     Learning Service                  Quiz Service
            │                                │
            ▼                                ▼
      Google Gemini API               Google Gemini API
            │                                │
            ▼                                ▼
    Markdown Learning Content          JSON Quiz Output
            │                                │
            ▼                                ▼
    Markdown Parser                  Quiz Parser
            │                                │
            └───────────────┬────────────────┘
                            ▼
                   Streamlit Dashboard
                            │
      ┌─────────┬──────────┬──────────┬──────────┬─────────┐
      ▼         ▼          ▼          ▼          ▼         ▼
 Transcript  Summary   Key Points  Study Notes Concepts   Quiz
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
│── .env.example

├── modules/
│   ├── ai_service.py
│   ├── learning_service.py
│   ├── quiz_service.py
│   └── transcript.py
│
├── models/
│   ├── transcript_model.py
│   └── quiz_model.py
│
├── prompts/
│   ├── learning_prompt.txt
│   └── quiz_prompt.txt
│
├── utils/
│   ├── markdown_parser.py
│   ├── quiz_parser.py
│   └── prompt_loader.py
│
└── assets/
```

---

# ⚙️ Technology Stack

| Category        | Technology             |
| --------------- | ---------------------- |
| Language        | Python                 |
| Frontend        | Streamlit              |
| AI              | Google Gemini          |
| Transcript API  | youtube-transcript-api |
| Environment     | python-dotenv          |
| Version Control | Git & GitHub           |

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Harshpoonia/youtube-ai-learning-assistant.git

cd youtube-ai-learning-assistant
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run the Application

```bash
python -m streamlit run app.py
```

---

# 📖 How It Works

1. Paste a YouTube video URL.
2. Extract the transcript.
3. Calculate transcript statistics.
4. Generate AI learning material using Google Gemini.
5. Parse structured Markdown output.
6. Generate an interactive AI quiz.
7. Display everything through a clean Streamlit interface.

---

# 📈 Project Evolution

This repository represents the evolution of my original BCA Minor Project.

The project has grown from a simple summarizer into a modular AI learning platform.

| Original Project         | Current Project                                                 |
| ------------------------ | --------------------------------------------------------------- |
| YouTube Video Summarizer | YouTube AI Learning Assistant                                   |
| Single Summary           | Executive Summary, Key Points, Study Notes & Important Concepts |
| Static Output            | Interactive AI Quiz                                             |
| Monolithic Code          | Modular Service-Oriented Architecture                           |
| Basic Interface          | Multi-Tab Learning Dashboard                                    |
| Basic NLP                | Google Gemini AI                                                |

---

# 📌 Current Features

* ✅ Transcript Extraction
* ✅ Transcript Analytics Dashboard
* ✅ Executive Summary
* ✅ Key Points
* ✅ Study Notes
* ✅ Important Concepts
* ✅ Interactive AI Quiz
* ✅ Google Gemini Integration
* ✅ Markdown Parsing
* ✅ JSON Quiz Parsing
* ✅ Session State Management
* ✅ Modular Project Architecture

---

# 📷 Screenshots

Screenshots and demo GIFs will be added after the UI polishing phase.

Planned screenshots:

* Home Screen
* Transcript Dashboard
* Executive Summary
* Study Notes
* Quiz Interface
* Quiz Results

---

# 🚧 Current Limitations

* Videos without captions cannot be processed.
* Private or age-restricted videos may not expose transcripts.
* YouTube may temporarily rate-limit transcript requests.
* Multi-language learning support is planned for future versions.

---

# 🛣️ Future Roadmap

Upcoming features include:

* 🗂️ Flashcards
* 💬 Chat with Video
* 📄 PDF Export
* 🔊 Text-to-Speech
* 🌍 Multi-language Support
* ⏱️ Timestamp Navigation
* 🧠 AI Tutor Mode
* 📈 Learning Progress Tracking

For the complete roadmap, see **PROJECT_ROADMAP.md**.

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you find a bug or have an idea for improvement, feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Harsh Poonia**

**MCA Student**
Artificial Intelligence • Machine Learning • Data Analytics

This project reflects my journey from a college academic project to a portfolio-focused AI application, emphasizing clean architecture, modular design, and practical use of Generative AI.

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub.
