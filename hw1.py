
class State(object):
    """
    Basic rep for states (will use to construct trees and graphs)
    """
    
    def __init__(self, name, pos=0,seen=False):
        """
        """
        self.name = name
        self.pos = pos
        self.next = []
        self.seen = False

    def __str__(self):
        """
        """
        return self.printTree()

    def __repr__(self):
        """
        """
        return self.__str__()
        
    def printTree(self, indent=''):
        """
        """
        output = indent + self.name + '\n'
        for state in self.next:
            output += state.printTree(indent + '-')
        return output

class Node(object):
    """
    Basic node class
    """
    
    def __init__(self,state=None,action=None,cost=None,parent=None):
        """        
        """
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent

    def __str__(self):
        """
        """
        ret = "State = %s\nAction = %s\nCost = %s\nParent=%s\n" % (self.state,
                                                                   self.action,
                                                                   self.cost,
                                                                   self.parent)
        return ret

    def __repr__(self):
        """
        """
        return self.__str__()

    def __len__(self):
        count = 0
        cur = self
        while cur != None:
            cur = cur.parent
            count += 1
        return count

def breadthFirst_LeftToRight(frontier):
    """
    """
    frontier.sort(key=lambda path: path.state.pos)
    frontier.sort(key=lambda path: len(path))
    return frontier.pop(0)

def breadthFirst_RightToLeft(frontier):
    """
    """
    frontier.sort(key=lambda path: path.state.pos, reverse=True)
    frontier.sort(key=lambda path: len(path))
    return frontier.pop(0)

def depthFirst_LeftToRight(frontier):
    """
    """
    frontier.sort(key=lambda path: path.state.pos)
    frontier.sort(key=lambda path: len(path), reverse=True)
    return frontier.pop(0)

def depthFirst_RightToLeft(frontier):
    """
    """
    frontier.sort(key=lambda path: path.state.pos, reverse=True)
    frontier.sort(key=lambda path: len(path), reverse=True)
    return frontier.pop(0)

def GraphSearch(problem,goal,remove_choice,finalProblem=False):
    """
    """
    explored = []
    frontier = []
    frontier.append(Node(problem))
    count = 0
    while 1:
        if len(frontier) == 0:
            return None
        path = remove_choice(frontier)
        explored.append(path)
        count += 1
        print count
        if path.state == goal:
            return path
        for a in path.state.next:
            newNode = Node(a)
            newNode.parent = path
            if newNode not in frontier and newNode not in explored:
                if finalProblem and not a.seen:
                    a.seen = True
                    frontier.append(newNode)
            else:
                print "BAD"

                
if __name__ == '__main__':
    """ Problem #4 """
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
    
    print a
    print 'Problem #5a'
    GraphSearch(a,m,breadthFirst_LeftToRight)
    print 'Problem #5b'
    GraphSearch(a,m,depthFirst_LeftToRight)
    print 'Problem #5c'
    GraphSearch(a,m,breadthFirst_RightToLeft)
    print 'Problem #5d'
    GraphSearch(a,m,depthFirst_RightToLeft)

    """Problem #5"""
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
    
    print a
    print 'Problem #6a'
    GraphSearch(a,j,breadthFirst_LeftToRight,True)
    print 'Problem #6b'
    """Problem #5"""
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
    GraphSearch(a,j,depthFirst_LeftToRight,True)
    print 'Problem #6c'
    """Problem #5"""
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
    GraphSearch(a,j,breadthFirst_RightToLeft,True)
    print 'Problem #6d'
    """Problem #5"""
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
    GraphSearch(a,j,depthFirst_RightToLeft,True)
