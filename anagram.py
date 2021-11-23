def anagram(a, b):
    for char in b:
        temp = a.find(char)
        if temp == -1:
            return False
        else:
            a = a.replace(a[temp],'',1)
    return True
print(anagram('ab', 'ba'))