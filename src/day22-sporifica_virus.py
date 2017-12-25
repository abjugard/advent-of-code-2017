from santas_little_helpers import base_ops, day, get_data, timed
from direction import Direction, ds

today = day(2017, 22)

the_map = {}

def infect(p: (int, int), evolved: bool = False) -> int:
  d = Direction.NORTH
  infections = 0
  bound = 10000000 if evolved else 10000
  for _ in range(bound):
    c = the_map[p] if p in the_map else '.'
    if c == '#':
      d = ds[d.right]
      the_map[p] = 'f' if evolved else '.'
    elif c == 'f':
      d = ds[d.back]
      the_map[p] = '.'
    elif c == '.':
      d = ds[d.left]
      the_map[p] = 'w' if evolved else '#'
      if not evolved:
        infections += 1
    elif c == 'w':
      the_map[p] = '#'
      infections += 1
    p = d + p
  return infections

def main() -> None:
  global the_map
  data = list(get_data(today, base_ops + [('func', list)]))
  reference = {}
  for y, row in enumerate(data):
    for x, val in enumerate(row):
      the_map[(x, y)] = val
      reference[(x, y)] = val
  start_pos = len(data) // 2, len(data) // 2
  print(f'{today} star 1 = {infect(start_pos)}')
  the_map = reference
  print(f'{today} star 2 = {infect(start_pos, evolved=True)}')

if __name__ == '__main__':
  timed(main)
