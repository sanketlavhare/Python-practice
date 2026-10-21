#Function TO find Longest String
def get_max(*string):
    if len(string) == 0:
        return None 
    max_string = string[0]
    for n in string:
        if len(n) > len(max_string):
            max_string = n
    return max_string

print(get_max("Ayush", "Mrunaal", "Riya"))