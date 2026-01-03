# import math
def check_palinfrom(str):
    # mid = math.floor(len(str)/2) no need to check mid this way
    mid = len(str) //2 # This will aslo works same
    last = len(str)-1
    print(str[last])
    for i in range(mid):
        if(str[i] != str[last-i]):
            return False
    return True
print(check_palinfrom("abcdcba"))
