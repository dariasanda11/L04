import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_daily_hay():
    assert daily_hay(4) == 12


# bug report 2
def test_r2_can_be_milked():
    assert can_be_milked(24, 120) == True


# bug report 3
def test_r3_average_milk_empty_list():
    assert average_milk([]) == 0


# bug report 4
def test_r4_winter_bales():
    assert winter_bales(2) == 0


# bug report 5
def test_r5_get_farmer_email_sql_injection():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, email TEXT)")
    db.execute("INSERT INTO users VALUES ('test', 'test@example.com')")
    db.commit()
    
    # Malicious input to test SQL injection
    malicious_username = "'; DROP TABLE users; --"
    result = get_farmer_email(db, malicious_username)
    
    # The function should not execute malicious SQL and should return None
    assert result is None
