import pytest
from solution import Solution

class TestSubsetsWithDup:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Basic case with duplicates"""
        nums = [1, 2, 2]
        expected = [[], [1], [1,2], [1,2,2], [2], [2,2]]
        result = self.solution.subsetsWithDup(nums)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_example_2(self):
        """Case with multiple duplicates"""
        nums = [0]
        expected = [[], [0]]
        result = self.solution.subsetsWithDup(nums)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_all_duplicates(self):
        """All elements are same"""
        nums = [1, 1, 1]
        expected = [[], [1], [1,1], [1,1,1]]
        result = self.solution.subsetsWithDup(nums)
        assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
    
    def test_no_duplicates(self):
        """No duplicate elements"""
        nums = [1, 2, 3]
        result = self.solution.subsetsWithDup(nums)
        assert len(result) == 2**3  # Should have 8 subsets

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
