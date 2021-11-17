def minPartitions(value):
    temp = str(value)
    current_max = 0
    for i in temp:
        current_max = max(current_max, int(i))
    return current_max


print(minPartitions(27346209830709182346))