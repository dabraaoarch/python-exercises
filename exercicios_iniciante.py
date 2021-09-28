import unittest

dict_operations = {
    '+' : lambda a, b: a+b,
    '-' : lambda a, b: a-b,
    '*' : lambda a, b: a*b,
    '/' : lambda a, b: a//b
}

def do_math(a: int, b: int, operation: str):
	 type_int = int(1)
    if type(a) != type(b) or type(a) != type(type_int):
        return False
    if type(operation) != type(''):
        return False
    
    return dict_operations.get(operation, lambda a, b: False)(a,b)

class TestCalculator(unittest.TestCase):
        def setUp(self):
            self.a = 5
            self.b = 10

        def test_invalid_operations(self):
            '''
                For wrong argumentos must return False
            '''
            result1 = do_math(a=5, b=6.5, operation='+')
            result2 = do_math(a='5', b=6, operation='+')
            result3 = do_math(a=self.a, b=self.b, operation='')
            self.assertFalse(result1)
            self.assertFalse(result2)
            self.assertFalse(result3)

        def test_valid_sum(self):
            '''
                If two int values were given and a valid operation (+)
                is informed it must return a value
            '''
            result = do_math(a=self.a, b=self.b,operation='+')
            self.assertEqual(result, 15)
            self.assertIsInstance(result, int)

        def test_valid_sub(self):
            '''
                If two int values were given and a valid operation (-)
                is informed it must return a value
            '''
            result = do_math(a=self.a, b=self.b,operation='-')
            self.assertEqual(result, -5)
            self.assertIsInstance(result, int)

        def test_valid_mul(self):
            '''
                If two int values were given and a valid operation (*)
                is informed it must return a value
            '''
            result = do_math(a=self.a, b=self.b,operation='*')
            self.assertEqual(result, 50)
            self.assertIsInstance(result, int)

        def test_valid_div(self):
            '''
                If two int values were given and a valid operation (/)
                is informed it must return a value
            '''
            result = do_math(a=self.a, b=self.b,operation='/')
            self.assertEqual(result, 0)
            self.assertIsInstance(result, int)        


if __name__ == "__main__":
    unittest.main()
#a = int(input("Enter the firs number (must be an integer):"))
#b = int(input("Enter the second number (must be an integer):"))
#op = str(input("Chose the operation (+,-,*,/)):"))
#print(do_math(a,b,op))