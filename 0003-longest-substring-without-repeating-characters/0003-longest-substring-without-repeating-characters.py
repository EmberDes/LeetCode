class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l =list(s)
        p1 = 0
       
        ml = 1 
        
        while p1<len(s):
            mc =set()
            for ch in range(p1,len(s)):
                if l[ch] not in mc:
                    mc.add(l[ch])
                    
                else:
                    break
            
            ml = max(ml,len(mc))
            p1 +=1

            
        return ml
