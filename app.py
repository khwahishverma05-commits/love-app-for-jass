import streamlit as st
import random
import time

st.set_page_config(page_title="For Jass 💖", layout="centered")

st.markdown("<h1 style='text-align:center;color:#ff4d6d;'>Hey Jass 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>I made something for you 🥺</h3>", unsafe_allow_html=True)

st.write("")

# typing effect
text = "You’re my favorite person, my peace, my everything 💖"
placeholder = st.empty()

typed = ""
for char in text:
    typed += char
    placeholder.markdown(f"<h3 style='text-align:center;'>{typed}</h3>", unsafe_allow_html=True)
    time.sleep(0.03)

st.write("")

messages = [
    "I love you so much ❤️",
    "You make my life beautiful 🌸",
    "I choose you. Always. 💍",
    "Forever yours 💫"
]

if st.button("Click Me 💌"):
    st.markdown(f"<h3 style='text-align:center;'>{random.choice(messages)}</h3>", unsafe_allow_html=True)

st.write("")

st.markdown("<h2 style='text-align:center;'>Do you love me? 😏</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("YES 😍"):
        st.balloons()
        st.success("I knew it 😭💖 Love you Jass 💘")

with col2:
    if st.button("NO 😒"):
        st.error("Wrong answer 😤 Try again 😈")

st.write("")
st.markdown("<h4 style='text-align:center;'>Made with love 💖 just for you, Jass 🥺</h4>", unsafe_allow_html=True)
