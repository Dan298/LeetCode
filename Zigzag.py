def convert(convert_string, num_rows):
    zigzaglist = [''] * num_rows
    count = 0
    ascend = True

    if num_rows == 1:
        return convert_string

    while len(convert_string) != 0:
        if count == num_rows-1:
            zigzaglist[count] += convert_string[0]
            count -= 1
            ascend = False

        elif count == 0:
            zigzaglist[count] += convert_string[0]
            count += 1
            ascend = True

        elif ascend:
            zigzaglist[count] += convert_string[0]
            count += 1

        else:
            zigzaglist[count] += convert_string[0]
            count -= 1

        convert_string = convert_string[1:]

    return ''.join(zigzaglist)
print(convert('ABC',1))