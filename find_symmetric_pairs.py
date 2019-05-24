class Solution: 
    '''
    Two pairs (a, b) and (c, d) are said to be symmetric if c is equal 
    to b and a is equal to d. For example, (10, 20) and (20, 10) are 
    symmetric. Given an array of pairs find all symmetric pairs in it.
    '''

    def find_symmetric_pairs(pairs):
        counter = {}
        symmetric_pairs = []
        for pair in pairs:
            pair.sort()
            try:
                counter[str(pair)]+=1
            except:
                counter[str(pair)]=1
            if counter[str(pair)]==2:
                symmetric_pairs.append(pair)
        return symmetric_pairs


