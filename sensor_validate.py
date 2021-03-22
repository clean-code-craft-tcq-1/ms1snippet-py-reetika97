
maxDelta={'soc':0.05, 'current':0.1}

def  _give_me_a_good_name(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_reading(values, param):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not _give_me_a_good_name(values[i], values[i + 1], maxDelta[param])):
      return False
  return True

