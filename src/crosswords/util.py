
def repr_grid(grid: list[list[None | str]]) -> str:
    result = "GRID:\n"
    for row in grid:
        result += "  ".join("_" if cell is None else str(cell) for cell in row) + "\n"
    return result
