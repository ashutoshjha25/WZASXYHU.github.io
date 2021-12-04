rows, cols, row2, col2 = (2,2,2,10000)
arr = [[[[-1 for i in range(cols)]for j in range(rows)]for k in range(row2)]for l in range(col2)]

def cal(n, i, j, k):
    if(n==1):
        arr[n][i][j][k] = 1;
        return arr[n][i][j][k]
    if(arr[n][i][j][k]!=-1):
        return arr[n][i][j][k]
    ans = 0
    if( i==1 and j==1 and k==1):
        ans = cal(n-1, 0, 1, 1)
    else:
        ans = cal(n-1, 0, i, j) + cal(n-1, 1 ,i, j)
    arr[n][i][j][k] = ans
    return arr[n][i][j][k]
    
n = int(input())
success = cal(n,0,0,0)
fail = cal(n, 1, 0, 0)

print ('%d / %d' %(fail, success+fail))