from nose.tools import assert_equal

def compress(string):
    """
    Problem:
    Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
    For this problem, you can falsely 'compress' strings of single or double letters. For instance, it
    is okay for 'AAB' to return 'A2B1' even though this thechnically takes more space.

    The function should aslo be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
    """
    result = ""
    length = len(string)
    
    # Edge case check
    if length == 0:
        return ''
    
    # Check for single letter
    if length == 1:
        return string + '1'
    
    count = 1
    index = 1

    while index < length:
        if string[index] == string[index - 1]:
            count += 1
        else:
            result = result + string[index - 1] + str(count)
            count = 1

        index += 1
    
    result = result + string[index - 1] + str(count)

    return result


# Test solution
class StringCompressionTest(object):
    def test(self, solution):
        try: 
            assert_equal(solution('AAAbbbCCdd'), 'A3b3C2d2')
            assert_equal(solution('AABBCC'), 'A2B2C2')
            assert_equal(solution('AAABCCDDDDD'), 'A3B1C2D5')
            print('\33[102m' + 'ALL TEST CASES PASSED' + '\33[102m')
        except AssertionError:
            print('\33[101m' + 'ALL TEST CASES FAILED' + '\33[101m')

# Run tests
testing  = StringCompressionTest()
testing.test(compress)