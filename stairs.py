class Solution:
    def climbStairs(self, n):
        climbing_routes = {}

        for i in range(n + 1):
            if i <= 2:
                climbing_routes[i] = i

            if i not in climbing_routes:
                climbing_routes[i] = climbing_routes[i - 1] + climbing_routes[i - 2]

        return climbing_routes[n]

S = Solution()
print(S.climbStairs(5))