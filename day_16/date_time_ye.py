from datetime import datetime, date, timedelta, time

#1.Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
timestamps = now.timestamp()
print(now)
print(timestamps)

#2.Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

time1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time1)

#3.Today is 5 December, 2019. Change this time string to time.

date1 = "5 December, 2041"
stripped_Date = datetime.strptime(date1, "%d %B, %Y")
print(stripped_Date)

#4.Calculate the time difference between now and new year.
now = datetime.now()
t1 = now
t2 = datetime(now.year + 1, 1, 1)
print(now.year +1)
t3= t2-t1
print(t3)

#5.Calculate the time difference between 1 January 1970 and now.
start_time = datetime(1970, 1, 1)

current_Time = now


time_diff = current_Time - start_time
print(time_diff)