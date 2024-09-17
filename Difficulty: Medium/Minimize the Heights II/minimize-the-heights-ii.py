#User function Template for python3

class Solution:
    def getMinDiff(self, l,k):
        # code here
        l.sort()
        z=l[-1]-l[0]
        for i in range(1,len(l)):
            if l[i]-k<0:
                continue
            mini=min(l[0]+k,l[i]-k)
            maxi=max(l[-1]-k,l[i-1]+k)
            z=min(z,maxi-mini)
        return z
            
        # l1=[]
        # l2=[]
        # for i in l:
        #     if(i-k>=0):
        #         l1.append(i-k)
        # for i in l:
        #     l2.append(i+k)
        # l1.sort()
        # l2.sort()
        # # print(l1)
        # # print(l2)
        # if(len(l)!=len(l1)):
        #     l1.sort()
        #     l2.sort()
        #     ll=[]
        #     x=l2[-1]-l2[0]
        #     x1=l1[-1]-l2[0]
        #     if(x>=0):
        #         ll.append(x)

        #     if(x1>=0):
        #         ll.append(x1)
        #     ll.sort()
        #     # print(ll)
        #     return ll[0]
            
        # ll=[]
        # x=l2[-1]-l1[0]
        # x1=l1[-1]-l2[0]
        # x2=l2[-1]-l2[0]
        # x3=l1[-1]-l1[0]
        # if(x>=0):
        #     ll.append(x)

        # if(x1>=0):
        #     ll.append(x1)
        # if(x2>=0):
        #     ll.append(x2)
        # if(x3>=0):
        #     ll.append(x3)
        # ll.sort()
        # # print(ll)
        # return ll[0]
        # #
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends