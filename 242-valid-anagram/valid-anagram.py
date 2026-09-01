class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        compare={}
        for i in range(len(s)):
            if s[i] in compare:
                compare[s[i]]+=1
            else:
                compare[s[i]]=1
            if t[i] in compare:
                compare[t[i]]-=1
            else:
                compare[t[i]]=-1
        return all(count == 0 for count in compare.values())

                


        