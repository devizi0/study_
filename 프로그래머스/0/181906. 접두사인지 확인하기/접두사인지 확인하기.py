def solution(my_string, is_prefix):
    prefixes = []
    for x in range(0,len(my_string)):
        if prefixes:
            prefixes.append(str(prefixes[-1]) + str(my_string[x]))
        else:
            prefixes.append(my_string[0])
    print(prefixes)
    if is_prefix in prefixes:
        return 1
    return 0