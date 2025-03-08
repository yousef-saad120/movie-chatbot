import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Team - Truman Movie Chatbot",
    page_icon="🎬",
    layout="centered"
)

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #f0f0f0;
        }
        .main-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-bottom: 1rem;
        }
        .subtitle {
            font-size: 1.5rem;
            color: #ffffff;
            font-weight: bold;
            margin-bottom: 0.5rem;
            border-bottom: 2px solid #ffffff;
            padding-bottom: 0.5rem;
            display: inline-block;
        }
        .team-member {
            background-color: #1e1e1e;
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            margin-bottom: 1rem;
            transition: transform 0.3s ease;
            color: #f0f0f0;
            border: 1px solid #333;
        }
        .team-member:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
        }
        .highlight {
            color: #ffffff;
            font-weight: bold;
        }
        .footer {
            margin-top: 2rem;
            font-size: 0.9rem;
            color: #888;
            text-align: center;
        }
        a.button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #ffffff;
            color: #121212;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: background-color 0.3s;
            margin-top: 20px;
            border: 2px solid #ffffff;
        }
        a.button:hover {
            background-color: #e0e0e0;
            color: #121212;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🎭 Meet the Team Behind Truman Movie Chatbot</div>', unsafe_allow_html=True)

st.write("Welcome to the **Team Page**! Get to know the brilliant minds behind this Truman-style movie chatbot.")

# Team Members Section
st.markdown('<div class="subtitle">👥 Team Members</div>', unsafe_allow_html=True)

# Function to display team member info
def display_team_member(name, role, description):
    st.markdown(
        f"""
        <div class="team-member">
            <h4>{name}</h4>
            <p><span class="highlight">Role:</span> {role}</p>
            <p>{description}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Team Members

display_team_member("Rind Al-Ajmi", "Regex & Chatbot Logic", 
                    "Developed regex-based patterns and improved chatbot interactions.")

display_team_member("Abdullah Al-Zahrani", "Regex & Chatbot Logic", 
                    "Developed the pattern-matching system and chatbot response logic using regular expressions.")

display_team_member("Abdulaziz Al-Kharjy", "Regex & Chatbot Logic", 
                    "Contributed to building and refining the chatbot's conversational flow using regex.")

display_team_member("Majd Al-Otaibi", "Regex & Chatbot Logic", 
                    "Enhanced chatbot responses and ensured smooth conversational logic.")

display_team_member("Yousef Al-Dayhani", "Streamlit Developer", 
                    "Designed and implemented all Streamlit pages and structured the web application.")


# Technologies Used Section
st.markdown('<div class="subtitle">📌 Technologies Used</div>', unsafe_allow_html=True)
technologies = ["Python (for chatbot logic)", "Regular Expressions (Regex) for pattern matching", "Streamlit (for the web interface)"]
for tech in technologies:
    st.write(f"- {tech}")

# Future Improvements Section
st.markdown('<div class="subtitle">🚀 Future Improvements</div>', unsafe_allow_html=True)
improvements = [
    "Expanding chatbot responses for a wider variety of movies.",
    "Enhancing conversation flow with more dynamic question-based responses.",
    "Adding a memory feature to remember previous interactions."
]
for improvement in improvements:
    st.write(f"- {improvement}")

# Navigation Link
st.markdown(
    '<div style="text-align: center; margin-top: 1.5rem;">'
    '<a href="/" class="button">👉 Go Back to Chat Page</a>'
    '</div>',
    unsafe_allow_html=True
)

# Footer
st.markdown('<div class="footer">© 2025 Truman Movie Chatbot Team. All Rights Reserved.</div>', unsafe_allow_html=True)
