#User function Template for python3


class Solution:

    def kthElement(self, arr1, arr2, k):
        c=0
        i,j=0,0
        while(i<len(arr1) and j<len(arr2)):
            if (arr1[i]<=arr2[j]):
                c+=1
                if c==k:
                    return arr1[i];
                i+=1
                
            elif (arr1[i]>arr2[j]):
                c+=1
                if c==k:
                    return arr2[j];
                j+=1
                
            # elif arr1[i]==arr2[j]:
            #     c+=2
            #     if c>=k:
            #         return arr1[i];
            #     i+=1
            #     j+=1
                
        # while(i<len(arr1)):
        #     if c==k:
        #         return arr1[i-1]
        #     else:
        #         c+=1
        #         i+=1
        # while(j<len(arr2)):
        #     if c==k:
        #         return arr2[j-1]
        #     else:
        #         c+=1
        #         j+=1 
        if i<len(arr1):
            return arr1[i+k-c-1]
        return arr2[j+k-c-1]
        
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends