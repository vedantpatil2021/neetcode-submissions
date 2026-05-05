class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # "racecar" & "carrace"
        # len(s) = len(t)
        # s= {r:2,a:2,c:2,e:1} t= {r:2,a:2,c:2,e:1}
        if sorted(list(s)) == sorted(list(t)):
            return True
        
        return False
