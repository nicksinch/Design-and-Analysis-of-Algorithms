""" 
    Graph class with the most essential and famous algorithms implemented 
"""


from vertex import Vertex
from collections import defaultdict
import heapq



class Graph:
    def __init__(self, graph_dict=None):
        """ 
            
            Initializes a graph object. If no dictionary is passed as an argument,
            an empty dictionary will be used. Graph is implemented as dictionary of dictionaries.
            This means that the key in the key-value pairs represents a vertex,
            and the value is a dictionary that represents the neighbour of the vertex
            mapped to its corresponding weight ( 0 if we don't want the graph to be weighted )
            
            {'A' : {'B': 2, 'C':3 } } 
            means that we get from A to B with cost of 2 and from A to C with cost of 3.

        """

        if graph_dict == None:
            graph_dict = {}

        self.__graph_dict = graph_dict


    def vertices(self):
        """ returns the vertices of the graph """
        return list(vertex.value for vertex in self.__graph_dict.keys())


    def edges(self):
        return self.__generate_edges()


    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex].keys():
                if {neighbour.value, vertex.value} not in edges:
                    edges.append({vertex.value, neighbour.value})
        return edges


    def add_vertex(self, vertex):
        """ If the vertex is not in the graph, a vertex : [] key-value is added
            to the graph_dictionary, otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = {}


    def add_edge(self, from_vertex, to_vertex, weight = 0):
        """ Connects a vertex that is in the graph to another vertex
            i.e. adds an edge. However if the vertex is not present in the graph,
            nothing can be connected, so we do nothing.
        """
        if from_vertex not in self.__graph_dict:
            return
        else:
            self.__graph_dict[from_vertex] = {to_vertex : weight}


    def prim_spanning_tree(self, starting_vertex):
        """ Runs the Prim's algorithm which results in generating a minimum spanning tree. """
        mst = defaultdict(set)
        visited = set([starting_vertex])
        edges = [
            (cost, starting_vertex, to.getValue())
            for to, cost in self.__graph_dict[starting_vertex].items()
        ]
        heapq.heapify(edges)

        while edges:
            cost, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst[frm].add(to)
                for to_next, cost in self.__graph_dict[to].items():
                    if to_next.getValue() not in visited:
                        heapq.heappush(edges, (cost, to.getValue(), to_next.getValue()))
        return mst


    def find_path(self, start_vertex, end_vertex, path = []):
       """ 
          finds a path from start_vertex to end_vertex 
          in graph in a recursive manner. ( DFS Modification )
       """
       path = path + [start_vertex]
       if start_vertex == end_vertex: # If we have reached the destination
            return path
       if start_vertex not in self.__graph_dict:
            return None
       for vertex in self.__graph_dict[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path: 
                    return extended_path
       return None
    

    def find_all_paths(self, start_vertex, end_vertex, current_path = []):
        """ 
            returns a list of lists representing all the possible paths from
            start_vertex to end_vertex 
        """
        current_path = current_path + [start_vertex]
        if start_vertex == end_vertex:
            return [current_path]
        if start_vertex not in self.__graph_dict:
            return []
        all_paths = []
        for vertex in self.__graph_dict[start_vertex]:
            if vertex not in current_path:
                extended_paths = self.find_all_paths(vertex, end_vertex, current_path)
                for p in extended_paths:
                    all_paths.append(p)
        return all_paths


    def DFS(self, start_vertex):
        visited = set()

        self.__DFSUtil(start_vertex, visited)


    def __DFSUtil(self, start_vertex, visited):
        visited.add(start_vertex)
        print(start_vertex, end=' ')
        for neighbour in self.__graph_dict[start_vertex]:
            if neighbour not in visited:
                self.__DFSUtil(neighbour,visited)


example_graph = {
    Vertex('A'): { Vertex('B'): 2, Vertex('C'): 3},
    Vertex('B'): { Vertex('A'): 2, Vertex('C'): 1, Vertex('D'): 1, Vertex('E'): 4},
    Vertex('C'): { Vertex('A'): 3, Vertex('B'): 1, Vertex('F'): 5},
    Vertex('D'): { Vertex('B'): 1, Vertex('E'): 1},
    Vertex('E'): { Vertex('B'): 4, Vertex('D'): 1, Vertex('F'): 1},
    Vertex('F'): { Vertex('C'): 5, Vertex('E'): 1, Vertex('G'): 1},
    Vertex('G'): { Vertex('F'): 1},
}

g = Graph(example_graph)
a = list(example_graph)[0]
print(a)
print(g.prim_spanning_tree(a))
# https://www.python-course.eu/graphs_python.php