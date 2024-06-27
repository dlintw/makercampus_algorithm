def max_profit_greedy(investments, budget):
    # 將投資項目按收益/成本比從高到低排序
    investments.sort(key=lambda x: x['profit'] / x['cost'], reverse=True)
    total_profit = 0
    for investment in investments:
        if budget == 0:
            break
        if investment['cost'] <= budget:
            budget -= investment['cost']
            total_profit += investment['profit']
    return total_profit

# 測試投資組合優化
investments = [
    {'cost': 100, 'profit': 10},
    {'cost': 200, 'profit': 20},
    {'cost': 300, 'profit': 30},
    {'cost': 400, 'profit': 40}
]
budget = 500
max_profit = max_profit_greedy(investments, budget)
print(f"最大預期回報: {max_profit}")
