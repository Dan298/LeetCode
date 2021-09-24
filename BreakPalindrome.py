class Solution(object):
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def convertStr(self, tempList):
        tempStr1 = ''
        for x in tempList:
            tempStr1 += x
        return tempStr1

    def isPalindrome(self, palList):
        str1 = self.convertStr(palList)
        if str1 == str1[::-1]:
            return True
        else:
            return False

    def breakPalindrome(self, palindrome):
        #Convert string into list to edit
        # Strings in Python are immutable
        temp = list(palindrome)
        placeholder = ''

        # Edge case 1: One character
        if len(palindrome) == 1:
            return ''


        # Edge case 2: All A's string
        if temp.count('a') == len(temp):
            temp[len(temp) - 1] = 'b'
            return self.convertStr(temp)

        # Regular case:
        for e in range(len(temp)):
            if temp[e] == 'a' and e != len(temp)-1:
                continue
            for letter in self.alphabet:
                placeholder = temp[e]
                temp[e] = letter
                if self.isPalindrome(temp):
                    temp[e] = placeholder
                    continue
                else:
                    return self.convertStr(temp)
        return self.convertStr(temp)


palindrome = Solution()
output = palindrome.breakPalindrome('aba')
print(output)