from collections import defaultdict
inf = 10000
order = []
error = -1
class Graph:
    def __init__(self, input_array):
        self.graph = defaultdict(list)
        for k in input_array:
            self.graph[k[0]].append((k[2], k[1]))
            self.graph[k[1]].append((k[2], k[0]))

    def dijkstra(self, start, end):
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
           # if(c_n == end):
            #    break 
        if d[end][0] == inf:
            return error
        return d[end][0]

def get_values(Graph):
    print("Enter N: ")
    end = input()
    if(end < 0)or(end > 100):
        print ("invalide input")
        return error
    print("Enter X: ")
    start = input()
    if(start < 1)or(start > end):
        print ("invalide input")
        return error
    result = Graph.dijkstra(start, end)
    return result

 
times =  [[2,1,1],[2,3,1],[3,4,1]]
t = Graph(times)
print (get_values(t))
