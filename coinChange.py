class Solution(object):
    def coinChange(self, coins, amount):
        coin_array = [amount+1] * (amount+1)
        coin_array[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    coin_array[i] = min(coin_array[i], coin_array[i-c] + 1)

        if coin_array[amount] == amount+1:
            return -1
        return coin_array[amount]
S = Solution()
print(S.coinChange([186,419,83,408],6249))
