import calendar

month, day, year = map(int, input().split())

Day_Name = calendar.day_name[calendar.weekday(year, month, day)]

print(Day_Name.upper())