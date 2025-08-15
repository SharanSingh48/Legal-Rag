import os
import re
import json

BASE_DIR = "processed_text"
OUTPUT_FILE = "processed_chunks.jsonl"

SECTION_PATTERNS = [
    r"(section\s+\d+)",
    r"(clause\s+\d+(\.\d+)*)",
    r"(article\s+\d+)"
]

MAX_WORDS = 550


def split_into_chunks(text, page_num):
    """Split text into chunks with section markers and page reference."""
    pattern = "(?i)" + "|".join(SECTION_PATTERNS)
    sections = re.split(pattern, text)
    sections = [s if s is not None else "" for s in sections]

    chunks = []

    if len(sections) > 1:
        for i in range(0, len(sections), 2):
            marker = sections[i].strip() if i < len(sections) else ""
            content = sections[i+1].strip() if i+1 < len(sections) else ""
            if marker or content:
                chunks.append({
                    "section": marker if marker else None,
                    "text": content,
                    "page": page_num
                })
    else:
        words = text.split()
        for i in range(0, len(words), MAX_WORDS):
            chunk_text = " ".join(words[i:i+MAX_WORDS])
            chunks.append({
                "section": None,
                "text": chunk_text,
                "page": page_num
            })

    return chunks



def process_folder():
    all_chunks = []

    for category in os.listdir(BASE_DIR):
        category_path = os.path.join(BASE_DIR, category)
        if not os.path.isdir(category_path):
            continue

        for filename in os.listdir(category_path):
            if filename.lower().endswith(".txt"):
                file_path = os.path.join(category_path, filename)

                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()

                # Split by "Page X" markers if you kept them during extraction
                pages = re.split(r"(?i)\bpage\s+\d+\b", text)
                if len(pages) == 1:
                    # Fallback: treat entire file as page 1
                    pages = [text]

                for page_index, page_text in enumerate(pages, start=1):
                    page_chunks = split_into_chunks(page_text, page_index)
                    for chunk in page_chunks:
                        all_chunks.append({
                            "text": chunk["text"].strip(),
                            "source": filename,
                            "category": category,
                            "section": chunk["section"],
                            "page": chunk["page"]
                        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"✅ Processed {len(all_chunks)} chunks saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    process_folder()

