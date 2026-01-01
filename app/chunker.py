import os
from pathlib import Path

INPUT_DIR = "data/processed"
OUTPUT_DIR = "data/chunks"

CHUNK_SIZE = 800
OVERLAP = 200

os.makedirs(OUTPUT_DIR, exist_ok=True)

def chunk_text(text):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + CHUNK_SIZE
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start = end - OVERLAP

    return chunks

def main():
    for file in os.listdir(INPUT_DIR):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(INPUT_DIR, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunk_text(text)

        out_path = os.path.join(OUTPUT_DIR, file.replace(".txt", "_chunks.txt"))
        with open(out_path, "w", encoding="utf-8") as f:
            for i, chunk in enumerate(chunks):
                f.write(f"[CHUNK {i}]\n{chunk}\n\n")

        print(f"Chunked: {file}")

if __name__ == "__main__":
    main()
