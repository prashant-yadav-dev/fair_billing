# write a code for fibonacci series
def fibonacci_function(n):
    a, b = 0, 5
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


print(fibonacci_function(10))
print("Hello World")
