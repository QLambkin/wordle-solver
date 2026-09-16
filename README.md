# Wordle Solver

A Python CLI tool that suggests possible Wordle answers based on your guesses. Excludes all past Wordle answers from suggestions.

## Setup

### 1. Clone and Create Virtual Environment
```bash
git clone https://github.com/YOUR_USERNAME/wordle-solver.git
cd wordle-solver
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 2. Download Past Wordle Answers
This project filters out all past Wordle answers. Download the latest list:

```bash
curl -o data/past_answers.txt https://raw.githubusercontent.com/eithan/wordlelist/main/words.txt
```

**Note:** This file updates with each new Wordle answer. Re-run this command periodically to stay current.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/wordle.py
```

Enter your guesses and feedback (G/Y/B for each position). The solver narrows down possible words, excluding past answers.

## Project Structure

- `src/loader.py` - Load word list and past answers
- `src/matcher.py` - Check if word matches constraints
- `src/wordle.py` - Main interactive solver
- `data/words.txt` - 5-letter word list
- `data/past_answers.txt` - All past Wordle answers (download via setup step 2)