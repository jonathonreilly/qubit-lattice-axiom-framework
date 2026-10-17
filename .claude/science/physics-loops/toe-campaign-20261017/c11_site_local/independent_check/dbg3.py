import itertools, collections
from ilib import *
ROTS=rotations()
ORD=list(itertools.permutations(range(6)))
o=ORD[0]; L=6
H=HalfModel(L); g=generators(H,o)
for M in ROTS:
    if rot_type(M)!='C2edge': continue
    perm=H.rot_qubit_perm(M)
    assert sorted(perm)==list(range(H.n))
    bad=0
    for v in H.lat.verts():
        for a in range(3):
            P=permute_pauli(H.A(o,v,a),perm)
            fl=[i for i,G in enumerate(g) if not commute(P,G)]
            if len(fl)!=2: bad+=1
    gimg=[permute_pauli(G,perm) for G in g]
    sp=span_of(H,g)
    print(M, 'bad rotated hops', bad, 'gens images in span', sum(sp.eig(G) is not None for G in gimg), len(g))
