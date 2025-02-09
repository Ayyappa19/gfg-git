
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		#Code here
		def solve(i,j,grid,k,v):
		    if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0 or v[i][j]):
		        return 0
		    if(grid[i][j]==2):
		        return 1
		    grid[i][j] = 0
		    return solve(i+1,j,grid,k,v) or solve(i,j+1,grid,k,v)or solve(i-1,j,grid,k,v)or solve(i,j-1,grid,k,v)
		  #  v[i][j]=False
		k=[False]
		v=[[False for _ in range(len(grid))] for i in range(len(grid))]
		x,y=0,0
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if(grid[i][j]==1):
		            x,y=i,j
		            break
		return solve(x,y,grid,k,v)





		


#{ 
 # Driver Code Starts
T = int(input())
for i in range(T):
    n = int(input())
    grid = []
    for _ in range(n):
        a = list(map(int, input().split()))
        grid.append(a)
    obj = Solution()
    ans = obj.is_Possible(grid)
    if (ans):
        print("1")
    else:
        print("0")
    print("~")

# } Driver Code Ends