class Solution(object):
    def plusOne(self, digits):
        temp_string = ''
        for digit in digits:
            temp_string += str(digit)
        temp_string = str(int(temp_string) + 1)
        return list(temp_string)
S =  Solution()
print(S.plusOne([9,9]))