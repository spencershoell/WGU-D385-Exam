# unit test case
import unittest

def multiply_numbers(x, y):
    #add your code here
    # use the assertIsNone() function from unittest module to check if the function returns None when one of the arguments is None
    
    if y is None:
        print(f'y is a null value')
    else:
        print(f'{y} is not None')
    if x is None:
        print(f'x is a null value')
    else: 
        print(f'{x} is not None')
   
    return x * y
   # add your code here
   
   
class TestForNone(unittest.TestCase):
        
    def test_when_a_is_null(self):
        try:
            self.assertIsNone(multiply_numbers(5, None))
        except AssertionError as msg:
            print(msg)

if __name__ == '__main__':  
    unittest.main()