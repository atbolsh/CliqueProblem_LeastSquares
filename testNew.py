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


G = getGraph(b200_4, N200_4)
#We add the main diagonal (that's really it).
H2 = graphToH(G)

x = np.ones(N200_4)/np.sqrt(N200_4)
#No idea why; fractional exponents work better
#Something about how the value is computed.
y = seek2(x, H2, 2.3, 1e-8)
R = biggestClique(ReLu(y), G)
print R
print len(R)
print verifyClique(R, G)

