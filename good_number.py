def good_number(num):
    if num == 0:  
        return "Bad Number"

    add = 0  
    temp = num  

    while temp > 0:
        add += temp % 10
        temp //= 10

    if add == 0:  
        return "Bad Number"

    if num % add == 0:  
        return "Good Number"
    else:
        return "Bad Number"

T = int(input().strip())  
for _ in range(T):
    num = int(input().strip())  
    print(good_number(num))  
