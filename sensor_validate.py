
maxDelta={'soc':0.05, 'current':0.1}

def readings_below_maxDelta(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_reading(values, param):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not readings_below_maxDelta(values[i], values[i + 1], maxDelta[param])):
      return False
  return True
  
