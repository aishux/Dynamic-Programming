# The complete function is same as Count of subset sums problem 

def numOfSubWithGivenDiff(arr,W,n):
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

arr = [1,1,2,3]
diff = 1
n = len(arr)

# This problem is basically that we need to find how many pairs of 2 subsets can have a difference equal to the given difference

#suppose the sum of the first subset is "s1" and second subset is "s2"

# So as per given situation 
# s1 - s2 = diff (given) -------- (1)
# and we also know that the sum of the two subsets will be equal to the whole array so
# s1 + s2 = sum(arr) -------------(2)

# Now on adding equation 1 and 2 we get the formula
# 2s1 = diff + sum(arr)  =>  s1 = (diff + sum(arr))/ 2

s1 = (diff + sum(arr))// 2

# as all the things on R.H.S of s1 are given we can easily find s1 

# Once we get what is s1 we just have to find how many subsets are present which have the sum s1 and that will be the answer.

############# VERY IMPORTANT ###############

# If (diff + sum(arr)) comes out to be odd that means there is no such difference possible and the question itself is not valid so we print 0 . For eg in this array try to put difference as 6 instead of 1

if (diff + sum(arr)) % 2 != 0:
    print(0)
else:
    t = [[0 for i in range(s1+1)] for j in range(n+1)]
    x = numOfSubWithGivenDiff(arr,s1,n)
    print(x)
