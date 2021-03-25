import unittest
import sensor_validate

class SensorValidatorTest(unittest.TestCase):
 # Tests for validate_readings() function
  def test_reports_error_when_soc_jumps(self):
    self.assertFalse(
      sensor_validate.validate_reading([0.0, 0.01, 0.5, 0.51],'soc')
    )
  
  def test_reports_error_when_current_jumps(self):
    self.assertFalse(
      sensor_validate.validate_reading([0.03, 0.03, 0.03, 0.33],'current')
    )
    
  def test_ignores_validation_when_values_none(self):
    self.assertTrue( sensor_validate.validate_reading([],'current') == None)
    
  def test_function_when_no_parameter_name_passed(self):
    self.assertTrue( sensor_validate.validate_reading([0.0,0.01,0.02,0.04]))
    
 #tests for is_values_notNone() function
  def test_function_when_no_parameter_name_passed(self):
    self.assertTrue( sensor_validate.is_values_notNone([0.0,0.01,0.02,0.04]))
    
  def test_function_when_no_parameter_name_passed(self):
    self.assertTrue( sensor_validate.is_values_notNone([])==None)
    
 #tests for differentialReading_below_maxDelta() function
  def test_function_when_no_parameter_name_passed(self):
    self.assertTrue( sensor_validate.differentialReading_notAbove_maxDelta(0.1,0.15,0.1))
    
  def test_function_when_no_parameter_name_passed(self):
    self.assertFalse( sensor_validate.differentialReading_notAbove_maxDelta(0.1,0.21,0.1))
    
  def test_function_when_no_parameter_name_passed(self):
    self.assertTrue( sensor_validate.differentialReading_notAbove_maxDelta(0.1,0.2,0.1))
  
if __name__ == "__main__":
  unittest.main()
