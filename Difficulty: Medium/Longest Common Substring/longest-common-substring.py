#User function Template for python3
class Solution:
    def longestCommonSubstr(self, str1: str, str2: str) -> int:
        c=0
        for i in range(len(str1)):
            for j in range(1,len(str1)-i+1):
                ans=str1[i:i+j]
                if ans in str2:
                    c=max(c,j)
                else:
                    break
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends