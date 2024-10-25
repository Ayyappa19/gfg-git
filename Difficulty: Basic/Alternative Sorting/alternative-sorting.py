class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        ans=[]
        arr.sort()
        a=len(arr)
        b=a//2
        for i in range(b):
            ans.append(arr[a-i-1])
            ans.append(arr[i])
        if a%2 == 1:
            ans.append(arr[b])
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends