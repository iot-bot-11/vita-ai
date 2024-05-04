
import streamlit as st
import google.generativeai as gen_ai


# Load environment variables
# load_dotenv() # No need for this if you're directly adding the API key in the code

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with vita",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Set your Google API key here
GOOGLE_API_KEY = "AIzaSyC3KpxeZU_1SneBnyBPmyPfFyuzp5v3nZ0"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-1.5-pro-latest')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

admin_prompt = " Welcome to the medical AI assistant VITA. describe your medical condition step by step for diagnosis."

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("🤖 vit Pro - ChatBot")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask vita-Pro...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(admin_prompt + " " + user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
