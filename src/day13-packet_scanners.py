from santas_little_helpers import *

today = day(2017, 13)

def waiting_time(data: [int]) -> (int, int):
  star1 = None
  delay = 0
  while delay or not star1:
    caught = 0
    for layer, severity in data:
      if not (layer+delay) % ((severity-1)*2):
        caught += layer*severity
        if star1: break
    else:
      if not star1:
        star1 = caught
      else: break
    delay += 1
  return star1, delay

def fun(line: str) -> [int]:
  return [int(i) for i in line]

def main() -> None:
  data = get_data(today, base_ops + [('split', ': '), ('func', fun)])
  star1, star2 = waiting_time(list(data))
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
