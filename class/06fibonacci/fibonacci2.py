def fibonacci_dynamic(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0] * (n + 1)
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]

# 測試動態規劃法計算Fibonacci數列
n = 10
print(f"第 {n} 項 Fibonacci 數為: {fibonacci_dynamic(n)}")
