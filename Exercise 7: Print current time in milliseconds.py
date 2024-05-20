# Exercise 7: Print current time in milliseconds
from datetime import datetime
import time
def main():
    # The request is to print time in miliseconds
    # Not time in full

    # today_date = datetime.today()
    # print(today_date.time())


    print(int(round(time.time()*1000)))

    # How I wanted to analyze the code
    # print(time.time())
    # print(round(time.time()))
    # print(type(round(time.time())))
if __name__=="__main__":
    main()