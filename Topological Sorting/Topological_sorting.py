class graph():
    def __init__(self):
        self.graph = {}
        self.vertices = []
    def Addnode(self,u,v):
        if u not in self.vertices:
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)

        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

        
    def print_graph(self):
        for v in self.graph:
            for node in self.graph[v]:
                print(v,"-->",node)
    

    def Visit(self,node,nodes_colore,nodes_vtime,nodes_ftime ,time,T_sort):
        print('nodes colore', nodes_colore)
        print('node visit time', nodes_vtime)
        print("node: ", node)
        print('time:' ,time)
        print('\n\n')
        
        time += 1
        nodes_colore[node] = 'grey'
        nodes_vtime[node] = time

        # print(self.graph[node])

        for child in self.graph[node]:
            print('self.graph[node]',self.graph[node])
            if nodes_colore[child] == 'white':
                time = self.Visit(child,nodes_colore,nodes_vtime,nodes_ftime,time,T_sort)

        T_sort.insert(0,node)
        print("T_sort: ",T_sort)
        print('node visit time', nodes_vtime)
        time += 1
        nodes_colore[node] = 'black'
        nodes_ftime[node] = time
        print('node finish time', nodes_ftime)
        print('nodes colore', nodes_colore)
        print('\n\n')

        return time 
        


    def DFS(self):

        # creat an array to save nodes colore.
        nodes_colore = []
        nodes_vtime = []
        nodes_ftime = []
        T_sort = []

        print('self.vertices',self.vertices)

        # set all the nodes colore to white.
        for n in range(1,len(self.vertices)+2):
            nodes_colore.append('white')
            nodes_vtime.append(999)
            nodes_ftime.append(999)
    
        time = 0

        # call the visit function for each vertice in graph
        for v in range(1,len(self.graph)):
            if nodes_colore[v] == 'white':
                self.Visit(v, nodes_colore,nodes_vtime,nodes_ftime,time,T_sort)
        
        
    
G = graph()

# G.Addnode(0,1)
# G.Addnode(0,2)
# G.Addnode(2,0)
G.Addnode(1,2)
G.Addnode(2,3)
G.Addnode(3,3)
G.Addnode(4,5)
G.Addnode(4,6)
G.Addnode(5,8)
G.Addnode(6,7)
G.Addnode(8,9)
G.Addnode(7,10)
G.Addnode(9,9)
G.Addnode(10,10)


G.print_graph()

G.DFS()