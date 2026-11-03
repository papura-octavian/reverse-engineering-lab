"""
Key needs `-` at indexes : 7, 15, 23, 31

key needs * acceptable char for fuction `check()`

key needs skip characters at positions: 8, 16, 24, 32

"""

indexes = [7, 15, 23, 31]

def check_index(idx):
    if indexes.count(idx):
        return True
    
    return False

# 40 chas long
key = ""

for i in range(0, 39):
    if check_index(i):
        key += '-'
    else:
        key += '*' # skip characters can also be acceptable char for fuction `check()`

print(key)