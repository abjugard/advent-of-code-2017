from santas_little_helpers import *

def solve_puzzle(arr, offset) -> int:
  for i in range(0, len(arr)):
    if arr[i] == arr[(i+offset) % len(arr)]:
      yield int(arr[i])

if __name__ == '__main__':
  data = get_data(day(2017, 1), base_ops + [])[0]

  print(f'The value for star 1 = {sum(solve_puzzle(data, 1))}')
  offset = int(len(data)/2)
  print(f'The value for star 2 = {sum(solve_puzzle(data, offset))}')
