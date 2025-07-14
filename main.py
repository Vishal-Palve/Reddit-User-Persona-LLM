from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

from app.reddit_scraper import scrape_user_data
from app.llm_analyzer import generate_persona
from app.persona_generator import save_persona


def extract_username_from_url(url):
    return url.strip("/").split("/")[-1]


def main():
    print("🔍 Enter a Reddit profile URL (e.g., https://www.reddit.com/user/kojied/):")
    url = input("> ").strip()
    username = extract_username_from_url(url)

    print(f"\n⏳ Scraping Reddit data for u/{username}...")
    data = scrape_user_data(username)

    print("🧠 Generating user persona with LLM...")
    persona = generate_persona(data)

    print("📁 Saving output...")
    save_persona(username, persona)


if __name__ == "__main__":
    main()
