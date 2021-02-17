# https://leetcode.com/problems/two-sum/

nums = [2,7,11,15]
target = 9
answer_dict = {}

    for index, num in enumerate(nums):
        try:
            return ((answer_dict[target-num], index))
        except:
            answer_dict[num] = index