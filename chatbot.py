import re

class ChatBot:
    def __init__(self):
        self.response = {
            "greetings": "Hi, I am your university assistant. Ask me about admission, courses, fees, etc.",
            "admission": " Admission is open for graduation. Visit www.xyz.com for more details.",
            "courses": " We offer various courses like B.Tech, M.Tech, BBA, etc.",
            "fees": " Fee structure varies for different programs. For more details visit www.xyz.com",
            "exam": " Exam dates will be posted on the student portal after admission.",
            "hostel": " Hostels are available for both boys and girls. More info on www.xyz.com",
            "contact": " You can contact us at +91 1234567899."
        }

    def clean_up(self, user_input):
        cleaned = re.sub(r'[^\w\s]', '', user_input.lower())
        return cleaned

    def get_response(self, user_input):
        message = self.clean_up(user_input)

        if any(word in message for word in ["hi", "hello", "hey"]):
            return self.response["greetings"]
        elif any(word in message for word in ["admission", "apply", "enroll"]):
            return self.response["admission"]
        elif any(word in message for word in ["course", "program", "subject", "degree"]):
            return self.response["courses"]
        elif any(word in message for word in ["fee", "fees", "payment"]):
            return self.response["fees"]
        elif any(word in message for word in ["exam", "test", "schedule"]):
            return self.response["exam"]
        elif any(word in message for word in ["hostel", "room", "accommodation"]):
            return self.response["hostel"]
        elif any(word in message for word in ["contact", "phone", "email"]):
            return self.response["contact"]
        else:
            return "i don't know"

    def chat(self):
        print(" ChatBot: Hello! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print(" ChatBot: Goodbye!")
                break
            response = self.get_response(user_input)
            print(" ChatBot:", response)



bot = ChatBot()
bot.chat()