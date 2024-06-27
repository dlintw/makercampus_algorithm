def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# 測試遞迴法計算Fibonacci數列
n = 10
print(f"第 {n} 項 Fibonacci 數為: {fibonacci_recursive(n)}")
