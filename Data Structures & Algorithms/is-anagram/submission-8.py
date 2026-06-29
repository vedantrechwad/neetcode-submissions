class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False 
        return True 

#countT.get(c, 0) this gets the frequency of the character in the other hasmap
#we add 0 so if it is not present it would return 0 as default 
#the equality condition would anyway break and it would return false 
        
        