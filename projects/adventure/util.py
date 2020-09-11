
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
    def __repr__(self):
        return str(self.queue)
    def __str__(self):
        return str(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
    def __repr__(self):
        return str(self.stack)
    def __str__(self):
        return str(self.stack)

def verbose(identifier='', message=False, end='\n'):
    go = False
    if not message and go:
        print(f'{identifier}', end=end)
    elif go:
        print(f'{identifier} -->  {message}', end=end)
testing = True
length = 60
def top(name):
    if not testing:
        n = ((length - len(name)) // 2 ) -1
        part = '=' * n
        print('\n'+part + ' ' + name + ' ' + part+'\n')

def bottom():
     if not testing:
        print('=' * length)
def mid(s):
    if not testing:
        s = str(s)
        n = ((length - len(s)) // 2 ) -1
        n = ' ' * n
        print(n + s)
    else:
        print(s)

"""
Simple graph implementation
"""
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = {}
        result = []
        q = Queue()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            current = q.dequeue()
            if current in visited:
                continue
            else:
                print(current)
                result.append(current)
                visited[current] = None
                verbose('Visited', visited)
                n = self.get_neighbors(current)
                for i in n:
                    q.enqueue(i)
        return result

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = {}
        result =[]
        s = Stack()
        s.push(starting_vertex)
        while s.size() > 0:
            current = s.pop()
            if current == None:
                break
            elif current in visited:
                continue
            else:
                result.append(current)
                visited[current] = None
                n = self.get_neighbors(current)
                n = reversed(list(n))
                for i in n:
                    s.push(i)
        return result

    def dft_recursive(self, starting_vertex, visited={}):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        n = self.get_neighbors(starting_vertex)
        visited[starting_vertex] = None
        for i in n:
            if i  in visited:
                continue
            visited[i] = None
            self.dft_recursive(i, visited)

    def bfs(self, starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # visited = {}
        # path = []
        # q = Queue()
        # current = starting_vertex
        # while '?' not in self.vertices[current].values(): #assuming dict of ded end does not contain '?'
        #     n = self.vertices[current]
        #     for i in n.items():
        #         if i[1] != None
            
            

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        top('Depth First Search')
        visited = {}
        s = Stack()
        s.push(starting_vertex)
        while s.size() > 0:
            current = s.pop()
            if current == destination_vertex:
                return True
            elif current in visited:
                continue
            else:
                visited[current] = None
                n = self.get_neighbors(current)
                n = reversed(list(n))
                for i in n:
                    s.push(i)
        return False

    def dfs_recursive(self, starting_vertex, destination_vertex, visited={}):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex == destination_vertex:
            return True

        n = self.get_neighbors(starting_vertex)
        result = False
        visited[starting_vertex] = None
        for i in n:
            if i not in visited:
                result = result or self.dfs_recursive(i, destination_vertex, visited)
                if result ==  True:
                    break
        return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)


    print(graph.bfs(1, 6))
    print(graph.bfs(1, 8))
