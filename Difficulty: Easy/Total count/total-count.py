#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        # code here
        c=0
        for i in arr:
            x=i//k
            y=i%k
            # c+=x+y
            if y!=0:
                x+=1
            c+=x
            # print(x+y)
        return c
            
                
                

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalCount(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends