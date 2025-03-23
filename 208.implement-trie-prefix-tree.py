#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
from typing import Set
# @lc code=start
class Trie:

    def __init__(self):
        self.key_map : Set[str] = set()
        self.word_map : Set[str] = set()
        

    def insert(self, word: str) -> None:
        self.word_map.add(word)
        for i in range(1, len(word)+1):
            prefix = word[:i]
            self.key_map.add(prefix)
        

    def search(self, word: str) -> bool:
        return word in self.word_map
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.key_map
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

