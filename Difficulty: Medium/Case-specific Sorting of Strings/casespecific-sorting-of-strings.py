class Solution:
    def caseSort(self,s):
        #code here
        i,j=0,0
        upper=[]
        lower=[]
        for i in s:
            if i.isupper():
                upper.append(i)
            else:
                lower.append(i)
        i=0
        k=""
        upper.sort(reverse=True)
        lower.sort(reverse=True)
        while(i<len(s)):
            if s[i].isupper():
                k+=upper.pop()
            else:
                k+=lower.pop()
            i+=1
        return k
        
        