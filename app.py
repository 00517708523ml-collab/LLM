
import os
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. "
                   "Answer in simple and clear language."
    }
]

def chatbot():

    print("\n🤖 Welcome to My AI Chatbot!")
    print("Type 'exit' to stop the chatbot.\n")

    while True:

        # Get user input
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        # Add user message
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            # Call Groq API
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                temperature=0.7,
                max_completion_tokens=1024
            )

            # Extract response
            bot_response = response.choices[0].message.content

            # Display response
            print("\nBot:", bot_response, "\n")

            # Save assistant response
            messages.append({
                "role": "assistant",
                "content": bot_response
            })

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    chatbot()
