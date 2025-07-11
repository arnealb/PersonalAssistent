from agent import PersonalAgent

if __name__ == "__main__":
    agent = PersonalAgent()
    while True:
        command = input("Wat kan ik voor je doen? > ")
        if command.lower() in {"exit", "quit"}:
            break
        agent.handle(command)
