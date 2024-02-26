

def fibonacci(n):
    t = 0
    x = 0
    y = 1
    tableau = [x, y]
    while (t < n) :
        x, y = y, x+y
        tableau.append(y)
        t += 1
    return tableau

print(fibonacci(n=5))