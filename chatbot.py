import json
import random
from datetime import datetime

# 1. Using a Dictionary for flexible intents and multiple randomized responses
INTENTS = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "sup", "greetings"],
        "responses": ["Hi there!", "Hello!", "Hey! How can I help you today?", "Greetings!"]
    },
    "wellbeing": {
        "keywords": ["how are you", "how's it going", "how do you do"],
        "responses": ["I'm doing great, thanks for asking!", "Fantastic! How about you?", "I'm just a bunch of code, but I'm feeling good!"]
    },
    "goodbyes": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit"],
        "responses": ["Goodbye!", "See you later!", "Have a great day!", "Bye! Take care."]
    }
}

def clean_input(user_input):
    """Sanitizes the input by lowering case and stripping whitespace."""
    return user_input.lower().strip()

def get_advanced_response(user_input):
    """Finds a matching intent based on keywords and returns a random response."""
    cleaned = clean_input(user_input)
    
    # 2. Advanced Matching: Checks if ANY keyword is inside the user's input
    for intent, data in INTENTS.items():
        for keyword in data["keywords"]:
            if keyword in cleaned:
                # Pick a random response from the list to feel more human
                return random.choice(data["responses"]), intent
                
    return "I'm not quite sure I understand. Could you rephrase that?", "unknown"

def save_chat_log(history):
    """Saves the conversation history to a JSON file."""
    with open("chat_history.json", "w") as file:
        json.dump(history, file, indent=4)

def start_chatbot():
    print("Chatbot: AI Activated. (Type 'bye' to exit)")
    chat_history = []
    
    while True:
        user_message = input("You: ")
        if not user_message.strip():
            continue
            
        bot_message, intent = get_advanced_response(user_message)
        print(f"Chatbot: {bot_message}")
        
        # Log the conversation with timestamps
        chat_history.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": user_message,
            "bot": bot_message,
            "intent_detected": intent
        })
        
        if intent == "goodbyes":
            print("\n[Saving chat logs...]")
            save_chat_log(chat_history)
            print("[History saved to chat_history.json. Goodbye!]")
            break

if __name__ == "__main__":
    start_chatbot()