from slideshow import slideshow
from graphviz import Graph

count=1

gv = Graph('G', filename='heading',format="png")
gv.node_attr.update(color='white', style='filled',fontsize="50")
gv.node("Reverse Delete Algorithm")
gv.render(str(count))
count+=1

gv = Graph('G', filename='Description',format="png")
gv.node_attr.update(color='white', style='filled',fontsize="25")
gv.edge("Start with graph G, which contains a list of edges E.","Go through E in decreasing order of edge weights.",color="white")
gv.edge("Go through E in decreasing order of edge weights.","For each edge, check if deleting the edge will further disconnect the graph.",color="white")
gv.edge("For each edge, check if deleting the edge will further disconnect the graph.","Perform any deletion that does not lead to additional disconnection.",color="white")
gv.render(str(count))
count+=1

gv = Graph('G', filename='Legend',format="png")
gv.node_attr.update(color='white', style='filled',fontsize="30")
gv.body.extend(['rankdir=LR', 'size="8,5"'])
gv.node("green",color="green")
gv.node("red",color="red")
gv.node("blue",color="blue")
gv.edge("Current edge:","green",color="green")
gv.edge("Deleted edge/Edge not in Spanning Tree:","red",color="red")
gv.edge("Edge present in Spanning Tree:","blue",color="blue")
gv.node('Legend:', shape='Mdiamond',color="yellow")
gv.render(str(count))
count+=1


gv = Graph('G', filename='rev_del',format='png')
gv.node_attr.update(color='lightblue2', style='filled')
gv.body.extend(['rankdir=LR'])

#input number of vertices n and edges m
n,m = map(int, raw_input("Enter the number of vertices and edges: ").split())

#Graph G
G = [[0 for x in range(n)] for x in range(n)]

weights=[]

for i in range(m):
  #input vertex number and weight of the edge
  u,v,d = map(int, raw_input().split())
  G[u-1][v-1]=G[v-1][u-1]=d
  weights.append(d)
  gv.edge(str(u),str(v),label=str(d))


gv.render(str(count))
count+=1

weights.sort(reverse=True)  #weights sorted in descending order

without_rep=[]

for x in weights:
  if x not in without_rep:
    without_rep.append(x)

A=[]
for i in range(len(without_rep)):
  for u in range(1,n+1):
    for v in range(u+1,n+1):
      if (G[u-1][v-1]==without_rep[i]):
        A.append([without_rep[i],u,v])
  
B=[]
for i in range(len(without_rep)):
  for u in range(1,n+1):
    for v in range(u+1,n+1):
      if (G[u-1][v-1]==without_rep[i]):
        B.append([without_rep[i],u,v])


def Connectivity(G,e,A,count,Y,N):  #checks connectivity of graph on removing edge e
  if A[0][0]==e:
    u=A[0][1]
    v=A[0][2]
    tup=A.pop(0)  
  index=len(B)-len(A)-1
  tup.append(index)
  G[u-1][v-1]=G[v-1][u-1]=0
  L=[]
  if path(G,u,v,u,L):
    N.append(tup)
    gv = Graph('G', filename='rev_del',format='png')
    gv.node_attr.update(color='lightblue2', style='filled')
    gv.body.extend(['rankdir=LR'])
    index=len(B)-len(A)-1
    for z in range(index+1,m):
      gv.edge(str(B[z][1]),str(B[z][2]),label=str(B[z][0]))
    for n in N: 
      gv.edge(str(B[n[3]][1]),str(B[n[3]][2]),label=str(B[n[3]][0]),color="red")
    for y in Y: 
      gv.edge(str(B[y[3]][1]),str(B[y[3]][2]),label=str(B[y[3]][0]),color="blue")
    gv.render(str(count))
    count+=1
    return count
  else:
    G[u-1][v-1]=G[v-1][u-1]=e
    Y.append(tup)
    gv = Graph('G', filename='rev_del',format='png')
    gv.node_attr.update(color='lightblue2', style='filled')
    gv.body.extend(['rankdir=LR'])
    index=len(B)-len(A)-1
    for z in range(index+1,m):
      gv.edge(str(B[z][1]),str(B[z][2]),label=str(B[z][0]))
    for n in N: 
      gv.edge(str(B[n[3]][1]),str(B[n[3]][2]),label=str(B[n[3]][0]),color="red")
    for y in Y: 
      gv.edge(str(B[y[3]][1]),str(B[y[3]][2]),label=str(B[y[3]][0]),color="blue")
    gv.render(str(count))
    count+=1
    return count

def path(g,u,v,p,L):
  L.append(p)
  if u==v :
    return True
  neighbors=[]
  for j in range(1,n+1):
    if g[u-1][j-1] !=0 and j not in L:
      neighbors.append(j)  
  
  if len(neighbors)==0:
    return False

  for x in neighbors :
    if path(g,x,v,u,L) == True:
      return True
  return False  

def rev_del(G,weights,count,Y,N):
  for i in range(m):
    gv = Graph('G', filename='rev_del',format='png')
    gv.node_attr.update(color='lightblue2', style='filled')
    gv.body.extend(['rankdir=LR'])
    for j in range(i+1,m):
      gv.edge(str(B[j][1]),str(B[j][2]),label=str(B[j][0]))
    for n in N: 
      gv.edge(str(B[n[3]][1]),str(B[n[3]][2]),label=str(B[n[3]][0]),color="red")
    for y in Y: 
      gv.edge(str(B[y[3]][1]),str(B[y[3]][2]),label=str(B[y[3]][0]),color="blue")
    gv.edge(str(B[i][1]),str(B[i][2]),label=str(B[i][0]),color="green")
    gv.render(str(count))
    count+=1
    count=Connectivity(G,weights[i],A,count,Y,N)
  return count
Y=[]
N=[]  
count=rev_del(G,weights,count,Y,N)
for w in G:
  print w

image_files = []
for i in range(1,count):
  s=str(i)+'.png'
  image_files.append(s)

slideshow(image_files)
