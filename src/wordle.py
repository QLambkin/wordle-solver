import loader
import matcher

def find_possible_words(all_words, guess_results):
    possible_words = []

    for word in all_words:
        if matcher.matches_constraints(word, guess_results):
            possible_words.append(word)

    return possible_words

def main():
    words = loader.load_words()
    all_constraints = []

    # While the user is still guessing
    while True:

        # Get the users guess
        while True:
            guess = input("Enter your guess: ").upper()
            if len(guess) != 5:
                print("Guess must be 5 characters, try again")
            else:
                break

        # Get results for this guess
        guess_results = []
        for position in [0,1,2,3,4]:
            while True:
                result = input(f"Enter Y, G, or B for position {position}: ")
                if result in ("Y","G","B"):
                    guess_results.append((guess[position], result, position))
                    print(guess_results)
                    break
                else:
                    print("Guess must be Y, G, or B, try again")

        # Accumulate possible guess restraints
        for results in guess_results:
            all_constraints.append(results)

        # Find possible guesses and display results
        possible_words = sorted(find_possible_words(words, all_constraints))
        print(f"Possible Words: {possible_words}")

        while True:
            answer = input("Guess Again? (Y/N): ")
            if answer == "Y":
                break
            elif answer == "N":
                print("Deuces")
                return
            else:
                print("Must answer Y or N")

if __name__ == "__main__":
    main()
