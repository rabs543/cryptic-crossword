import crosswords.scraper as scraper
from crosswords.algo_1 import can_place_entries
from crosswords.util import repr_grid

url = "https://timesforthetimes.co.uk/times-29073-a-semi-to-make-me-quaver"
entries = scraper.getCluesFromUrl(url)

print("Successfully scraped entries: {}".format(entries))
for size in [14, 15, 16]:
    grid = [[None for _ in range(size + 2)] for _ in range(size + 2)]
    for i in range(size + 2):
        grid[0][i] = grid[size + 1][i] = '_'
        grid[i][0] = grid[i][size + 1] = '_'
    result = can_place_entries(entries, grid, 1, 1)
    if result:
        print(repr_grid(result))
        break