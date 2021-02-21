# This problem is using the code of subset sum so from line 8-18 there not a single line changed

def equalSumPartition(arr,sumx,n):
    if sumx % 2 != 0: 
        #checks if the sum of the complete array is odd and if it is odd then it cannot be divided into half so there is no chance that it will be divided into equal halves. So we directly return False
        return False

    sumx = sumx // 2 #Now if the sum is even then we have to check suppose the sum is 22 then we have to check if it could be divided into equal subsets of sum 11 and 11 so if we find that there is even one subset of 11 then the other subset is by default 11 and it will be true. So here we half the sum i.e to 11 and we check if there is a subset which has a sum of 11 which is the problem statement of subsetsum.  

    t = [[False for i in range(sumx+1)] for j in range(n+1)] 
    
    for i in range(n+1):
        for j in range(sumx+1):
            if i == 0:
                t[i][j] = False
            elif j == 0:
                t[i][j] = True
            else:
                if arr[i-1] > j:
                    t[i][j] =  t[i-1][j]
                else:
                    t[i][j] =  t[i-1][j-arr[i-1]] or t[i-1][j]
    return t[n][sumx]

arr = [1,5,11,5]
n = len(arr)
sumx = sum(arr) #here we ourselves have to find the sum of the complete array

print(equalSumPartition(arr,sumx,n))
