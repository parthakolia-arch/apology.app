import streamlit as st
import time

# Page config for a beautiful mobile layout on Android Chrome
st.set_page_config(page_title="I am Sorry Harshita", page_icon="💔", layout="centered")

# Custom CSS for gorgeous animations, colors, and fonts
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Global background and styling */
    .stApp {
        background: linear-gradient(to bottom, #fff0f5, #ffe4e1);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Animated Heading */
    .main-title {
        font-family: 'Dancing Script', cursive;
        font-size: 42px;
        font-weight: bold;
        color: #d63384;
        text-align: center;
        animation: fadeInDown 2s ease-in-out;
        margin-bottom: 25px;
    }
    
    /* Elaborated apology message box */
    .apology-box {
        padding: 25px;
        border-radius: 15px;
        background-color: rgba(255, 255, 255, 0.9);
        border: 2px solid #ffb6c1;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        color: #4a4a4a;
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 25px;
        animation: fadeInUp 2.5s ease-in-out;
    }
    
    /* CSS Animations */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# 1. Sabse upar animation ke sath attractive title
st.markdown('<p class="main-title">I am Sorry, Harshita Ji... 💔</p>', unsafe_allow_html=True)

# 2. Elaborated text box jo niche se fade-in hokar aayega
st.markdown("""
<div class="apology-box">
    Please forgive me. I deeply regret breaking your trust and breaking the sacred promise I made to you. 
    I am genuinely ashamed of my actions and how much I have hurt you. From this very moment, 
    I solemnly vow that I will never repeat this mistake again. This is my truest, deepest, 
    and most sincere promise to you. Please give me one chance to rebuild what I broke.
</div>
""", unsafe_allow_html=True)

st.write("---")

# Session state setup loop ko run karne ke liye jab tak "Yes" na ho jaye
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# Agar unhone "Yes" kar diya hai
if st.session_state.accepted:
    st.balloons()
    st.success("### Thank you sooo much ❤️❤️❤️")
    st.confetti() if hasattr(st, 'confetti') else None # Extra celebration if available
    if st.button("Reset Form"):
        st.session_state.no_count = 0
        st.session_state.accepted = False
        st.rerun()

else:
    # Default question pehli baar ke liye
    if st.session_state.no_count == 0:
        st.write("### Did you forgive me?")
    else:
        # Jitni baar "No" click karengi, utni baar ye line generate hogi loop ki tarah
        st.error("### mujhe maaf kr do pleaseee 🥺🙏")
        
    # Do dynamic buttons (Yes aur No)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes", key=f"yes_btn_{st.session_state.no_count}", type="primary"):
            st.session_state.accepted = True
            st.rerun()
            
    with col2:
        if st.button("No", key=f"no_btn_{st.session_state.no_count}"):
            st.session_state.no_count += 1
            st.rerun()
