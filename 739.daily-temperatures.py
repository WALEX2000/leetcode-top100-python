#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for idx, temperature in enumerate(temperatures):
            answer.append(0)
            for next_idx, next_temperature in enumerate(temperatures[idx+1:]):
                if next_temperature > temperature:
                    answer[idx] = next_idx + 1
                    break
        
        return answer
# @lc code=end

