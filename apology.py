import streamlit as st
import time

# Page config for a beautiful mobile layout on Android Chrome
st.set_page_config(page_title="I am Sorry Harshita", page_icon="💔", layout="centered")

# Advanced CSS for background animations, glowing text, and premium typography
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ffdee9, #b5fffc, #ffe4e1, #fff0f5);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Poppins', sans-serif;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Main Animated Title - Sorry Harshita Ji */
    .main-title {
        font-family: 'Great Vibes', cursive;
        font-size: 50px;
        font-weight: bold;
        color: #d63384;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        animation: fadeInDown 2s ease-in-out, pulse 3s infinite alternate;
        margin-bottom: 10px;
    }
    
    /* Premium Styled Apology Paragraph */
    .apology-paragraph {
        font-family: 'Dancing Script', cursive;
        font-size: 26px;
        line-height: 1.5;
        color: #4a154b;
        text-align: center;
        padding: 30px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 182, 193, 0.6);
        box-shadow: 0 8px 32px 0 rgba(214, 51, 132, 0.15);
        animation: fadeInUp 2.5s ease-in-out;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
    }
    
    /* Keyframe Animations */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.03); }
    }
    
    /* Subheading style */
    .sub-ques {
        font-weight: 600;
        color: #4a4a4a;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Main Head Animation
st.markdown('<p class="main-title">I am Sorry, Harshita Ji... 💔</p>', unsafe_allow_html=True)

# 2. Fully Elaborated & Styled Apology Paragraph
st.markdown("""
<div class="apology-paragraph">
    Please forgive me. I deeply regret breaking your trust and breaking the sacred promise I made to you. 
    I am genuinely ashamed of my actions and how much I have hurt you. From this very moment, 
    I solemnly vow that I will never repeat this mistake again. This is my truest, deepest, 
    and most sincere promise to you. Please give me one chance to rebuild what I broke.
</div>
""", unsafe_allow_html=True)

st.write("---")

# Session State for Infinite Loop Setup
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# Action Logic
if st.session_state.accepted:
    st.balloons()
    st.markdown("<h2 style='text-align: center; color: #d63384;'>Thank you sooo much ❤️❤️❤️</h2>", unsafe_allow_html=True)
    if st.button("Reset Form"):
        st.session_state.no_count = 0
        st.session_state.accepted = False
        st.rerun()
else:
    if st.session_state.no_count == 0:
        st.markdown("<h3 class='sub-ques'>Did you forgive me?</h3>", unsafe_allow_html=True)
    else:
        st.error("### mujhe maaf kr do pleaseee 🥺🙏")
        
    # Beautiful responsive buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes", key=f"yes_btn_{st.session_state.no_count}", type="primary", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()
            
    with col2:
        if st.button("No", key=f"no_btn_{st.session_state.no_count}", use_container_width=True):
            st.session_state.no_count += 1
            st.rerun()

