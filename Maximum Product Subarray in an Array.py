def max_product_subarray(nums):
    max_product = float('-inf')
    
    for i in range(N):
        current_product = 1
        for j in range(i, N):
            current_product *= nums[j]
            max_product = max(max_product, current_product)
            
    return max_product

# Input
N=6
nums = [1,2,3,4,5,0]
result = max_product_subarray(nums)
print("Result:", result)
