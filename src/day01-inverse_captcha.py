from santas_little_helpers import day, get_data, timed

today = day(2017, 1)

def inverse_captcha(captcha: list, offset: int = 1) -> [int]:
  for i, val in enumerate(captcha):
    if val == captcha[(i+offset) % len(captcha)]:
      yield int(val)

def main() -> None:
  data = list(get_data(today))[0]

  print(f'{today} star 1 = {sum(inverse_captcha(data))}')
  print(f'{today} star 2 = {sum(inverse_captcha(data, len(data)//2))}')

if __name__ == '__main__':
  timed(main)
