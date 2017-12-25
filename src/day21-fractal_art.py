from santas_little_helpers import day, get_data, timed

today = day(2017, 21)
book = {}

def rotate(grid: tuple) -> tuple:
  size = len(grid)
  new = []
  for x in range(size):
    row = ''
    for y in range(size):
      row += grid[size-1-y][x]
    new += [row]
  grid = new
  return tuple(grid)
        
def mirror(grid: tuple) -> tuple:
  size = len(grid)
  new = []
  for y in range(size):
    row = ''
    for x in range(size):
      row += grid[y][size-1-x]
    new += [row]
  return tuple(new)

def pixels(grid: [str], bound: int = 5) -> int:
  for _ in range(bound):
    size = len(grid)
    n_grid = []
    n = 2+(size%2)
    for r in range(size//n):
      n_grid += [''] * (n+1)
      for c in range(size//n):
        sub_grid = [row[n*c:n*(c+1)] for row in grid[n*r:n*(r+1)]]
        expanded = book[tuple(sub_grid)]
        for j in range(n+1):
          n_grid[j-n-1] += expanded[j]
    grid = n_grid
  count = 0
  for c in str(grid):
    if c == '#':
      count += 1
  return count

def parse(line: str) -> (str, str):
  pattern, becomes = line.strip().split(' => ')
  return tuple(pattern.split('/')), becomes.split('/')

def main() -> None:
  artbook = get_data(today, [('func', parse)])
  for pattern, becomes in artbook:
    book[pattern] = becomes
    for _ in range(1,4):
      pattern = rotate(pattern)
      book[pattern] = becomes
      book[mirror(pattern)] = becomes
  grid = ['.#.',
          '..#',
          '###']
  print(f'{today} star 1 = {pixels(grid)}')
  print(f'{today} star 2 = {pixels(grid, 18)}')

if __name__ == '__main__':
  timed(main)
