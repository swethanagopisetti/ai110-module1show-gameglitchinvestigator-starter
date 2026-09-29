# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
Identify three potential "edge case" inputs (e.g., negative numbers, decimals, or extremely large values) that might still break the game. Generate a suite of pytest cases that verify your game handles these inputs gracefully. Fix the failing tests. 

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
It listed the edge cases as negative numbers, decimals, extremely large numbers. It added a test case called test_invalid_or_out_of_range_guess_is_rejected.

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
I did not need any fixing. I asked it to fix the failing tests and it was able to fix the failing tests. After it fixed, I ran the tests to ensure that they are all running fine.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative Numbers| Generate a suite of pytest cases that verify your game handles these inputs gracefully. | test_invalid_or_out_of_range_guess_is_rejected | Yes | |
| Decimals| Generate a suite of pytest cases that verify your game handles these inputs gracefully. | test_invalid_or_out_of_range_guess_is_rejected | Yes | |
| Extremely large numbers| Generate a suite of pytest cases that verify your game handles these inputs gracefully. | test_invalid_or_out_of_range_guess_is_rejected | Yes | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
