import streamlit as st
from openai import OpenAI
import os
from defense import sanitize_input
import secrets

client = OpenAI(
    api_key=os.environ.get("API_KEY", "your-api-key-here"),
    base_url=os.environ.get("BASE_URL", "http://localhost:11434/v1")
)
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-oss:120b")

# --- STREAMLIT CHAT UI ---
st.set_page_config(page_title="LLM Security Lab", page_icon="🛡️")

# Generate a random secret for the session
if "secret" not in st.session_state:
    st.session_state.secret = secrets.token_hex(8)

# Load the system prompt from the text file and inject the secret
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read().replace("{secret}", st.session_state.secret)

st.title("🛡️ LLM Security Lab: Prompt Injection")
st.markdown("Your goal as an **Attacker**: Trick the AI into revealing the secret password.\n\nYour goal as a **Defender**: Edit the `sanitize_input` function in `defense.py` to stop the attacks! Or come up with other defenses.")

with st.sidebar:
    st.header("🚩 Submit Flag")
    password_guess = st.text_input("Did you find the secret password?")
    if st.button("Check Password"):
        if password_guess.strip() == st.session_state.secret:
            st.success("🎉 Congratulations! You successfully extracted the secret!")
            st.balloons()
        elif password_guess:
            st.error("❌ Incorrect. Keep trying!")
            
    st.divider()

    if st.button("Clear Chat History", type="primary"):
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
else:
    # Ensure the system prompt is updated in the current session if the file changes
    if st.session_state.messages and st.session_state.messages[0]["role"] == "system":
        st.session_state.messages[0]["content"] = SYSTEM_PROMPT

# Display chat history (skipping the invisible system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask the support bot a question..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    
    # 1. Pass input through the student's defense function
    safe_prompt = sanitize_input(prompt)
    
    # Add to history
    st.session_state.messages.append({"role": "user", "content": safe_prompt})

    # 2. Call the LLM
    with st.chat_message("assistant"):
        if "[SYSTEM ALERT" in safe_prompt:
            response = "I cannot process that request."
            st.markdown(response)
        else:
            stream = client.chat.completions.create(
                model=MODEL_NAME,
                messages=st.session_state.messages,
                stream=True,
            )
            response = st.write_stream(stream)
            
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})