from intents import email, calendar, reminders
from utils.parser import detect_intent

class PersonalAgent:
    def handle(self, command: str):
        intent = detect_intent(command)
        
        if intent == "read_email":
            email.read_emails()
        elif intent == "create_event":
            calendar.get_events(5)
        elif intent == "set_reminder":
            reminders.set_reminder()
        else:
            print("Sorry, dat begrijp ik niet.")
