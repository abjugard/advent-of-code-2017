from santas_little_helpers import day, get_data, timed
from collections import defaultdict
import operator

today = day(2017, 8)

regs = defaultdict(int)

ops = {
  '==': operator.eq,
  '!=': operator.ne,
  '<=': operator.le,
  '>=': operator.ge,
  '<':  operator.lt,
  '>':  operator.gt
}

class Instruction():
  def __init__(self, arr):
    self.reg = arr[0]
    self.run = self.__inc if arr[1] == 'inc' else self.__dec
    self.__amt = int(arr[2])
    self.__cond_reg = arr[4]
    self.__cond_op = ops[arr[5]]
    self.__cond_amt = int(arr[6])

  def valid(self):
    return self.__cond_op(regs[self.__cond_reg], self.__cond_amt)

  def __inc(self):
    regs[self.reg] += self.__amt

  def __dec(self):
    regs[self.reg] -= self.__amt

def solve(data):
  highest = 0
  for inst in data:
    if inst.valid():
      inst.run()
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
