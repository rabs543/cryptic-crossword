import copy

from crosswords.entry import Entry


class Grid:

    def __init__(self, size: int):
        self.size = size
        self.grid = {i: {j: None for j in range(size)} for i in range(size)}
        self.history = []

    def place_entry(
        self, entry: Entry, cursor_row: int, cursor_column: int, is_across: bool
    ) -> None:
        new_grid = copy.deepcopy(self.grid)
        self.history.append(self.grid)
        self.grid = new_grid
        for i, letter in enumerate(entry.answer):
            if is_across:
                new_grid[cursor_row][cursor_column + i] = letter
            else:
                new_grid[cursor_row + i][cursor_column] = letter

    def revert(self):
        self.grid = self.history.pop()

    def can_place_entry(
        self,
        entry: Entry,
        cursor_row: int,
        cursor_column: int,
        is_across: bool,
    ) -> bool:
        """
        Returns true if placing the entry wouldn't lead to conflicts with existing letters in the grid.
        """
        if is_across and entry.length() > self.size - cursor_column:
            return False
        if not is_across and entry.length() > self.size - cursor_row:
            return False
        if is_across:
            return all(
                self.grid[cursor_row][cursor_column + i] is None
                or self.grid[cursor_row][cursor_column + i] == letter
                for i, letter in enumerate(entry.answer)
            )
        else:
            return all(
                self.grid[cursor_row + i][cursor_column] is None
                or self.grid[cursor_row + i][cursor_column] == letter
                for i, letter in enumerate(entry.answer)
            )

    def __repr__(self):
        result = "GRID:\n"
        for row in self.grid.values():
            result += "  ".join(
                map(lambda x: "_" if x is None else str(x), row.values())
            )
        return result
