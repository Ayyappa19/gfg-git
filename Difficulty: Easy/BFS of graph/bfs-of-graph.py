#User function Template for python3
class Solution:
    # Function to return Breadth First Traversal of given graph.
    from typing import List
    from collections import deque 
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        # code here
        from queue import deque
        l=[0]
        q=deque()
        q.append(0)
        v=[True]*len(adj)
        v[0]=False
        while(len(q)!=0):
            k=q.popleft()
            for i in adj[k]:
                if(v[i]):
                    q.append(i)
                    l.append(i)
                    v[i]=not v[i]
        return l
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        V = int(input())  # Number of vertices
        E = int(input())  # Number of edges
        adj = [[] for i in range(V)]  # Adjacency list
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph

        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        print(" ".join(map(str, ans)))  # Print the BFS traversal result

# } Driver Code Ends