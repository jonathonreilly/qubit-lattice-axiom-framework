# R12-5 s1: exact Z_N algebra of the 09-14 N-type clock complex on L^3 tori.
# Which X1 hypothesis does an unblocked qubit (N=2) code violate?  Lifting (N > 36 M).
# Stencils copied from docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_..._2026-09-14.md:95-101.
# Slots per site x: q = (h_xx,h_yy,h_zz, 2h_xy, 2h_yz, 2h_xz) [off-diag on faces], p = (E_xx,..,E_xy,E_yz,E_xz).
# Stabilizers: X^(G row) (functions of p=E), Z^(S row) (functions of q=h, shift p).  X^r Z^s = w^(r.s) Z^s X^r.
#  E-character X^r is invariant  <=>  S r = 0 mod N ;  h-character Z^m invariant <=> G m = 0 mod N.
import numpy as np, itertools, sys
from fractions import Fraction
import sympy as sp

OFF = {(0,1):3,(1,2):4,(0,2):5}
def offslot(i,j): return OFF[(min(i,j),max(i,j))]
def build(L):
    V=L**3; n=6*V
    def sid(x): return ((x[0]%L)*L+(x[1]%L))*L+(x[2]%L)
    def col(x,s): return 6*sid(x)+s
    E=np.eye(3,dtype=int)
    G=np.zeros((3*V,n),dtype=np.int64); S=np.zeros((V,n),dtype=np.int64)
    for x in itertools.product(range(L),repeat=3):
        x=np.array(x)
        for j in range(3):
            r=3*sid(x)+j
            G[r,col(x+E[j],j)]+=1; G[r,col(x,j)]-=1
            for i in range(3):
                if i==j: continue
                G[r,col(x,offslot(i,j))]+=1; G[r,col(x-E[i],offslot(i,j))]-=1
        r=sid(x)
        for j in range(3):
            for i in range(3):
                if i==j: continue
                S[r,col(x+E[i],j)]+=1; S[r,col(x-E[i],j)]+=1; S[r,col(x,j)]-=2
        for (i,j) in [(0,1),(1,2),(0,2)]:
            s=offslot(i,j)
            S[r,col(x,s)]-=1; S[r,col(x-E[i],s)]+=1; S[r,col(x-E[j],s)]+=1; S[r,col(x-E[i]-E[j],s)]-=1
    return G,S,col,sid

def rank_mod_p(A,p):
    A=np.array(A,dtype=np.int64)%p; m,n=A.shape; r=0
    for c in range(n):
        piv=None
        for i in range(r,m):
            if A[i,c]%p: piv=i;break
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]
        inv=pow(int(A[r,c]),p-2,p); A[r]=(A[r]*inv)%p
        nz=np.nonzero(A[:,c])[0]
        for i in nz:
            if i!=r: A[i]=(A[i]-A[i,c]*A[r])%p
        r+=1
        if r==m: break
    return r
def rank_Q(A): return np.linalg.matrix_rank(A.astype(float))

out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); sys.stdout.flush(); out.append(s)

P("== 1. integer identity G S^T = 0 and code counts (CSS: k = n - rank G - rank S) ==")
for L in [3,4,5]:
    G,S,col,sid=build(L); n=G.shape[1]; V=L**3
    gs=np.abs(G@S.T).max()
    rQ=(rank_Q(G),rank_Q(S))
    line=f"L={L}: n={n} slots, max|G S^T|={gs}, ranks over Q: G {rQ[0]}, S {rQ[1]} -> physical pairs over Q = {n-rQ[0]-rQ[1]} = 2V + {n-rQ[0]-rQ[1]-2*V}"
    for p in [2,3,5,7]:
        rg,rs=rank_mod_p(G,p),rank_mod_p(S,p); k=n-rg-rs
        line+=f"\n      N={p}: rank G {rg}, rank S {rs}, logical qudits k = {k} = 2V + {k-2*V}"
    P(line)
    P(f"      max |row coeff| G={np.abs(G).max()} (l1 {np.abs(G).sum(1).max()}), S={np.abs(S).max()} (l1 {np.abs(S).sum(1).max()})")

