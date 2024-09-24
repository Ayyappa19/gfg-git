#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, t):
        #code here
        a={}
        for i in t:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
    
        i=0
        b=0
        x=len(s)+1
        res="-1"
        c={}
    
        for j in range(len(s)):
            d=s[j]
            if d in a:
                c[d]=c.get(d, 0) + 1
                if c[d]==a[d]:
                    b+=1
    
            while b == len(a):
                if (j-i+1)<x:
                    x=j-i+1
                    res= s[i:j+1]
    
                e=s[i]
                if e in a:
                    c[e]-=1
                    if c[e]<a[e]:
                        b-=1
                i+=1
    
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends