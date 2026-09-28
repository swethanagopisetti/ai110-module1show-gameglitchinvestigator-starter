# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of the game is to guess a random number in the given number of attempts.
- [ ] Detail which bugs you found.
The hints were reversed. The Show hint button was not working. The Submit guess does not work after a new game starts.
- [ ] Explain what fixes you applied.
I fixed the reversed hints in check_guess function by reversing the comparison operator. I also fixed the string input for secret to the check_guess function. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user enters a guess in the "Enter your guess" box and clicks "Submit Guess" button.
2. Game shows a hint saying "Go Lower" or "Go Higher"
3. User enters another guess based on the hint, and the game shows the hint again "Too High"
4. Score and the number of attempts left updates after each guess
5. Game ends after the correct guess is entered by the user

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
python3 -m pytest -q tests/test_game_logic.py
....                                                                               [100%]
4 passed in 0.01s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
