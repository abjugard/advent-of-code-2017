from santas_little_helpers import day, get_data, timed

today = day(2017, 10)
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

def hash_data(lengths: [int], repeat: int = 1) -> [int]:
  l = list(range(arr_size))
  idx = 0
  skip = 0
  for _ in range(repeat):
    for n in lengths:
      l = l[idx % arr_size:]+l[:idx % arr_size]
      l = list(reversed(l[:n]))+l[n:]
      l = l[(arr_size-idx) % arr_size:]+l[:(arr_size-idx) % arr_size]
      idx += n+skip
      skip += 1
  return l

def main() -> None:
  data = next(get_data(today)).strip()
  new_list = hash_data([int(x) for x in data.split(',')])
  final_list = hash_data(to_ascii(data), 64)
  print(f'{today} star 1 = {new_list[0]*new_list[1]}')
  print(f'{today} star 2 = {hex_representation(final_list)}')

if __name__ == '__main__':
  timed(main)
