from santas_little_helpers import day, get_data, timed
from typing import Callable

regs = {}

today = day(2017, 23)

def put(args: tuple) -> int:
  reg, val = args
  if val in regs:
    val = regs[val]
  regs[reg] = val
  return 1

def sub(args: tuple) -> int:
  reg, val = args
  if val in regs:
    val = regs[val]
  regs[reg] -= val
  return 1

def mul(args: tuple) -> int:
  reg, val = args
  if val in regs:
    val = regs[val]
  regs[reg] *= val
  return 1

def jnz(args: tuple) -> int:
  cond, jmp = args
  if cond in regs:
    cond = regs[cond]
  if cond != 0:
    if jmp in regs:
      jmp = regs[jmp]
    return jmp
  return 1

def run(stack: [(Callable, tuple)], star2: bool = False) -> int:
  for r in 'abcdefgh':
    regs[r] = 0
  if star2:
    regs['a'] = 1
  pc = 0
  muls = 0
  while pc >= 0 and pc < len(stack):
    if pc == 10 and star2:
      if any([regs['b'] % d == 0 for d in range(2, regs['b'])]):
        regs['h'] += 1
      pc = 26
    instr, args = stack[pc]
    if instr == mul:
      muls += 1
    pc += instr(args)
  return regs['h'] if star2 else muls

def main() -> None:
  instrs = {
    'sub': sub, 'set': put,
    'mul': mul, 'jnz': jnz
  }
  stack = list(get_data(today, [('asmbunny', instrs)]))
  print(f'{today} star 1 = {run(stack)}')
  print(f'{today} star 2 = {run(stack, star2=True)}')

if __name__ == '__main__':
  timed(main)
