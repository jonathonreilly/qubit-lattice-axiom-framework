# S4: which lattice elements give the TM1 column; is C3 the only charged-lepton residual that does?
import itertools, numpy as np
rng=np.random.default_rng(3)
def el(p,s):
    M=np.zeros((3,3))
    for i in range(3): M[p[i],i]=s[i]
    return M
B3=[(p,s,el(p,s)) for p in itertools.permutations(range(3)) for s in itertools.product([1,-1],repeat=3)]
def basis(g):
    C=g+0.37*g@g; w,V=np.linalg.eig(C+1e-3*np.diag([0,0,0]))
    w,V=np.linalg.eig(g)
    if min(abs(w[i]-w[j]) for i in range(3) for j in range(i+1,3))<1e-6: return None
    return V/np.linalg.norm(V,axis=0)
def uvec(g):
    w,V=np.linalg.eig(g); w=np.round(w,8); vals,c=np.unique(w,return_counts=True)
    if len(vals)==2 and min(c)==1: v=V[:,list(w).index(vals[c==1][0])]; return v/np.linalg.norm(v)
tm1=np.array(sorted([1/6,1/6,2/3]))
hits={}
for pl,sl,gl in B3:
    B=basis(gl)
    if B is None: continue
    for pn,sn,gn in B3:
        if not np.allclose(gn@gn,np.eye(3)) or np.allclose(gn,gn[0,0]*np.eye(3)): continue
        v=uvec(gn)
        if v is None: continue
        col=np.sort(np.abs(B.conj().T@v)**2)
        if np.allclose(col,tm1,atol=1e-9):
            order=next(k for k in range(1,13) if np.allclose(np.linalg.matrix_power(gl,k),np.eye(3)))
            hits.setdefault(('Dirac order',order,'perm cycle type',len(set(pl))-sum(pl[i]==i for i in range(3))),set()).add((pn,sn))
for k,v in hits.items(): print(k,"-> Z2 elements (perm,signs):",sorted(v)[:6],"... total",len(v))
