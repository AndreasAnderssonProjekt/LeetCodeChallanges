def canFinish(self, numCourses, prerequisites):
        G = courseGraph(numCourses,prerequisites)
        return topologicalSort(G)
        
        
def topologicalSort(G):
    visited = [0] * len(G)

    for n in G.keys():
        if not sortUtil(n,visited,G):
            return False
    return True

def sortUtil(n,visited,G):
    if visited[n] == -1:
        return False

    if visited[n] == 1:
        return True

    visited[n] = -1
    for m in G[n]:
        if not sortUtil(m,visited,G):
            return False
        
    visited[n] = 1
    return True


def courseGraph(numcourses,prerequisites):
    G = {}
    for c in range(numcourses):
        G[c] = []
        
    for p in prerequisites:
        G[p[1]].append(p[0])
        
    return G
