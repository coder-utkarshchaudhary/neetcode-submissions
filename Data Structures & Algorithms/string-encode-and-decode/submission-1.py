class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans+=str(len(s))+"%"+s
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        ans = []
        while i<n:
            j = i
            while s[j]!="%":
                j+=1

            cnt = int(s[i:j])
            ans.append(s[j+1:j+1+cnt])
            
            i=j+1+cnt

        return ans