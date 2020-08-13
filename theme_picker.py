import os
import ast
import difflib

os.chdir(os.getcwd())

CONTRIB_THEMES = "Contributed Themes"
EXCLUDED_THEMES = []  # todo: change me


def str_sim(a, b):
  return difflib.SequenceMatcher(a=a, b=b).ratio()


def main():
  available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
  available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
  available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
  print('\nAvailable themes:')
  for idx, theme in enumerate(available_themes):
    print('{}. {}'.format(idx + 1, theme))
  print('\nChoose a theme to install (by name or index)')
  while 1:
    selected_theme = input('Selected theme: ').strip().lower()
    if selected_theme.isdigit():
      return available_themes[int(selected_theme) - 1]
    else:
      sims = [str_sim(selected_theme, t.lower()) for t in available_themes]
      print(sims)


if __name__ == "__main__":
  main()
