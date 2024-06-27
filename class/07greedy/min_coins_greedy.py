def min_coins_greedy(coins, amount):
    # 將硬幣按面值從大到小排序
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        # 使用盡可能多的當前面值硬幣
        count += amount // coin
        amount %= coin
    return count

# 測試貪心算法解決貨幣找零問題
coins = [1, 5, 10, 25]
amount = 63
min_coins = min_coins_greedy(coins, amount)
print(f"最少需要的硬幣數量: {min_coins}")
