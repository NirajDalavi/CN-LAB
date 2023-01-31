class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printSol(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))


    def BellmanFord(self, src):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        self.printSol(dist)


# Driver's code
if __name__ == '__main__':
    v=int(input("Enter the number of vertices: "))
    e=int(input("Enter the number of edges: "))
    print("Enter the src dest & weight of the edges:")
    g = Graph(v)
    i=0
    while i < e:
        s,d,w=map(int,input().split())
        if s > v-1 or s < 0 or d > v-1 or d < 0:
            print("Invalid edge. Enter again.")
            i-=1
        else:
            g.addEdge(s, d, w)
        i+=1          
    src=int(input('Enter Source vertex: '))
    flag = False
    while flag == False:
        if src > v-1 or src < 0:
            src=int(input('Invalid Source vertex Enter again! : '))
        else:
            flag = True    

    # function call
    g.BellmanFord(src)
