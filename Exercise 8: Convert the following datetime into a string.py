# Exercise 8: Convert the following datetime into a string
# Given:

# given_date = datetime(2020, 2, 25)

# Expected output:

# "2020-02-25 00:00:00"
from datetime import datetime
def main():
    given_date = datetime(2020, 2, 25)
    string_date = str(given_date.strftime("%Y-%m-%d %H:%M:%S"))
    # Guess this is already a string with strftime
    # Good to know firsthand
    string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
    print(string_date)
    print(type(string_date))
if __name__=="__main__":
    main()