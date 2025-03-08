import streamlit as st
import random
import time

# Set page title
st.set_page_config(page_title="🎬 Welcome to Truman - Your Movie Companion 🤖", page_icon="🎥")

# Main Page Header
st.title("🎬 Welcome to Truman - The Movie Enthusiast Chatbot! 🤖")

# Introduction
st.markdown(
    """
    ## 🌟 Why Truman?  
    Truman is inspired by *The Truman Show* (1998), where the main character, Truman Burbank, lived in a world that was carefully controlled behind the scenes.  
    Just like Truman discovered the truth about his world, this chatbot is here to reveal the hidden secrets of the movie universe!  
    Truman is more than just a chatbot — he’s your movie-loving friend who knows all the trivia, facts, and behind-the-scenes details.  
    """
)

# Add an image banner
st.image("https://cdn.pixabay.com/photo/2019/04/24/21/55/cinema-4153289_640.jpg", caption="Let’s Talk Movies!", use_container_width=True)

# 🎯 Game Section
st.markdown("## 🎯 Test Your Movie Knowledge with Truman!")
st.write(
    """
    Think you know movies better than Truman?  
    Try this quick movie trivia challenge — answer the questions and see how well you score!  
    Truman might know the answers… but do you?  
    """
)

# Quiz Data
questions = [
    {"question": "Who directed the movie *Inception*?", "choices": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Quentin Tarantino"], "answer": "Christopher Nolan"},
    {"question": "What is the highest-grossing film of all time?", "choices": ["Titanic", "Avatar", "Avengers: Endgame", "The Lion King"], "answer": "Avatar"},
    {"question": "Which movie features the line 'I see dead people'?", "choices": ["The Sixth Sense", "The Shining", "Psycho", "Halloween"], "answer": "The Sixth Sense"},
    {"question": "What is the name of the hobbit played by Elijah Wood in *The Lord of the Rings*?", "choices": ["Sam", "Frodo", "Merry", "Pippin"], "answer": "Frodo"},
    {"question": "Who played the iconic character Jack Dawson in *Titanic*?", "choices": ["Leonardo DiCaprio", "Brad Pitt", "Johnny Depp", "Tom Cruise"], "answer": "Leonardo DiCaprio"}
]

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'show_quiz' not in st.session_state:
    st.session_state.show_quiz = False
if 'game_finished' not in st.session_state:
    st.session_state.game_finished = False

# Function to handle quiz
def handle_answer(choice):
    if choice == questions[st.session_state.current_question]['answer']:
        st.session_state.score += 1

    # Go to next question
    st.session_state.current_question += 1

    if st.session_state.current_question >= len(questions):
        st.session_state.game_finished = True

    st.rerun()

def run_quiz():
    if st.session_state.current_question < len(questions):
        q = questions[st.session_state.current_question]
        st.write("---")

        # Display the question
        st.markdown(f"### {q['question']}")

        # Create two columns for answers
        col1, col2 = st.columns(2)

        # Answer buttons (auto-submit on click)
        with col1:
            if st.button(q['choices'][0]):
                handle_answer(q['choices'][0])
            if st.button(q['choices'][1]):
                handle_answer(q['choices'][1])

        with col2:
            if st.button(q['choices'][2]):
                handle_answer(q['choices'][2])
            if st.button(q['choices'][3]):
                handle_answer(q['choices'][3])

# Display results when the game ends
def display_results():
    st.write("## 🏆 Results 🏆")
    st.write(f"**Final Score: {st.session_state.score}/{len(questions)}**")

    if st.session_state.score <= 2:
        st.error("You should definitely talk to Truman — he'll help you brush up on your movie knowledge!")
    elif st.session_state.score <= 4:
        st.warning("Not bad! But Truman might know a few more secrets about the movie world.")
    else:
        st.success("You're a true movie buff! Truman is impressed.")

    # Reset quiz
    if st.button("Play Again"):
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.show_quiz = True
        st.session_state.game_finished = False
        st.rerun()

# Start Button
if st.button("🎯 Start the Game"):
    st.session_state.show_quiz = True
    st.session_state.score = 0
    st.session_state.current_question = 0
    st.session_state.game_finished = False

# Show quiz or results in a popup
if st.session_state.show_quiz:
    with st.expander("📢 Movie Trivia", expanded=True):
        if st.session_state.game_finished:
            display_results()
        else:
            run_quiz()


# ➡️ Trivia Facts Section (With Clean Animation)
st.markdown("---")
st.markdown("## 🎬 Did You Know?")

trivia_facts = [
    "Pixar’s *Toy Story 2* was almost deleted due to a server error, but a backup saved it! 🧸",
    "The first movie ever made was *Roundhay Garden Scene* (1888), lasting only 2.11 seconds! 🎥",
    "*Inception* has a musical secret – the soundtrack is a slowed-down version of 'Non, Je Ne Regrette Rien' by Edith Piaf! 🎶",
    "The longest movie ever made is *Logistics* (2012), which lasts for 35 days! 🕒"
]

# Typing effect (simple font)
placeholder = st.empty()
for _ in range(100):  # Loop for continuous animation
    for fact in trivia_facts:
        full_text = f"💡 {fact}"
        for i in range(len(full_text) + 1):
            placeholder.markdown(f"<p style='font-family: sans-serif; font-size: 18px; font-weight: 400;'>{full_text[:i]}</p>", unsafe_allow_html=True)
            time.sleep(0.05)  # Typing speed

        time.sleep(1.5)  # Pause before deleting

        for i in range(len(full_text), 0, -1):
            placeholder.markdown(f"<p style='font-family: sans-serif; font-size: 18px; font-weight: 400;'>{full_text[:i]}</p>", unsafe_allow_html=True)
            time.sleep(0.02)  # Deleting speed

        time.sleep(0.5)  # Pause before next fact


# Footer
st.write("---")
st.write("🎭 *'Movies touch our hearts and awaken our vision, and change the way we see things.'* - Martin Scorsese 🎬")
st.write("🎥 **Start exploring now using the sidebar!**")
