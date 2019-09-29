'''
Was used algorithm Dijkstra to find the shortest way from start node to end node
'''

from collections import defaultdict
error = "error"
inf = 10000
order = []
tmp = 0

class Graph:
    def __init__(self, input_array):
        self.graph = defaultdict(list)
        for k in input_array:
            self.graph[k[0]].append((k[2], k[1]))
            self.graph[k[1]].append((k[2], k[0]))

    def dijkstra(self, start, end):
        order.append(start)
        c_n = start
        d = [(inf, i) for i in range(6)]
        d[c_n] = (0, c_n)
        next_ = set(d)
        n = 0
        while next_:
            m_n = min(next_)
            c_w, c_n = m_n
            next_.remove(m_n)
            for w, n in self.graph[c_n]: 
                tmp = c_w
                if w + c_w < d[n][0]:
                    next_.remove(d[n])
                    d[n] = (w + c_w, n)
                    next_.add(d[n])
                    if(d[n-1][0] == tmp):
                        order.append(d[n-1][1])
            if(c_n == end):
                if not order[-1] == end:
                    order.append(end)
                print("order:",order)
                break 
        if d[end][0] == inf:
            return error
        return d[end][0]

def get_values(Graph):
    print("Enter start node: ")
    start = input()
    print("Enter end node: ")
    end = input()
    if start or end > 5:
        print ("invalide input")
    else:
        result = Graph.dijkstra(start, end)
    return result

arr = [[0, 3, 5], [1, 3, 11], [2, 3, 56], [4, 3, 77], [5, 4, 89]]
g = Graph(arr)
print ("weigth:",get_values(g))
