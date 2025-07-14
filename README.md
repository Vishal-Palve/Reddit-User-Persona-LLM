# 🧠 Reddit User Persona Generator using LLMs

Generate detailed psychological profiles of Reddit users by analyzing their posts and comments using a free open-source LLM via Together.ai.

---

## ✨ Features

- 🔍 Scrapes posts and comments from any Reddit profile
- 🤖 Uses Together.ai's Mixtral-8x7B model (Free, Open Source)
- 🧠 Builds structured user personas (traits, behavior, interests)
- 📝 Saves persona outputs as `.txt` files
- 📦 Modular, PEP-8 compliant, beginner-friendly codebase

---

## 🚀 Tech Stack

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![PRAW](https://img.shields.io/badge/PRAW-Reddit%20API-yellow)
![Together.ai](https://img.shields.io/badge/LLM-Together.ai-green)
![License](https://img.shields.io/badge/License-MIT-blue)

- **Python**
- **PRAW** – Reddit scraping
- **Together.ai** – LLM-powered persona generation
- **dotenv** – Secure API key management
- **requests** – LLM API integration

---

## 📁 Project Structure

```
Reddit-User-Persona-LLM/
│
├── app/
│   ├── reddit_scraper.py         # Scrapes Reddit data
│   ├── llm_analyzer.py           # Generates persona via Together API
│   └── persona_generator.py      # Saves persona to output/
│
├── output/                       # Persona output files
│   └── output_kojied.txt
│
├── main.py                       # CLI entry point
├── .env                          # API keys (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Vishal-Palve/Reddit-User-Persona-LLM.git
   cd Reddit-User-Persona-LLM
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your API Keys**  
   Create a `.env` file in the root directory and add:
   ```
   TOGETHER_API_KEY=your_together_api_key
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   ```

4. **Run the App**
   ```bash
   python main.py
   ```

5. **Example Reddit User**
   ```
   https://www.reddit.com/user/kojied/
   ```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributions

Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.
