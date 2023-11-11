from nose.tools import assert_equal

def unique_char(string):
    """
    Given a string, determine if it is compreised of all unique characters. For
    example, the string 'abcde' has all unique characters and should return True.
    The string 'aabcde' contains duplicate characters and should return false.
    """
    chars = set()

    for letter in string:
        if letter in chars:
            return False
        else:
            chars.add(letter)

    return True


# Test solution
class UniqueCharTest(object):
    def test(self, solution):
        try: 
            assert_equal(solution(''), True)
            assert_equal(solution('goo'), False)
            assert_equal(solution('abcdefg'), True)
            print('\33[102m' + 'ALL TEST CASES PASSED' + '\33[102m')
        except AssertionError:
            print('\33[101m' + 'ALL TEST CASES FAILED' + '\33[101m')

# Run tests
testing  = UniqueCharTest()
testing.test(unique_char)