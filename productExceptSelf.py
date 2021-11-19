from math import prod

class Solution(object):
    def productExceptSelf(self, nums):
        final_nums = list(nums)
        for i in range(len(nums)):
            temp = nums.pop(i)
            product = prod(nums)
            nums.insert(i, temp)
            final_nums[i] = product
        return final_nums
print(Solution.productExceptSelf(Solution,[1,2,3,4]))