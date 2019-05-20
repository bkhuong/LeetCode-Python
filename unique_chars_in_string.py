class Solution: 
    '''
    Given a string,determine if it is compreised of all unique characters. 
    For example, the string 'abcde' has all unique characters and should return 
    True. The string 'aabcde' contains duplicate characters and should return false.
    '''
    def uni_char(s:str) -> bool: 
        counter = {} 
        for char in s:
            try:
                counter[char]+=1
                return False
            except:
                counter[char] = 1
        return True 
    
    def uni_char_2(s:str) -> bool: 
        return len(set(s)) == len(s)

