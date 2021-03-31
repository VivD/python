def fastfib(x, memo = {}):
    if x == 0 or x == 1:
        return 1
    try:
        return memo[x]
    except:
        result = fastfib(x-1, memo) + fastfib(x-2, memo)
        memo[x] = result
        return result

temp = fastfib(120)
print(temp)
