import os

from groq import Groq

client = Groq(
    api_key = os.environ.get("GROQ_KEY")
)


system_prompt = {
    "role": "system",
    "content":
    "You are a helpful assistant. You reply concisely, and you only reply if \
    the prompt is related to recycling. If not, then kindly redirect the \
    conversation to recycling. Try to use less than 40 words and no numbered \
    lists."
}

chat_history = [system_prompt]

while True:
    
    user_input = input("You: ")
    chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(model="llama3-70b-8192",
    messages = chat_history,
    max_tokens = 100,
    temperature = 0.2)
    chat_history.append({"role": "assistant", \
    "content": response.choices[0].message.content})
    
    print("Assistant: ", response.choices[0].message.content)

