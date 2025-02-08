#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        def solve(i):
            v[i]=False
            for j in range(len(adj)):
                if(adj[i][j]==1 and v[j] ):
                    solve(j)
        v=[True]*V
        c=0
        for i in range(len(adj)):
            if v[i]:
                c+=1
                solve(i)
        return c
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
        print("~")
# } Driver Code Ends