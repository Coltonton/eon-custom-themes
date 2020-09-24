import os
import time
import difflib
from support.support_variables import BACKUPS_DIR, CONTRIB_THEMES, EXCLUDED_THEMES, MIN_SIM_THRESHOLD, WELCOME_TEXT, AUTO_WELCOME_TEXT

# Created by @ShaneSmiskol some modifications by coltonton
def get_user_theme():           # Auto discover themes and let user choose!
  available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
  available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
  available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
  lower_available_themes = [t.lower() for t in available_themes]
  print('\nAvailable themes:')
  for idx, theme in enumerate(available_themes):
    print('{}. {}'.format(idx + 1, theme))
  print('\nType `restore` or enter 69 to restore a backup')
  print('Type `exit` or enter 70 to exit.')
  while 1:
    theme = input('\nChoose a theme to install (by name or index): ').strip().lower()
    print()
    if theme in ['restore', 'Restore', 'r', 'R', 69]:
      return 'restore'
    if theme in ['exit', 'Exit', 'E', 'e', 70]:
      return None

    if theme.isdigit():
      theme = int(theme)
      if theme == 69:
        print('\nnice\n')
        return 'restore'
      if theme == 70:
        return None
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
        if input().lower().strip() in ['yes', 'y', 1, 'ye', 'Yes', 'Y', 'Ye']:
          return theme
      else:
        print('Unknown theme, try again!')

# Created by @ShaneSmiskol
def print_welcome_text():       # This center formats text automatically

  max_line_length = max([len(line) for line in WELCOME_TEXT]) + 4
  print(''.join(['+' for _ in range(max_line_length)]))
  for line in WELCOME_TEXT:
    padding = max_line_length - len(line) - 2
    padding_left = padding // 2
    print('+{}+'.format(' ' * padding_left + line + ' ' * (padding - padding_left)))
  print(''.join(['+' for _ in range(max_line_length)]))
  time.sleep(2)  # Pause for suspense, and so can be read

# Created by @ShaneSmiskol
def print_auto_welcome_text():  # This center formats text automatically

  max_line_length = max([len(line) for line in AUTO_WELCOME_TEXT]) + 4
  print(''.join(['+' for _ in range(max_line_length)]))
  for line in AUTO_WELCOME_TEXT:
    padding = max_line_length - len(line) - 2
    padding_left = padding // 2
    print('+{}+'.format(' ' * padding_left + line + ' ' * (padding - padding_left)))
  print(''.join(['+' for _ in range(max_line_length)]))
  time.sleep(2)  # Pause for suspense, and so can be read

# Created by @ShaneSmiskol
def str_sim(a, b):              # Part of Shane's theme picker code
  return difflib.SequenceMatcher(a=a, b=b).ratio()

# Created by @ShaneSmiskol
def is_affirmative():           # Ask user for confirmation
  u = input('[1.Yes / 2.No]: ').lower().strip()
  return u in ['yes', 'ye', 'y', '1']

# Created by @ShaneSmiskol modified version of get_user_theme() to get all backups by Coltonton
def get_user_backups(exclude):
  excludes = exclude
  available_backups = [t for t in os.listdir(BACKUPS_DIR)]
  available_backups = [t for t in available_backups if os.path.isdir(os.path.join(BACKUPS_DIR, t))]
  available_backups = [t for t in available_backups if t not in excludes]
  lower_available_backups = [t.lower() for t in available_backups]
  print('\nAvailable backups:')
  for idx, backup in enumerate(available_backups):
    print('{}. {}'.format(idx + 1, backup))
  print('Type `exit` or enter 70 to exit.')
  while 1:
    backup = input('\nChoose a backup to install (by index value): ').strip().lower()
    print()
    if backup in ['exit', 'Exit', 'E', 'e', 70]:
      return None

    if backup.isdigit():
      backup = int(backup)
      if backup == 70:
        return None
      if backup > len(available_backups):
        print('Index out of range, try again!')
        continue
      return available_backups[int(backup) - 1]
    else:
      print('Please enter only Index number value!!')
      continue