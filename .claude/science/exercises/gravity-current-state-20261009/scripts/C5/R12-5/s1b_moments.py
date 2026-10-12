# R12-5 s1b: moments of aliased (mod-2 / mod-3) invariant characters on 3x3x3 blocks of an L=7 torus.
# Lifted theorem (09-14:227-249): invariant E-char has zero 0th moment; invariant h-char has zero 0th and 1st moments.
# Question: does aliasing at N=2 supply an invariant character with a TRACELESS 0th moment (E side) or nonzero 0th/1st moment (h side)?
import numpy as np, itertools, sys
sys.path.insert(0,'.')
from s1_alias import build, rank_mod_p, rank_Q
out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
def nullspace_modp(A,p):
    A=A.copy()%p; m,n=A.shape; piv=[]; r=0
    for c in range(n):
        rows=[i for i in range(r,m) if A[i,c]%p]
        if not rows: continue
        A[[r,rows[0]]]=A[[rows[0],r]]; A[r]=(A[r]*pow(int(A[r,c]),p-2,p))%p
        for i in range(m):
            if i!=r and A[i,c]: A[i]=(A[i]-A[i,c]*A[r])%p
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]; B=[]
    for f in free:
        v=np.zeros(n,dtype=np.int64); v[f]=1
        for i,c in enumerate(piv): v[c]=(-A[i,f])%p
        B.append(v)
    return np.array(B)
L=7; G,S,col,sid=build(L)
for b in [2,3]:
    pts=[np.array((2,2,2))+np.array(d) for d in itertools.product(range(b),repeat=3)]
    blk=[col(x,s) for x in pts for s in range(6)]; n=len(blk)
    pos=np.array([x for x in pts for s in range(6)],dtype=float); slot=np.array([s for x in pts for s in range(6)])
    for nm,A in [('E',S[:,blk]),('h',G[:,blk])]:
        A=A[np.any(A!=0,axis=1)]
        dQ=n-rank_Q(A)
        for p in [2,3]:
            B=nullspace_modp(A,p)
            m0=np.array([[v[slot==s].sum()%p for s in range(6)] for v in B]) if len(B) else np.zeros((0,6),int)
            r0=rank_mod_p(m0,p) if len(B) else 0
            msg=f"block {b}^3, {nm}-side, GF({p}): dim {len(B)} (Q: {dQ}); rank of 0th moments mod {p}: {r0}"
            if nm=='E' and len(B):
                tl=[t for t in set(map(tuple,m0.tolist())) if any(t) and not (t[0]==t[1]==t[2] and t[3]==t[4]==t[5]==0)]
                msg+=f"; non-trace 0th moments present: {len(tl)>0}"
            if nm=='h' and len(B):
                # 1st moments mod p (integer positions): sum v * x_a per slot
                m1=np.array([[ (v[slot==s]*pos[slot==s,a]).sum()%p for s in range(6) for a in range(3)] for v in B]).astype(np.int64)
                msg+=f"; rank of (0th,1st) moments mod {p}: {rank_mod_p(np.hstack([m0,m1]),p)}"
            P(msg)
open(__file__.replace('.py','.out'),'w').write('\n'.join(out)+'\n')
