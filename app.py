import streamlit as st # type: ignore
import random
from datetime import datetime

#main structure of the app
st.set_page_config(page_title="Growth Mindset App By Nabeel", page_icon="🌱")

st.title("Growth Mindset Challenge App By Nabeel Ali") 
st.write("Embrace challenges, learn from mistakes, and persist through difficulties!")

#Daily Challenges:
challenges = [
    "Try learning a new skill today.",
    "Seek feedback on your recent work.",
    "Step out of your comfort zone in a small way."
]
daily_challenge = random.choice(challenges)
st.header("Today's Challenge")
st.write(daily_challenge)

#Reflection Journal:
st.header("Reflection Journal")
reflection = st.text_area("Reflect on today's experiences:")
if st.button("Save Reflection"):
    with open("reflections.txt", "a") as file:
        file.write(f"{datetime.now()}: {reflection}\n")
    st.success("Reflection saved!")

#Progress Tracking:
st.header("Set a Goal")
goal = st.text_input("Enter your goal:")
progress = st.slider("Progress", 0, 100, 0)
if st.button("Save Progress"):
    with open("progress.txt", "a") as file:
        file.write(f"{datetime.now()}: {goal} - {progress}%\n")
    st.success("Progress saved!")


#Inspirational Quotes:
quotes = [
    "The only way to achieve the impossible is to believe it is possible.",
    "Mistakes are proof that you are trying.",
    "Every day is a new opportunity to grow and improve."
]
st.header("Inspirational Quote")
st.write(random.choice(quotes))
