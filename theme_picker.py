import os
import ast
import difflib

os.chdir(os.getcwd())

CONTRIB_THEMES = "Contributed Themes"
EXCLUDED_THEMES = []  # todo: change me
MIN_SIM_THRESHOLD = 0.8  # user's input needs to be this percent or higher similar to a theme to select it


def str_sim(a, b):
  return difflib.SequenceMatcher(a=a, b=b).ratio()


def main():
  available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
  available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
  available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
  lower_available_themes = [t.lower() for t in available_themes]
  print('\nAvailable themes:')
  for idx, theme in enumerate(available_themes):
    print('{}. {}'.format(idx + 1, theme))
  print('\nChoose a theme to install (by name or index)')
  while 1:
    selected_theme = input('>> ').strip().lower()

    if selected_theme.isdigit():
      selected_theme = int(selected_theme)
      if selected_theme > len(available_themes):
        print('Index out of range, try again!')
        continue
      return available_themes[int(selected_theme) - 1]
    else:
      if selected_theme in lower_available_themes:
        return available_themes[lower_available_themes.index(selected_theme)]
      sims = [str_sim(selected_theme, t.lower()) for t in available_themes]
      most_sim = max(range(len(sims)), key=sims.__getitem__)
      print(sims[most_sim])
      selected_theme = available_themes[most_sim]
      if selected_theme > MIN_SIM_THRESHOLD:
        print('Selected theme: {}'.format(selected_theme))
        print('Is this correct?')
        if input('[Y/n]: ').lower().strip() in ['yes', 'y']:
          return selected_theme


if __name__ == "__main__":
  print(main())
