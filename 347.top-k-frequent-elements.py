#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_counter = defaultdict(int)
        for number in nums:
            number_counter[number] += 1

        heap = []
        for number, counter in number_counter.items():
            heapq.heappush(heap, (-counter, number))
        
        result = []
        
        for _ in range(k):
            _, number = heapq.heappop(heap)
            result.append(number)

        return result

        
# @lc code=end

