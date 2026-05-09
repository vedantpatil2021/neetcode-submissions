from collections import Counter
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ["bat","bag","bank","band"] --> "ba"
        # ["dance","dag","danger","damage"] -> "da"
        #  n --> 4,, b -> 4,a -> 4 
        #  e -> 2, first element !+ return ""
        # result = []
        # for s in strs:        
        #     for c in s:  
        #         result.append(c)
    

        # c = Counter(result)
        # r = ""
        # for key, value in c.items():
        #     if len(strs) == value:
        #         r += key
        
        # print(result)  
        if len(strs)==1:
            return strs[0]
        if len(strs) ==0:
            return ""
        strs = sorted(strs,key=len)
        smal_word = strs[0] 
        n = len(strs)-1
        for i in range(len(strs[0])):
            contain=0
            for remain in strs[1:]:
                print(remain , smal_word[:len(smal_word)-i], remain.find(smal_word[:len(smal_word)-i]))
                if remain.find(smal_word[:len(smal_word)-i]) != -1:
                    contain += 1
                    print(contain)
                else:
                    contain -= 1
            if contain==n:
                return smal_word[:len(strs[0])-i]
        return ""
        

