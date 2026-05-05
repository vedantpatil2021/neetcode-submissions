class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted() --> nlogn
        # if sorted(list(s)) == sorted(list(t)):
        #     return True        
        # return False

        s = Counter(list(s))
        t = Counter(list(t))

        if s == t:
            return True
        
        return False
