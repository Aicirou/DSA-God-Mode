import pytest
from solution import Solution

class TestPalindromePartitioning:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Basic case with multiple palindromes"""
        s = "aab"
        expected = [["a","a","b"], ["aa","b"]]
        result = self.solution.partition(s)
        assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
    
    def test_example_2(self):
        """Single character"""
        s = "a"
        expected = [["a"]]
        assert self.solution.partition(s) == expected
    
    def test_all_same_chars(self):
        """All same characters"""
        s = "aaa"
        expected = [["a","a","a"], ["a","aa"], ["aa","a"], ["aaa"]]
        result = self.solution.partition(s)
        assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
    
    def test_no_long_palindrome(self):
        """No palindrome longer than 1"""
        s = "abc"
        expected = [["a","b","c"]]
        assert self.solution.partition(s) == expected
    
    def test_full_palindrome(self):
        """Entire string is palindrome"""
        s = "aba"
        result = self.solution.partition(s)
        assert ["aba"] in result
        assert ["a","b","a"] in result

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
