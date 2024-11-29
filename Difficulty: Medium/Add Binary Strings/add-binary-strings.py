#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        s1 = s1[::-1]
        s2 = s2[::-1]
        
        carry = 0
        n = max(len(s1),len(s2))
        i = 0
        res = []
        while i<n:
          a = s1[i] if i<len(s1) else 0
          b = s2[i] if i<len(s2) else 0
          total = int(a)+int(b)+carry 
          if total>=2:
            carry = 1
          else:
            carry = 0
            
          if total==1 or total==3:
            res.append('1')
          else:
            res.append('0')
          i+=1
          
          
        if carry==1:
          res.append('1')
        res = res[::-1]
        ss=""
        for i in res:
            ss+=i
        return ss


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends