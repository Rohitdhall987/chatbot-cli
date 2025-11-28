def main():
    print("Welcome to the Chatbot CLI!")
    print("type 'exit' or 'quit' to exit the program")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        print(f"Chatbot: You said '{user_input}'")


if __name__ == "__main__":
    main()