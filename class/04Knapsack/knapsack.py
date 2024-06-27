def knapsack(weights, values, capacity):
    n = len(weights)
    # 初始化dp表，dp[i][j]表示前i個物品在容量為j的背包中的最大價值
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # 填充dp表
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # 取不取物品i
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# 測試0/1背包問題
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_value = knapsack(weights, values, capacity)
print(f"背包的最大價值: {max_value}")
