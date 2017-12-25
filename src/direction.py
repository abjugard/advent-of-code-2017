from enum import Enum

class Direction(Enum):
  NORTH = (0, -1, 'wse')
  WEST  = (-1, 0, 'sen')
  SOUTH = (0,  1, 'enw')
  EAST  = (1,  0, 'nws')

  def __init__(self, x: int, y: int, dirs: str) -> None:
    self.x = x
    self.y = y
    self.left  = dirs[0]
    self.back  = dirs[1]
    self.right = dirs[2]

  def __add__(self, t: tuple) -> (int, int):
    return self.x+t[0], self.y+t[1]

ds = {
  'n': Direction.NORTH,
  'e': Direction.EAST,
  's': Direction.SOUTH,
  'w': Direction.WEST
}
