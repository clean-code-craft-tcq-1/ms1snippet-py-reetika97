
maxDelta={'soc':0.05, 'current':0.1} #maxDeltas corresponding to parameters -> new parameters can be added
lowest_maxDelta=min(list(maxDelta.values()))    #to find the least maxDelta -> future readiness incase more parameters are added
maxDelta['lowest_maxDelta']=lowest_maxDelta #appending lowest to the dictionary for validate_reading() function call
        
#Error to see if values are not passed
class ListEmptyError(Exception):
    pass

def differentialReading_below_maxDelta(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

#Function that raises ListEmptyError if empty values is are passed
def is_values_notNone(values):
  try:
    if(len(values)<=0):
      raise ListEmptyError
    else:
      return True
  except ListEmptyError:
    print("No values read!")
    return None

#Validate readings passed with default param of lowest maxDelta if parameter name not passed.
#if the differential readings are valid for least maxDelta it can be valid for all parameters. 
#The function expects parameter name to be passed, this logic is not replacing the need for parameter name, but avoiding unwanted errors.
#Note: the readings may show invalid for valid readings of higher maxDelta.
def validate_reading(values, param='lowest_maxDelta'):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not differentialReading_below_maxDelta(values[i], values[i + 1], maxDelta[param])):
      ValidFlag=False
      return ValidFlag
  ValidFlag=is_values_notNone(values)
  return ValidFlag

  
  
