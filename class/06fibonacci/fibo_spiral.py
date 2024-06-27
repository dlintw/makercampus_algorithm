import turtle

def draw_fibonacci_spiral(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    turtle.speed(10)
    for i in range(n):
        turtle.circle(fib[i] * 10, 90)

    turtle.done()

# 繪製Fibonacci螺旋圖案
draw_fibonacci_spiral(10)
