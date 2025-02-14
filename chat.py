import google.generativeai as ai
import dotenv
import os

# Load the API key from environment variables
dotenv.load_dotenv()

API_KEY = os.getenv("GENEMAI_API_KEY")

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodby")
        break
    response = chat.send_message(user_input)
    print("Chatbot:", response.text)
    