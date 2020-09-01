import os
import time
import difflib
from support.support_variables import CONTRIB_THEMES, EXCLUDED_THEMES, MIN_SIM_THRESHOLD, WELCOME_TEXT


def check_auto_installability():
  auto_installed_path = 'auto_theme_installed.txt'
  if os.path.exists(auto_installed_path):  # if auto installed before
    with open(auto_installed_path, 'r') as f:  # check if override set
      override = f.read().strip().strip('\n')

    if override == '1':  # if overide
      return True  # overide and Do Auto install theme
    else:
      return False  # do not override reinstall, do not pass go do not collect $200

  else:  # If auto_theme_installed.txt does not exist
    with open(auto_installed_path, 'w') as f:  # Create auto_theme_installed.txt to prevent more installs
      f.write('0')  # this was previously 1, causing it to keep installing when it shouldn't have
    return True


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


def go_back(picker):  # part of the picker code
  return None, -1


def str_sim(a, b):  # part of Shane's theme picker code
  return difflib.SequenceMatcher(a=a, b=b).ratio()


def is_affirmative():
  u = input('[Yes/No]: ').lower().strip()
  return u in ['yes', 'ye', 'y', '1']
