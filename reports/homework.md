# Bug reports for homework.py

Line: 3
Problem: daily_hay adds 3 to the number of cows, but the docstring says each cow eats 3 kg, so total should be cows * 3.
Example: daily_hay(4) returns 7, expected 12.
Fix: return cows * 3

Line: 8
Problem: can_be_milked uses > instead of >= for age_months and weight_kg, but the docstring says "24 months or older" and "at least 120 kg".
Example: can_be_milked(24, 120) returns False, expected True.
Fix: return age_months >= 24 and weight_kg >= 120

Line: 13
Problem: average_milk crashes on empty list because len(liters) is 0, causing division by zero.
Example: average_milk([]) returns error, expected 0.
Fix: return sum(liters) / len(liters) if liters else 0

Line: 18
Problem: winter_bales returns (cows - 3) * 2 for up to 3 cows, which is negative or zero, but the docstring says "0 for up to 3 cows".
Example: winter_bales(2) returns -2, expected 0.
Fix: return max(0, min((cows - 3) * 2, 10))

Line: 23
Problem: get_farmer_email directly concatenates user input into SQL query, risking SQL injection.
Example: get_farmer_email(db, "'; DROP TABLE users; --") executes malicious SQL.
Fix: query = "SELECT email FROM users WHERE username = ?"
