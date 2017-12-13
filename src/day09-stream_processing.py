from santas_little_helpers import day, get_data, timed

today = day(2017, 9)

def process(stream: str) -> (int, int):
  skip_next = False
  in_garbage = False
  count = 0
  depth = 0
  garbage_count = 0
  for x in stream:
    if skip_next:
      skip_next = False
    else:
      if x == '!':
        skip_next = True
      elif in_garbage:
        if x == '>':
          in_garbage = False
        else:
          garbage_count += 1
      elif x == '<':
        in_garbage = True
      elif x == '{':
        depth += 1
        count += depth
      elif x == '}':
        depth -= 1
  return count, garbage_count

def main() -> None:
  stream = next(get_data(today))
  star1, star2 = process(stream)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
