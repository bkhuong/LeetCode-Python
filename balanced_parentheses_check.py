class Solution: 
    '''
    Given a string of opening and closing parentheses, check whether it’s balanced. 
    We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. 
    Assume that the string doesn’t contain any other character than these, no spaces words or numbers. 
    As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse 
    order opened. For example ‘([])’ is balanced but ‘([)]’ is not.
    '''
    def balance_check(s:str) -> bool: 
        pairs = {'(':')', '{':'}', '[':']'}

        stack = [s[0]]
        for i in range(1,len(s)):
            # if stack is empty, append 
            if len(stack)==0:
                stack.append(s[i])
            # if stack isn't empty, check for pairs 
            else:
                if stack[-1] in pairs.keys():
                    if pairs[stack[-1]] == s[i]:
                        stack.pop(-1)
                    else:
                        stack.append(s[i])                    
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
    def balance_check_2(s:str) -> bool: 
        pairs = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s: 
            if char in pairs.keys():
                if stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return len(stack)==0         
    
 
