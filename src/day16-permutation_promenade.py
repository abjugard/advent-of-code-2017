from santas_little_helpers import day, get_data, timed

today = day(2017, 16)

def spin(progs: str, n: int) -> str:
  return progs[-n:]+progs[:-n]

def exchange(progs: str, a: int, b: int) -> str:
  progs[a], progs[b] = progs[b], progs[a]
  return progs

def partner(progs: str, a: str, b: str) -> str:
  return exchange(progs, progs.index(a), progs.index(b))

def dance(routine: list, progs: str, repetitions: int = 1) -> str:
  seen = []
  for i in range(repetitions):
    s = ''.join(progs)
    if s in seen:
      return seen[repetitions % i]
    seen += [s]
    for move in routine:
      if move[0] == 's':
        progs = spin(progs, int(move[1:]))
      elif move[0] == 'x':
        args = move[1:].split('/')
        progs = exchange(progs, int(args[0]), int(args[1]))
      elif move[0] == 'p':
        args = move[1:].split('/')
        progs = partner(progs, args[0], args[1])
  return ''.join(progs)

def main() -> None:
  data = get_data(today, [('split', ',')])
  routine = list(next(data))
  progs = [chr(x) for x in range(ord('a'), ord('p')+1)]
  print(f'{today} star 1 = {dance(routine, progs)}')
  print(f'{today} star 2 = {dance(routine, progs, 1000000000)}')

if __name__ == '__main__':
  timed(main)
