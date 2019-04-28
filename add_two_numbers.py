class Solution:
    '''
    Given two non-empty linked lists representing two non-negative integers, add the
    two numbers and return it as a linked list. 

    Assume the digits are stored in reverse order and each of their nodes contain 
    a single digit. You may assume the two numbers do not contain any leading zero, 
    except the number 0 itself.

    The definition of a  ListNode is as follows: 
    Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
          self.val = x
          self.next = None
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lls = [l1, l2] 
        numbers = []

        for ll in lls:
            listnode = ll 
            s = ''
            while True:
                if listnode is None:
                    break
                s += str(listnode.val) 
                print(listnode.val)
                listnode = listnode.next 
            numbers.append(int(s[::-1]))
               
        return [int(s) for s in str(sum(numbers))[::-1]]
