#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        v=[[True for _ in range(len(grid[0]))] for i in range(len(grid))]
        def solve(i,j,grid,v,n,m):
            if(i<0 or j>=m or j<0 or i>=n or not v[i][j] or grid[i][j]==0):
                return 
            v[i][j]=False
            solve(i+1,j,grid,v,n,m)
            solve(i-1,j,grid,v,n,m)
            solve(i-1,j+1,grid,v,n,m)
            solve(i+1,j-1,grid,v,n,m)
            solve(i,j-1,grid,v,n,m)
            solve(i,j+1,grid,v,n,m)
            solve(i+1,j+1,grid,v,n,m)
            solve(i-1,j-1,grid,v,n,m)
                 
            
       
        c=0
        n=len(grid)
        m=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(type(grid[i][j]))
                # print(v[i][j],grid[i][j])
                if(v[i][j]==True and grid[i][j]==1):
                    # print("hi")
                    # v[i][j]=False
                    c+=1
                    solve(i,j,grid,v,n,m)
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends