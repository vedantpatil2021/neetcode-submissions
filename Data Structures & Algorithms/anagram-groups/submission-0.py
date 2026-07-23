class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        groups = {}
        for i in range(len(strs)):
            sign = ''.join(sorted(strs[i]))
            if sign in groups:
                groups[sign].append(i)
            else:
                groups[sign] = [i]


        for indx in groups.values():
            words = [strs[i] for i in indx]
            output.append(words)
        
        output.reverse()

        return output
        