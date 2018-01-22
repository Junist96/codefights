def isLucky(n):
    number = str(n)

    sh = number[:int(len(number)/2)]
    he = number[int(len(number)/2):]

    return sum([int(i) for i in sh]) == sum([int(i) for i in he])
