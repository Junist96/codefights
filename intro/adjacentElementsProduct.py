def adjacentElementsProduct(inputArray):
    ia = inputArray
    return max([ia[i] * ia[i+1] for i in range(len(ia)-1)])
