import pytest
from solution import Solution

class TestPermutations:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Basic case from LeetCode"""
        nums = [1, 2, 3]
        expected = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        result = self.solution.permute(nums)
        assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
    
    def test_two_elements(self):
        """Edge case: two elements"""
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        result = self.solution.permute(nums)
        assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
    
    def test_single_element(self):
        """Edge case: single element"""
        nums = [1]
        expected = [[1]]
        assert self.solution.permute(nums) == expected
    
    def test_count_permutations(self):
        """Test that we get the correct number of permutations"""
        nums = [1, 2, 3, 4]
        result = self.solution.permute(nums)
        # 4! = 24 permutations
        assert len(result) == 24
        # All permutations should be unique
        assert len(result) == len(set(map(tuple, result)))

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
