class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=""
        n=0
        for i,j in d.items():
            if j==1:
                c=i
                n+=1
            if n==k:
               return i
        return ""
