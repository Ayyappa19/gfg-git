#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        k=1
        c=0
        for i in nums:
            if i==0 and c==0:
                c=1
                continue
            else:
                k*=i
        # print(k)
        if c!=0:
            # print('hi')
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=k
                else:
                    nums[i]=0
            return nums
        else:
            # print('hello')
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=k
                else:
                    nums[i]=k//nums[i]
            return nums
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends