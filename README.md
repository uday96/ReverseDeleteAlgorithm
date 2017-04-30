#**Reverse-Delete Algorithm**

The **Reverse-Delete Algorithm** is an algorithm in graph theory used to obtain a **minimum spanning tree** from a given connected, edge-weighted graph.

The algorithm works as follows:

    Start with graph G, which contains a list of edges E.
    Go through E in decreasing order of edge weights.
    For each edge, check if deleting the edge will further disconnect the graph.
    Perform any deletion that does not lead to additional disconnection.


---------------------------
**Legend:**
---------------------------
For graphical visualisation, the edges are denoted with colours.
**Green Color:** Current edge / the edge E which is passed as parameter as in 1 of pseudo code
**Red Color:** Deleted edge/ Edge not part of the MIN Spanning Tree								
**Blue Color:** Edge present in the MIN Spanning Tree/ line 8 of pseudo code				

---------------------------
**Pseudo Code:**
---------------------------
    1  function ReverseDelete(edges[] E)
	2    sort E in decreasing order
	3    Define an index i ← 0
	4    while i < size(E)
	5       Define edge ← E[i]
	6         delete E[i]
	7         if edge.v1 is not connected to edge.v2
	8             E[i] ← edge
	9         i ← i + 1
	10   return edges[] E
 

In the above the graph is the set of edges E with each edge containing a weight and connected vertices v1 and v2.


---------------------------
**Proof of correctness:**
---------------------------

The remaining sub-graph (g) produced by the algorithm is not disconnected since the algorithm checks for that in line 7.
So at every stage, our graph is connected and hence there is a spanning tree.
We traverse through edges in the descending order of their weights, hence the final spanning tree obtained is a MIN Spanning Tree.