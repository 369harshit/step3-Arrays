def longest_subarray_with_sum(arr, N, k):
    max_length = 0

    for i in range(N):
        current_sum = 0
        for j in range(i, N):
            current_sum += arr[j]
            if current_sum == k:
                max_length = max(max_length, j - i + 1)

    return max_length

N = 3
k = 1
array = [-1, 1, 1]
result = longest_subarray_with_sum(array, N, k)
print("The longest subarray length with sum", k, "is:", result)
