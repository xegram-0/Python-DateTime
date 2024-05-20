# Exercise 9: Calculate the date 4 months from the current date
# Given:

# # 2020-02-25
# given_date = datetime(2020, 2, 25).date()

# Expected output:

# 2020-06-25

from datetime import datetime
from dateutil.relativedelta import relativedelta
def main():
    given_date = datetime(2020, 2, 25).date()
    new_date = given_date + relativedelta(months=4)
    print(new_date)
if __name__=="__main__":
    main()