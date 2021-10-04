class Solution:
    def maxArea(self, height):
        final_area = 0
        left_iter = 0
        right_iter = len(height) - 1

        while left_iter < right_iter:
            container_top = min(height[left_iter], height[right_iter])
            container_width = right_iter - left_iter
            container_area = container_top * container_width
            final_area = max(final_area, container_area)

            if height[left_iter] <= height[right_iter]:
                left_iter += 1
            else:
                right_iter -= 1

        return final_area
