#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
from typing import Dict, List
# @lc code=start
class Trie:

    def __init__(self):
        self.key_map : Dict[str, List[str]] = dict()
        

    def insert(self, word: str) -> None:
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if not self.key_map.get(prefix):
                self.key_map[prefix] = []
            self.key_map[prefix].append(word)
        

    def search(self, word: str) -> bool:
        return word in self.key_map.get(word, [])
        

    def startsWith(self, prefix: str) -> bool:
        return len(self.key_map.get(prefix, [])) > 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

