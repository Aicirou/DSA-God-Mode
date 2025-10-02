import pytest
from solution import Solution

class TestSubsets:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Basic case from LeetCode"""
        nums = [1, 2, 3]
        expected = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
        result = self.solution.subsets(nums)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_single_element(self):
        """Edge case: single element"""
        nums = [1]
        expected = [[], [1]]
        result = self.solution.subsets(nums)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_empty_array(self):
        """Edge case: empty array"""
        nums = []
        expected = [[]]
        assert self.solution.subsets(nums) == expected
    
    def test_larger_set(self):
        """Larger input"""
        nums = [1, 2, 3, 4]
        result = self.solution.subsets(nums)
        assert len(result) == 2**4  # Should have 16 subsets

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
