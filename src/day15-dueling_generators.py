from santas_little_helpers import day, get_data, timed
from typing import Iterator

today = day(2017, 15)

def generator(val: int, mult: int, mod: int = 1) -> Iterator:
  while True:
    val *= mult
    val %= 2147483647
    if val % mod == 0:
      yield val & 0xffff

def duel(a_val: int, b_val: int) -> (int, int):
  a_mult, b_mult = 16807, 48271
  gen_a, gen_b = generator(a_val, a_mult), generator(b_val, b_mult)
  star1 = sum(next(gen_a) == next(gen_b) for _ in range(40000000))
  a_mod, b_mod = 4, 8
  gen_a, gen_b = generator(a_val, a_mult, a_mod), generator(b_val, b_mult, b_mod)
  return star1, sum(next(gen_a) == next(gen_b) for _ in range(5000000))

def main() -> None:
  data = get_data(today)
  gs = tuple()
  for x in data:
    gs += int(x[-3:]),
  star1, star2 = duel(*gs)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
