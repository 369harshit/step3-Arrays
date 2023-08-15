def rearrange_array_by_sign(arr, N):
    positives = []
    negatives = []

    for num in arr:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)

    rearranged_array = []

    for i in range(N):
        if i < len(positives):
            rearranged_array.append(positives[i])
        if i < len(negatives):
            rearranged_array.append(negatives[i])

    return rearranged_array

arr = [1, 2, -4, -5]
N = 4
result = rearrange_array_by_sign(arr, N)
print("Rearranged array by sign:", result)
