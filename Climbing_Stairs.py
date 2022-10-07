# Program helps to find solution to climbing stairs dynamic programming problem in leetcode
def climbStairs(self, n: int, memo={}) -> int:
    if n in memo:
      return memo[n]

    if n <= 0:
      return 0 

    if n <= 2:
      return n 

    memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

    return memo[n]
