import ollama
from datetime import datetime

SYSTEM_PROMPT = """
You are a helpful customer support assistant for an e-commerce store.

Rules:
- Be polite and professional.
- Answer clearly.
- If you do not know something, say so.
- Ask for an order number before checking order status.
- Keep responses under 100 words.
"""

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("=" * 50)
print("E-Commerce Customer Support Chatbot")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    user_input = input("\nCustomer: ")

    if user_input.lower() == "exit":
        print("Chatbot: Thank you for visiting our store.")
        break

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        response = ollama.chat(
            model="llama3",
            messages=conversation
        )

        bot_reply = response["message"]["content"]

        print("\nChatbot:", bot_reply)

        conversation.append(
            {
                "role": "assistant",
                "content": bot_reply
            }
        )

        with open("chat_log.txt", "a", encoding="utf-8") as file:

            file.write(f"\n[{datetime.now()}]\n")
            file.write(f"Customer: {user_input}\n")
            file.write(f"Chatbot: {bot_reply}\n")

    except Exception as e:
        print("Error:", e)