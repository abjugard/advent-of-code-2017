from santas_little_helpers import day, get_data, timed
from knot_hash import hash_data

today = day(2017, 14)

def bits(h: str) -> [int]:
  return [int(b) for b in f'{int(h, 16):0128b}']

def defrag(seed: str) -> (int, int):
  def neighbors(i, j):
    if ((i, j)) in seen:
      return
    if not rows[i][j]:
      return
    seen.add((i, j))
    if i > 0:   neighbors(i-1, j)
    if j > 0:   neighbors(i, j-1)
    if i < 127: neighbors(i+1, j)
    if j < 127: neighbors(i, j+1)
  count = 0
  rows = []
  for i in range(128):
    h = hash_data(f'{seed}-{i}')
    row = bits(h)
    count += sum(row)
    rows += [row]
  star1 = count
  seen = set()
  count = 0
  for i in range(128):
    for j in range(128):
      if (i,j) in seen:
        continue
      if not rows[i][j]:
        continue
      count += 1
      neighbors(i, j)
  return star1, count

def main() -> None:
  seed = str(next(get_data(today)))
  star1, star2 = defrag(seed)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
