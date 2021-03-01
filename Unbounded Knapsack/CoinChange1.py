def coinChange(arr,W,n):
    for i in range(n+1):
        for j in range(W+1):
            if j == 0:
                t[i][j] = 1
            else:
                if arr[i-1] > j:
                    t[i][j] =  t[i-1][j]
                else:
                    t[i][j] =  t[i][j-arr[i-1]] + t[i-1][j]
    return t[n-1][W]
    
arr = [1, 2, 3] 
W = 4
n = len(arr)

t = [[0 for i in range(W+1)] for j in range(n+1)]

x = coinChange(arr,W,n)
print(x)