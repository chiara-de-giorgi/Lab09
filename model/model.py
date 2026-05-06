import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._aeroporti=DAO.getAllAeroporti()
        self._grafo=nx.Graph()
        self._idMap={}
        for a in self._aeroporti:
            self._idMap[a.ID]=a

    def buildGraph(self, x):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._aeroporti)
        edges=DAO.getAllEdgesPesati(self._idMap, x)

        for u, v, dist in edges:
                self._grafo.add_edge(u, v, weight=dist)



    def getNumNodes(self):
       return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getEdgesPesati(self):
        return self._grafo.edges(data=True)