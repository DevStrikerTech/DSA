from nose.tools import assert_equal

def remove_whitespaces(string):
    words = []
    length = len(string)
    spaces = [' ']

    index = 0

    while index < length:
        if string[index] not in spaces:
            word_start = index

            while index < length and string[index] not in spaces:
                index += 1

            words.append(string[word_start:index])

        index += 1

    return words

def reverse_sentence(string):
    """
    Problem:
    Given a string of words, reverse all the words.

    Example:
        Given:
            'This is the best'

        Return:
            'best the is this'

    Note:
    You should remove all leading and trailing whitespace. So that inputs
    such as:
        '  space here' and 'space here  '

    both become:
        'here space'
    """
    reverse_list = []
    words = remove_whitespaces(string)

    for index in range(1, len(words)+1):
        reverse_list.append(words[-index])

    return " ".join(reverse_list)


# Test solution
class SentenceReversalTest(object):
    def test(self, solution):
        try: 
            assert_equal(solution('    space before'), 'before space')
            assert_equal(solution('space after     '), 'after space')
            assert_equal(solution('   Hello John    how are you    '), 'you are how John Hello')
            print('\33[102m' + 'ALL TEST CASES PASSED' + '\33[102m')
        except AssertionError:
            print('\33[101m' + 'ALL TEST CASES FAILED' + '\33[101m')

# Run tests
testing  = SentenceReversalTest()
testing.test(reverse_sentence)