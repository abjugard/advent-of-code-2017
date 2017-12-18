from santas_little_helpers import day, get_data, timed

today = day(2017, 17)

def hurricane(data: int) -> (int, int):
  l = [0]
  idx = 0
  for x in range(1,2017+1):
    idx = (idx + data) % len(l) + 1
    l = l[:(idx+1)] + [x] + l[(idx+1):]
  star1 = l[(l.index(2017)+1) % len(l)]
  second_val = 0
  for x in range(1,50000000+1):
    idx = (idx + data) % x + 1
    if idx == 1:
      second_val = x
  return star1, second_val

def main() -> None:
  data = int(next(get_data(today)))
  star1, star2 = hurricane(data)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
