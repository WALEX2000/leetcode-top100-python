#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.word_map = dict()
        

    def insert(self, word: str) -> None:
        self.word_map[word] = True
        

    def search(self, word: str) -> bool:
        return self.word_map.get(word) == True
        

    def startsWith(self, prefix: str) -> bool:
        for word in self.word_map.keys():
            if word.startswith(prefix):
                return True
        
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

