import random

def generate_error():
  random_number = random.randint(1, 3)

  if random_number == 1:
    result = 1 / 0
  elif random_number == 2:
    print(invalid_variable)
  elif random_number == 3:
    num = int('not_a_number')