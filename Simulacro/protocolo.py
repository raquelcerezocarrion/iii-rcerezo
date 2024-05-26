# protocol.py
import datetime

class Protocol:
    @staticmethod
    def handle_message(message: str) -> str:
        message = message.strip().upper()
        if message == "FECHA":
            return datetime.datetime.now().strftime("%Y-%m-%d")
        elif message == "HORA":
            return datetime.datetime.now().strftime("%H:%M:%S")
        else:
            return "ERROR"

