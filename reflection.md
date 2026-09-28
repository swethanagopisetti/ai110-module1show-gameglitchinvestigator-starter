# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked faulty because when I entered 0, it still kept saying to "Go Lower". 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. Hints were reversed. If my guess is lower than the secret, it must say "Go higher" but it said "Go lower"
2. "Show Hint" button does nothing. 
3. After I won the game, I clicked on "New Game" and I entered a new number and clicked on "Submit Guess" but it still said "You already won. Start a new game to play again." and did not accept my guesses. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 12    | "Go higher"       | "Go lower"      | check_guess() if guess > secret:|
| 95    | "Go lower"        | "Go higher"     | check_guess() if guess > secret:|
| 95    | "Go lower"        | "Go higher"     | check_guess() if guess > secret:|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It suggested moving the check_guess into logic_utils.py and imported it in app.py. It also corrected the high/low outcomes, hint directions and the string secrets. All these suggestions that AI gave are correct. I verified the result by running the pytest in the terminal. I also played the game to verify its working. 
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
None
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I verified the result by running the pytest in the terminal. I also played the game to verify its working. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran all the tests in the terminal using python3 -m pytest -q tests/test_game_logic.py. I also played the game in the browser window for the secrets - 13, 45, etc. It showed that the code is working correctly.
- Did AI help you design or understand any tests? How?
Yes, it designed a new test test_numeric_string_secret_uses_numeric_comparison to verify that the string input for secret is being handled. It also explained how the test works.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Have logic separate from UI and have test cases for every scenario.
- What is one thing you would do differently next time you work with AI on a coding task?
I will give more context to the AI so that it thinks and responds correctly.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It did edge case handling very well. I liked how it did type cast to int at the beginning of the function.
