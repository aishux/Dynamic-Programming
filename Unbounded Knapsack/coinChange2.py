def coinChange2(coins,sumx,n):
    # We initialize the the 1st(index 0) column with 0
    for i in range(1, n + 1):
        t[i][0] = 0

    # We initialize the the 2nd (index 1) row with either the divident or with the max value of 999999999  
    for j in range(1, (sumx + 1)):
        if j % coins[0] == 0:
            t[1][j] = j // coins[0]
        else:
            t[1][j] = 999999999
    
    ######## IMPORTANT #############

    # We are not initializing the 1st row(index 0 ) with the maximum value because at the time of matrix creation we already filled the matrix with 999999999 completely.

    # As we have already filled the 0th and 1st row we iterate i from 2

    for i in range(2, n + 1):
        # As we have already filled the 1st column we iterate j from 1
        for j in range(1, (sumx + 1)):
            if coins[i - 1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = min(t[i-1][j], 1 + t[i][j-coins[i-1]]) # here we are choosing the minimum of the two and also to see here is that 1 is added to the second argument to avoid error of size

    return -1 if t[n][sumx] == 999999999  else t[n][sumx] # If we get the output as the max value then it means there is no possibility of getting the amount with the provided coins so we return -1 or else we provide the required output

coin = [25, 10, 5]
sumx = 30
n = len(coin) 

t = [[999999999 for i in range(sumx+1)] for j in range(n+1)] 
# we initialise it with 999999999 so that on line 25 when we are taking the min this argument remains the max and doesn't disturb our choice making

print(coinChange2(coin,sumx,n))