# 定義產品列表，每個產品包含名稱和價格
products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 699.99},
    {"name": "Tablet", "price": 499.99},
    {"name": "Monitor", "price": 199.99},
    {"name": "Keyboard", "price": 49.99}
]

# 使用快速排序按價格排序產品列表
def quick_sort_products(products):
    if len(products) <= 1:
        return products
    else:
        pivot = products[len(products) // 2]["price"]
        left = [product for product in products if product["price"] < pivot]
        middle = [product for product in products if product["price"] == pivot]
        right = [product for product in products if product["price"] > pivot]
        return quick_sort_products(left) + middle + quick_sort_products(right)

sorted_products = quick_sort_products(products)

# 打印排序後的產品列表
print("按價格排序後的產品列表:")
for product in sorted_products:
    print(f"{product['name']}: ${product['price']}")
