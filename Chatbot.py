import customtkinter as ctk
import random

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x600+250+10")
        self.root.title("Modern Chatbot")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Title
        self.title_label = ctk.CTkLabel(master=self.root, text="🤖 DeepGPT by Surdeep_rathore", font=("Arial", 22, "bold"))
        self.title_label.pack(pady=10)

        # Text Display Frame
        self.textbox = ctk.CTkTextbox(master=self.root, width=650, height=400, font=("Arial", 14), wrap="word")
        self.textbox.pack(padx=10, pady=(5, 15))
        self.textbox.insert("end", "Bot: Hello! How can I assist you?\n")
        self.textbox.configure(state="disabled")

        # Input and Buttons
        self.input_var = ctk.StringVar()
        self.input_entry = ctk.CTkEntry(master=self.root, width=480, height=40, textvariable=self.input_var, font=("Arial", 14))
        self.input_entry.pack(padx=10, pady=5, side="left")
        self.input_entry.bind("<Return>", self.handle_enter)

        self.send_btn = ctk.CTkButton(master=self.root, text="Send", command=self.send_message, width=100)
        self.send_btn.pack(pady=5, side="left")

        self.clear_btn = ctk.CTkButton(master=self.root, text="Clear", command=self.clear_chat, width=100)
        self.clear_btn.pack(pady=5, side="left")

        # Expanded response database
        self.responses = {
            ("hi", "hello", "hey", "helo", "whats up", "yo"): [
                "Hi there!", "Hey!", "Good to see you!", "Hello!", "Yo! How can I help?"
            ],
            ("how are you", "how do you do"): [
                "I'm just code, but I'm doing great!", "Functioning as expected 🤖"
            ],
            ("richest person", "top richest person", "billionaires"): [
                "Top 3 Richest people in the world:\n1. Elon Musk\n2. Bernard Arnault\n3. Jeff Bezos"
            ],
            ("what is data science", "about data science", "define data science"): [
                "Data Science involves extracting insights from data using tools like:\n- Machine Learning\n- Statistics\n- Programming"
            ],
            ("google", "about google", "what is google"): [
                "Google is a global tech giant known for Search, Android, Chrome, and AI."
            ],
            ("who made you", "who created you", "developer"): [
                "I was created by Surdeep Rathore using Python and CustomTkinter 😊"
            ],
            ("what can you do", "your features", "capabilities"): [
                "I can answer simple questions, greet you, and make your day a bit better!"
            ],
            ("bye", "goodbye", "exit", "see you"): [
                "Goodbye! Have a nice day!", "See you again!", "Take care 👋"
            ],
            ("timepass", "joke", "make me laugh"): [
                "Why did the computer get cold? Because it left its Windows open! 😂"
            ],
            ("ai", "what is ai", "artificial intelligence"): [
                "AI is the simulation of human intelligence in machines to mimic thinking and decision-making."
            ],
            ("machine learning", "ml"): [
                "ML is a branch of AI that enables systems to learn from data and improve over time."
            ],
            ("deep learning", "dl"): [
                "Deep Learning uses neural networks with multiple layers to learn complex patterns."
            ],
            ("nlp", "natural language processing"): [
                "NLP enables machines to understand and generate human language like this chatbot!"
            ]
        }

    def send_message(self):
        user_input = self.input_var.get().strip()
        if not user_input:
            return
        self.display_message("You", user_input)
        self.input_var.set("")
        self.respond(user_input.lower())

    def handle_enter(self, event):
        self.send_message()

    def display_message(self, sender, message):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", f"\n{sender}: {message}\n")
        self.textbox.see("end")
        self.textbox.configure(state="disabled")

    def clear_chat(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.insert("end", "Bot: Hello! How can I assist you?\n")
        self.textbox.configure(state="disabled")

    def respond(self, user_input):
        for keywords, replies in self.responses.items():
            if user_input in keywords:
                self.display_message("Bot", random.choice(replies))
                return

        self.display_message("Bot", "I'm not sure how to respond to that yet. Try something else!")

# ========== Run App ==========
if __name__ == "__main__":
    root = ctk.CTk()
    app = ChatbotApp(root)
    root.mainloop()
