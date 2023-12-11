import streamlit as st

def main():
    st.title("YouTube Video Summarizer")
    
    youtube_link = st.text_input("Enter YouTube video link:")
    
    if st.button("Summarize"):
        if youtube_link:
            st.success(f"You entered: {youtube_link}")
            # Implement further functionalities here
        else:
            st.warning("Please enter a YouTube video link.")

if __name__ == "__main__":
    main()
