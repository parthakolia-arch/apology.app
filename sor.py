import streamlit as st
import time

st.set_page_config(page_title="I am Sorry Harshita", page_icon="💔", layout="centered")

# Initialize Session States to prevent typewriter re-running
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "text_typed" not in st.session_state:
    st.session_state.text_typed = False

# Premium CSS for Custom Giant Teddy Neck-tilt, Floating Emojis like balloons, and Popups
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

    /* Giant Cute Teddy Bear with Neck Wiggle Animation */
    .giant-teddy {
        font-size: 150px;
        text-align: center;
        display: block;
        margin: 0 auto;
        animation: teddyWiggle 2s ease-in-out infinite alternate;
        transform-origin: bottom center;
    }

    @keyframes teddyWiggle {
        0% { transform: rotate(-8deg); }
        100% { transform: rotate(8deg); }
    }

    /* Floating Emoji Balloon Effect container */
    .emoji-floater {
        position: fixed;
        bottom: -50px;
        font-size: 30px;
        animation: floatUp 4s linear infinite;
        opacity: 0.8;
        z-index: 999;
    }

    @keyframes floatUp {
        0% { transform: translateY(0) translateX(0); opacity: 1; }
        100% { transform: translateY(-105vh) translateX(50px); opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- CASE 1: IF YES IS TAPPED (SUCCESS SCREEN) -----------------
if st.session_state.accepted:
    st.balloons()
    
    # 1. Custom Floating Loving Emojis rising like balloons from bottom
    love_emojis = ["❤️", "🥰", "💖", "💝", "💘", "💋", "💕", "🧸"]
    html_love = ""
    for i in range(25):
        left_pos = (i * 7) % 100 
        delay = (i * 0.3) % 3
        html_love += f'<div class="emoji-floater" style="left: {left_pos}%; animation-delay: {delay}s;">{love_emojis[i % len(love_emojis)]}</div>'
    st.markdown(html_love, unsafe_allow_html=True)
    
    # 2. Giant Pop-up Thank You
    st.markdown("<br><br><br><div class='pop-title' style='font-size: 75px;'>Thank you sooo much! 💕</div>", unsafe_allow_html=True)
    
    if st.button("Reset Webpage"):
        st.session_state.no_count = 0
        st.session_state.accepted = False
        st.session_state.text_typed = False
        st.rerun()

# ----------------- CASE 2: MAIN FORM RUNNING -----------------
else:
    # 1. Giant Cute Animated Teddy Bear (Neck moves left-right beautifully)
    st.markdown('<div class="giant-teddy">🧸</div>', unsafe_allow_html=True)

    # 2. Top Giant Pop-up Title
    st.markdown('<p class="pop-title">I am Sorry, Harshita Ji... 💔</p>', unsafe_allow_html=True)

    # 3. Smart Typewriter Control Block
    full_paragraph = (
        "Please forgive me. I deeply regret breaking your trust and breaking the sacred promise I made to you. "
        "I am genuinely ashamed of my actions and how much I have hurt you. From this very moment, "
        "I solemnly vow that I will never repeat this mistake again. This is my truest, deepest, "
        "and most sincere promise to you. Please give me one chance to rebuild what I broke."
    )
    
    st.markdown("<div style='font-family: \"Dancing Script\", cursive; font-size: 26px; line-height: 1.5; color: #4a154b; text-align: center; padding: 20px; background: rgba(255,255,255,0.3); border-radius: 15px;'>", unsafe_allow_html=True)
    
    # If first time, type it live. If already clicked No, show instantly without re-typing!
    if not st.session_state.text_typed:
        def stream_text():
            for word in full_paragraph.split(" "):
                yield word + " "
                time.sleep(0.04)
        st.write_stream(stream_text)
        st.session_state.text_typed = True
    else:
        st.write(full_paragraph)
        
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("---")

    # 4. Handle "No" Clicks with Error Popups and Floating Crying Emojis
    if st.session_state.no_count > 0:
        st.error("### 🛑 mujhe maaf kr do pleaseee 🥺🙏")
        
        # Dynamic Floating Sad Emojis multiplying based on No count
        sad_emojis = ["😭", "🥺", "💔", "😢", "😔", "🌧️"]
        html_sad = ""
        total_sad_balloons = min(st.session_state.no_count * 5, 30) # cap to prevent lag
        for i in range(total_sad_balloons):
            left_pos = (i * 11) % 100
            delay = (i * 0.25) % 2.5
            html_sad += f'<div class="emoji-floater" style="left: {left_pos}%; animation-delay: {delay}s;">{sad_emojis[i % len(sad_emojis)]}</div>'
        st.markdown(html_sad, unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: #4a4a4a;'>Did you forgive me?</h3>", unsafe_allow_html=True)

    # Clean Action Interface Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes", key=f"yes_{st.session_state.no_count}", type="primary", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()
            
    with col2:
        if st.button("No", key=f"no_{st.session_state.no_count}", use_container_width=True):
            st.session_state.no_count += 1
            st.rerun()
