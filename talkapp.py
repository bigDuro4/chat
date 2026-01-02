from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

def generate():
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"

    history = [
        types.Content(
            role="system",
            parts=[types.Part.from_text(
                text="You are an expert historian educating a beginner about pivotal moments in human history"
            )],
        )
    ]

    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        history.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_input)],
            )
        )

        response = client.models.generate_content(
            model=model,
            contents=history,
        )

        model_text = response.text
        print(f"Bot: {model_text}\n")

        history.append(
            types.Content(
                role="model",
                parts=[types.Part.from_text(text=model_text)],
            )
        )

if __name__ == "__main__":
    generate()
