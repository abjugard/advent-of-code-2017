from santas_little_helpers import day, get_data, timed
from collections import defaultdict
from typing import Callable

regs = []

today = day(2017, 18)

def snd(p: int, val: int, threads: int) -> int:
  if val in regs[p]:
    val = regs[p][val]
  if threads == 1:
    regs[p]['snd'] = val
  else:
    regs[(p+1)%threads]['rcv'] += [val]
    regs[p]['snd'] += 1
  return 1

def put(p: int, args: tuple, _) -> int:
  reg, val = args
  if val in regs[p]:
    val = regs[p][val]
  regs[p][reg] = val
  return 1

def add(p: int, args: tuple, _) -> int:
  reg, val = args
  if val in regs[p]:
    val = regs[p][val]
  regs[p][reg] += val
  return 1

def mul(p: int, args: tuple, _) -> int:
  reg, val = args
  if val in regs[p]:
    val = regs[p][val]
  regs[p][reg] *= val
  return 1

def mod(p: int, args: tuple, _) -> int:
  reg, val = args
  if val in regs[p]:
    val = regs[p][val]
  regs[p][reg] %= val
  return 1

def rcv(p: int, reg: str, threads: int) -> int:
  if threads == 1:
    if regs[p][reg] != 0:
      regs[p][reg] = regs[p]['snd']
    return 1
  elif len(regs[p]['rcv']) > 0:
    regs[p][reg], *regs[p]['rcv'] = regs[p]['rcv']
    return 1
  return 0

def jgz(p: int, args: tuple, _) -> int:
  cond, jmp = args
  if cond in regs[p]:
    cond = regs[p][cond]
  if cond > 0:
    if jmp in regs[p]:
      jmp = regs[p][jmp]
    return jmp
  return 1

def waiting(p: int, pc: int, stack: [(Callable, tuple)]) -> bool:
  if pc < 0 or pc >= len(stack):
    return True
  return stack[pc][0] == rcv and len(regs[p]['rcv']) < 1

def reset(threads: int) -> [int]:
  global regs
  regs = []
  pc = []
  for i in range(threads):
    regs += [defaultdict(int)]
    regs[i]['p'] = i
    regs[i]['rcv'] = []
    pc += [0]
  return pc

def run(stack: [(Callable, tuple)], threads: int = 1) -> int:
  pc = reset(threads)
  while True:
    for p in range(threads):
      if not waiting(p, pc[p], stack):
        instr, args = stack[pc[p]]
        pc[p] += instr(p, args, threads)
    if all([waiting(p, pc[p], stack) for p in range(threads)]):
      break
  return regs[1%threads]['snd']

def main() -> None:
  instrs = {
    'snd': snd, 'set': put, 'add': add,
    'mul': mul, 'mod': mod, 'rcv': rcv,
    'jgz': jgz
  }
  stack = list(get_data(today, [('asmbunny', instrs)]))
  print(f'{today} star 1 = {run(stack)}')
  print(f'{today} star 2 = {run(stack, threads=2)}')

if __name__ == '__main__':
  timed(main)
