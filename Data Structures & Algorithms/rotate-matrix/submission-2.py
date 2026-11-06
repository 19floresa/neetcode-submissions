class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        LEFT, RIGHT = 0, len(matrix) - 1
        while LEFT < RIGHT:
            for i in range(RIGHT-LEFT):
                top, bottom = LEFT, RIGHT
                entry_saved = matrix[top][LEFT+i]
                matrix[top][LEFT+i] = matrix[bottom-i][LEFT]
                matrix[bottom-i][LEFT] = matrix[bottom][RIGHT-i]
                matrix[bottom][RIGHT-i] = matrix[top+i][RIGHT]
                matrix[top+i][RIGHT] = entry_saved
            LEFT, RIGHT = LEFT + 1, RIGHT - 1
            