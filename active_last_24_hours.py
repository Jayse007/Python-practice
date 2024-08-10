from datetime import datetime, timedelta

last_login = datetime(2024, 6, 28, 13)
today = datetime.now()

threshold = today - timedelta(hours= 24)

print(last_login > threshold)

