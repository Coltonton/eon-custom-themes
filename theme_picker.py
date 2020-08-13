import os
import difflib

os.chdir(os.getcwd())
CONTRIB_THEMES = "Contributed Themes"


def str_sim(a, b):
  return difflib.SequenceMatcher(a=a, b=b).ratio()


def main():
  available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
  available_themes = [t.lower() for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
  print('\nAvailable themes:')
  for idx, theme in enumerate(available_themes):
    print('{}. {}'.format(idx + 1, theme))
  print('Choose a theme to install (by name or index)')
  while 1:
    selected_theme = input('Selected theme: ').strip().lower()




if __name__ == "__main__":
  main()
