import numpy as np
import math

n = 3
m = 4

map = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]



def way_finder(map, m, n):

    res = 0
    extended_map = np.zeros( (n+1, m+1) )
    dp = np.zeros((n + 1, m + 1))

    for i in range(1, m+1):
        dp[0][i] = math.inf
    for i in range(1, n+1):
        dp[i][0] = math.inf

    for i in range(1, n+1):
        for j in range(1, m+1):
            extended_map[i][j] = map[i-1][j-1]

    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + extended_map[i][j]


    print(dp[n][m])
    return dp[n][m]

way_finder(map, m, n)

