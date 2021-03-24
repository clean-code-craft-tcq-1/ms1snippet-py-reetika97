
maxDelta={'soc':0.05, 'current':0.1}

#Error to see if values are not passed
class ListEmptyError(Exception):
    pass

def diffrentialReading_below_maxDelta(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def is_values_None(values):
  try:
    if(len(values)<=0):
      raise ListEmptyError
    else:
      return False
  except ListEmptyError:
    print("No values read!")
    return True


def validate_reading(values, param):
  if(not is_values_None(values)):
    return None
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not differentialReading_below_maxDelta(values[i], values[i + 1], maxDelta[param])):
      return False
  return True
  
