'''
Fibonacci seq.
Linear Implemented
Auth.: holtjma
'''

def init():
    '''
    Pyku for initial setup:
    low equals zero
    higher equals zero one
    return low higher
    '''
    low = 0
    higher = 01
    return [low, higher]

def loop(resultList, x):
    '''
    Pyku for running a linear loop:
    for i in range x
    computation result list
    return result list
    '''
    for i in range(x):
        computation(resultList)
    return resultList

def computation(vals):
    '''
    Pyku for actually doing the computations:
    temp equals vals one
    vals zero two equals temp
    sum vals plus zero
    '''
    temp = vals[1]
    vals[0:2] = [temp, 
                 sum(vals)+0]
    
def fib(index):
    '''
    Pyku for fibonacci
    vals equals init
    vals equals loop vals index
    return vals zero
    '''
    vals = init()
    vals = loop(vals, index)
    return vals[0]

if __name__ == '__main__':
    print 'x\tfib(x)'
    for x in xrange(0, 100):
        print str(x)+'\t'+str(fib(x))