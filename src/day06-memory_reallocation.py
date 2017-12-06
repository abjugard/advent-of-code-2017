from santas_little_helpers import *

today = day(2017, 6)

def redistribute(data: [int], mem_banks: int = 16) -> [int]:
  i = data.index(max(data))
  val = data[i]
  data[i] = 0
  for idx in range(i, i+val):
    data[(idx+1) % mem_banks] += 1
  return data

def reallocate(data: [int]) -> (int, [int]):
  results = set([str(data)])
  prev = None
  while len(results) != prev:
    data = redistribute(data)
    prev = len(results)
    results.add(str(data))
  return len(results), data

def main() -> None:
  data = get_data(today, [('split', '\t'), ('func_each', int)])

  data = list(data)[0]
  star1, data = reallocate(data)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {reallocate(data)[0]}')

if __name__ == '__main__':
  timed(main)
