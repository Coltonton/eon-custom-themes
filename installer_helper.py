import os

os.chdir(os.getcwd())
CONTRIB_THEMES = "Contributed Themes"


def main():
  available_themes = os.listdir(CONTRIB_THEMES)
  print('Available themes:')
  for theme in [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]:
    print(theme)


if __name__ == "__main__":
  main()
