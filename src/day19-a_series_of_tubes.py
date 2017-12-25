from santas_little_helpers import day, get_data, timed
from direction import Direction, ds

today = day(2017, 19)

the_map = {}

def follow(the_map: [str]) -> (int, int):
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
