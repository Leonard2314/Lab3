import Lab2.Lab2 as bmi
def test_bmi_normal_weight():
  assert bmi.calculate_bmi(1.7,65)==0
def test_bmi_over_weight():
  assert bmi.calculate_bmi(1.5,100)==1
def test_bmi_under_weight():
  assert bmi.calculate_bmi(1.8,55)==-1
        

