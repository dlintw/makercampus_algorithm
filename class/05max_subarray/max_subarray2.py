def max_crossing_sum(nums, left, mid, right):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += nums[i]
        if total > left_sum:
            left_sum = total
    
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += nums[i]
        if total > right_sum:
            right_sum = total
            
    return left_sum + right_sum

def max_subarray_sum_divide_and_conquer(nums, left, right):
    if left == right:
        return nums[left]
    
    mid = (left + right) // 2
    
    left_sum = max_subarray_sum_divide_and_conquer(nums, left, mid)
    right_sum = max_subarray_sum_divide_and_conquer(nums, mid + 1, right)
    cross_sum = max_crossing_sum(nums, left, mid, right)
    
    return max(left_sum, right_sum, cross_sum)

# 測試分治法解決最大子序列和問題
example_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum_divide_and_conquer(example_arr, 0, len(example_arr) - 1)
print(f"最大子序列和為: {max_sum}")
