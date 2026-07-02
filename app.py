from engine.engine import ToolCallingEngine


def main():
    engine = ToolCallingEngine()

    print("AI Utility Assistant")
    print("Commands: 'exit' to quit | '/clear' to reset chat history\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("System: Goodbye!")
            break

        if not user_input:
            continue

        # Allow the user to wipe context to save token costs
        if user_input.lower() == "/clear":
            engine.messages = []
            print("System: Conversation memory cleared.\n") 
            continue

        response = engine.chat(user_input)

        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()