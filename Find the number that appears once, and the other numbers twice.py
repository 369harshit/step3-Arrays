def find_single_number(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num

arr = [4,1,2,1,2]
result = find_single_number(arr)
print("The number that appears once:", result)
