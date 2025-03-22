#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = [list(s)]

        def create_new_full_palindromes(palindrome: str, prefix_length: str, suffix_length : int, existing_palindromes: List[List[str]]) ->  List[List[str]]:
            new_full_palindromes = []
            for existing_palindrome in existing_palindromes:
                
                prefix = []
                missing_prefix_characters = prefix_length
                while(missing_prefix_characters > 0):
                    try:
                        prefix_character = existing_palindrome[len(prefix)]
                    except IndexError:
                        missing_prefix_characters = -1
                        break
                    prefix.append(prefix_character)
                    missing_prefix_characters -= len(prefix_character)
                if missing_prefix_characters < 0:
                    continue

                suffix = []
                missing_suffix_characters = suffix_length
                while(missing_suffix_characters > 0):
                    try:
                        suffix_character = existing_palindrome[len(prefix) + len(palindrome) + len(suffix)]
                    except IndexError:
                        missing_suffix_characters = -1
                        break

                    suffix.append(suffix_character)
                    missing_suffix_characters -= len(suffix_character)
                if missing_suffix_characters < 0:
                    continue

                new_palindrome = prefix + [palindrome] + suffix
                if new_palindrome in new_full_palindromes:
                    continue
                
                new_full_palindromes.append(new_palindrome)
            
            return new_full_palindromes


        for palindrome_end_offset in range(1,len(s)):
            for substring_start_index in range(len(s)-palindrome_end_offset):
                substring_end_index = substring_start_index + palindrome_end_offset
                
                substring = s[substring_start_index:substring_end_index+1]
                reversed_substring = substring[::-1]
                if substring == reversed_substring:
                    suffix_length = len(s) - (substring_end_index + 1)
                    new_palindromes = create_new_full_palindromes(substring, substring_start_index, suffix_length, palindromes)
                    palindromes += new_palindromes

        return palindromes

    def partition_incomplete(self, s: str) -> List[List[str]]:
        palindromes = [list(s)]

        for palindrome_end_offset in range(1,len(s)):
            for substring_start_index in range(len(s)-palindrome_end_offset):
                substring_end_index = substring_start_index + palindrome_end_offset
                
                substring = s[substring_start_index:substring_end_index+1]
                reversed_substring = substring[::-1]
                if substring == reversed_substring:
                    palindrome_prefix = list(s[:substring_start_index])
                    palindrome_suffix = list(s[substring_end_index+1:])
                    palindrome = palindrome_prefix + [substring] + palindrome_suffix
                    palindromes.append(palindrome)

        return palindromes
        
# @lc code=end

