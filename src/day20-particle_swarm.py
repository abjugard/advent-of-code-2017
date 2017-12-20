from santas_little_helpers import day, get_data, timed
from operator import add
from collections import defaultdict

today = day(2017, 20)

def distance(p: dict) -> int:
  return sum([abs(x) for x in p['p']])

def simulate(particles: [dict], bound: int) -> (int, int):
  uncollided = [_ for _ in range(len(particles))]
  for _ in range(bound):
    closest, minimum = None, None
    for idx, p in enumerate(particles):
      p['v'] = tuple(map(add, p['v'], p['a']))
      p['p'] = tuple(map(add, p['p'], p['v']))
      if minimum is None or distance(p) < minimum:
        closest, minimum = idx, distance(p)
    collissions = defaultdict(list)
    for idx, p in [(idx, p) for idx, p in enumerate(particles) 
                            if uncollided[idx]]:
      collissions[p['p']] += [idx]
    for idx in [idx for idxs in collissions.values() 
                    for idx in idxs 
                    if len(idxs) > 1]:
      uncollided[idx] = None
  return closest, len([_ for p in uncollided if p])

def fun(line: str) -> dict:
  l = [tuple(map(int, x[3:-1].split(','))) 
        for x in line.strip().split(', ')]
  return {'p': l[0], 'v': l[1], 'a': l[2]}

def main() -> None:
  particles = list(get_data(today, [('func', fun)]))
  bound = 345 # likely specific for my input
  star1, star2 = simulate(particles, bound) 
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
