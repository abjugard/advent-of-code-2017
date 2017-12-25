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
