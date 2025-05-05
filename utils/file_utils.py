import os

def load_texts(folder):
    texts = {}
    for file_name in os.listdir(folder):
        if file_name.endswith('.txt'):
            with open(os.path.join(folder, file_name), 'r', encoding='utf-8') as f:
                texts[file_name] = f.read()
    return texts
