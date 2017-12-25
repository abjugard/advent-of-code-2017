from santas_little_helpers import day, get_data, timed
from collections import defaultdict

today = day(2017, 25)

def turing(machine: {}) -> int:
  state = machine[machine['start']]
  pos = 0
  tape = defaultdict(int)
  for _ in range(machine['check']):
    tape[pos], m, s = state[tape[pos]]
    pos += m
    state = machine[s]
  return sum(tape.values())

def main() -> None:
  machine = {}
  for l in get_data(today, [('func', lambda l: l.strip())]):
    if   l[:3] == 'Beg': machine['start'] = l[-2]
    elif l[:3] == 'Per': machine['check'] = int(l.split(' ')[-2])
    elif l[:3] == 'In ': c_s, machine[c_s] = l[-2], {}
    elif l[:3] == 'If ': c_v = int(l[-2])
    elif l[:3] == '- W': machine[c_s][c_v] = (int(l[-2]),)
    elif l[:3] == '- M': machine[c_s][c_v] += (1 if l[-6] == 'r' else -1,)
    elif l[:3] == '- C': machine[c_s][c_v] += (l[-2],)
  print(f'{today} star 1 = {turing(machine)}')
  print(f'{today} star 2 = Merry Christmas!')

if __name__ == '__main__':
  timed(main)
