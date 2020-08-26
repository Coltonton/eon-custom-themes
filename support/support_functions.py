import difflib


def str_sim(a, b):   #part of Shane's theme picker code
  return difflib.SequenceMatcher(a=a, b=b).ratio()