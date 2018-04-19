from LevMaqGeo import *
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
start = np.array([1, 1, 1, 1, 1])
x = seek2(start, H, 6, 1e-6)


print x 


G = getGraph(c250_9, N250_9)
#We add the main diagonal (that's really it).
H2 = graphToH(G)

x = np.ones(N250_9)/np.sqrt(N250_9)
#No idea why; fractional exponents work better
#Something about how the value is computed.
y = seek2(x, H2, 3.5, 1e-8)
R = biggestClique(np.fabs(y), G)
print R
print len(R)
print verifyClique(R, G)

