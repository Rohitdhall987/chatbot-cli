from dotenv import load_dotenv
import os
from llm import LLM

def main():
    print("Welcome to the Chatbot CLI!")
    print("type 'exit' or 'quit' to exit the program")

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    llm = LLM(api_key)

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        print("Gemini: " + llm.generate("gemini-2.0-flash", user_input))


if __name__ == "__main__":
    main()