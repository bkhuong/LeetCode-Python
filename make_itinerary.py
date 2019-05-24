class Solution: 
    '''
    Given a list of tickets, find itinerary in order using the given list.
    '''
    
    def find_route(tickets:list) -> str: 
        routes = {} 
        start = [] 

        # create map 
        for ticket in tickets:
            routes[ticket[0]] = {'to':ticket[1]}
            try: 
                routes[ticket[1]].update({'from':ticket[0]})
            except:
                routes[ticket[1]] = {'from':ticket[0]}

        # find starting point 
        for k,v in routes.items():
            if 'from' not in v.keys():
                departure = k 
                break

        # walk dictionary for route:
        while 'to' in routes[departure].keys():
            print(f'{departure} -> {routes[departure]["to"]}')
            departure = routes[departure]['to']

