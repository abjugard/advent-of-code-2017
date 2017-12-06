from santas_little_helpers import *

today = day(2017, 6)

def redistribute(page: list, page_size: int = 16) -> tuple:
  i = page.index(max(page))
  val = page[i]
  page[i] = 0
  for idx in range(i, i+val):
    page[(idx+1) % page_size] += 1
  return tuple(page)

def reallocate(page: tuple) -> (int, int):
  seen = {}
  count = 0
  while page not in seen:
    seen[page] = count
    page = redistribute(list(page))
    count += 1
  return count, count-seen[page]

def main() -> None:
  data = next(get_data(today, [('split', '\t'), ('map', int)]))
  star1, star2 = reallocate(tuple(data))
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
