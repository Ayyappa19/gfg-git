#User function Template for python3

class Solution:
    def roundToNearest (self, k) : 
        
        #Complete the function
        x = len(k)
        a = int(k[x - 1])
        
        k = list(k)
        
        if a <= 5:
            k[x - 1] = '0'
        else:
            k[x - 1] = '0'
            c = 1
            for b in range(x - 2, -1, -1):
                num = int(k[b])
                sum_val = num + c
                k[b] = str(sum_val % 10)
                c = sum_val // 10
                if c == 0:
                    break
            if c == 1:
                return '1' + ''.join(k)
        
        return ''.join(k)
            
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends