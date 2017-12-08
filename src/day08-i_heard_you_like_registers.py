from santas_little_helpers import *
from collections import defaultdict

today = day(2017, 8)

regs = defaultdict(int)

class Instruction():
  def __init__(self, arr):
    self.reg = arr[0]
    self.op = arr[1]
    self.amt = int(arr[2])
    self.cond_reg = arr[4]
    self.cond_op = arr[5]
    self.cond_amt = int(arr[6])

def condition(inst):
  reg = inst.cond_reg
  op = inst.cond_op
  amt = inst.cond_amt
  if op == '==':
    return regs[reg] == amt
  if op == '!=':
    return regs[reg] != amt
  if op == '<=':
    return regs[reg] <= amt
  if op == '>=':
    return regs[reg] >= amt
  if op == '<':
    return regs[reg] < amt
  if op == '>':
    return regs[reg] > amt
  else:
    print(f'missing operator {op}')
    exit(0)

def solve(data):
  highest = 0
  for inst in data:
    if condition(inst):
      if inst.op == 'inc':
        regs[inst.reg] += inst.amt
      else:
        regs[inst.reg] -= inst.amt
      if regs[inst.reg] > highest:
        highest = regs[inst.reg]
  return highest

def main() -> None:
  data = get_data(today, [('split', ' '), ('func', Instruction)])
  star2 = solve(data)
  print(f'{today} star 1 = {regs[max(regs, key=regs.get)]}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
