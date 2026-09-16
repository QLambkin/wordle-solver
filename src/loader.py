from pathlib import Path
def load_words():
    words = Path("data/words.txt").read_text().splitlines()
    return {word.upper() for word in words if len(word) == 5}

def load_past_answers():
    answers = Path("data/past_answers.txt").read_text().splitlines()
    return {answer.upper() for answer in answers if len(answer) ==  5}

if __name__ == "__main__":
    words = load_words()
    past = load_past_answers()
    
    print(f"Total words: {len(words)}")
    print(f"Past answers: {len(past)}")
    print(f"Sample past answers: {sorted(list(past))[:10]}")