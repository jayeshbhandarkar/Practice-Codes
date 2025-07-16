"""
Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to cycling with his
friends. So every time when the months starts he counts the number of sundays he will get to enjoy. Considering the 
month can start with any day, be it Sunday, Monday…. Or so on. Count the number of Sunday jack will get within n 
number of days.

Example 1:
Input 
mon-> input String denoting the start of the month.
13  -> input integer denoting the number of days from the start of the month.

Output :
2    -> number of days within 13 days.

Explanation:
The month start with mon(Monday). So the upcoming sunday will arrive in next 6 days. And then next Sunday in next 7 
days and so on. Now total number of days are 13. It means 6 days to first sunday and then remaining 7 days will end 
up in another sunday. Total 2 sundays may fall within 13 days."
"""

def count_sundays(start_day, num_days):
    days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    
    # Find index of the start day
    start_index = days.index(start_day.lower())

    # Calculate the number of Sundays within num_days
    return (num_days + start_index) // 7

start_day = "mon"  
num_days = 13  
print(count_sundays(start_day, num_days))  
