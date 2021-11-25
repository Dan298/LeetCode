class Solution:
    def canJump(self, jumps):
        if len(jumps) < 2:
            return True
        if jumps[0] > len(jumps) - 1:
            return True
        midpoint = len(jumps) - 1

        for index in reversed(range(len(jumps) - 1)):
            if jumps[index] >= midpoint - index:
                midpoint = index
        return midpoint == 0
