class Solution:
    def __init__(self):
        self.values = {}

    def rob(self, nums):
        self.values = {}
        return self.rob_house(0, nums)

    def rob_house(self, i, nums):
        # Base case
        if i >= len(nums):
            return 0

        # Return house value
        if i in self.values:
            return self.values[i]

        # Recursive case
        ans = max(self.rob_house(i + 1, nums), self.rob_house(i + 2, nums) + nums[i])

        # Store house value
        self.values[i] = ans
        return ans


s = Solution()
print(s.rob([2, 7, 9, 3, 1]))
