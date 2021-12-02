class Solution(object):
    def coinChange(self, coins, amount):
        total = 0
        coins.sort()
        for coin in reversed(coins):
            temp = amount // coin
            if temp >= 1:
                amount = amount - (coin*temp)
                total += temp
            if amount == 0:
                return total
        return -1
S = Solution()
print(S.coinChange([186,419,83,408],6249))