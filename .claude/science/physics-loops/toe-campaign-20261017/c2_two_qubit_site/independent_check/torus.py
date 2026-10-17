import numpy as np, sys
from orbits import site
def gf2rank(M):
    M=M.copy()%2; M=M.astype(np.uint8); r=0; rows,cols=M.shape
    for c in range(cols):
        piv=np.nonzero(M[r:,c])[0]
        if len(piv)==0: continue
        p=piv[0]+r
        if p!=r: M[[r,p]]=M[[p,r]]
        nz=np.nonzero(M[:,c])[0]; nz=nz[nz!=r]
        M[nz]^=M[r]
        r+=1
        if r==rows: break
    return r
def check_matrix(rule,L):
    n=2*L**3  # qubits: (site, q) q=0 spin,1 flavour
    def qi(v,q): return 2*(((v[0]%L)*L+(v[1]%L))*L+(v[2]%L))+q
    rows=[]
    for u in np.ndindex(L,L,L):
        for g in rule:
            row=np.zeros(2*n,np.uint8)
            for r in range(7):
                v=tuple(u[k]+site[r][k] for k in range(3)); l=g[r]
                for q,bits in ((0,l&3),(1,l>>2)):
                    if bits&1: row[qi(v,q)]^=1
                    if bits&2: row[n+qi(v,q)]^=1
            rows.append(row)
    return np.array(rows),n
def logdim(rule,L):
    H,n=check_matrix(rule,L)
    # commutation sanity
    Om=(H[:,:n].astype(int)@H[:,n:].T.astype(int)+H[:,n:].astype(int)@H[:,:n].T.astype(int))%2
    assert not Om.any()
    return n-gf2rank(H)
if __name__=='__main__':
    CH=(0,1,1,3,3,2,2); Dx=(0,)+tuple(l|4 for l in CH[1:])
    for L in (4,6): print('L',L,'log2 dim',logdim([Dx],L), 'pure chamon', logdim([CH],L)-L**3)
