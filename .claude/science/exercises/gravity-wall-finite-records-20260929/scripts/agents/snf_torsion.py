# Torsion of the landed tensor stencils G (vector rule) and S (scalar rule):
# do Z_N clock "aliases" (G m = 0 mod N, G m != 0) reduce to lifted kernel
# characters as operators (m = k + N u with G k = 0)?  They do iff coker G has
# no N-torsion, i.e. all Smith invariant factors are 1 (or coprime to N).
import itertools, numpy as np, sys
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
pairs=[(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
def incidence(L, periodic=True):
    sites=list(itertools.product(range(L),repeat=3)); ids={x:i for i,x in enumerate(sites)}; n=len(sites)
    def sid(x):
        if periodic: return ids[tuple(int(a)%L for a in x)]
        t=tuple(int(a) for a in x); return ids.get(t,None)
    def col(x,a):
        s=sid(x); return None if s is None else 6*s+a
    G=np.zeros((3*n,6*n),dtype=int); S=np.zeros((n,6*n),dtype=int); unit=np.eye(3,dtype=int)
    for s,site in enumerate(sites):
        v=np.array(site)
        for j in range(3):
            row=3*s+j
            for (x,a,c) in [(v+unit[j],j,1),(v,j,-1)]:
                cc=col(x,a)
                if cc is not None: G[row,cc]+=c
            for i in range(3):
                if i==j: continue
                a=pairs.index(tuple(sorted((i,j))))
                for (x,aa,c) in [(v,a,1),(v-unit[i],a,-1)]:
                    cc=col(x,aa)
                    if cc is not None: G[row,cc]+=c
                for (x,aa,c) in [(v+unit[i],j,1),(v-unit[i],j,1),(v,j,-2)]:
                    cc=col(x,aa)
                    if cc is not None: S[s,cc]+=c
        for a,(i,j) in enumerate(pairs[3:],3):
            for (x,aa,c) in [(v,a,-1),(v-unit[i],a,1),(v-unit[j],a,1),(v-unit[i]-unit[j],a,-1)]:
                cc=col(x,aa)
                if cc is not None: S[s,cc]+=c
    return G,S
def invariant_factors(M):
    D=smith_normal_form(Matrix(M.tolist()),domain=ZZ)
    d=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]!=0]
    return sorted(set(d)), len(d)
for L,per in [(2,True),(3,True),(3,False),(4,True)]:
    G,S=incidence(L,per)
    fG,rG=invariant_factors(G); fS,rS=invariant_factors(S)
    print(f"L={L} periodic={per}: G shape {G.shape} rank {rG} invariant factors {fG};  S shape {S.shape} rank {rS} invariant factors {fS}")
    sys.stdout.flush()
