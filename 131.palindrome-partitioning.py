#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List
# @lc code=start

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(string : str) -> bool:
            return string == string[::-1]
         
        def find_palindromes(palindrome: List[str], s : str) -> List[List[str]]:
            found_palindromes = []

            if not s:
                found_palindromes.append(palindrome)

            for palindrome_size in range(1, len(s)+1):
                palindrome_candidate = s[:palindrome_size]
                if is_palindrome(palindrome_candidate):
                    new_palindrome = palindrome + [palindrome_candidate]
                    found_palindromes += find_palindromes(new_palindrome, s[palindrome_size:])
            
            return found_palindromes

        return find_palindromes([], s)
        
# @lc code=end

