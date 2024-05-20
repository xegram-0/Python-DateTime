# Exercise 10: Calculate number of days between two given dates
# Given:

# # 2020-02-25
# date_1 = datetime(2020, 2, 25)

# # 2020-09-17
# date_2 = datetime(2020, 9, 17)

# Expected output:

# 205 days
from datetime import datetime,timedelta
def main():
    date_1 = datetime(2020, 2, 25)
    date_2 = datetime(2020, 9, 17)

    # Another way is comparing two dates and
    # switching for positive number of days
    #num_days = date_2 - date_1
    num_days = date_1 - date_2
    
    # Can compare with number using timedelta
    # if num_days < timedelta(0):
    #     print("Negative")

    # abs works on datetime type
    print(f"{abs(num_days.days)} days")
if __name__=="__main__":
    main()