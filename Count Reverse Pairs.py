def count_reverse_pairs(arr):
    count = 0
    
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] > 2 * arr[j]:
                count += 1
                
    return count

# Input
N = 5
array = [1, 3, 2, 3, 1]
result = count_reverse_pairs(array)
print("Result:", result)
