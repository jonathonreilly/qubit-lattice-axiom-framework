import itertools, collections
from ilib import *
ROTS=rotations()
ORD=list(itertools.permutations(range(6)))
o=ORD[0]; L=6
H=HalfModel(L); g=generators(H,o)
M=((-1, 0, 0), (0, 0, 1), (0, 1, 0))
perm=H.rot_qubit_perm(M)
inv=[0]*H.n
for i,p in enumerate(perm): inv[p]=i
v=(1,2,3); a=0
A=H.A(o,v,a)
print('A anti', [i for i,G in enumerate(g) if not commute(A,G)])
P=permute_pauli(A,perm)
fl=[i for i,G in enumerate(g) if not commute(P,G)]
print('PAP anti', fl)
for i in fl:
    pre=permute_pauli(g[i],inv)
    print(i, 'preimage anticommutes with A:', not commute(A,pre), 'preimage in span:', span_of(H,g).eig(pre))
