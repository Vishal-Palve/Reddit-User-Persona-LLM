import os
import requests
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def build_prompt(data):
    text = "\n\n".join(data["posts"][:10] + data["comments"][:10])
    return f"""
Based on the following Reddit posts and comments, generate a detailed user persona with personality traits, interests, and behavior. Cite a post/comment after each trait.

{text}
"""


def generate_persona(data):
    prompt = build_prompt(data)

    headers = {
        "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.7,
    }

    response = requests.post("https://api.together.xyz/v1/completions", json=payload, headers=headers)

    try:
        return response.json()['choices'][0]['text'].strip()
    except Exception as e:
        print("[❌] API Error:", e)
        print("Full response:", response.text)
        return "[ERROR] Failed to generate persona."
