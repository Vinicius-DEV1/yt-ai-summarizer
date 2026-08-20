# yt-ai-summarizer

A simple Python tool that extracts transcripts from YouTube videos and generates concise, structured summaries using the Google Gemini API.

---

## Features

- Automatically extracts transcripts from YouTube URLs.
- Cleans and formats raw subtitle text.
- Generates clear bulleted summaries using Google Gemini.
- Lightweight, easy to set up, and beginner-friendly.

---

## 📋 Prerequisites

- Python 3.9 or higher installed.
- A Google Gemini API Key (get a free key at [Google AI Studio](https://aistudio.google.com/)).

---

## Getting Started

### 1. Clone the repository
git clone https://github.com/your-username/yt-ai-summarizer.git
cd yt-ai-summarizer

### 2. Create and activate a virtual environment
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up environment variables
Create a `.env` file from the example:
cp .env.example .env

Add your Gemini API key inside `.env`:
GEMINI_API_KEY=your_actual_api_key_here

---

## 💻 Usage

Run the script:
python main.py

Provide a YouTube URL when prompted:
Enter YouTube URL: https://www.youtube.com/watch?v=EXAMPLE_ID

---

## 📄 Example Output

### Summary
- **Main Topic:** Core concept discussed in the video.
- **Key Takeaways:**
  - First critical point explained by the author.
  - Practical tips or examples highlighted.
- **Actionable Steps:** Next steps or recommendations provided.

---

## 🛠️ Built With

- Python
- youtube-transcript-api
- google-genai
- python-dotenv

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
