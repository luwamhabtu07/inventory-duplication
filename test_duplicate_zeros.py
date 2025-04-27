import unittest
from  duplicate_zeros import duplicate_zeros

class TestDuplicateZeros(unittest.TestCase):
    # normal test case
    def test_normal_case1(self):
        arr = [4,0,1,3,0,2,5,0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [4,0,0,1,3,0,0,2])

    def  test_normal_case2(self):
        arr = [3,2,1]
        duplicate_zeros(arr)
        self.assertEqual(arr, [3,2,1])
    
    def test_normal_case3(self):
        arr = [0,1,0,2]
        duplicate_zeros(arr)
        self.assertEqual(arr, [0,0,1,0])

    # edge test case 
    def test_edge_case_full_zeros(self):
        arr = [0,0,0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [0,0,0])

    def test_edge_case_no_zero(self):
        arr = [5,6,7]
        duplicate_zeros(arr)
        self.assertEqual(arr, [5,6,7])
    
    def test_edge_case_one_element_zero(self):
        arr = [0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [0])


if __name__ == "__main__":
    unittest.main()


