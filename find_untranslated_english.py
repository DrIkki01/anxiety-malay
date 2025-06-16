import os
import re

SCENES_DIR = "./scenes"

# Basic English word pattern
english_word = re.compile(r'\b[a-zA-Z]{3,}\b')

# Basic Malay stopword list (add more if needed)
common_malay_words = {
    "saya", "tidak", "dan", "dengan", "dia", "kerana", "akan", "untuk", "kami",
    "awak", "kamu", "mereka", "ada", "ini", "itu", "dalam", "ke", "adalah", "boleh"
}

def is_mostly_english(text):
    words = english_word.findall(text.lower())
    if not words:
        return False
    english_count = sum(1 for word in words if word not in common_malay_words)
    return english_count / len(words) >= 0.8  # At least 80% English

for filename in os.listdir(SCENES_DIR):
    if filename.endswith(".md"):
        filepath = os.path.join(SCENES_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                if is_mostly_english(line):
                    print(f"[{filename}:{lineno}] {line.strip()}")
