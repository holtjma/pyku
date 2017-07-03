'''
Factorial int
Recurse Implementation
Auth.: holtjma
'''

def dec(Input):
    '''
    Pyku for decrement:
    y equals input
    y equals y minus two
    return y plus one
    '''
    y = Input
    y = y-2
    return y+1

def fac(x):
    '''
    Pyku for factorial:
    if x and not false
    return x times fac dec x
    return 1 and 1
    '''
    if x and not False:
        return x*fac(dec(x))
    return 1 & 1

if __name__ == '__main__':
    print 'x\tfac(x)'
    for x in xrange(1, 10):
        print str(x)+'\t'+str(fac(x))
    