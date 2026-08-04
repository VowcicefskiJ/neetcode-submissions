class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        leader_x = self.find(x)
        leader_y = self.find(y)
        
        if leader_x == leader_y:
            return False
        
        if self.size[leader_x] < self.size[leader_y]:
            self.parent[leader_x] = leader_y
            self.size[leader_y] += self.size[leader_x]
        else:
            self.parent[leader_y] = leader_x
            self.size[leader_x] += self.size[leader_y]
        
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components