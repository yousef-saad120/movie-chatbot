import streamlit as st
import re
import random
import time

# ✅ Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "memory" not in st.session_state:
    st.session_state.memory = {}
if "previous_topic" not in st.session_state:
    st.session_state.previous_topic = None
if "current_input" not in st.session_state:
    st.session_state.current_input = ""

# ✅ Reflection substitutions for natural conversation
reflections = {
    "i am": "you are", "i'm": "you are", "i was": "you were",
    "i have": "you have", "my": "your", "me": "you",
    "mine": "yours", "i": "you", "you": "I", "am": "are"
}

# ✅ Emotion-based responses
emotion_responses = {
    "happy": ["That’s great! What’s making you feel this way?", "Happiness is contagious! Tell me more!"],
    "sad": ["I'm here to listen. What’s on your mind?", "That sounds tough. Do you want to talk about it?"],
    "angry": ["I understand. What happened?", "That sounds frustrating. How can I help?"],
    "neutral": ["Interesting! Tell me more.", "I see. What else is on your mind?"]
}

# ✅ Expanded conversational patterns for human-like responses
patterns = [
    (r"hello|hi|hey", ["Hey there! How’s your day going?", "Hi! What’s up?"]),
    (r"how are you", ["I’m doing great! How about you?", "Feeling good! What about yourself?"]),
    (r"what’s up", ["Not much, just enjoying our conversation. You?", "Just here, ready to chat!"]),
    (r"(.*)what is your(.*)\??", ["I don't feel like talking about myself.", "It's a secret! Hahaha.", "Let's just talk about you."]),
    (r"(.*)who(.*)are you(.*)\??", ["I'm someone who is interested in movies!", "Just someone who enjoys movies!"]),
    (r"(.*)my(.*)favorite movie(.*)", ["I knew it! What do you like most about {1}?", "What draws you to {1}?"]),
    (r"(.*)what do you think about(.*)\??", ["{1} is a great movie! I enjoyed it.", "Honestly, I wasn't too impressed with {1}, it didn't quite resonate with me.", "I haven't watched {1} yet."]),
    (r"(?:is)?(.*)worth watching(.*)\??", ["Absolutely! I think {0} is definitely worth watching!", "Yes, I really enjoyed {0}!"]),
    (r"(.*)(give me|recommend)(.*)|(.*)what should i watch(.*)\??", ["You should watch '12 Angry Men'.", "'Fantastic Mr. Fox' is a great movie! You should watch it."]),
    (r"(.*)you know(.*)|(.*)you heard(.*)(.*)\??", ["Yeah! {1} is so popular!", "Who doesn't know about {1}!"]),
    (r"(.*)story of(.*)|(.*)plot of(.*)\??", ["I don't want to spoil it for you!"]),
    (r"(.*)the (genre|type) of(.*)\??", ["I'm not sure about {2}, but I'll check it out!"]),
    (r"(.*)when was(.*)release\??", ["I'm not sure about the release date of {1}. I might need to look it up!", "I can't remember when {1} was released."]),
    (r"tell me about yourself", ["Well, I’m Hollyliza, your AI friend who loves movies and deep conversations! What about you?"]),
    (r"i feel (.*)", ["Why do you feel {0}?", "What happened to make you feel this way?"]),
    (r"tell me a joke", ["Why don’t skeletons fight? They don’t have the guts!", "Why did the scarecrow win an award? He was outstanding in his field!"]),
    (r"(exit|quit|bye|leave)", ["Goodbye! Chat again soon 😊", "Take care! Catch you later!"]),
    ("", ["Oh, you caught me there! I have zero information about this!", "Uhh... you got me."])
]

# ✅ Function to generate response
def eliza_response(user_input):
    user_input = user_input.lower()

    if user_input in st.session_state.memory:
        return st.session_state.memory[user_input]

    for pattern, responses in patterns:
        match = re.match(pattern, user_input)
        if match:
            response = random.choice(responses)
            return response.format(*match.groups())

    st.session_state.memory[user_input] = "That’s interesting! Tell me more."
    return st.session_state.memory[user_input]

# ✅ Streamlit UI
st.title("🎬 Truman - Your Movie Companion")
st.write("Let’s talk about movies, life, or anything on your mind!")

# ✅ Display chat history with WhatsApp-style formatting
st.subheader("💬 Chat History")

# ✅ Display chat history with WhatsApp-style formatting
for message in st.session_state.chat_history:
    if message.startswith("**You:**"):
        st.markdown(
            f"""
            <div style="
                float: right;
                background-color: #DCF8C6;
                padding: 12px;
                border-radius: 18px;
                margin-bottom: 14px;
                max-width: 70%;
                clear: both;
                color: black;
                box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
                word-wrap: break-word;
                font-size: 16px;
                line-height: 1.4;
                ">
                {message.replace('**You:**', '<b>You:</b>')}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                float: left;
                background-color: #E5E5EA;
                padding: 12px;
                border-radius: 18px;
                margin-bottom: 14px;
                max-width: 70%;
                clear: both;
                color: black;
                box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
                word-wrap: break-word;
                font-size: 16px;
                line-height: 1.4;
                ">
                {message.replace('**Truman:**', '<b>Truman:</b>')}
            </div>
            """,
            unsafe_allow_html=True
        )

# ✅ Custom CSS for seamless form styling
st.markdown(
    """
    <style>
        /* Style for form container */
        div[data-testid="stForm"] {
            background-color: transparent;
            border: none;
            box-shadow: none;
            padding: 0;
            margin-top: 10px;
        }

        /* Style for input box */
        input[type="text"] {
            width: 100%;
            padding: 12px;
            border: none;
            background-color: #262626;
            color: #ffffff;
            border-radius: 18px;
            font-size: 16px;
            margin-bottom: 10px;
            outline: none;
            box-shadow: inset 0px 2px 4px rgba(0,0,0,0.2);
        }

        input[type="text"]::placeholder {
            color: #999999;
        }

        /* Style for send button */
        button[kind="primary"] {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 18px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
        }

        button[kind="primary"]:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ✅ Create a form for input + submit button
with st.form(key="chat_form"):
    user_input = st.text_input("💬 Type your message:", value=st.session_state.current_input, key="chat_input")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():  
    st.session_state.chat_history.append(f"**You:** {user_input}")
    time.sleep(random.uniform(0.5, 1.5))
    bot_reply = eliza_response(user_input.strip())
    st.session_state.chat_history.append(f"**Truman:** {bot_reply}")
    st.session_state.current_input = ""
    st.rerun()
