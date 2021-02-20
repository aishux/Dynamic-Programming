# The complete function is same as subsetsum problem only difference being that at line 15 instead of "or" we write "+"

def subsetproblem(arr,W,n):
    for i in range(n+1):
        for j in range(W+1):
            if i == 0:
                t[i][j] = 0
            if i==0 and j == 0:
                t[i][j] = 1
            elif j == 0:
                t[i][j] = 1
            else:
                if arr[i-1] > j:
                    t[i][j] =  t[i-1][j]
                else:
                    t[i][j] =  t[i-1][j-arr[i-1]] + t[i-1][j]
    return t[n][W]

arr = [2,3,5,6,8,10]
W = 10
n = len(arr)
t = [[0 for i in range(W+1)] for j in range(n+1)]
x = knapsack(arr,W,n)
print(x)
