def detect_intent(command: str) -> str:
    cmd = command.lower()
    if "mail" in cmd or "e-mail" in cmd:
        return "read_email"
    if "afspraak" in cmd or "event" in cmd:
        return "create_event"
    if "herinner" in cmd or "reminder" in cmd:
        return "set_reminder"
    return "unknown"
