def matches_constraints(word, guess_results):
    # Check GREEN constraints first
    for letter, color, position in guess_results:
        if color == "G":
            if word[position] != letter:
                return False
    
    # Check YELLOW constraints
    for letter, color, position in guess_results:
        if color == "Y":
            if (letter not in word) or (word[position] == letter):
                return False
    
    # Check BLACK constraints (accounting for duplicates)
    for letter, color, position in guess_results:
        if color == "B":
            # Count how many times this letter is GREEN or YELLOW
            accounted_for = sum(1 for l, c, p in guess_results if (c == "G" or c == "Y") and l == letter)
            
            # Count how many times the letter appears in the word
            letter_count = word.count(letter)
            
            # If the word has more instances than accounted for, constraint fails
            if letter_count > accounted_for:
                return False
    
    return True

if __name__ == "__main__":    
    # Test Case 4: Multiple constraints (green + yellow + black)
    # Pick a word and constraints that mix all three colors
    result = matches_constraints("SLATE", [("S", "G", 0), ("T", "B", 1),("A", "G", 2), ("T", "G", 3),("E", "G", 4)])
    print(f"Test 4 (should be True): {result}")