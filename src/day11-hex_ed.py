from santas_little_helpers import base_ops, day, get_data, timed
from collections import defaultdict

today = day(2017, 11)

def hex_walk(data: [str]) -> (int, int):
  maximum = 0
  x = 0
  y = 0
  for d in data:
    if d == 'n':
      y += 1
    elif d == 'ne':
      x += 1
      y += 1
    elif d == 'se':
      x += 1
    elif d == 's':
      y -= 1
    elif d == 'sw':
      x -= 1
      y -= 1
    elif d == 'nw':
      x -= 1
    dist = (abs(x)+abs(y)+abs(x-y))//2
    if dist > maximum:
      maximum = dist
  return dist, maximum

def main() -> None:
  data = get_data(today, base_ops + [('split',',')])
  star1, star2 = hex_walk(next(data))
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
