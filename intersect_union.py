class Solution:
    '''
    Given two Linked Lists, create union and intersection lists that contain union 
    and intersection of the elements present in the given lists. Order of elments 
    in output lists doesn’t matter.
    '''
    def intersection_and_union(list_1: list, list_2:list) -> tuple: 
        lists = [list_1, list_2]
        counter = {}
        intersection = [] 
        union = [] 
        for list_ in lists: #2 
            for i in list_: #m, n 
                try: 
                    counter[i]+=1
                    union.append(i)
                    intersection.append(i)
                except:
                    counter[i]=0 
                    union.append(i)
        return (set(intersection), set(union))


