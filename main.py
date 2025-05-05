import os
from utils.file_utils import load_texts
from llm_clients.openai_client import process_with_openai
from llm_clients.groq_client import process_with_groq
from llm_clients.openrouter_client import process_with_openrouter
from llm_clients.together_client import process_with_together

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def analyze_text_with_llms(texts):
    for file_name, content in texts.items():
        print(f"📄 Analisando {file_name}...")

        responses = {
            "ChatGPT": process_with_openai(content),
            "Groq_LLaMA3": process_with_groq(content),
            "OpenRouter": process_with_openrouter(content),
            "Together_Mistral": process_with_together(content),
        }

        with open(os.path.join(OUTPUT_DIR, f"analysis_{file_name}.md"), "w", encoding="utf-8") as f:
            f.write(f"# 📄 Análise do arquivo: {file_name}\n\n")
            for model, response in responses.items():
                f.write(f"## 🤖 {model}\n")
                f.write(response + "\n\n")

if __name__ == "__main__":
    texts = load_texts("data")
    analyze_text_with_llms(texts)
