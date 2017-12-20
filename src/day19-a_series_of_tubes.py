from santas_little_helpers import day, get_data, timed
from enum import Enum

today = day(2017, 19)

class Direction(Enum):
  NORTH = (0, -1, 'w', 'e')
  WEST = (-1, 0, 's', 'n')
  SOUTH = (0, 1, 'e', 'w')
  EAST = (1, 0, 'n', 's')

  def __init__(self, x: int, y: int, left: str, right: str):
    self.x = x
    self.y = y
    self.left = left
    self.right = right

  def __add__(self, t: tuple):
    return self.x+t[0], self.y+t[1]

ds = {
  'n': Direction.NORTH,
  'e': Direction.EAST,
  's': Direction.SOUTH,
  'w': Direction.WEST
}

def follow(the_map: [[str]]) -> (int, int):
  p = the_map[0].index('|'), 0
  d = Direction.SOUTH
  letters = ''
  steps = 0
  while True:
    c = the_map[p[1]][p[0]]
    if c == ' ':
      break
    elif c == '+':
      l = ds[d.left] + p
      d = ds[d.left] if the_map[l[1]][l[0]] != ' ' else ds[d.right]
    elif c not in '-|':
      letters += c
    p = d + p
    steps += 1
  return letters, steps

def main() -> None:
  data = get_data(today, [('func', list)])
  star1, star2 = follow(list(data))
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
