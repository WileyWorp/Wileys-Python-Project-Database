import requests
import random


def main():
    currentGuess = 1
    correct = []
    misplaced = []
    targetList = []
    wordUrl = "https://random-word-api.herokuapp.com/word?length=5"
    wordResponse = requests.get(wordUrl)
    if wordResponse.status_code == 200:
        print("Word status code: 200, all good to go")
        targetWord = wordResponse.json()[0]
    else:
        print(f"ERROR! Word status code: {wordResponse.status_code}")
    targetWord = "glyph"
    for i in targetWord:
        targetList.append(i)
    hintUrl = f"https://api.datamuse.com/words?rel_jja={targetWord}"
    hintResponse = requests.get(hintUrl)
    if hintResponse.status_code == 200:
        print("Hint status code: 200, all good to go")
    else:
        print(f"ERROR! Hint status code: {hintResponse.status_code}")

    def getHints():
        hintList = []
        for h in range(5):
            index = random.randint(0, len(hintResponse.json()))
            hintList.append(hintResponse.json()[index]["word"])

    print("The word is 5 letters, you have 6 guesses. Go!")

    while True:
        guess = input(f"Guess {currentGuess}: ")
        guessList = []
        for g in guess:
            guessList.append(g)
        if len(guess) > 5:
            print("Invalid input!")
        elif len(guess) < 5:
            print("Invalid input!")
        elif guess != targetWord:
            for l in guessList:
                if l == targetList[guessList.index(l)]:
                    print(l)
                    correct.append(l)
                else:
                    for t in targetList:
                        if l == t:
                            print(t)
                            misplaced.append(l)
                        else:
                            break
            currentGuess += 1
            if currentGuess > 6:
                print(f"You ran out of guesses, the word was {targetWord}")
                break
            print(f"Incorrect! {correct} are correct and {misplaced} are misplaced.")
            correct.clear()
            misplaced.clear()
        elif guess == targetWord:
            print("Correct!")
            break
        else:
            print("Error occured")


if __name__ == "__main__":
    print(
        """Welcome to Infinitle!
        This is a little project that I decided to make on 2/10/25
        Input !hints if you need to!"""
    )
    while True:
        play_query = input("Input 'p' to play or 'q' to quit: ")
        if play_query.lower() == "p":
            main()
        elif play_query.lower() == "q":
            quit()
        else:
            print("Invalid input!")
