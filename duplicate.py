class Solution(object):
    def containsDuplicate(self, nums):
        unique_nums = set(nums)
        if len(unique_nums) != len(nums):
            return True
        else:
            return False


s = Solution()
s.containsDuplicate([1, 2, 3, 2])
