import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def process_with_groq(text):
    prompt = f"""Você é um analista. Recebeu o texto abaixo. Responda:
1. Traduza o texto para português.
2. Resuma o conteúdo.
3. O que deu certo?
4. O que não deu certo?
5. A tradução fez sentido?
6. O resumo foi fiel ao texto?
7. Quem pode ser o autor do texto?

Texto:
{text}"""

    body = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=HEADERS, json=body)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()
