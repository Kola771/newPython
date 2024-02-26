

def fibonacci(n):
    x = 0
    y = 1
    tableau = [x, y]
    while (x < n) :
        x, y = y, x+y
        tableau.append(y)
    return tableau

print(fibonacci(n=1000))