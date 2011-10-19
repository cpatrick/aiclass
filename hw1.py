from aiclassutils import *

def generateGraphForQuestion4():
    """
    """
    a = State('a',0)
    b = State('b',1)
    c = State('c',2)
    d = State('d',3)
    e = State('e',4)
    f = State('f',5)
    g = State('g',6)
    h = State('h',7)
    i = State('i',8)
    j = State('j',9)
    a.next = [b,c,d]
    b.next = [e,f]
    c.next = [g,h]
    d.next = [i,j]
    return (a,f)

def generateGraphForQuestion5():
    """
    """
    a = State('a',0)
    b = State('b',1)
    c = State('c',2)
    d = State('d',3)
    e = State('e',4)
    f = State('f',5)
    g = State('g',6)
    h = State('h',7)
    i = State('i',8)
    j = State('j',9)
    k = State('k',10)
    l = State('l',11)
    m = State('m',12)
    a.next = [b,c,d]
    b.next = [e,f]
    c.next = [g,h]
    d.next = [i,j]
    g.next = [k,l]
    h.next = [m]
    return (a,m)

def generateGraphForQuestion6():
    """
    """
    a = State('a',0)
    b = State('b',1)
    c = State('c',2)
    d = State('d',3)
    e = State('e',4)
    f = State('f',5)
    g = State('g',6)
    h = State('h',7)
    i = State('i',8)
    j = State('j',9)
    k = State('k',10)
    l = State('l',11)
    m = State('m',12)
    n = State('n',13)
    o = State('o',14)
    p = State('p',15)
    a.next = [b,c]
    b.next = [d,e]
    c.next = [e,f]
    d.next = [g,h]
    e.next = [h,i]
    f.next = [i,j]
    g.next = [k]
    h.next = [k,l]
    i.next = [l,m]
    j.next = [m]
    k.next = [n]
    l.next = [n,o]
    m.next = [o]
    n.next = [p]
    o.next = [p]
    return (a,j)

if __name__ == '__main__':
    """ Problem #4 """
    a,f = generateGraphForQuestion4()
    print a
    print 'Problem #4a'
    GraphSearch(a,f,breadthFirst_LeftToRight)
    print 'Problem #4b'
    GraphSearch(a,f,depthFirst_LeftToRight)
    print 'Problem #4c'
    GraphSearch(a,f,breadthFirst_RightToLeft)
    print 'Problem #4d'
    GraphSearch(a,f,depthFirst_RightToLeft)
    
    """Problem #5"""
    a,m = generateGraphForQuestion5()
    print a
    print 'Problem #5a'
    GraphSearch(a,m,breadthFirst_LeftToRight)
    print 'Problem #5b'
    GraphSearch(a,m,depthFirst_LeftToRight)
    print 'Problem #5c'
    GraphSearch(a,m,breadthFirst_RightToLeft)
    print 'Problem #5d'
    GraphSearch(a,m,depthFirst_RightToLeft)
    
    """Problem #6"""
    a,j = generateGraphForQuestion6()
    print a
    print 'Problem #6a'
    GraphSearch(a,j,breadthFirst_LeftToRight,True)
    print 'Problem #6b'
    a,j = generateGraphForQuestion6()
    GraphSearch(a,j,depthFirst_LeftToRight,True)
    print 'Problem #6c'
    a,j = generateGraphForQuestion6()
    GraphSearch(a,j,breadthFirst_RightToLeft,True)
    print 'Problem #6d'
    a,j = generateGraphForQuestion6()
    GraphSearch(a,j,depthFirst_RightToLeft,True)
