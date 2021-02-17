# https://leetcode.com/problems/detect-capital

if word.islower():
            return True
        elif word.isupper():
            return True
        else:
            return (word[1:].islower() & word[0].isupper())