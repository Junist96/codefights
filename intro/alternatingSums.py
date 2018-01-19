def alternatingSums(a):

    lst = [a[i] for i in range(len(a)) if i == 0 or i % 2 == 0]
    lst2 = [a[i] for i in range(len(a)) if a[i] not in lst]

    return [sum(lst), sum(lst2)]