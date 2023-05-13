def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    mod = 10 ** 9 + 7
    dp = {}

    def dfs(length):
        if length > high:
            return 0
        if length in dp:
            return dp[length]

        result = 1 if length >= low else 0
        result += dfs(length + zero) + dfs(length + one)
        return result % mod

    return dfs(0)
