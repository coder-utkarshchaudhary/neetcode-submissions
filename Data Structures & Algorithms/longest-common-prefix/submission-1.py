class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = strs[0]
        for s in strs[1:]:
            if len(s) < len(p):
                p, s = s, p

            for i in range(len(p)):
                if p[i]!=s[i]:
                    if i>0:
                        p = p[:i]
                        break
                    else:
                        return ""
        
        return p