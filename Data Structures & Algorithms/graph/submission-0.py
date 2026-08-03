class Graph:

    def __init__(self):
        # adj[vertex] = set of vertices that 'vertex' points to.
        # Using a set means duplicate edges are impossible automatically.
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        # Make sure both vertices exist, then draw the arrow src → dst.
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        # If the arrow src → dst exists, erase it and report True.
        # If either vertex or the edge is missing, report False.
        if src in self.adj and dst in self.adj[src]:
            self.adj[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        # Walk the arrows from src using DFS, remembering where we've been,
        # and see if we can ever reach dst.
        visited = set()

        def dfs(node):
            if node == dst:
                return True
            visited.add(node)
            for neighbor in self.adj.get(node, set()):
                if neighbor not in visited and dfs(neighbor):
                    return True
            return False

        return dfs(src)