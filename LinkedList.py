class Node:
    def __init__(self, val):
        self.r = None
        self.v = val

class list:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if (self.head == None):
            self.head = Node(val)
        else:
            return self._insert(val, self.head)

    def _insert(self, val, node):
        if (node.r == None):
            node.r = Node(val)
        else:
            return self._insert(val, node.r)

    def find(self, val):
        if (self.head != None) and (self.head.v == val):
            return self.head.v
        if (self.head != None) and (self.head.v != val):
            return self._find(self.head.r, val)
        if (self.head == None):
            return None

    def _find(self, node, val):
        if (node == None):
            return None
        elif (node != None) and (node.v != val):
            return self._find(node.r, val)
        elif (node != None) and (node.v == val):
            return node.v
    

    def printList(self):
        print(str(self.head.v) + ", ")
        self._printList(self.head.r)

    def _printList(self, node):
        if (node == None):
            print ("")
        elif (node != None):
            print (str(node.v) + ", ")
            self._printList(node.r)

    def delete(self, val):
        if (self.head != None) and (self.head.v == val):
            self.head = self.head.r
        if (self.head != None) and (self.head.v != val):
            return self._delete(self.head, val)
        if (self.head == None):
            return None

    def _delete(self, node, val):
        if (node.r == None):
            return
        elif (node.r.v != val):
            return self._delete(node.r, val)
        node.r = node.r.r
        return self._delete(node, val)
            
        




list = list()
list.insert(5)
list.insert(7)
list.insert(8)
list.insert(7)
list.insert(17)
list.insert(70)
list.insert(27)
list.insert(87)
list.insert(1)
list.insert(5)
list.insert(7)


list.delete(5)
list.delete(7)
list.delete(70)

list.printList()
