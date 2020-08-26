import difflib
import time


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
