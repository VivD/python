import math
print('number?')
n = int(input())
a = n
k = 0
g = 0
l = 0
for i in range(n):
    if i > 0:
        k = n * (n-1)
    else:
        n = n * 1
    n = n - 1
g = math.gcd(k, k+1)
l = (a * (a+1))/g
print(f'The gcd is:{g: .2f}')
print(f'The lcm is:{l: .2f}')