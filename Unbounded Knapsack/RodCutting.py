# This completely uses the unbounded knapsack code only naming is different

def rodCutting(length,price,W,n):
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            else:
                if length[i-1] > j:
                    t[i][j] =  t[i-1][j]
                else:
                    t[i][j] =  max(price[i-1]+t[i][j-length[i-1]],t[i-1][j])
    return t[n][W]
    
length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
W = 8
n = len(length)

t = [[0 for i in range(W+1)] for j in range(n+1)]

x = rodCutting(length,price,W,n)
print(x)