#this problem again uses subsetsum code from line 3 to 14 for filling the matrix with True or False
def minimumSubsetSumDiff(arr,sumx,sumy,n):
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
                
    z = t[-1] # We do this to get the last row of the matrix.

    mindiff = sumy # the max sum we can get is the total sum of the array so we initialize it with this

    for i in range(len(z)): 
        if z[i] == True: 
            # if the sum is possible i.e it is True that a subset of this sum can be formed then we enter.
         
            mindiff = min(mindiff,sumy-(2*i)) 
            
            # here we are taking the minimum of the mindiff and the calculation (sum of total array - (2 * sum of first subset)) so that we always get the minimum.

    return mindiff

arr = [1,6,11,5]
n = len(arr)

# the formula derived from the video was minimum value of (sum of total array - (2 * sum of first subset))

sumy = sum(arr) # this will be later used in the function

sumx = sumy // 2 # as mentioned in the video we need to only take the first half range so we first only divide the sum by 2

t = [[False for i in range(sumx+1)] for j in range(n+1)] 
print(minimumSubsetSumDiff(arr,sumx,sumy,n))
