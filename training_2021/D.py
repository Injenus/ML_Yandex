a = int(input())
b = int(input())
c = int(input())


def sol_eq(a, b, c):
    if a != 0:
        if abs((c ** 2 - b)) % abs(a):
            return "NO SOLUTION"
        else:
            x = (c ** 2 - b) // a
            if a * x + b >= 0 and c >= 0:
                return x
            else:
                return "NO SOLUTION"
    elif b >= 0 and c >= 0:
        if b == c ** 2:
            return "MANY SOLUTIONS"
        else:
            return "NO SOLUTION"
    else:
        return "NO SOLUTION"


print(sol_eq(a, b, c))
