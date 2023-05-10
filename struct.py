'''
stack LIFO
push pop
uses: undo redo parsing 
'''

class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop()
    def print_stack(self):
        print(self.items)

s=Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack()

'''
queue
rear end (inserted, enqueue) 
front end (deleted, dequeue)
fifo
uses: printer call center systems
'''

class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def print_queue(self):
        print(self.items)

q=Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.print_queue()

q.dequeue()
q.print_queue()

'''
linked list
each node stores data and links to another node (linked chain)
first node (head)
last node connects to none to determine end of list
insert and remove at any position
uses: undo redo linked data playlist of music
other DS like stack queue graphs
'''

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def front(self, data):
        self.head=Node(data, self.head)    
    def end(self, data):
        if not self.head:
            self.head=Node(data, None)
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=Node(data,None)
    def get_last_node(self):
        n=self.head
        while(n.next != None):
            n=n.next
        return n.data
    def is_empty(self):
        self.head==None
    def print_list(self):
        n=self.head
        while n!=None:
            print(n.data, end = '=>')
            n=n.next
        print()
l=LinkedList()
l.front(5)
l.front(6)
l.front(7)
l.end(8)
l.print_list()
print(l.get_last_node())

'''
uses: netwroks
node = vertex 
paths = edge

0 1 1
1 0 0 
1 0 0

1 is edge
adjacency matrix
'''
class Graph():
    def __init__(self, size):
        self.adj = [[0]*size for i in range(size)]
        self.size = size
    def edge(self, orig, dest):
        if orig>self.size or dest>self.size or orig<0 or dest <0:
            print('Invalid Edge')
        else:
            self.adj[orig-1][dest-1]=1
            self.adj[dest-1][orig-1]=1
    def remove_edge(self, orig, dest):
        if orig>self.size or dest>self.size or orig<0 or dest<0:
            print('Invalid Edge')
        else:
            self.adj[orig-1][dest-1]=0
            self.adj[dest-1][orig-1]=0
    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print('{:4}'.format(val),end='')

G=Graph(4)
G.edge(1, 3)
G.edge(3, 4)
G.display()
print()