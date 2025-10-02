import pytest
from solution import Solution

class TestCombinationSum2:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Basic case with duplicates"""
        candidates = [10,1,2,7,6,1,5]
        target = 8
        expected = [[1,1,6], [1,2,5], [1,7], [2,6]]
        result = self.solution.combinationSum2(candidates, target)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_example_2(self):
        """Case with many duplicates"""
        candidates = [2,5,2,1,2]
        target = 5
        expected = [[1,2,2], [5]]
        result = self.solution.combinationSum2(candidates, target)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_no_solution(self):
        """No valid combination"""
        candidates = [2]
        target = 1
        assert self.solution.combinationSum2(candidates, target) == []
    
    def test_single_element(self):
        """Single element matches target"""
        candidates = [1]
        target = 1
        assert self.solution.combinationSum2(candidates, target) == [[1]]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
