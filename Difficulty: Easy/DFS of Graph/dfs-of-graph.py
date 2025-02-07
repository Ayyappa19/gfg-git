#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        def solve(i,l,adj,v):
            v[i]=not v[i]
            l.append(i)
            for i in adj[i]:
                if(v[i]):
                    solve(i,l,adj,v)
                
            
            
        l=[]
        v=[True]*len(adj)
        for i in range(len(adj)):
            if(v[i]):
                solve(i,l,adj,v)
        return l
                


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        # Create adjacency list with V vertices
        adj = [[] for i in range(V)
               ]  # List of lists (vector of vectors equivalent)

        # Reading edges
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Create an object of Solution class
        ob = Solution()
        ans = ob.dfsOfGraph(adj)

        # Printing the result
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
        print("~")
# } Driver Code Ends