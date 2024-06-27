def min_coins_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# 測試動態規劃解法
coins = [1, 3, 4]
amount = 6
min_coins = min_coins_dp(coins, amount)
print(f"最少需要的硬幣數量（正確解法）: {min_coins}")
