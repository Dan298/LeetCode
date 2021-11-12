def findTheWinner( n, k):
    player_list = []
    iterator = 0
    for i in range(n):
        player_list.append(i+1)

    while len(player_list) > 1:
        iterator += k - 1
        if iterator >= len(player_list):
            iterator = iterator % len(player_list)
        player_list.pop(iterator)

    return player_list[0]

print(findTheWinner(5, 2))