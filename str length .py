class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        start = 0
        i = 0

        for char in s:
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            
            
            char_index_map[char] = i
            
            
            max_length = max(max_length, i - start + 1)
            
            i += 1  
        
        return max_length
