from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_with_openai(text):
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
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
