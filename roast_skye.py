
import streamlit as st
import random

# Custom CSS styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=UnifrakturCook:wght@700&display=swap');

        h1.gothic-title {
            font-family: 'UnifrakturCook', cursive;
            text-align: center;
            font-size: 4em;
            margin-bottom: 0.2em;
            color: #cc0000; /* blood red */
        }

        .roast-text {
            font-family: 'Special Elite', monospace;
            font-size: 1.6em;
            color: #cc0066;
            text-align: center;
            padding: 1em;
        }

        .stButton>button {
            background-color: #ff66b2;
            color: white;
            padding: 0.75em 2em;
            font-size: 1.3em;
            border-radius: 12px;
            display: block;
            margin: 0 auto;
            border: none;
            transition: background-color 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #ff3385;
        }

        img {
            display: block;
            margin: 0 auto 20px auto;
        }
    </style>
""", unsafe_allow_html=True)

# Sparkling heart GIF 💖
st.image("https://i.pinimg.com/originals/78/4e/43/784e43d7b7f90f9609e5b160cd61535e.gif", width=200)

# Title & subtitle
st.markdown("<h1 class='gothic-title'>Feeling sad?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Slam this button to dunk on Skye’s dumbass!</p>", unsafe_allow_html=True)

# Load roasts
@st.cache_data
def load_roasts():
    with open("roasts.txt", "r", encoding="utf-8") as file:
        return list(set(line.strip() for line in file if line.strip()))

roasts = load_roasts()

# Button
if st.button("Roast Skye"):
    st.markdown(f"<div class='roast-text'>{random.choice(roasts)}</div>", unsafe_allow_html=True)
