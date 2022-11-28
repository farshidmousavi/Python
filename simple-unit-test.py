import unittest #Import unitTest library
        
def userNameFunc(name): #simple function for test with unitTest
    return name

class testSimpleClass(unittest.TestCase): #a class with inheritance of unit test class
    def test_a_simple_function(self): #all unit test function most start with 'test' at the start and continue Ex:testone,test_two, testThree
        result = userNameFunc('myname') #call function that we want to test and get result
        self.assertEqual(result,'myname') #check function result for be same as we want to be

#at the end we most call main function to run the unit test
if __name__ == "__main__":
    unittest.main()
