# creating a class for graph and it's calculation's.
class graph():
    # set the self.graph to a dictionary.
    def __init__(self):
        self.graph = {}
    
    # create a function to add node'to the graph
    def addnode(self,u,v):
        # chek if the node is already in the graph or
        # not and if it is then add it to the graph.
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    #  funcion to print the graph.
    def print_graph(self):
        for node in self.graph:
            print(node,'-->',self.graph[node])
    
    # the main function to this programm that will
    # visit all the node's(you read tent's) and 
    # find their maximum size of soldier in them.
    def visit(self, visited, root, soldiers):
        # set the id to the current root and
        # it will finally find the max id of
        # the soldires in the node's.
        id = root

        death = soldiers[root]
        injured = 0

        # creat an stack to push and pull the
        # chiledren of the current node.
        stack = [root]

        # set the current node visiting state
        # to true.
        visited[root] = True

        # this loop will visit all the node's
        # till all the node's have been visited.
        while stack:
            # pop node's in k one by one in the k.
            k = stack.pop()

            # add this try so if there wasn't a
            # key in the self.graph it won't make
            # any problems.
            try:
                for i in self.graph[k]:
                    # visit all the node's children
                    # if their not visited before.
                    if visited[i] is False:
                        visited[i] = True

                        # push the node's children
                        # in to the stack.
                        stack.append(i)
                        
                        # chek if the soldire inside the current node(tent)
                        # is the maximum, and if it is then set id to it's
                        # index.
                        if (id > i and soldiers[i] >= death) or soldiers[i] > death:
                            id = i

                            # put last max death to injuries and replace
                            # death to current maximum death number.
                            injured += death
                            death = soldiers[i]
                        else:
                            # if it's not bigger than current death number
                            # then just add it's soldier number to injures.
                            injured += soldiers[i]
            except:
                pass
        
        return id + 1, death, injured


    # create a funcion to prepare and call the
    # visit funtion for DFS.
    def dfs(self, N, army):
        
        # creat a visit array to save visited node's
        visited = [False] * (N + 1)
        injured = death = 0
        id = []

        # visit all nodes that's aren't visited yet.
        for i in range(N):
            if visited[i] is False:

                # get index, death and injuries from
                #  the dfs function.
                idx, d, j = self.visit(visited, i, army)

                id.append(idx)
                death += d
                injured += j
        
        # srot the tent index for printing.
        id.sort()
        return id , death , injured


# create an object of graph class.
G = graph()

# get n and m input.
nm = input()
n = int(nm.split()[0])
m = int(nm.split()[1])

# get the soldiers number.
army = []
raw_army = input()
raw_army = raw_army.split()
for c in raw_army:
    army.append(int(c))

# add nodes connection to the graph.
for i in range(m):
    node1_2 = input()
    node1 = int(node1_2.split()[0])
    node2 = int(node1_2.split()[1])

    G.addnode(node1-1,node2-1)
    G.addnode(node2-1,node1-1)

# call the dfs funcion to get the answers.
DFS_ANS = G.dfs(n, army)
tent_on_fire = DFS_ANS[0]
death = DFS_ANS[1]
injured = DFS_ANS[2]

# print the final answers.
print(death, injured)
for tent in tent_on_fire:
    print(tent,end=' ')
    