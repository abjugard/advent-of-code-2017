from santas_little_helpers import day, get_data, timed
from operator import itemgetter

today = day(2017, 24)

def fits(socket: int, left: int, right: int) -> bool:
  return any([socket == left, 
              socket == right])

def bridges(cmps: {}, loops: {}, l:int=0, s:int=0, port:int=0) -> (int, int):
  l += 1
  compatible = [nxt for nxt in cmps if fits(port, *nxt)]
  if port in loops:
    l += 1
    s += port*2
    if len(compatible) < 1:
      yield l, s
  for c in compatible:
    ns = s+sum(c)
    yield l, ns
    other = c[(c.index(port)+1)%2]
    yield from bridges(cmps-{c}, loops-{port}, l, ns, other)

def parse(line: str) -> (int, int):
  return tuple(sorted(map(int, line.split('/'))))

def main() -> None:
  all_components = set(get_data(today, [('func', parse)]))
  loops = set((a,b) for a,b in all_components if a==b)
  table = set(bridges(all_components-loops, set(a for a, _ in loops)))

  print(f'{today} star 1 = {max(table, key=itemgetter(1))[1]}')
  print(f'{today} star 2 = {max(table)[1]}')

if __name__ == '__main__':
  timed(main)
