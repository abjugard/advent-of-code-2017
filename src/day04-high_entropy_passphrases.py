from santas_little_helpers import base_ops, day, get_data, timed

today = day(2017, 4)

def valid(passphrase: [str]) -> (bool, bool):
  word_count = len(passphrase)
  if word_count != len(set(passphrase)):
    return False, False
  ordered = set(''.join(sorted(word)) for word in passphrase)
  return True, word_count == len(ordered)

def main() -> None:
  data = get_data(today, base_ops + [('split', ' '), ('func', sorted)])

  star1 = 0
  star2 = 0
  for passphrase in data:
    s1, s2 = valid(passphrase)
    if s1: star1 += 1
    if s2: star2 += 1

  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
