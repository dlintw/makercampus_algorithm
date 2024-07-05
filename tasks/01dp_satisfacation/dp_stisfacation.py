# 假設的麥當勞食物清單和滿足度
menu = [
    {"name": "Big Mac", "price": 72, "satisfaction": 80},
    {"name": "Chicken McNuggets (6 pcs)", "price": 65, "satisfaction": 70},
    {"name": "Medium Fries", "price": 45, "satisfaction": 50},
    {"name": "Coca-Cola (Medium)", "price": 30, "satisfaction": 30},
    {"name": "McFlurry", "price": 50, "satisfaction": 60},
    {"name": "Filet-O-Fish", "price": 55, "satisfaction": 60},
    {"name": "McChicken", "price": 70, "satisfaction": 75},
    {"name": "Double Cheeseburger", "price": 70, "satisfaction": 75},
    {"name": "Spicy McWings (2 pcs)", "price": 45, "satisfaction": 50},
    {"name": "Chocolate Sundae", "price": 35, "satisfaction": 40},
    {"name": "Apple Pie", "price": 30, "satisfaction": 35},
]

budget = 500

def max_satisfaction(menu, budget):
    # 建立 dp 陣列，dp[i] 表示預算為 i 時的最大滿足度
    dp = [0] * (budget + 1)
    choices = [[] for _ in range(budget + 1)]

    for item in menu:
        for j in range(budget, item["price"] - 1, -1):
            if dp[j] < dp[j - item["price"]] + item["satisfaction"]:
                dp[j] = dp[j - item["price"]] + item["satisfaction"]
                choices[j] = choices[j - item["price"]] + [item["name"]]

    return dp[budget], choices[budget]

# 計算最大滿足度
max_satis, chosen_items = max_satisfaction(menu, budget)
print(f"在預算為 {budget} 元時，最大的滿足度為: {max_satis}")
print(f"選擇的食物為: {', '.join(chosen_items)}")

