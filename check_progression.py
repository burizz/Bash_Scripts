def ArithGeo(arr):
    """
    Check if arr is a list of numbers that are in Arithmetic, Geometric or without any progression.

    Exmaple :
    return "Arithmetic" if ex. [2, 4, 6, 8]
    return "Geometric" if ex. [2, 6, 18, 54]
    return -1 if none
    """

    # Check if array is with at least 3 elements
    if len(arr) < 3: return 0

    # Calculate difference between numbers in list
    diffAr = arr[1] - arr[0]
    diffGeo = arr[1] / arr[0]

    # Temp vars to check if list is in progression
    isA = True
    isG = True

    for num in range(1, len(arr)):
        if arr[num] - arr[num - 1] != diffAr:  #Check if progression is Arithmetic
            isA = False
        if arr[num] / arr[num -1] != diffGeo:  #Check if progression is Geometric
            isG = False

    if isA:
        return "Arithmetic"
    elif isG:
        return "Geometric"
    else:
        return "-1"
 
