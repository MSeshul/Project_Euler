ones_list = [3, 3, 5, 4, 4, 3, 5, 5, 4]
tens_list = [6, 6, 5, 5, 5, 7, 6, 6]
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
hundred = 7
thousand = 11
total = 0

#ones place
total = sum(ones_list) * 90

#tens
total = total + (sum(teens) * 10)
total = total + (sum(tens_list) *100)

#hundreds place
total = total + (hundred * 900)
total = total + (sum(ones_list) *100)
total = total + (891 * 3)
total = total + thousand

print(total)




        