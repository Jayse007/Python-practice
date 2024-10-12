from datetime import datetime, timedelta
"""
This code checks if a user was active in the last 24 hours.
"""
last_login = datetime(2024, 8, 21, 1, 36)
today = datetime.now()

checker = today - timedelta(hours= 24)

print(last_login > checker)

