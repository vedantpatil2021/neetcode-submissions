class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []

        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                ans[stk_i] = i - stk_i

            stk.append((t,i))

        return ans        


















###### ==================== Brute Force =======================
        # out_stk = []
    
        # for i in range(len(temperatures)):
        #     days_count = 0
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             days_count = j - i
        #             break
            
        #     out_stk.append(days_count)

        # return out_stk