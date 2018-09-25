from collections import defaultdict
from heapq import *
#funçao que inicia o algoritmo
def dijkstra(arestas, f, t):
    g = defaultdict(list)#lista de prioridades
    for l,r,c in arestas:
        g[l].append((c,r))

    q, visita, mins = [(0,f,())], set(), {f: 0}#inicializado o grafo com data set
    while q:#enquanto a fila nao estiver vazia.
        (cost,v1,caminho) = heappop(q)##ExtractMin(Q)
        if v1 not in visita:#se v1 estiver sido visitado
            visita.add(v1)
            caminho = (v1, caminho)
            if v1 == t: return (cost, caminho)

            for c, v2 in g.get(v1, ()):
                if v2 in visita: continue#verificaçao para o vertice repetido.
                predecessor = mins.get(v2, None)#retirando da fila
                proximo = cost + c
                if predecessor is None or proximo < predecessor:#para cada vizinho de v
                    mins[v2] = proximo
                    heappush(q, (proximo, v2, caminho))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print ("=== Dijkstra ===")
    print (edges)
    print ("A -> E:")
    print (dijkstra(edges, "A", "E"))
    print ("F -> G:")
    print (dijkstra(edges, "F", "G"))

    # Codigo desenvolvido com carinho e noites de sono perdidas por:
    # José de Sousa Magalhaes
    # Acadêmico do curso de Sistemas de Informaçao da UFPI.