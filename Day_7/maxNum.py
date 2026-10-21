def get_max(*num):
    if len(num) == 0:
        return None 
    max_num = num[0]
    for n in num:
        if n > max_num:
            max_num = n
    return max_num 
print (get_max(10, 8, 15, 20))