from nose.tools import assert_equal

def large_cont_sum(array):
    """
    Problem:
    Given an array of integers (positive and negative) find the largest continuous sum.
    """
    # Edge case check
    if len(array) == 0:
        return 0
    
    max_sum = current_sum = array[0]

    for number in array[1:]:
        current_sum = max(current_sum + number, number)
        max_sum = max(current_sum, max_sum)

    return max_sum


# Test solution
class LargeCoutSumTest(object):
    def test(self, solution):
        try: 
            assert_equal(solution([1, 2, -1, 3, 4, -1]), 9)
            assert_equal(solution([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
            assert_equal(solution([-1, 1]), 1)
            print('\33[102m' + 'ALL TEST CASES PASSED' + '\33[102m')
        except AssertionError:
            print('\33[101m' + 'ALL TEST CASES FAILED' + '\33[101m')

# Run tests
testing  = LargeCoutSumTest()
testing.test(large_cont_sum)