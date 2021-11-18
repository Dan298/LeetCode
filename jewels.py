def numJewelsIsInStones(jewels, stones):
    unique_jewels = set(list(jewels))
    total = 0
    for i in unique_jewels:
        total += stones.count(i)
    return total
print(numJewelsIsInStones('', 'AAAabbb'))