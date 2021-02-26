#Gabriel Crew
import unittest 


def calculate_value(x):
  if (x > 0):
    if(x == 1):
      return 0
    elif(x == 2):
      return 1
    else:
      temp1 = 1
      temp2 = 0
      for i in range(x):
        if (i == 0): 
          temp1 = temp1
        else:
          temp3 = temp1
          temp1 = temp1 + temp2
          temp2 = temp3
      print (temp1)
      return temp1
  else:
      return "Undefined"

def calculate_value2(x):
  if (x > 0):
    temp1 = 1
    temp2 = 0
    for i in range(x):
          temp2 = i +1
          temp1 = temp1 * temp2   
    print (temp1)
    return temp1
  else:
      return "Undefined"

x_in = input("Which Fibonacci index/ factorial would you like to find?:  ")
x_in = int(x_in)
calculate_value(x_in)
calculate_value2(x_in)

class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(calculate_value(0),"Undefined")
  def test2(self): self.assertEqual(calculate_value(2),1)
  def test3(self): self.assertEqual(calculate_value(5),5)
  def test4(self): self.assertEqual(calculate_value(-2),"Undefined")



if __name__ == '__main__':
  unittest.main()
