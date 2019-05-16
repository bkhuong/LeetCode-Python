class Solution:
    '''
    Given a string of words, reverse all the words.
    '''
    def rev_word(s: str) -> str:
        return " ".join(s.split()[::-1])

