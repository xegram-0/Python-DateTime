# Exercise 3: Subtract a week (7 days)  from a given date in Python
# Given:

# given_date = datetime(2020, 2, 25)

# Expected output:

# 2020-02-18

from datetime import timedelta, datetime
def main():
    given_date = datetime(2020, 2, 25)
    new_date = given_date - timedelta(days=7)
    print(new_date)
if __name__=="__main__":
    main()