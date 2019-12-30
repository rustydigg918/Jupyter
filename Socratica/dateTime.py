import datetime as dt

gvr = dt.date(1956, 1 ,31)
print(gvr)

print(gvr.year)
print(gvr.day)
print(gvr.month)

# Lets add some days in date
mill = dt.date(2000,1,1)
td = dt.timedelta(100)
print(mill+td)

 # So Default format of date in python is yyyy-mm-dd
 # Let's change it in the following format:
 # Day-name, Month-name Day-#, year

# Lets do it the old way
print(gvr.strftime("%A, %B %d, %Y"))
# Let's try iy the new way
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

# Let's use time, date and datetime
launch_date = dt.date(2017, 3, 30)
launch_time = dt.time(22,27,0)
launchdatetime = dt.datetime(2017, 3, 30, 22, 27, 0)

print;
print(launch_date)
print(launch_time)
print(launchdatetime)

print;
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)

print;
print(launchdatetime.year)
print(launchdatetime.month)
print(launchdatetime.day)
print(launchdatetime.hour)
print(launchdatetime.minute)
print(launchdatetime.second)


# For today's datetime
print;
now = dt.datetime.today()
print(now)

# look at microseconds
print(now.microsecond)


# Converting datetime string into datetime object
print;
moon_landing = "7/20/1969"
moon_landing_datetime = dt.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
