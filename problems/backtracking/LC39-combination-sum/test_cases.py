import pytest
from solution import Solution

class TestCombinationSum:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Basic case from LeetCode"""
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2,2,3], [7]]
        result = self.solution.combinationSum(candidates, target)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_example_2(self):
        """Multiple uses of same element"""
        candidates = [2, 3, 5]
        target = 8
        expected = [[2,2,2,2], [2,3,3], [3,5]]
        result = self.solution.combinationSum(candidates, target)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_single_element(self):
        """Single candidate"""
        candidates = [2]
        target = 1
        expected = []
        assert self.solution.combinationSum(candidates, target) == expected
    
    def test_exact_match(self):
        """Target equals single candidate"""
        candidates = [1]
        target = 1
        expected = [[1]]
        assert self.solution.combinationSum(candidates, target) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
