import os
import time
import difflib
from support.support_variables import CONTRIB_THEMES, CURRENT_AUTO_VER, EXCLUDED_THEMES, MIN_SIM_THRESHOLD, WELCOME_TEXT, AUTO_WELCOME_TEXT


# Created by @ShaneSmiskol
def get_user_theme():  # Auto discover themes and let user choose!
  available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
  available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
  available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
  lower_available_themes = [t.lower() for t in available_themes]
  print('\nAvailable themes:')
  for idx, theme in enumerate(available_themes):
    print('{}. {}'.format(idx + 1, theme))
  print('\nType `exit` to exit.')
  while 1:
    theme = input('\nChoose a theme to install (by name or index): ').strip().lower()
    print()
    if theme in ['exit', '']:
      return None

    if theme.isdigit():
      theme = int(theme)
      if theme > len(available_themes):
        print('Index out of range, try again!')
        continue
      return available_themes[int(theme) - 1]
    else:
      if theme in lower_available_themes:
        return available_themes[lower_available_themes.index(theme)]
      sims = [str_sim(theme, t.lower()) for t in available_themes]
      most_sim_idx = max(range(len(sims)), key=sims.__getitem__)
      theme = available_themes[most_sim_idx]
      if sims[most_sim_idx] >= MIN_SIM_THRESHOLD:
        print('Selected theme: {}'.format(theme))
        print('Is this correct?')
        print('[Y/n]: ', end='')
        if input().lower().strip() in ['yes', 'y']:
          return theme
      else:
        print('Unknown theme, try again!')


def print_welcome_text():  # this center formats text automatically

  max_line_length = max([len(line) for line in WELCOME_TEXT]) + 4
  print(''.join(['+' for _ in range(max_line_length)]))
  for line in WELCOME_TEXT:
    padding = max_line_length - len(line) - 2
    padding_left = padding // 2
    print('+{}+'.format(' ' * padding_left + line + ' ' * (padding - padding_left)))
  print(''.join(['+' for _ in range(max_line_length)]))
  time.sleep(2)  # Pause for suspense, and so can be read


def print_auto_welcome_text():  # this center formats text automatically

  max_line_length = max([len(line) for line in AUTO_WELCOME_TEXT]) + 4
  print(''.join(['+' for _ in range(max_line_length)]))
  for line in AUTO_WELCOME_TEXT:
    padding = max_line_length - len(line) - 2
    padding_left = padding // 2
    print('+{}+'.format(' ' * padding_left + line + ' ' * (padding - padding_left)))
  print(''.join(['+' for _ in range(max_line_length)]))
  time.sleep(2)  # Pause for suspense, and so can be read


def go_back(picker):  # part of the picker code
  return None, -1


def str_sim(a, b):  # part of Shane's theme picker code
  return difflib.SequenceMatcher(a=a, b=b).ratio()


def is_affirmative():
  u = input('[Yes/No]: ').lower().strip()
  return u in ['yes', 'ye', 'y', '1']
