import streamlit as st
import time

st.set_page_config(page_title="I am Sorry Harshita", page_icon="💔", layout="centered")

# Custom CSS for Premium Animations, Popups, and the Moving Teddy Bear
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp {
        background: linear-gradient(-45deg, #ffdee9, #b5fffc, #ffe4e1, #fff0f5);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        font-family: 'Poppins', sans-serif;
        overflow: hidden;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Giant Pop-up Title Style */
    .pop-title {
        font-family: 'Great Vibes', cursive;
        font-size: 65px;
        font-weight: bold;
        color: #d63384;
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.15);
        animation: popIn 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 5px;
    }

    @keyframes popIn {
        0% { transform: scale(0.3); opacity: 0; }
        70% { transform: scale(1.1); opacity: 0.9; }
        100% { transform: scale(1); opacity: 1; }
    }

    /* Moving Teddy Bear Container */
    .teddy-container {
        text-align: center;
        margin: 10px 0;
        animation: teddyMove 2.5s ease-in-out infinite alternate;
    }

    @keyframes teddyMove {
        0% { transform: translateX(-30px) rotate(-5deg); }
        100% { transform: translateX(30px) rotate(5deg); }
    }

    /* Sad Emoji Background elements */
    .sad-bg {
        font-size: 24px;
        opacity: 0.25;
        text-align: center;
        letter-spacing: 10px;
        animation: pulse 2s infinite alternate;
    }
    
    /* Happy Emoji Background elements */
    .happy-bg {
        font-size: 35px;
        text-align: center;
        letter-spacing: 15px;
        animation: popIn 1s ease-out;
    }
    </style>
""", unsafe_allow_html=True)

# State variable initializations
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# List of emotional emojis that grow with every "No" click
sad_emojis = ["😭", "🥺", "💔", "😢", "🩹", "😔", "🧸", "🌧️"]
current_sad_string = " ".join([sad_emojis[i % len(sad_emojis)] for i in range(st.session_state.no_count * 4)])

# ----------------- CASE 1: IF YES IS TAPPED -----------------
if st.session_state.accepted:
    st.balloons()
    # Pop-up Thank you message taking full screen focus with love background
    st.markdown("<br><br><br><div class='pop-title' style='font-size: 75px;'>Thank you sooo much! 💕</div>", unsafe_allow_html=True)
    st.markdown("<div class='happy-bg'>❤️🥰💖🌟✨💝💫🎉🤩✨❤️🥰💖</div>", unsafe_allow_html=True)
    st.markdown("<div class='happy-bg'>💖💝💘🥰✨❤️💖💝💘🥰✨❤️</div>", unsafe_allow_html=True)
    
    if st.button("Reset Webpage"):
        st.session_state.no_count = 0
        st.session_state.accepted = False
        st.rerun()

# ----------------- CASE 2: MAIN FORM RUNNING -----------------
else:
    # 1. Continuous Moving Teddy Bear (Age-piche loop animation)
    st.markdown('<div class="teddy-container"><span style="font-size: 80px;">🧸</span></div>', unsafe_allow_html=True)

    # 2. Top-most Giant Pop-up Title
    st.markdown('<p class="pop-title">I am Sorry, Harshita Ji... 💔</p>', unsafe_allow_html=True)

    # 3. Typewriter Animated Long Paragraph Letter-by-Letter
    full_paragraph = (
        "Please forgive me. I deeply regret breaking your trust and breaking the sacred promise I made to you. "
        "I am genuinely ashamed of my actions and how much I have hurt you. From this very moment, "
        "I solemnly vow that I will never repeat this mistake again. This is my truest, deepest, "
        "and most sincere promise to you. Please give me one chance to rebuild what I broke."
    )
    
    # Custom Typewriter script execution via safe streaming
    def stream_text():
        for word in full_paragraph.split(" "):
            yield word + " "
            time.sleep(0.06) # Controls the typing speed character fluidity
            
    st.markdown("<div style='font-family: \"Dancing Script\", cursive; font-size: 26px; line-height: 1.5; color: #4a154b; text-align: center; padding: 20px; background: rgba(255,255,255,0.3); border-radius: 15px;'>", unsafe_allow_html=True)
    st.write_stream(stream_text)
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")

    # 4. Handle "No" clicks with Increasing Sad Background Emojis and Error Popup
    if st.session_state.no_count > 0:
        # Beautiful structural error pop up
        st.error("### 🛑 mujhe maaf kr do pleaseee 🥺🙏")
        # Background crying lines that increase dynamically
        st.markdown(f"<div class='sad-bg'>{current_sad_string}</div>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: #4a4a4a;'>Did you forgive me?</h3>", unsafe_allow_html=True)

    # Action Interface buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes", key=f"yes_{st.session_state.no_count}", type="primary", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()
            
    with col2:
        if st.button("No", key=f"no_{st.session_state.no_count}", use_container_width=True):
            st.session_state.no_count += 1
            st.rerun()
