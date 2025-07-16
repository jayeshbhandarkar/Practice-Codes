def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Yes"
    
    else:
        return "No"
    
year = int(input())
answer = is_leap_year(year)
print(answer)