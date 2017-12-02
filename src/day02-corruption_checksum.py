from typing import Iterator
from santas_little_helpers import day, get_data, timed

today = day(2017, 2)

def spreadsheet_combinations(inp: list) -> Iterator[tuple]:
  for i in range(0, len(inp)-1):
    yield (inp[i], inp[i+1:])

def find_even_div(inp: list) -> int:
  for x, l in spreadsheet_combinations(inp):
    for quotient, remainder in [divmod(y, x) for y in l]:
      if remainder == 0:
        return quotient

def fmt(l: list) -> list:
  return sorted([int(s) for s in l])

def main() -> None:
  data = get_data(today, [('split', '\t'), ('func', fmt)])
  star1 = 0
  star2 = 0
  for row in data:
    star1 += row[-1]-row[0] # sorted list
    star2 += find_even_div(row)

  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
