def count_subarrays_with_sum(arr, k):
    count = 0
    n = len(arr)
    
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == k:
                count += 1
                
    return count

# Input
N = 3
array = [1,2,3]
k = 3

result = count_subarrays_with_sum(array, k)
print("Result:", result)
