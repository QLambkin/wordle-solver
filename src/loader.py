from pathlib import Path

def load_words():
    words = Path("data/words.txt").read_text().splitlines()
    return {word.upper() for word in words if len(word) == 5}

if __name__ == "__main__":
    words = load_words()
    print(f"Loaded {len(words)} words")
    print(f"Type: {type(words)}")
    print(f"Sample: {list(words)[:5]}")  # Show first 5