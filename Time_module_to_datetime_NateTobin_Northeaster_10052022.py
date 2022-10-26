Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time
timestamp = time.time()
dt_datetime = time.ctime(timestamp)
print(dt_datetime)

date = int(timestamp)

number_of_days = date // 3600 // 24
print(number_of_days, "days since epoch")
