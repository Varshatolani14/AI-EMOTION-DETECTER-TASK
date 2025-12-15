# AI Internet Mood Content Engine

A lightweight AI-powered content system that converts live internet signals into short-form, visually reactive content — designed for daily posting on TikTok, IG Reels, or X.

This project was built as a 48-hour execution trial focused on shipping output, not prompts or explanations.

---

## What this system does

- Pulls **live headlines** from the internet
- Runs **real AI emotion detection** on each headline
- Aggregates signals into a **dominant emotional mood**
- Visualizes results using **color, emoji, and motion**
- Produces **camera-ready output** in seconds

Each run generates fresh content based on what is happening in the world at that moment.

---

## Why this is interesting

Most AI content demos generate scripts or captions.

This system:
- Uses **external live data**, not prompts
- Makes AI output **visually obvious**
- Behaves like a **content pipeline**, not a one-off tool
- Can be run repeatedly without manual work

It’s designed to feel alive on screen, which is critical for short-form platforms.

---

## How this can scale

- Run on a schedule (hourly / daily)
- Add more data sources (social trends, forums, news)
- Auto-record and auto-post clips
- Apply brand-specific visual themes
- Extend emotion aggregation into dashboards or alerts

The core logic stays the same, only the input signals change.

---

## Demo flow (what the video shows)

1. Live headlines load automatically  
2. Each headline is classified by emotion  
3. Visual elements react instantly  
4. A dominant mood snapshot is computed  
5. The system updates without manual input  

The same flow works every time the app runs.

---

## Tech stack (kept intentionally simple)

- Python
- Streamlit
- Hugging Face Transformers (open sentiment model)
- PyMuPDF, python-docx for document parsing

Tool choice was secondary to speed and reliability.

---

## Setup

```bash
# install dependencies
python -m pip install streamlit transformers torch pymupdf python-docx

# run the app
python -m streamlit run app.py
