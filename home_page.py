import streamlit as st

st.set_page_config(page_title="Game Hub", page_icon="🎮", layout="centered")

games = {
    "Ping Pong": {
        "description":"Ping Pong, also known as table tennis, is a fast-paced game where players use paddles to hit a lightweight ball across a table divided by a net. The objective is to score points by making the ball land on the opponent's side without being returned.",
        "link":"https://siddharth-sinha00.itch.io/ping-pong"
    },
    "Classic Snake": {
        "description":"Snake Game is a classic arcade game where players guide a growing snake to eat food while avoiding collisions.",
        "link":"https://siddharth-sinha00.itch.io/classic-snake"
    },
    "Space Invader": {
        "description":"Space Invader is a thrilling, fast-paced shooting game set in the vast reaches of space. Your mission? Defend your spacecraft from relentless waves of alien invaders. Armed with powerful lasers, you must shoot down the aliens before they can reach your spacecraft and chip away at its health.",
        "link":"https://siddharth-sinha00.itch.io/space-invader"
    },
    "Hangman": {
        "description":"Hangman is a classic word-guessing game where players try to figure out a hidden word by guessing letters. Each incorrect guess adds a part to a hanging stick figure. The goal is to guess the word before the figure is fully drawn.",
        "link":"https://project-hangman.streamlit.app/"
    }
}

st.title("🎮 Welcome to Game Hub!")
st.subheader("Select a game to learn more and play!")

for game,details in games.items():
    if st.button(game,key=game):
        st.write(details["description"])
        st.markdown(
            f'<a href="{details["link"]}" target="_blank" style="display:inline-block; text-decoration:none; background-color:#4CAF50; color:white; padding:10px 20px; border-radius:5px; font-weight:bold;">Play Now</a>',
            unsafe_allow_html=True,
        )
        st.markdown("---")
