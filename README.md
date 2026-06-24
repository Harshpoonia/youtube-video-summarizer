# YouTube Video Summarizer

An AI-powered application that generates concise summaries from YouTube videos using transcript extraction, Natural Language Processing (NLP), and text-to-speech conversion.

## Features

- Extract transcripts from YouTube videos
- Generate automatic video summaries
- Convert summaries into audio
- User-friendly Streamlit interface
- Fast and lightweight workflow

## Tech Stack

- Python
- Streamlit
- YouTube Transcript API
- NLP
- gTTS (Google Text-to-Speech)

## Project Structure

```text
youtube-video-summarizer/
│
├── app.py
├── streamlitApp.py
├── YouTubeAPIModule.py
├── summarization.py
├── text_to_speech_module.py
├── requirements.txt
└── README.md
```

## Workflow

1. Enter a YouTube video URL
2. Extract video transcript
3. Generate summary
4. Display summarized content
5. Generate audio output

## Installation

```bash
git clone https://github.com/Harshpoonia/youtube-video-summarizer.git

cd youtube-video-summarizer

pip install -r requirements.txt

streamlit run app.py
```

## Future Improvements

- Multi-language support
- AI-powered summarization using LLMs
- PDF export
- Chapter-wise summaries

## Author

Harsh Poonia

MCA Student, Thapar Institute of Engineering & Technology

Interested in Data Analytics, Machine Learning, and Software Development.
