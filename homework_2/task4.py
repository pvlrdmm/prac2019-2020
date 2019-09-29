next = 0
order_of_visit_dfs = []
order_of_visit_bfs = []
class Graph:
    def __init__(self, input_inf):
        self.adj_list = []
        i = 0
        while i < len(input_inf):
            while len(self.adj_list) <= input_inf[i][0]:
                self.adj_list.append([])
            while len(self.adj_list) <= input_inf[i][1]:
                self.adj_list.append([])
            self.adj_list[input_inf[i][0]].append(input_inf[i][1])
            self.adj_list[input_inf[i][1]].append(input_inf[i][0])
            i += 1
        self.r = len (self.adj_list)
    
    def get_number_of_v (self):
        ver = []
        for i in range(0, self.r):
             for k in  self.adj_list[i]:
                  if k not in ver:
                     ver.append(k)
        self.v = len(ver)
        self.visited = [False]*self.v
        self.level = [1]*self.v

    def dfs(self, start):
        self.visited[start]=True
        order_of_visit_dfs.append(start)
        for next in self.adj_list[start]:
            if(not self.visited[next]):
                    self.dfs(next)

    def bfs(self, start):
        self.level[start] = 0
        queue = [start]
        while queue:
            current = queue.pop(0)
            order_of_visit_bfs.append(current)
            for w in self.adj_list[current]:
                if self.level[w] is 1:
                    queue.append(w)
                    self.level[w] = self.level[current] - 1
             
        
adj_list =  [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

g = Graph (adj_list)
g.get_number_of_v()
g.dfs(0)
g.bfs(0)

print(order_of_visit_dfs)
print(order_of_visit_bfs)

