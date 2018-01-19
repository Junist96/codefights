def isIPv4Address(inputString):
    splt = inputString.split('.')

    return len(splt) == 4 and all(i.isdigit() and 0 <= int(i) <= 255 for i in splt)
