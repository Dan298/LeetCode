class Solution:
    def combinationSum4(self, nums, target):
        memory = dict()

        def combinations(target):
            if target in memory: return memory[target]
            if target == 0:
                return 1
            if target < 0:
                return 0

            output = 0
            for num in nums:
                output += combinations(target - num)
            memory[target] = output
            return output

        return combinations(target)

S = Solution()
print(S.combinationSum4([1,2,3],4))
