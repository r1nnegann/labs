from datetime import datetime, timedelta
today = datetime.now()
day=timedelta(days=1)
print(today-day, today, today+day, sep="\n")
