import datetime
day1 = datetime.date(2021,12,14)

from datetime import date
day1 = date(2024,1,1)
day2 = date(2024, 12, 31)
diff = day2 - day1
print(diff)
print(diff.days)
'''
365 days, 0:00:00
365
'''
day = date(2024,9,24)
print(day.weekday()) # 0 mon
print(day.isoweekday()) # 1 mon 

from time import time, localtime, asctime, ctime, strftime
print(time()) #1727162058.5233262
print(localtime(time()))
'''
time.struct_time(tm_year=2024, tm_mon=9, tm_mday=24, tm_hour=16, tm_min=14, tm_sec=55, tm_wday=1, tm_yday=268, tm_isdst=0)
'''
print(localtime())
print(asctime(localtime(time()))) # Tue Sep 24 16:15:51 2024
print(asctime(localtime()))
print(ctime())

print(strftime('%Y-%m-%d', localtime(time()))) # 2024-09-24
print(strftime('%x', localtime(time()))) 
print(strftime('%c', localtime(time()))) 
print(strftime('%c'))
'''
09/24/24
Tue Sep 24 16:19:20 2024
'''

print(strftime('%Y-%m-%d %H:%M:%S', localtime())) # 2024-09-24