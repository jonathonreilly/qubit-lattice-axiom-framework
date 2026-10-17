import itertools, collections
from ilib import *
ROTS=rotations()
ORD=list(itertools.permutations(range(6)))
def base(model,o):
    v0=(0,0,0)
    return [model.B(v0)]+model.gens_extra(v0)+[S(model,o,v0,a,b) for (a,b) in PLANES]
o=ORD[0]
for L in (4,5,6,8):
    for Mod in (HalfModel(L),EdgeModel(L)):
        sp=span_of(Mod,generators(Mod,o))
        st=[rot_type(M) for M in ROTS if all(sp.eig(permute_pauli(P,Mod.rot_qubit_perm(M))) is not None for P in base(Mod,o))]
        print(L, type(Mod).__name__, Mod.n-sp.rank(), st)
