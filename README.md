# 🎥 YouTube AI Learning Assistant

> Transform any YouTube video into structured learning material using **Google Gemini AI**.

A modern AI-powered learning assistant that extracts YouTube transcripts and converts them into organized study resources including executive summaries, key points, study notes, and important concepts through a clean, interactive Streamlit interface.

---

## ✨ Features

### 📺 Transcript Extraction

* Extract transcripts directly from YouTube videos
* Supports manually created and auto-generated captions
* Automatic transcript language detection
* Graceful handling of unavailable transcripts

### 🤖 AI-Powered Learning Content

Generate high-quality educational resources with a single AI request:

* 📝 Executive Summary
* 📌 Key Points
* 📚 Study Notes
* 🧠 Important Concepts

### 📊 Transcript Analytics

Automatically calculates:

* Word Count
* Character Count
* Estimated Reading Time
* Transcript Language

### 🖥️ Interactive Learning Interface

* Multi-tab layout
* Clean dashboard
* Structured AI output
* Responsive Streamlit UI

---

# 🏗️ System Architecture

```text
                        User
                          │
                          ▼
                   Streamlit Interface
                          │
                          ▼
                 Transcript Extraction
                          │
                          ▼
                 Transcript Data Model
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
      Analytics Engine         Learning Service
                                         │
                                         ▼
                                  Google Gemini
                                         │
                                         ▼
                              Markdown Content Parser
                                         │
      ┌──────────────┬─────────────┬──────────────┬──────────────┐
      ▼              ▼             ▼              ▼
 Executive Summary  Key Points  Study Notes  Important Concepts
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
│   └── transcript.py
│
├── models/
│   └── transcript_model.py
│
├── prompts/
│   └── learning_prompt.txt
│
├── utils/
│   ├── markdown_parser.py
│   ├── prompt_loader.py
│   └── text_statistics.py
│
└── assets/
```

---

# ⚙️ Tech Stack

| Category       | Technology             |
| -------------- | ---------------------- |
| Language       | Python                 |
| Frontend       | Streamlit              |
| AI Model       | Google Gemini          |
| Transcript API | youtube-transcript-api |
| Environment    | python-dotenv          |
| Text-to-Speech | gTTS                   |

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/Harshpoonia/youtube-ai-learning-assistant.git

cd youtube-ai-learning-assistant
```

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

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

## Run the Application

```bash
python -m streamlit run app.py
```

---

# 📖 How It Works

1. Paste a YouTube video URL.
2. The application extracts the transcript.
3. Transcript statistics are calculated.
4. Google Gemini analyzes the transcript.
5. AI-generated learning resources are parsed into structured sections.
6. The content is displayed through dedicated learning tabs.

---

# 📈 Project Evolution

This repository began as my **BCA Minor Project**, where the goal was to generate a basic summary from YouTube videos.

During my MCA, I redesigned and significantly expanded the application into a modular AI-powered learning assistant.

## Evolution

| Original Version         | Current Version                                                 |
| ------------------------ | --------------------------------------------------------------- |
| YouTube Video Summarizer | YouTube AI Learning Assistant                                   |
| Single Summary           | Executive Summary, Key Points, Study Notes & Important Concepts |
| Monolithic Structure     | Modular Service-Oriented Architecture                           |
| Basic UI                 | Dashboard + Multi-Tab Interface                                 |
| Basic NLP                | Google Gemini Integration                                       |

The project now follows modern software engineering practices including modular architecture, reusable services, feature branches, pull requests, and continuous feature-based development.

---

# 📷 Screenshots

> Screenshots and demo GIF will be added after UI polishing.

---

# 🚧 Current Limitations

* Videos without captions cannot be processed.
* Private, age-restricted, or restricted videos may not expose transcripts.
* Multi-language learning support is planned for a future release.

---

# 🛣️ Roadmap

### ✅ Completed

* Transcript Extraction
* Transcript Analytics Dashboard
* Executive Summary
* Key Points
* Study Notes
* Important Concepts
* Google Gemini Integration
* Markdown Parser
* Modular Architecture

### 🚧 In Progress

* AI Quiz Generator
* Flashcards
* Chat with Video
* PDF Export
* Text-to-Speech
* Multi-language Support
* Timestamp Navigation

For the complete roadmap, see **PROJECT_ROADMAP.md**.

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Harsh Poonia**

MCA Student | Data Analytics | Machine Learning | Artificial Intelligence

If you found this project helpful, consider giving it a ⭐ on GitHub.
