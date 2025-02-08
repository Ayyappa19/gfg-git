#User function Template for python3

class Solution:
    def fill(self,  board):
        # code here
        n=len(board)
        m=len(board[0])
        from collections import deque
        q=deque()

        for i in range(n):
            if(board[i][0]=='O'):
                q.append((i,0))
            if((board[i][m-1])=='O'):
                q.append((i,m-1))


        for j in range(m):
            if(board[0][j]=='O'):
                q.append((0,j))
            if(board[n-1][j]=='O'):
                q.append((n-1,j))
        def check(i,j):
            return (0<=i<n) and (0<=j<m)

        while q:
            i,j=q.popleft()
            board[i][j]='?'
            dir=[(i+1,j),(i,j+1),(i-1,j),(i,j-1)]

            for ii,jj in dir:
                if not check(ii,jj):
                    continue
                if board[ii][jj]!="O":
                    continue
                q.append((ii,jj))
                board[ii][jj]="?"

        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    board[i][j]='X'
                elif board[i][j]=='?':
                    board[i][j]='O'
        return board



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            s = list(map(str, input().split()))
            mat.append(s)

        ob = Solution()
        ans = ob.fill(mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends