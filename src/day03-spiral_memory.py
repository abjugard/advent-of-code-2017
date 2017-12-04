from santas_little_helpers import day, get_data, timed
from enum import Enum
from typing import Type

today = day(2017, 3)

class Direction(Enum):
  NORTH = ('y', 1)
  WEST = ('x', -1)
  SOUTH = ('y', -1)
  EAST = ('x', 1)

  def __init__(self, axis: str, diff: int):
    self.axis = axis
    self.diff = diff

star1 = None
star2 = None

target = None
x, y = (1, 0)
step = 1

adjacency_values = {(0,0):1}
adjacency_matrix = [(-1, 1), (0, 1), (1, 1),
                    (-1, 0),         (1, 0),
                    (-1,-1), (0,-1), (1,-1)]
def adjacent_value(x: int, y: int):
  global star2
  if star2:
    return
  val = 0
  for i, j in adjacency_matrix:
    if (i+x, j+y) in adjacency_values:
      val += adjacency_values[(i+x, j+y)]
  if val >= target and not star2:
    star2 = val
  else:
    adjacency_values[(x,y)] = val

def move(side_length: int, direction: Type[Direction]) -> None:
  global step, x, y, star1
  if step + side_length < target:
    if not star2:
      for n in range(1, side_length+1):
        if direction.axis == 'x':
          adjacent_value(x+n*direction.diff, y)
        else:
          adjacent_value(x, y+n*direction.diff)
    if direction.axis == 'x':
      x += side_length*direction.diff
    else:
      y += side_length*direction.diff
    step += side_length
  else:
    for n in range(0, side_length):
      if step == target:
        star1 = abs(x)+abs(y)
        return
      step += 1
      if direction.axis == 'x':
        x += direction.diff
      else:
        y += direction.diff

def main() -> None:
  global target, x, y
  target = int(list(get_data(today))[0])
  side_length = 2
  while not star1:
    y -= 1
    for direction in Direction:
      move(side_length, direction)
    x += 1
    side_length += 2

  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
