from santas_little_helpers import *
import re

today = day(2017, 7)

class Node():
  rx = re.compile(r'([\w]*) \(([\d]*)([\w, ->]+)')
  def __init__(self, string):
    m = self.rx.match(string)
    self.name = m.group(1)
    self.weight = int(m.group(2))
    self.total_weight = self.weight
    self.nodes = []
    subnodes = m.group(3)[5:].split(', ')
    if len(subnodes[0]) == 0:
      subnodes = [] 
    self.carrying = subnodes

  def carries(self, other):
    self.nodes += [other]
    self.total_weight += other.total_weight

def get_node(string, nodes):
  for node in nodes:
    if node.name == string:
      return node
  return None

def build_tree(root, nodes):
  for node_name in root.carrying:
    node = build_tree(get_node(node_name, nodes), nodes)
    root.carries(node)
  return root

def has_outlier(root):
  if len(root.nodes) == 0:
    return False
  return len(set([node.total_weight for node in root.nodes])) > 1

def balance(root):
  weights = [node.total_weight for node in root.nodes]

  for node in root.nodes:
    if weights.count(node.total_weight) == 1:
      if has_outlier(node):
        return balance(node)
      weights.remove(node.total_weight)
      diff = node.total_weight-weights.pop()
      return node.weight-diff

def main():
  data = list(get_data(today, [('func', Node)]))

  carried = []
  for x in data:
    if len(x.carrying) != 0:
      carried += x.carrying

  root = None
  for x in data:
    if x.name not in carried:
      root = build_tree(x, data)

  print(f'{today} star 1 = {root.name}')
  print(f'{today} star 2 = {balance(root)}')

if __name__ == '__main__':
  timed(main)
