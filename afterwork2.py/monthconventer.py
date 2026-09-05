import datetime

for month in range(1, 13):
    date = datetime.date(2026, month, 1)
    print(date.strftime("%B"))
