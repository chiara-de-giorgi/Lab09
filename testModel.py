from model.model import Model

mdl=Model()
mdl.buildGraph(500)
print(f"Il grafo creato contiene {mdl.getNumNodes()} nodi e {mdl.getNumEdges()} archi")