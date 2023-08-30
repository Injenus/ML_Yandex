a = int(input())
b = int(input())
c = int(input())
if 2 * max(a, b, c) < a + b + c:
    print('YES')
else:
    print('NO')
