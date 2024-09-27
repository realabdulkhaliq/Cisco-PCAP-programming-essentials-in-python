#Scenario
# Your task is to prepare a simple code able to evaluate the end time of a period of time, 
# given as a number of minutes (it could be arbitrarily large). 
# The start time is given as a pair of hours (0..23) and minutes (0..59). 
# The result has to be printed to the console.

# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

# Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒ 
# the most important thing is that the code produces valid results for valid input data.

# Test your code carefully. Hint: using the % operator may be the key to success.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

end_time_in_minutes = (hour * 60) + mins + dura
hour = end_time_in_minutes // 60
mins = end_time_in_minutes % 60
hour = hour % 24
print(hour, mins, sep=":")


# By Netacad
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# mins = mins + dura # find a total of all minutes
# hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
# mins = mins % 60 # correct minutes to fall in the (0..59) range
# hour = hour % 24 # correct hours to fall in the (0..23) range
# print(hour, ":", mins, sep='')



