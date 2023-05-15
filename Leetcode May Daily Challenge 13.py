def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    dp = {0: 1}
    mod = 10 ** 9 + 7

    for i in range(1, high + 1):
        dp[i] = (dp.get(i - one, 0) + dp.get(i - zero, 0)) % mod

    return sum([dp[i] for i in range(low, high + 1)]) % mod

    # def dfs(length):
    #     if length > high:
    #         return 0
    #     if length in dp:
    #         return dp[length]
    #
    #     result = 1 if length >= low else 0
    #     result += dfs(length + zero) + dfs(length + one)
    #     return result % mod
    #
    # return dfs(0)

print(countGoodStrings(3, 3, 1, 1))