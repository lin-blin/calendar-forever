def f(d, m, c, y):
    ned = (d + int((13 * m - 1) / 5) + y + int(y / 4) + int(c / 4) - 3 * c + 777) % 7
    return ned
d = 30
m = 8
c = 21
y = 19
print(f(d,m,c,y))
