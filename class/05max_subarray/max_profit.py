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

def max_profit(prices):
    changes = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
    # return max_subarray_sum(changes)
    return max_subarray_sum_divide_and_conquer(changes, 0, len(changes)-1)

# 測試股票價格分析
prices = [100, 180, 260, 310, 40, 535, 695]
profit = max_profit(prices)
print(f"最大利潤為: {profit}")
