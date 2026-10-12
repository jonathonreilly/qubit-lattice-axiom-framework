# R12-5 s1c: identify the aliased GF(2) h-character on a 2x2x2 block, and the extra GF(2) E-characters.
import numpy as np, itertools, sys, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from s1_alias import build, rank_Q
    from s1b_moments import nullspace_modp
names=['xx','yy','zz','2xy','2yz','2xz']
L=7; G,S,col,sid=build(L)
pts=[np.array((2,2,2))+np.array(d) for d in itertools.product(range(2),repeat=3)]
blk=[col(x,s) for x in pts for s in range(6)]
lab=[(tuple(x-2),names[s]) for x in pts for s in range(6)]
A=G[:,blk]; A=A[np.any(A!=0,axis=1)]
B=nullspace_modp(A,2)
for v in B:
    print("aliased h-char (mod 2):",[lab[i] for i in np.nonzero(v)[0]])
    w=np.zeros(G.shape[1],dtype=np.int64); w[blk]=v
    print("  integer syndrome G m: nonzero values",sorted(set((G@w).tolist())-{0}), " count",np.count_nonzero(G@w))
A=S[:,blk]; A=A[np.any(A!=0,axis=1)]
BQ=nullspace_modp(A,3)   # GF(3) == Q dims here (14)
B2=nullspace_modp(A,2)
# find GF(2) vectors not in span of integer-invariant ones reduced mod 2: check via rank
from s1_alias import rank_mod_p
import sympy as sp
M=sp.Matrix(A.tolist()); ns=M.nullspace()
NQ=np.array([[int(sp.fraction(sp.nsimplify(c))[0]*0+0) for c in v] for v in ns])  # placeholder
# integer basis of Q-nullspace: clear denominators
ints=[]
for v in ns:
    den=sp.ilcm(*[sp.fraction(c)[1] for c in v]); vi=[int(c*den) for c in v]; g=int(np.gcd.reduce(np.abs(vi))); ints.append([x//g for x in vi])
ints=np.array(ints)
print("Q-nullspace dim",len(ints),"; its mod-2 rank",rank_mod_p(ints%2,2),"; GF(2) nullspace dim",len(B2))
for v in B2:
    if rank_mod_p(np.vstack([ints%2,v]),2)>rank_mod_p(ints%2,2):
        print("extra GF(2) E-char:",[lab[i] for i in np.nonzero(v)[0]])
