from engine.engine import ToolCallingEngine


def main():
    engine = ToolCallingEngine()

    print("AI Utility Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        response = engine.chat(user_input)

        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()