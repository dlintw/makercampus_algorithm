# 定義產品列表，每個產品包含名稱和價格
products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 699.99},
    {"name": "Tablet", "price": 499.99},
    {"name": "Monitor", "price": 199.99},
    {"name": "Keyboard", "price": 49.99}
]

# 使用lambda函數按價格排序產品列表
sorted_products = sorted(products, key=lambda x: x["price"])

# 打印排序後的產品列表
print("按價格排序後的產品列表:")
for product in sorted_products:
    print(f"{product['name']}: ${product['price']}")
