from nose.tools import assert_equal

def pair_sum(arr, sum_val):
    """
    Problem:
    Given an integer array, output all the unique pairs that sums up to a specific value k.

    So the input:
        pair_sum([1,3,2,2], 4)

    would return 2 pairs:
        (1, 3)
        (2, 2)

    Note:
    For testing purposes change your function so it outputs the number of pairs.
    """

    # Edge case check
    if len(arr) < 2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()

    for number in arr:
        target = sum_val - number

        if target not in seen:
            seen.add(number)
        else:
            output.add(((min(number, target)), max(number, target)))

    return len(output)


# Test solution
class PairSumTest(object):
    def test(self, solution):
        try: 
            assert_equal(solution([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10), 6)
            assert_equal(solution([1,2,3,1], 3), 1)
            assert_equal(solution([1,3,2,2], 4), 2)
            print('\33[102m' + 'ALL TEST CASES PASSED' + '\33[102m')
        except AssertionError:
            print('\33[101m' + 'ALL TEST CASES FAILED' + '\33[101m')

# Run tests
testing  = PairSumTest()
testing.test(pair_sum)