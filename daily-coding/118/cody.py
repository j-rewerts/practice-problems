def squareSort(numbers):
    i = 0
    j = len(numbers) - 1

    if len(numbers) == 0:
        return numbers

    # all numbers are positive
    if numbers[i] >= 0:
        for m in range(len(numbers)):
            numbers[m] = numbers[m]**2
        return numbers

    # all numbers are negative
    if numbers[j] < 0:
        m = j
        for n in range(len(numbers)//2):
            numbers[m], numbers[n] = numbers[n]**2, numbers[m]**2
            m -= 1
        return numbers

    # some numbers are negative and some are positive
    negatives = []
    positives = []
    k = 0
    while numbers[k] < 0:
        negatives.append(numbers[k]**2)
        k += 1

    while k < len(numbers):
        positives.append(numbers[k]**2)
        k += 1

    r = len(negatives) - 1
    s = 0
    t = 0
    
    while r >= 0 and s < len(positives):
        if negatives[r] < positives[s]:
            numbers[t] = negatives[r]
            r -= 1
        else:
            numbers[t] = positives[s]
            s += 1
        t += 1

    while r >= 0:
        numbers[t] = negatives[r]
        r -= 1
        t += 1

    while s > len(positives):
        numbers[t] = positives[s]
        s += 1
        t += 1

    return numbers


print(squareSort([-9, -2, 0, 2, 3]))
print(squareSort([1, 2, 3, 4]))
print(squareSort([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))