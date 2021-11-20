def romanToInt(roman):
    count = 0
    subtract = False
    roman = roman[::-1]
    roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman)):
        if subtract:
            count -= roman_value[roman[i]]
            subtract = False
        else:
            count += roman_value[roman[i]]
            subtract = False
        if i == len(roman)-1:
            continue
        else:
            if roman_value[roman[i]] > roman_value[roman[i+1]]:
                subtract = True

    return count

print(romanToInt('LVIII'))

