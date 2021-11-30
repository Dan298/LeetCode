class Solution:
    def kthSmallest(self, matrix, k):
        length = len(matrix)
        left = matrix[0][0]
        right = matrix[length - 1][length - 1]

        while left <= right:
            mid = left + (right - left) // 2
            if self.compare(mid, matrix) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def compare(self, mid, matrix):
        length = len(matrix)
        count = 0
        row = length - 1
        col = 0
        while row >= 0 and col < length:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count
