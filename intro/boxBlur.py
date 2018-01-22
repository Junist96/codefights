def boxBlur(image):

    row = len(image)
    col = len(image[0])

    result = []

    # 두 번째 행부터 마지막 전 행까지 탐색
    for i in range(1, row - 1):
        init = [] #
        # 두 번째 열부터 마지막 전 행까지 탐색
        for j in range(1, col - 1):
            init.append(sum([image[i+k][j+l] for k in [-1, 0, 1] for l in [-1, 0, 1]]) // 9)
        result.append(init)

    return result
