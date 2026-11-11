# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns False for grade 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password accepts passwords shorter than 8 characters, but the docstring requires "at least 8 characters".
Example: is_valid_password("1234567") returns True, expected False.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: clamp returns low when x is less than low, but the docstring says "limited to the range from low to high", and the code incorrectly uses min(x, low) which can cause x to be below low.
Example: clamp(3, 5, 10) returns 5, expected 5 (correct), but clamp(2, 5, 10) returns 5, which is correct; however, the logic is flawed because min(x, low) when x < low gives x, not low. The correct logic should be max(low, min(x, high)).
Example: clamp(2, 5, 10) returns 5, expected 5 (correct), but the code has a typo: min(x, low) should be min(x, high). The actual bug is in the logic: it says min(x, low) twice.
Fix: return max(low, min(x, high))
