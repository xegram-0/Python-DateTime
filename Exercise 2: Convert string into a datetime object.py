# Exercise 2: Convert string into a datetime object

# Given:

# date_string = "Feb 25 2020 4:20PM"

# Expected output:

# 2020-02-25 16:20:00
from datetime import datetime
def main():
    date_string = "Feb 25 2020 4:20PM"

    # dt_obj = datetime.strptime(date_string, "%m/%d/%Y %H:%M:%S")
    dt_obj = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
    print(dt_obj)
if __name__=="__main__":
    main()