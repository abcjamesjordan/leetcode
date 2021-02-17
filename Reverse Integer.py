# https://leetcode.com/problems/reverse-integer/

if x >= 0:
    temp = str(x)
    temp = int(temp[::-1])
    if (temp > (2**31 -1)) or (temp < -2**31):
        return 0
    else:
        return temp
elif x == 0:
    return 0
else:
    temp = abs(x)
    temp = str(temp)
    temp = int(temp[::-1])
    temp *= -1
    if (temp > (2**31 -1)) or (temp < -2**31):
        return 0
    else:
        return temp