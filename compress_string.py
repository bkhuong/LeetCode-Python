class Solution:
    '''
    Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. 
    For this problem, you can falsely "compress" strings of single or double letters. 
    For instance, it is okay for 'AAB' to return 'A2B1' even though this technically 
    takes more space.
    '''
    def compress(s: str) -> str:
        count = {}
        chars = []
        # update count dictionary
        for char in s:
            try:
                count[char] += 1
            except:
                count[char] = 1
                # keep track of string order
                chars.append(char)
        return "".join([char+str(count[char]) for char in chars])

    def compress_2(s: str) -> str:
        r = ''
        count = 1
        l = len(s)
        if l == 0:
            return r 
        
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1 
            else:
                r = r + s[i] + str(count)
                count = 1 
        r = r + s[-1] + str(count)
        return r
