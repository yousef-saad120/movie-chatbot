import streamlit as st

# Team Page - Information about the project and contributors
st.set_page_config(page_title="Team - ELIZA Movie Chatbot", page_icon="🎬")

st.title("🎭 Meet the Team Behind ELIZA Movie Chatbot")

st.write("Welcome to the **Team Page**! Here, you can learn more about the creators of this ELIZA-style movie chatbot.")

# Team Member Details
st.header("👥 Team Members")

st.subheader("Abdullah Al-Zahrani")
st.write("Role: Streamlit Developer")
st.write("Description: Worked on designing and implementing the Streamlit pages for the chatbot interface.")

st.subheader("Yousef Al-Dayhani")
st.write("Role: Streamlit Developer")
st.write("Description: Focused on building and structuring the Streamlit web application for the chatbot.")

st.subheader("Abdulaziz Al-Kharjy")
st.write("Role: Regex & Chatbot Logic")
st.write("Description: Developed the pattern-matching system and chatbot response logic using regular expressions.")

st.subheader("Majd Al-Otaibi")
st.write("Role: Regex & Chatbot Logic")
st.write("Description: Contributed to refining chatbot responses and ensuring smooth conversational flow.")

st.subheader("Rind Al-Ajmy")
st.write("Role: Regex & Chatbot Logic")
st.write("Description: Assisted in building regex-based responses and testing chatbot interactions.")

# Project Overview
st.header("🎬 Project Overview")
st.write(
    "This project is an ELIZA-style chatbot that responds to user queries about movies using pattern matching and substitution."
    " Instead of using AI or databases, it mimics a conversation between a movie enthusiast and someone with little knowledge about films."
)

st.write("Users can ask about movies, directors, and recommendations, and the chatbot will respond with questions to maintain an interactive conversation.")

st.header("📌 Technologies Used")
st.write("- **Python** (for chatbot logic)")
st.write("- **Regular Expressions (Regex)** (for pattern matching)")
st.write("- **Streamlit** (for the web interface)")

st.header("🚀 Future Improvements")
st.write("- Expanding chatbot responses for a wider variety of movies.")
st.write("- Enhancing conversation flow with more dynamic question-based responses.")
st.write("- Adding a memory feature to make the chatbot remember previous interactions.")

st.write("\n")
st.write("👉 Go back to the **Chat Page** to interact with ELIZA!")
