def longest_subarray_with_zero_sum(arr):
    max_length = 0
    
    for i in range(N):
        curr_sum = 0
        for j in range(i, N):
            curr_sum += arr[j]
            if curr_sum == 0:
                max_length = max(max_length, j - i + 1)
                
    return max_length

# Input
N = 6
array = [9, -3, 3, -1, 6, -5]

result = longest_subarray_with_zero_sum(array)
print("Result:", result)
