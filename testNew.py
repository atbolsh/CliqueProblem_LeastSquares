from LevMaq import *
from graphReader import *
from BigC import biggestClique
from BigC import verifyClique

#First, a simplistic test.
G = np.array(
[[0, 1, 1, 0, 0],
[1, 0, 1, 0, 1],
[1, 1, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 0, 0]])

H = graphToH(G)
start = np.array([1, 0, 0, 0, 0])
x = seek(start, H, 3, 2, 1e-6)


print x 


G = getGraph(c125_9, N125_9)
#We add the main diagonal (that's really it).
H2 = graphToH(G)

x = np.ones(N125_9)/np.sqrt(N125_9) 
y = seek(x, H2, 36, 4, 1e-8)
R = biggestClique(ReLu(y), G)
print R
print len(R)
print verifyClique(R, G)

