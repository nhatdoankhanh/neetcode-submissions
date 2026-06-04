class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr_s = [0 for _ in range(26)]
        arr_t = [0 for _ in range(26)]
        s.lower()
        t.lower()
        for i in range(len(s)):
            arr_s[ord(s[i]) - 97] += 1
            arr_t[ord(t[i]) - 97] += 1
            
        for i in range(26):
            if arr_s[i] != arr_t[i]:
                return False
        return True
        
        