P("\n== 2. single-site invariant characters: integer (lifted) vs mod N (aliased) ==")
L=5; G,S,col,sid=build(L); x0=(2,2,2)
cols=[col(np.array(x0),s) for s in range(6)]
Ssub=S[:,cols]; Gsub=G[:,cols]
Ssub=Ssub[np.any(Ssub!=0,axis=1)]; Gsub=Gsub[np.any(Gsub!=0,axis=1)]
P("integer nullspace dims: E-side (S r=0):",6-rank_Q(Ssub)," h-side (G m=0):",6-rank_Q(Gsub))
names=['xx','yy','zz','xy','yz','xz']
for N in [2,3,4,5,6,8,12]:
    solsE=[r for r in itertools.product(range(N),repeat=6) if any(r) and not np.any((Ssub@np.array(r))%N)]
    solsH=[m for m in itertools.product(range(N),repeat=6) if any(m) and not np.any((Gsub@np.array(m))%N)]
    P(f"N={N:2d}: # nonzero single-site E-characters with S r=0 mod N: {len(solsE)};  h-characters with G m=0 mod N: {len(solsH)}")
    for r in solsE[:4]:
        P(f"      E example r={dict((names[i],r[i]) for i in range(6) if r[i])}  integer syndrome S r (nonzero entries) = {sorted(set((Ssub@np.array(r)).tolist())-{0})}")
    for m in solsH[:3]:
        P(f"      h example m={dict((names[i],m[i]) for i in range(6) if m[i])}  integer syndrome G m (nonzero) = {sorted(set((Gsub@np.array(m)).tolist())-{0})}")

P("\n== 3. invariant characters on a 2x2x2 block (48 slots): dim over Q vs GF(p) ==")
blk=[col(np.array(x0)+np.array(d),s) for d in itertools.product(range(2),repeat=3) for s in range(6)]
for nm,A in [('E-side S r=0',S[:,blk]),('h-side G m=0',G[:,blk])]:
    A=A[np.any(A!=0,axis=1)]
    line=f"{nm}: dim over Q = {48-rank_Q(A)}"
    for p in [2,3,5,7,37]: line+=f", GF({p}) = {48-rank_mod_p(A,p)}"
    P(line)

P("\n== 4. zeroth moments of aliased E-characters (09-14:227-237 says every lifted invariant E-character has zero zeroth moment) ==")
# r = trace at one site, N=2: zeroth moment = (1,1,1,0,0,0) != 0 ; it is TT-blind (trace).  Search traceless-moment aliased chars on 2x2x2 block mod 2
A=S[:,blk]; A=A[np.any(A!=0,axis=1)]%2
# nullspace mod 2 basis
def nullspace_mod2(A):
    A=A.copy()%2; m,n=A.shape; piv=[]; r=0
    for c in range(n):
        rows=[i for i in range(r,m) if A[i,c]]
        if not rows: continue
        A[[r,rows[0]]]=A[[rows[0],r]]
        for i in range(m):
            if i!=r and A[i,c]: A[i]=(A[i]+A[r])%2
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]; B=[]
    for f in free:
        v=np.zeros(n,dtype=int); v[f]=1
        for i,c in enumerate(piv): v[c]=A[i,f]%2
        B.append(v)
    return np.array(B)
B=nullspace_mod2(A)
mom=np.array([[v[[k for k in range(48) if k%6==s]].sum()%2 for s in range(6)] for v in B])
P(f"GF(2) invariant E-characters on block: basis size {len(B)}; span of their zeroth moments (mod 2) has rank {rank_mod_p(mom,2)}; moment vectors include:",
  sorted(set(tuple(x) for x in mom.tolist()))[:8])
open(__file__.replace('.py','.out'),'w').write('\n'.join(out)+'\n')
