def ArrayAdditionI(arr):
    """
    Take arr and check if the highest number in
    arr == to the sum of the rest of the numers.

    ex.[4, 6, 23, 10, 1, 3]
    return 'true' if  4 + 6 + 10 + 3 = 23
    """

    nums = sorted(arr)

    #Get highest num
    highestNum = max(arr)
    currentSum = 0 - highestNum

    for num in nums:
        currentSum += num
        
    if currentSum < highestNum:
        return 'false'
    else:
        return 'true'