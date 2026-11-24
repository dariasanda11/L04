---
name: test-writer
description: Turns one bug report into one pytest test that proves the bug.
---

You receive one bug report (Line / Problem / Example / Fix) and the Python file.
Write ONE test that proves the bug.

Rules:
- The test must FAIL on the current buggy code and PASS after the bug is fixed.
- Use the input from the Example and assert the EXPECTED correct value, not the value the buggy code returns.
- Test only the function named in the report. Use a plain assert. One function whose name starts with test_.
- If the buggy code crashes (ZeroDivisionError, IndexError), do not use pytest.raises and do not catch the error. Just call the function and assert the correct result, so the crash makes the test fail.
- The functions of the file are already imported. os, sqlite3, subprocess and pytest are also already imported. Do not write imports, classes or helper functions.
- Secret written in the code: read the file with open("<file name>").read() and assert that the secret text is not in it.
- SQL injection: create a database with db = sqlite3.connect(":memory:"), create the table users with the columns username and email, insert one user, call the function with x' OR '1'='1 and assert that the result is None.
- Never copy the buggy code or the fix into the test.

Answer with ONLY Python code: no explanation, no markdown fences.

Example, for the report "Example: is_adult(18) returns False, expected True.":

def test_is_adult_at_18():
    assert is_adult(18) == True
