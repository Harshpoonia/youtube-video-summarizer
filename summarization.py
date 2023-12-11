from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    summary_text = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    return summary_text
