# Bug reports for exercise1.py

Line: 3
Problem: The function checks if n % 2 == 1, which is true for odd numbers, not even numbers. It should check for even numbers where n % 2 == 0.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, but the docstring says it computes the area of a rectangle, which should be width times height.
Example: rectangle_area(3, 4) returns 7, expected 12.
Fix: return width * height

Line: 12
Problem: The function adds 2 to n, but the docstring says it returns twice the number, i.e., n * 2.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
