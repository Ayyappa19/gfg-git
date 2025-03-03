# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        a.sort()
        b.sort()
        i,j=0,0
        if(len(a)!=len(b)):
            return False
        else:
            i,j=0,0
            while(i<len(a) and j<len(b)):
                if(a[i]!=b[i]):
                    return False
                i+=1
                j+=1
            return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        arr1 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        ob = Solution()
        if ob.checkEqual(arr1, arr2):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends