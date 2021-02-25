def subsetproblem(arr,sumx,n):
    for i in range(n+1):
        for j in range(sumx+1):
            if i == 0:
                t[i][j] = False
            if i==0 and j == 0:
                t[i][j] = True
            elif j == 0:
                t[i][j] = True
            else:
                if arr[i-1] > j:
                    t[i][j] =  t[i-1][j]
                else:
                    t[i][j] =  t[i-1][j-arr[i-1]] or t[i-1][j]
    return t[n][sumx]

arr = [2,3,7,8,10]
n = len(arr)
sumx = 12
t = [[False for i in range(sumx+1)] for j in range(n+1)]
print(subsetproblem(arr,sumx,n))