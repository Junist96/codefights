def boxBlur(image):

    height = len(image)
    weight = len(image[0])

    idx = 0
    lst = [sum([i[idx], i[idx+1], i[idx+2]]) for i in image]


image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

∂
boxBlur(image)