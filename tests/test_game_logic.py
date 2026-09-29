from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

APP_PATH = Path(__file__).resolve().parents[1] / "app.py"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📈 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📉 Go HIGHER!"

def test_numeric_string_secret_uses_numeric_comparison():
    outcome, message = check_guess(9, "10")
    assert outcome == "Too Low"
    assert message == "📉 Go HIGHER!"


@pytest.mark.parametrize("raw_guess", ["-1", "12.5", "1000000"])
def test_invalid_or_out_of_range_guess_is_rejected(raw_guess):
    app = AppTest.from_file(str(APP_PATH)).run()
    attempts_before = app.session_state["attempts"]

    app.text_input[0].set_value(raw_guess)
    app.button[0].click().run()

    assert not app.exception
    assert app.error
    assert app.session_state["attempts"] == attempts_before
    assert app.session_state["history"] == []
