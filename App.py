import streamlit as st
import random

# Set page title
st.set_page_config(page_title="🎬 Welcome to ELIZA - Your Movie Companion 🤖", page_icon="🎥")

# Main Page Header
st.title("🎬 Welcome to ELIZA - The Movie Enthusiast Chatbot! 🤖")

# Introduction with a cool layout
st.markdown(
    """
    ## 🎥 Dive into the World of Movies!
    **ELIZA** is your personal movie companion, designed to chat about films in a unique and engaging way.
    Whether you're a casual viewer or a die-hard cinephile, ELIZA is here to make movie discussions fun!
    """
)

# Add an image banner with a valid URL
st.image("https://cdn.pixabay.com/photo/2019/04/24/21/55/cinema-4153289_640.jpg", caption="Let’s Talk Movies!", use_container_width=True)

# Instructions for Navigation
st.subheader("📌 How to Use ELIZA")
st.write("1. 🎬 **Go to the Chat Page** to have a movie conversation with ELIZA.")
st.write("2. 👥 **Visit the Team Page** to meet the creators behind this project.")
st.write("3. 🚀 **Stay tuned for exciting updates and new features!")

# Fun Movie Trivia
st.header("🎞️ Did You Know?")
trivia_facts = [
    "The first movie ever made was *Roundhay Garden Scene* (1888), lasting only 2.11 seconds! 🎥",
    "Did you know? *Inception* has a musical secret – the soundtrack is a slowed-down version of 'Non, Je Ne Regrette Rien' by Edith Piaf! 🎶",
    "The longest movie ever made is *Logistics* (2012), which lasts for 35 days! 🕒",
    "Pixar’s *Toy Story 2* was almost deleted due to a server error, but a backup saved it! 🧸"
]
st.write(f"💡 {random.choice(trivia_facts)}")

# Footer with a motivational movie quote
st.write("---")
st.write(
    "🎭 *'Movies touch our hearts and awaken our vision, and change the way we see things.'* - Martin Scorsese 🎬"
)
st.write("🎥 **Start exploring now using the sidebar!**")