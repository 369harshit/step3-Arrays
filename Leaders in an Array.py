def find_leaders(arr, N):
    leaders = []

    for i in range(N):
        is_leader = True
        for j in range(i + 1, N):
            if arr[j] > arr[i]:
                is_leader = False
                break
        
        if is_leader:
            leaders.append(arr[i])

    return leaders

arr = [10, 22, 12, 3, 0, 6]
N = 6
result = find_leaders(arr, N)
print("Leaders in the array:", result)
