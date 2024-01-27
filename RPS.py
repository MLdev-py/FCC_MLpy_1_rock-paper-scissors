# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random
from collections import Counter

target = {"R": "R", "P": "S", "S": "P"}
result = {}


def player(prev_play, opponent_history=[]):
  global result
  n = 3

  if prev_play in ["R", "P", "S"]:
    opponent_history.append(prev_play)

  guess = "R"

  if len(opponent_history) > n:
    inp = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n + 1):]) in result.keys():
      result["".join(opponent_history[-(n + 1):])] += 1
    else:
      result["".join(opponent_history[-(n + 1):])] = 1

    possible = [inp + "R", inp + "P", inp + "S"]

    for i in possible:
      if not i in result.keys():
        result[i] = 0

    predict = max(possible, key=lambda key: result[key])

    guess = target[predict[-1]]
  return guess
