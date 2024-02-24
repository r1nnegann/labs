from datetime import datetime, timedelta

def date_difference(date1, date2):
    if date1 < date2:
        return (date2 - date1).total_seconds()
    return (date1 - date2).total_seconds()

print(date_difference(datetime.now(), datetime(2020, 1, 5)))