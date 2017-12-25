from santas_little_helpers import day, get_data, timed

today = day(2017, 5)

def maze(data: [int], decrement: bool = False) -> int:
  index = 0
  steps = 0
  instructions = len(data)
  while index < instructions:
    offset = data[index]
    if decrement and offset >= 3:
      data[index] -= 1
    else:
      data[index] += 1
    index += offset
    steps += 1
  return steps

def main() -> None:
  data = list(get_data(today, [('func', int)]))

  print(f'{today} star 1 = {maze(data.copy())}')
  print(f'{today} star 2 = {maze(data, decrement=True)}')

if __name__ == '__main__':
  timed(main)
