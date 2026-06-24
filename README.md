# 🎥 YouTube Video Summarizer & Speech Generator

## 📖 Overview

YouTube Video Summarizer & Speech Generator is a Python-based web application developed as a **BCA Minor Project**. The application extracts information from YouTube videos using the YouTube Data API, generates concise summaries using Natural Language Processing (NLP), and converts the generated summary into speech.

---

## 🎯 Objectives

* Extract information from YouTube videos
* Generate concise summaries using NLP
* Convert summaries into speech
* Provide an interactive web interface

---

## ✨ Features

* 🔗 Accepts YouTube video URLs
* 📺 Extracts video information using YouTube Data API
* 📝 Generates automated text summaries
* 🔊 Converts summaries into audio (MP3)
* 🌐 Interactive Streamlit interface
* ⚡ Simple and user-friendly workflow

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Streamlit
* Transformers (Hugging Face)
* Google API Python Client
* gTTS (Google Text-to-Speech)

### APIs

* YouTube Data API v3

---

## 📂 Project Structure

```text
youtube-video-summarizer/
│
├── StreamlitApp.py
├── YouTubeAPIModule.py
├── summarization.py
├── text-to-speech.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Working Process

1. 🔗 User enters a YouTube video URL
2. 🆔 Video ID is extracted
3. 📡 Video information is fetched using YouTube Data API
4. 📝 NLP-based summarization is performed
5. 🔊 Summary is converted to speech
6. 🎧 Audio output is generated

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Harshpoonia/youtube-video-summarizer.git
cd youtube-video-summarizer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 YouTube API Configuration

Obtain a YouTube Data API v3 key from Google Cloud Console.

Replace:

```python
API_KEY = "YOUR_YOUTUBE_API_KEY"
```

with your own API key.

---

## ▶️ Running the Application

```bash
streamlit run StreamlitApp.py
```

---

## 📚 Learning Outcomes

* API Integration
* Natural Language Processing
* Text Summarization
* Text-to-Speech Systems
* Streamlit Development
* Python Programming
* Software Modularization

---

## 🔮 Future Enhancements

* 🌍 Multi-language support
* 📜 Transcript-based summarization
* 📄 PDF export functionality
* 🤖 Advanced NLP models
* ☁️ Cloud deployment
* 👤 User authentication

---

## 🎓 Academic Information

* **Project Type:** BCA Minor Project
* **Domain:** NLP & Web Application Development
* **Academic Level:** Undergraduate Project

---

## 👨‍💻 Author

**Harsh Poonia**

MCA Student, Thapar Institute of Engineering & Technology

**Areas of Interest**

* 📊 Data Analytics
* 🤖 Machine Learning
* 🧠 Artificial Intelligence
* 💻 Software Development
