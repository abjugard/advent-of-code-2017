from santas_little_helpers import *
from collections import defaultdict
import networkx

today = day(2017, 12)
rx = re.compile(r'([\d]*) <-> ([\w, ]*)')

def graph(data: [(int, [int])]) -> (int, int):
  graph = networkx.Graph()
  for x, l in data:
    graph.add_edges_from((x, n) for n in l)

  star1 = len(networkx.node_connected_component(graph, 0))
  star2 = networkx.number_connected_components(graph)
  return star1, star2

def fun(line: str) -> (int, [int]):
  m = rx.match(line)
  return int(m.group(1)), [int(x) for x in m.group(2).split(', ')]

def main() -> None:
  data = get_data(today, base_ops + [('func', fun)])
  star1, star2 = graph(data)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')

if __name__ == '__main__':
  timed(main)
