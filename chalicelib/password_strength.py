import re

special_symbols = re.escape('½/!"#¤%&/()=?`@£$‚{[]}¸^*:;>\<|’̣¨~+-')
patterns = [
  '[a-z]+',
  '\d+',
  '[A-Z]+',
  f'[{special_symbols}]+',
  '.{8,}'
]

def compute_strength(password):
    strength = 0
    for pattern in patterns:
        if len(re.findall(pattern, password)) > 0:
            strength += 1
    return strength * 2