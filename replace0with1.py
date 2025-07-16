def replace_zeros_with_ones(n):
    str_n = str(n)
    str_n = str_n.replace('0', '1')
    return int(str_n)

print(replace_zeros_with_ones(102003))  
print(replace_zeros_with_ones(204))     
print(replace_zeros_with_ones(0))       
print(replace_zeros_with_ones(12345)) 
