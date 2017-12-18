from santas_little_helpers import day, get_data, timed

today = day(2017, 14)

arr_size = 256

def to_ascii(data: str) -> [int]:
  return [ord(x) for x in data]+[17, 31, 73, 47, 23]

def hex_representation(l: [int]) -> str:
  hex_list = []
  for i in range(0, 16):
    num, *rest = l[i*16:(i+1)*16]
    for j in rest:
      num ^= j
    hex_list += [hex(num)]
  return ''.join([h[2:4].zfill(2) for h in hex_list])

def hash_data(seed: str) -> str:
  lengths = to_ascii(seed)
  l = list(range(arr_size))
  idx = 0
  skip = 0
  for _ in range(64):
    for n in lengths:
      l = l[idx % arr_size:]+l[:idx % arr_size]
      l = list(reversed(l[:n]))+l[n:]
      l = l[(arr_size-idx) % arr_size:]+l[:(arr_size-idx) % arr_size]
      idx += n+skip
      skip += 1
  return hex_representation(l)

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
