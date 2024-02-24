from datetime import datetime
def drop_microseconds(date):
    return date.replace(microsecond=0)

print(drop_microseconds(datetime.now()))