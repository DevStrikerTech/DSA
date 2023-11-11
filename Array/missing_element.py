from collections import defaultdict
from nose.tools import assert_equal

def finder(array1, array2):
    """
    Problem:
    Consider an array of non-negative integers. A second array is formed by shuffling the elements
    of the first array and deleting a random element. Given these two arrays, find which element is
    missing in the second array.

    Exmaple:
    The first array is shuffled and the number 5 is removed to construct
    the second array.

    Input:
        finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
    
    Output:
        5 is the missing number.
    """
    counter = defaultdict(int)
    
    for number in array2:
        counter[number] += 1

    for number in array1:
        if counter[number] == 0:
            return number
        else:
            counter[number] -= 1


# Test solution
class FinderTest(object):
    def test(self, solution):
        try: 
            assert_equal(solution([5, 5, 7, 7], [5, 7, 7]), 5)
            assert_equal(solution([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
            assert_equal(solution([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
            print('\33[102m' + 'ALL TEST CASES PASSED' + '\33[102m')
        except AssertionError:
            print('\33[101m' + 'ALL TEST CASES FAILED' + '\33[101m')

# Run tests
testing  = FinderTest()
testing.test(finder)