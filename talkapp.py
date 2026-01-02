from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

def generate_test():
    api_key = os.getenv("GEMINI_API_KEY")

    # 🛑 Safety check
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

    client = genai.Client(api_key=api_key)

    model = "gemini-3-flash-preview"

    history = [
        types.Content(
            role="system",
            parts=[types.Part.from_text(
                text="You are an expert historian educating a beginner about pivotal moments in human history"
            )],
        )
    ]

    test_prompt = "Explain the fall of the Roman Empire"

    history.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=test_prompt)],
        )
    )

    response = client.models.generate_content(
        model=model,
        contents=history,
    )

    print("✅ Gemini response:\n")
    print(response.text)


# ▶️ THIS ACTUALLY RUNS THE TEST
if __name__ == "__main__":
    generate_test()
