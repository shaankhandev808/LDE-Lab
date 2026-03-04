# Section E: Datetime

# The datetime module in Python is how we work
# with times. We are going to get the current date,
# modify the current date, format date strings, then
# get epoch and format epoch into date strings.

# Import the necessary modules.
from datetime import datetime
from datetime import timedelta
import time

# Generate the current datetime.
datetime_now = datetime.now()
print(datetime_now)
# > blah blah blah

# Modify the current datetime and subtract an hour. 
datetime_now_minus_one_hour = datetime_now - timedelta(hours=1)
print(datetime_now_minus_one_hour)
# > blah blah blah

# Modify the current datetime and add two hours. 
datetime_now_plus_one_hour = datetime_now + timedelta(hours=2)
print(datetime_now_plus_one_hour)
# > blah blah blah

# Use the strftime() function---string from time. 
datetime_minus_one_reformatted = datetime_now_minus_one_hour.strftime("%d/%m/%Y %H:%M:%S")
print(datetime_minus_one_reformatted)
# > blah blah blah

# Convert datetime to epoch using timestamp()
# Epoch is a single number output. 
epoch = datetime_now.timestamp()
print(epoch)
# > # > blah blah blah

# Turn the epoch, which is in UTC, convert it to a local timezone,
# then make it into a timestamp. 
timestamp_from_epoch = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
print(timestamp_from_epoch)
# > 'blah blah blah'
