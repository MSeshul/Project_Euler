'''How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''
import calendar
count = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if calendar.weekday(i, j, 1) == 6:
            count = count + 1

print(count)

