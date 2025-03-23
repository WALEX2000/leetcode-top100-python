#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            fingerprint = [0] * 26

            for char in word:
                fingerprint[ord(char) - ord('a')] += 1
            
            anagram_groups[tuple(fingerprint)].append(word)
        
        return list(anagram_groups.values())
        
# @lc code=end

