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

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, edge):
        self.edges.add(edge)

    def print_vertices(self):
        print("Graph Vertices:")
        for vertex in self.vertices:
            print(vertex)

    def print_unique_edges(self):
        print("Unique Graph Edges:")
        for edge in self.edges:
            print(edge)


# Create an instance of the graph
graph = Graph()

# Add vertices to the graph
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

# Print the vertices
graph.print_vertices()

# Add an edge to the graph
graph.add_edge(("A", "B"))
graph.add_edge(("B", "C"))
graph.add_edge(("C", "D"))
graph.add_edge(("D", "A"))
graph.add_edge(("A", "C"))

# Print the unique edges
graph.print_unique_edges()



class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * len(vertices) for _ in range(len(vertices))]

    def add_edge(self, src, dest):
        src_index = self.vertices.index(src)
        dest_index = self.vertices.index(dest)
        self.adj_matrix[src_index][dest_index] = 1
        self.adj_matrix[dest_index][src_index] = 1

    def print_adjacency_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
            
# Create an instance of the graph
graph = Graph(["A", "B", "C", "D"])

# Add edges to the graph
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")
graph.add_edge("A", "C")

# Print the adjacency matrix
graph.print_adjacency_matrix()


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue item.")
        else:
            if self.is_empty():
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(f"Enqueued item: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue item.")
            return None
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            print(f"Dequeued item: {item}")
            return item

