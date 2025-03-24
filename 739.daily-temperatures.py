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
            while stack:
                previous_idx = stack[-1]
                previous_temperature = temperatures[previous_idx]
                if temperature > previous_temperature:
                    answer[previous_idx] = idx - previous_idx
                    stack = stack[:-1]
                else:
                    break
            
            stack.append(idx)

        return answer
# @lc code=end

