import streamlit as st
from streamlit_autorefresh import st_autorefresh

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# --------------------------------------------------
st.set_page_config(
    page_title="Deep Emotion Detector",
    page_icon="😉",
    layout="centered",
)

import warnings
warnings.filterwarnings("ignore")
def mood_pulse(mood):
    st_autorefresh(interval=1500, key="pulse")

    pulse_colors = {
        "happy": ["🟢", "🟢", "🟢", "🟡"],
        "sad": ["🔵", "🔵", "🟣", "🔵"],
        "neutral": ["⚪", "⚪", "⚪", "⚪"],
        "positive": ["🟢", "🟢", "🟡", "🟢"],
        "negative": ["🔴", "🔴", "🟣", "🔴"]
    }

    sequence = pulse_colors.get(mood.lower(), ["⚪"] * 4)

    tick = st.session_state.get("pulse_tick", 0)
    st.session_state["pulse_tick"] = tick + 1

    bar = sequence[tick % len(sequence)]

    st.markdown(
        f"""
        <div style="
            font-size: 42px;
            text-align: center;
            letter-spacing: 12px;
            margin-top: 12px;
        ">
            {bar} {bar} {bar} {bar}
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# IMPORTS (AFTER PAGE CONFIG)
# --------------------------------------------------
from PIL import Image
import os

# original repo helpers
from app_funcs import *

# new system modules
from src.feed_loader import get_headlines
from src.emotion_engine import detect_emotion
from src.mood_engine import update_memory, get_dominant_mood
from src.visual_engine import get_visuals

# --------------------------------------------------
# SAFE IMAGE LOADER (NO CRASHES)
# --------------------------------------------------
def load_image(path):
    try:
        return Image.open(path)
    except Exception:
        return None

# --------------------------------------------------
# ASSETS (MATCHING YOUR FOLDERS)
# --------------------------------------------------
top_image = load_image("assets/banners/banner_top.png")
bottom_image = load_image("assets/banners/banner_bottom.png")
main_image = load_image("assets/banners/main_banner.png")

upload_path = "uploads"
download_path = "downloads"

os.makedirs(upload_path, exist_ok=True)
os.makedirs(download_path, exist_ok=True)

# --------------------------------------------------
# SIDEBAR (UNCHANGED)
# --------------------------------------------------
if top_image:
    st.sidebar.image(top_image, use_container_width=True)

mode = st.sidebar.selectbox(
    "Input Source 😯",
    ["Live World Feed 🌍", "Plain Text 📝", "Documents 📑"]
)

if bottom_image:
    st.sidebar.image(bottom_image, use_container_width=True)

# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
if main_image:
    st.image(main_image, use_container_width=True)

st.title("😲 AI Emotion Detector")


def apply_mood_background(mood):
    mood_colors = {
        "happy": "#2ecc71",
        "sad": "#3498db",
        "neutral": "#3a3a3a",
        "positive": "#27ae60",
        "negative": "#c0392b"
    }

    bg = mood_colors.get(mood.lower(), "#3a3a3a")

    st.markdown(
        f"""
        <style>
        .moving-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                120deg,
                {bg},
                rgba(255,255,255,0.08),
                {bg}
            );
            animation: moveBg 12s ease-in-out infinite;
            z-index: -1;
        }}

        @keyframes moveBg {{
            0% {{ transform: translate(0%, 0%); }}
            50% {{ transform: translate(-25%, -25%); }}
            100% {{ transform: translate(0%, 0%); }}
        }}
        </style>

        <div class="moving-bg"></div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# LIVE WORLD FEED MODE (UNCHANGED)
# --------------------------------------------------
if mode == "Live World Feed 🌍":
    st.subheader("🌍 Live Emotional Pulse of the World")

    headlines = get_headlines(limit=5)

    for headline in headlines:
        emotion = detect_emotion(headline)
        update_memory(emotion)

        visuals = get_visuals(emotion)

        st.markdown(
            f"""
            <div style="
                padding: 14px;
                margin-bottom: 10px;
                border-radius: 10px;
                background-color: {visuals['color']};
                opacity: {visuals['opacity']};
                color: white;
                transition: all 0.4s ease;
            ">
                {visuals['emoji']} {headline}
            </div>
            """,
            unsafe_allow_html=True,
        )

    dominant_mood = get_dominant_mood()
    apply_mood_background(dominant_mood)

    st.info(f"🧠 Dominant Emotional Mood: **{dominant_mood.upper()}**")
    mood_pulse(dominant_mood)

# --------------------------------------------------
# TEXT MODE (CTRL + ENTER MAGIC HERE)
# --------------------------------------------------
elif mode == "Plain Text 📝":
    st.caption("Press Ctrl + Enter to analyze")

    text = st.text_area(
        "Paste text below 👇",
        height=250,
        key="plain_text_input"
    )

    # Streamlit runs on every Ctrl+Enter automatically
    if text.strip():
        emotion_output = emotion_generate(text)
        update_memory(emotion_output)

        visuals = get_visuals(emotion_output)
        apply_mood_background(emotion_output)

        st.success(
            f"{visuals['emoji']} Detected Emotion: **{emotion_output.title()}**"
        )

        dominant_mood = get_dominant_mood()
        st.info(f"🧠 Emotional Context: **{dominant_mood.upper()}**")
        mood_pulse(emotion_output)

# --------------------------------------------------
# DOCUMENT MODE (UNCHANGED)
# --------------------------------------------------
elif mode == "Documents 📑":
    st.info("Supports TXT, PDF, DOCX 📄")
    uploaded_file = st.file_uploader(
        "Upload Document", type=["txt", "pdf", "docx"]
    )

    if uploaded_file:
        file_path = os.path.join(upload_path, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Analyzing emotional context... 💫"):
            if uploaded_file.name.lower().endswith(".txt"):
                processed = os.path.join(
                    download_path, "processed_" + uploaded_file.name
                )
                text = extract_text_txt(file_path, processed)

            elif uploaded_file.name.lower().endswith(".pdf"):
                text = extract_text_pdf(file_path)

            elif uploaded_file.name.lower().endswith(".docx"):
                text = extract_text_docx(file_path)

            emotion_output = emotion_generate(text)
            update_memory(emotion_output)

        visuals = get_visuals(emotion_output)
        apply_mood_background(emotion_output)

        st.success(
            f"{visuals['emoji']} Detected Emotion: **{emotion_output.title()}**"
        )

        dominant_mood = get_dominant_mood()
        st.info(f"🧠 Emotional Context: **{dominant_mood.upper()}**")

        download_success()
