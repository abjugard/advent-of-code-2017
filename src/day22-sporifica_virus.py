from santas_little_helpers import base_ops, day, get_data, timed
from enum import Enum

today = day(2017, 22)

class Direction(Enum):
  NORTH = (0, -1, 'w', 'e', 's')
  WEST = (-1, 0, 's', 'n', 'e')
  SOUTH = (0, 1, 'e', 'w', 'n')
  EAST = (1, 0, 'n', 's', 'w')

  def __init__(self, x:int, y:int, left:str, right:str, back:str) -> None:
    self.x = x
    self.y = y
    self.left = left
    self.right = right
    self.back = back

  def __add__(self, t:tuple) -> (int, int):
    return self.x+t[0], self.y+t[1]

ds = {
  'n': Direction.NORTH,
  'e': Direction.EAST,
  's': Direction.SOUTH,
  'w': Direction.WEST
}

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
  for y in range(len(data)):
    for x in range(len(data[0])):
      the_map[(x, y)] = data[y][x]
      reference[(x, y)] = data[y][x]
  start_pos = len(data) // 2, len(data) // 2
  print(f'{today} star 1 = {infect(start_pos)}')
  the_map = reference
  print(f'{today} star 2 = {infect(start_pos, evolved=True)}')

if __name__ == '__main__':
  timed(main)
