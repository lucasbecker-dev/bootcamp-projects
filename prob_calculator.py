from copy import deepcopy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    try:
      for key, val in kwargs.items():
        for i in range(val):
          self.contents.append(str(key))
    except Exception as e:
      print(e)
  
  def __str__(self):
    return str(self.contents)
  
  def draw(self, draws):
    try:
      if draws >= len(self.contents):
        res = deepcopy(self.contents)
        self.contents = []
        return res
      res = random.sample(self.contents, draws)
      for i in res:
        self.contents.remove(i)
      return res
    except Exception as e:
      print(e)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  matches_needed_for_success = len(expected_balls)
  try:
    for i in range(num_experiments):
      cur_hat = deepcopy(hat)
      drawn = cur_hat.draw(num_balls_drawn)
      matches = 0
      for ball in expected_balls:
        if drawn.count(ball) >= expected_balls[ball]:
          matches += 1
      if matches == matches_needed_for_success:
        successes += 1
    probability = successes / num_experiments
    return probability
  except Exception as e:
      print(e)
