from nose.tools import assert_equal

def anagram(string1, string2):
    """
    Problem:
    Given two strings, check to see if they are anagrams. An anagram is when the two strings can
    be written using the exact same letters (so you can just rearrange the letters to get a different
    phrase or word)

    Example:
    "public relations" is an anagram of "crap built on lies"
    "clint eastwood" is an anagram of "old west action"

    Note:
    Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and " o d g"
    """

    # Remove spaces in string and make them all lowercase
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()

    # Edge case check if strings are anagram or not
    if len(string1) != len(string2):
        return False
    
    # Check the posibility of anagram
    count = {}

    for letter in string1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in string2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for value in count:
        if count[value] != 0:
            return False
        
    return True


# Test solution
class AnagramTest(object):
    def test(self, solution):
        try: 
            assert_equal(solution('go go go', 'gggooo'), True)
            assert_equal(solution('abc', 'cba'), True)
            assert_equal(solution('hi mom', 'hi     mom'), True)
            assert_equal(solution('aabbcc', 'aabbc'), False)
            assert_equal(solution('123', '1 2'), False)
            print('\33[102m' + 'ALL TEST CASES PASSED' + '\33[102m')
        except AssertionError:
            print('\33[101m' + 'ALL TEST CASES FAILED' + '\33[101m')

# Run tests
testing  = AnagramTest()
testing.test(anagram)