import difflib
import time
import os


def str_sim(a, b):  # part of Shane's theme picker code
  return difflib.SequenceMatcher(a=a, b=b).ratio()


def print_welcome_text():
  welcome_text = ['Created By: Colton (Brandon) S. EndLine \\n',
                  'Special Thanks to @ShaneSmiskol for all the help!!!',
                  'Free to use! Free to Edit! Free to integrate!',
                  'Design and contribute your themes today!',
                  '(See the developer folder in this repo)',
                  'It\'s your EON, do what you want!']
  max_line_length = max([len(line) for line in welcome_text]) + 4
  print(''.join(['+' for _ in range(max_line_length)]))
  for line in welcome_text:
    padding = max_line_length - len(line) - 2
    padding_left = padding // 2
    print('+{}+'.format(' ' * padding_left + line + ' ' * (padding - padding_left)))
  print(''.join(['+' for _ in range(max_line_length)]))
  time.sleep(1)  # Pause for suspense, and so can be read  # todo: change back to 3


def check_auto_installability():
  doInstall = False
  if os.path.exists('auto_theme_installed.txt'):  # if auto installed before
    isOveride = open('override_auto_install.txt', 'r')  # check if override set
    if isOveride.mode == 'r':
      contents = isOveride.read()
      if contents == 1:  # if overide == 1
        doInstall = True  # overide and Do Auto install theme
      else:
        doInstall = False  # do not override reinstall, do not pass go do not collect $200
  else:  # If auto_theme_installed.txt does not exist
    doInstall = True  # Do Auto install theme
    f = open('auto_theme_installed.txt', 'w+')  # Create auto_theme_installed.txt to prevent more installs
    f.write('1')
    f.close()

    return doInstall


def go_back(picker):  # part of the picker code
  return None, -1
