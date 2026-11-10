class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict={}
        for ch in s:
            if ch not in dict:
                dict[ch]=s.count(ch)
        for ch in t:
            if ch in dict:
                if t.count(ch)==dict[ch]:
                    continue
                else:
                    return False
            else:
                return False
        return True
        
        