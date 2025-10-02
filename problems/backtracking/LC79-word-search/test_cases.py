import pytest
from solution import Solution

class TestWordSearch:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Basic case - word exists"""
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        word = "ABCCED"
        assert self.solution.exist(board, word) == True
    
    def test_example_2(self):
        """Word with path that backtracks"""
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        word = "SEE"
        assert self.solution.exist(board, word) == True
    
    def test_example_3(self):
        """Word does not exist"""
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        word = "ABCB"
        assert self.solution.exist(board, word) == False
    
    def test_single_cell(self):
        """Single cell board"""
        board = [['A']]
        assert self.solution.exist(board, "A") == True
        assert self.solution.exist(board, "B") == False
    
    def test_single_letter_word(self):
        """Single letter word"""
        board = [['A','B'],['C','D']]
        assert self.solution.exist(board, "A") == True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
