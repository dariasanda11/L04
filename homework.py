def daily_hay(cows):
    """each mini cow eats 3 kg of hay per day. total kg for all the cows"""
    return cows * 3


def can_be_milked(age_months, weight_kg):
    """true if the mini cow is 24 months or older and weighs at least 120 kg"""
    return age_months >= 24 and weight_kg >= 120


def average_milk(liters):
    """average liters of milk per day. an empty list has average 0"""
    if not liters:
        return 0
    return sum(liters) / len(liters)


def winter_bales(cows):
    """hay bales for winter: 0 for up to 3 cows, then 2 for every extra cow, never more than 10"""
    return max(0, min((cows - 3) * 2, 10))


def get_farmer_email(db, username):
    """email of the farmer with this username, or None if there is no such farmer"""
    query = "SELECT email FROM users WHERE username = ?"
    row = db.execute(query, (username,)).fetchone()
    return row[0] if row else None
