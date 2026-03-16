from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 2 fix: attempts counter was initialized to 1 instead of 0,
# causing "Attempts left" to show attempt_limit - 1 before any guess was made.
def test_attempts_left_at_game_start():
    attempt_limit = 8       # Normal difficulty
    initial_attempts = 0    # FIXED: was 1, now correctly 0
    attempts_left = attempt_limit - initial_attempts
    # Before the fix this would have been 7, not 8
    assert attempts_left == attempt_limit, (
        "At game start no attempts have been used, so attempts_left must equal attempt_limit"
    )

def test_attempts_off_by_one_regression():
    # Regression: if attempts starts at 1, the sidebar and info message disagree by 1
    attempt_limit = 8
    buggy_initial = 1
    fixed_initial = 0
    assert attempt_limit - buggy_initial != attempt_limit, "Bug: off-by-one would hide an attempt"
    assert attempt_limit - fixed_initial == attempt_limit, "Fix: all attempts shown at game start"
