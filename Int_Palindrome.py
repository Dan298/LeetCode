def isPalindrome(x):
    output = str(x)
    if output == output[::-1]:
        return True
    else:
        return False
