# YouTube Video Summarizer & Speech Generator

## Overview

YouTube Video Summarizer & Speech Generator is a Python-based web application developed as a **BCA Minor Project**. The application extracts information from YouTube videos using the YouTube Data API, generates concise summaries using Natural Language Processing (NLP), and converts the generated summary into speech.

The project demonstrates the integration of APIs, machine learning models, and web application development using Python.

---

## Objectives

* Extract information from YouTube videos.
* Generate concise summaries using NLP techniques.
* Convert text summaries into speech.
* Provide a simple and interactive web interface for users.

---

## Features

* Accepts YouTube video URLs as input.
* Extracts video information using YouTube Data API.
* Generates automated text summaries.
* Converts summaries into audio format (MP3).
* Interactive web application built with Streamlit.
* Simple and user-friendly interface.

---

## Tech Stack

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

## Project Structure

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

## Working Process

1. User enters a YouTube video URL.
2. The application extracts the video ID.
3. Video information is retrieved using the YouTube Data API.
4. NLP-based summarization is performed on the retrieved content.
5. The generated summary is converted into speech.
6. Audio output is provided to the user.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Harshpoonia/youtube-video-summarizer.git
cd youtube-video-summarizer
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

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

## YouTube API Configuration

Obtain a YouTube Data API v3 key from Google Cloud Console.

Replace the placeholder value in:

```python
API_KEY = "YOUR_YOUTUBE_API_KEY"
```

with your own API key.

---

## Running the Application

```bash
streamlit run StreamlitApp.py
```

The application will launch in your default browser.

---

## Learning Outcomes

This project helped in understanding:

* API Integration
* Natural Language Processing
* Text Summarization
* Text-to-Speech Systems
* Python Application Development
* Streamlit Web Applications
* Software Modularization

---

## Future Enhancements

* Transcript-based video summarization
* Multi-language support
* PDF export of summaries
* Advanced NLP models
* Cloud deployment
* User authentication and history tracking

---

## Academic Information

**Project Type:** BCA Minor Project

**Domain:** Natural Language Processing (NLP) / Web Application Development

**Year:** 2023–2024

---

## Author

**Harsh Poonia**

MCA Student
Thapar Institute of Engineering & Technology

Interests:

* Data Analytics
* Machine Learning
* Artificial Intelligence
* Software Development
