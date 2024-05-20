# Exercise 6: Add a week (7 days) and 12 hours to a given date
# Given:

# 2020-03-22 10:00:00
# given_date = datetime(2020, 3, 22, 10, 0, 0)

# Expected output:

# 2020-03-29 22:00:00
from datetime import datetime, timedelta

def main():
    given_date = datetime(2020, 3, 22, 10, 0, 0)
    print(f"The given date is {given_date.strftime("%Y-%m-%d %H:%M:%S")}")
    new_date = given_date + timedelta(days=7,hours=12)
    print(f"The new date is {new_date.strftime("%Y-%m-%d %H:%M:%S")}")
if __name__=="__main__":
    main()