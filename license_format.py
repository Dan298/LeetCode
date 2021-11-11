def license_format(string, k):
    string = string.upper()
    string = string.replace('-','')
    format_list = []
    iterator = 0
    t = k
    final = ''
    temp = len(string) % k
    if len(string) <= k:
        return string
    if temp == 0:
        temp = len(string)//k
        for i in range(temp - 1):
            format_list.append(string[iterator:t])
            iterator += k
            t += k
            format_list.append('-')
        format_list.append(string[iterator:t])
    else:
        format_list.append(string[iterator:temp])
        format_list.append('-')
        string = string[temp:len(string)]
        temp = len(string) // k
        for i in range(temp - 1):
            format_list.append(string[iterator:t])
            iterator += k
            t += k
            format_list.append('-')
        format_list.append(string[iterator:t])

    for x in format_list:
        final += x
    return final

print(license_format("5F3Z-2e-9-w", 4))