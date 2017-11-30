import re, json
from pathlib import Path
from requests import request
from datetime import date, datetime

base_ops = [('replace', (r'\n', ''))]

aoc_root = Path('../')
aoc_data = aoc_root / 'data'
aoc_src = aoc_root / 'src'

with open(aoc_root / 'config.json', 'r') as f:
  config = json.load(f)

def format_line(line, ops) -> str:
  for op, args in ops:
    if op == 'replace':
      line = re.sub(args[0], args[1], line)
    if op == 'split':
      line = line.split(args)
    if op == 'func':
      line = args(line)
  return(line)

def day(year, theday) -> datetime:
  return datetime(year, 12, theday)

def get_data(today=date.today(), ops=base_ops) -> str:
  if not aoc_data.exists():
    aoc_data.mkdir()

  def save_daily_input(today):
    url = f'http://adventofcode.com/{today.year}/day/{today.day}/input'
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
      line = format_line(line, ops)
      data.append(line)
  return(data)
