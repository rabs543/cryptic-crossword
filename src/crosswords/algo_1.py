from crosswords.entry import Entry


def can_place_entries(
    entries: list[Entry],
    grid,
    cursor_row,
    cursor_column,
    unchecked_cells: list[tuple[int, int]] = [],
):
    if not entries:
        return grid

    island_unchecked_cells = [
        cell
        for cell in unchecked_cells
        if (
            not entries[0].is_across
            and (
                (cell[0], cell[1] - 1)
                in unchecked_cells
                and (cell[0], cell[1] - 2)
                in unchecked_cells
            )
            or entries[0].is_across
            and (
                ((cell[0] - 1, cell[1]) in unchecked_cells)
                and ((cell[0] - 2, cell[1]) in unchecked_cells)
            )
        )
    ]

    entry = entries[0]
    first_unchecked = min(island_unchecked_cells, default=None)

    # Generate possible starting positions
    possible_starts = (
        (r, c)
        for r in range(cursor_row, len(grid))
        for c in range((cursor_column if r == cursor_row else 0), len(grid))
        if not first_unchecked or (r, c) <= first_unchecked
    )

    for row, column in possible_starts:
        if can_place_single_entry(
            grid, *get_adjusted_position(row, column, entry.is_across), entry
        ):
            if c := can_place_entries(
                entries[1:],
                grid_with_entry(
                    grid, *get_adjusted_position(row, column, entry.is_across), entry
                ),
                row,
                column + (0 if entry.is_across else 2),
                new_unchecked_cells(unchecked_cells, row, column, entry),
            ):
                return c
    return False


def can_place_single_entry(grid, row, column, entry) -> bool:
    """Check if the entry can be placed at the given position."""
    if row < 0 or column < 0:
        return False

    if entry.is_across and column + entry.length() > len(grid):
        return False
    if not entry.is_across and row + entry.length() > len(grid):
        return False

    cells = (
        (row, column + i) if entry.is_across else (row + i, column)
        for i in range(entry.length())
    )
    return all(
        grid[r][c] in (None, letter)
        for (r, c), letter in zip(cells, entry.answer)
    )


def grid_with_entry(grid, row, column, entry):
    """Return a new grid with the entry placed."""
    new_grid = [row[:] for row in grid]  # Shallow copy for efficiency
    for i, letter in enumerate(entry.answer):
        if entry.is_across:
            new_grid[row][column + i] = letter
        else:
            new_grid[row + i][column] = letter
    return new_grid


def new_unchecked_cells(unchecked_cells, row, column, entry: Entry):
    """Update the unchecked cells after placing an entry."""
    affected_cells = [
        (row, column + i) if entry.is_across else (row + i, column)
        for i in range(entry.length() - 2)
    ]
    return [
        cell for cell in unchecked_cells if cell not in affected_cells
    ] + [
        cell for cell in affected_cells if cell not in unchecked_cells
    ]


def get_adjusted_position(row, column, is_across: bool):
    """Adjust the position based on the orientation."""
    return (row, column - 1) if is_across else (row - 1, column)