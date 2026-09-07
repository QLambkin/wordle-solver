# Wordle Solver

A Python CLI tool that suggests possible Wordle answers based on your guesses.

## Setup

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Usage

```bash
python src/wordle.py
```

Enter your guesses and feedback (G/Y/B for each position). The solver narrows down possible words.

## Project Structure

- `src/loader.py` - Load word list
- `src/matcher.py` - Check if word matches constraints
- `src/wordle.py` - Main interactive solver
- `data/words.txt` - 5-letter word list