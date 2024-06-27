def investment_portfolio(weights, returns, budget):
    n = len(weights)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(1, budget + 1):
            if weights[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - weights[i - 1]] + returns[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    return dp[n][budget]

# 測試投資組合優化
investment_costs = [100, 200, 300, 400]
expected_returns = [10, 20, 30, 40]
total_budget = 500
max_return = investment_portfolio(investment_costs, expected_returns, total_budget)
print(f"最大預期回報: {max_return}")
