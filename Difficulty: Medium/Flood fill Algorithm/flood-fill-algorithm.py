class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    def solve(i,j,k,adj,x):
	        if(i<0 or j<0 or i>len(adj)-1 or j>len(adj[0])-1 or adj[i][j]!=x):
	            return
	        adj[i][j]=k
	        solve(i+1,j,k,adj,x)
	        solve(i-1,j,k,adj,x)
	        solve(i,j+1,k,adj,x)
	        solve(i,j-1,k,adj,x)
		#Code here
		v=[False]*len(image)
		if(image[sr][sc]==newColor):
		    return image
		solve(sr,sc,newColor,image,image[sr][sc])
		return image
		



#{ 
 # Driver Code Starts
T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    # Print the modified image
    for row in ans:
        print(" ".join(map(str, row)))

    # Print the separator
    print("~")

# } Driver Code Ends