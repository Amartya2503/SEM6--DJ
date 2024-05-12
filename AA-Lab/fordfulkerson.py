# from collections import defaultdict

# class Graph():
#     def __init__(self):
#         self.graph = defaultdict(lambda : defaultdict(int))
#         self.nodes = set()
    
#     def insertEdge(self, u,v,capacity):
#         self.graph[u][v] = capacity
#         self.nodes.add(u)
#         self.nodes.add(v)
    
#     def bfs(self, source, sink, parent):
#         visited = {Node : False for Node in self.nodes}
#         visited[source] = True
#         parent[source] = -1
        
#         queue = [source]
#         while queue:
#             u = queue.pop(0)
#             for v in self.graph[u]:
#                 if not visited[v] and self.graph[u][v] >0 :
#                     visited[v] = True
#                     parent[v] = u
#                     queue.append(v)
            
#         return visited[sink]
    
#     def fordFulkerson(self, source, sink):
#         parent = {node : False for node in self.nodes}
#         path_count = 0
#         max_flow = 0
#         while self.bfs(source,sink, parent):
#             v = sink
#             path = []
#             path_flow = float("Inf")
#             while v!= source:
#                 u = parent[v]
#                 path.insert(0,u)
#                 path_flow = min(path_flow, self.graph[u][v])
#                 v = u
            
#             print(f"Augmented path {path_count+1} : {'->'.join(path)}")
#             v = sink
#             while v!= source:
#                 u = parent[v]
#                 self.graph[u][v] -= path_flow
#                 self.graph[v][u] += path_flow
#                 v = u
#             max_flow += path_flow
#             path_count += 1
#         return max_flow

# g = Graph()
# g.insertEdge("S","1",11)
# g.insertEdge("S", "2", 12)
# g.insertEdge("2", "1", 1)
# g.insertEdge("2", "4", 11)
# g.insertEdge("1", "3", 12)
# g.insertEdge("4", "3", 7)
# g.insertEdge("4", "T", 4)
# g.insertEdge("3", "T", 19)

# maxflow = g.fordFulkerson("S","T")
# print(f'maxflow is {maxflow}')


                
from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(lambda : defaultdict(int))
        self.nodes = set()
        
    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.nodes.add(u)
        self.nodes.add(v)
    
    def bfs(self, source, sink, parent):
        visited = {node : False for node in self.nodes}
        visited[source] = True
        parent[source] = -1
        
        queue = [source]
        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if not visited[v] and self.graph[u][v] >0:
                    visited[v] = True
                    queue.append(v)
                    parent[v] = u
        return visited[sink]
    
    def fordFulkerson(self, source , sink):
        parent = {node : False for node in self.nodes}
        path_count = 0
        max_flow = 0
        while self.bfs(source, sink, parent):
            v = sink
            path = []
            path_flow = float("Inf")
            
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                path.append(u)
                v = u
            print(f"Augmenting path {path_count} : {'->'.join(path)}")
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u
            max_flow += path_flow
            path_count+=1
        return max_flow
    
g = Graph()
g.add_edge("S","1",11)
g.add_edge("S", "2", 12)
g.add_edge("2", "1", 1)
g.add_edge("2", "4", 11)
g.add_edge("1", "3", 12)
g.add_edge("4", "3", 7)
g.add_edge("4", "T", 4)
g.add_edge("3", "T", 19)

maxFlow = g.fordFulkerson("S","T")
print(f'maxflow is {maxFlow}')
                