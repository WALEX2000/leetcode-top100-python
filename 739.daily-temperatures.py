#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        stack = []
        for idx, temperature in enumerate(temperatures):

            while stack and temperature > temperatures[stack[-1]]:
                previous_idx = stack.pop()
                answer[previous_idx] = idx - previous_idx
            
            stack.append(idx)

        return answer
# @lc code=end

