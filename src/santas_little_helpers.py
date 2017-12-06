import json, re, time
from bs4 import BeautifulSoup
from datetime import date, datetime
from pathlib import Path
from requests import request
from typing import Callable, Iterator

base_ops = [('replace', (r'\n', ''))]

aoc_root = Path('../')
aoc_data = aoc_root / 'data'

with (aoc_root / 'config.json').open('r') as f:
  config = json.load(f)

def day(year: int, theday: int) -> date:
  return date(year, 12, theday)

def format_line(line: str, ops: list):
  for op, args in ops:
    if op == 'replace':
      line = re.sub(args[0], args[1], line)
    if op == 'split':
      line = line.split(args)
    if op == 'func':
      line = args(line)
    if op == 'func_each':
      line = [args(x) for x in line]
  return line

def get_data(today: date = date.today(), ops: list = base_ops) -> Iterator:
  if not aoc_data.exists():
    aoc_data.mkdir()

  def save_daily_input(today: date) -> None:
    url = f'https://adventofcode.com/{today.year}/day/{today.day}/input'
    res = request('GET', url, cookies=config)
    res.raise_for_status()
    with file_path.open('wb') as f:
      for chunk in res.iter_content(chunk_size=128):
        f.write(chunk)
        print(chunk.decode('utf-8'), end='')
      print()

  file_path = aoc_data / f'day{today.day:02}.txt'
  if not file_path.exists():
    print(f'Data for day {today.day} not available, downloading!')
    save_daily_input(today)
  data = []
  with file_path.open() as f:
    for line in f.readlines():
      yield format_line(line, ops)

def submit_answer(today: date, answer: str, level: int = 1) -> None:
  url = f'https://adventofcode.com/{today.year}/day/{today.day}/answer'
  payload = {
    'level': level,
    'answer': answer
  }
  res = request('POST', url, cookies=config, data=payload)
  soup = BeautifulSoup(res.content, 'html.parser')
  for content in soup.find_all('article'):
    print(content.text)

def time_fmt(delta: float) -> (float, str):
  if delta < 1e-6:
    return 1e9, 'ns'
  elif delta < 1e-3:
    return 1e6, 'µs'
  elif delta < 1:
    return 1e3, 'ms'
  return 1, 'seconds'

def timed(func: Callable) -> None:
  start = time.time()
  func()
  delta = time.time()-start
  multiplier, unit = time_fmt(delta)
  print(f'--- {delta*multiplier:.2f} {unit} ---')
