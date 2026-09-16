from pathlib import Path

file_path = Path("data/past_answers.txt")
print(f"File exists: {file_path.exists()}")
print(f"File size: {file_path.stat().st_size} bytes")

# Read the first 5 lines
content = file_path.read_text().splitlines()
print(f"Total lines: {len(content)}")
print(f"First 5 lines: {content[:5]}")