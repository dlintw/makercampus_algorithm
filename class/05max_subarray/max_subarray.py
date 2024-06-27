def max_subarray_sum(nums):
    # 初始化
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        # 更新當前子數列的最大和
        current_sum = max(num, current_sum + num)
        # 更新全局最大和
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# 測試最大子序列和問題
example_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(example_arr)
print(f"最大子序列和為: {max_sum}")
