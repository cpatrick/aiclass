
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
                # This is a bit messy. I special case for the last question
                # on hw1 because it doesn't allow for nodes to be seen more
                # than once.
                if finalProblem:
                    if not a.seen:
                        a.seen = True
                        frontier.append(newNode)
                else:
                    frontier.append(newNode)
            else:
                print "BAD"
