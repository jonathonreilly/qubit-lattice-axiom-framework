"""Kill-round check: count how many random group elements actually entered the 'exists' branch of the attack's cone.py
(the attack prints only flips=0, not the number of effective trials)."""
import numpy as np, sys
sys.path.insert(0, "../../attacks/T13_scratch")
rng = np.random.default_rng(11)
def metric(p,q): return np.diag([-1.0]*p+[1.0]*q)
def rot(n,i,j,a):
    R=np.eye(n); R[i,i]=np.cos(a);R[j,j]=np.cos(a);R[i,j]=-np.sin(a);R[j,i]=np.sin(a);return R
def boost(n,i,j,e):
    B=np.eye(n);B[i,i]=np.cosh(e);B[j,j]=np.cosh(e);B[i,j]=np.sinh(e);B[j,i]=np.sinh(e);return B
def in_group(G,g,tol): return np.linalg.norm(G.T@g@G-g)<tol and abs(np.linalg.det(G)-1)<tol
def random_element(p,q,k=6):
    n=p+q;G=np.eye(n)
    for _ in range(k):
        i,j=rng.choice(n,2,replace=False)
        same=(i<p)==(j<p)
        G=G@(rot(n,i,j,rng.uniform(0,2*np.pi)) if same else boost(n,i,j,rng.normal(scale=1.5)))
    return G
for (p,q) in [(1,3),(3,1),(1,2),(2,1),(1,4),(4,1)]:
    n=p+q;g=metric(p,q);axis=0 if p==1 else p;sg=-1.0 if p==1 else 1.0
    used=0;flips=0;tot=4000
    for _ in range(tot):
        G=random_element(p,q)
        if not in_group(G,g,1e-6*max(1.0,np.abs(G).max()**2)): continue
        u=np.zeros(n);u[axis]=1.0
        v=u+0.3*rng.normal(size=n)*(np.arange(n)!=axis)/np.sqrt(n)
        if (v@g@v)*sg<=0: continue
        used+=1
        w=G@v
        if w[axis]<=0: flips+=1
    print((p,q),"effective trials",used,"of",tot,"flips",flips)
# independent necessity check for min(p,q)>=2: maximal compact SO(p)xSO(q) fixes no nonzero vector in R^{p+q}
for (p,q) in [(2,2),(3,2),(2,3),(3,3),(1,3),(3,1),(0,3)]:
    n=p+q
    # generators of so(p)+so(q): stack (A x = 0) over all rotation generators; fixed space = null space
    rows=[]
    for blk,off in ((p,0),(q,p)):
        for i in range(blk):
            for j in range(i+1,blk):
                A=np.zeros((n,n));A[off+i,off+j]=1;A[off+j,off+i]=-1;rows.append(A)
    M=np.vstack(rows) if rows else np.zeros((1,n))
    s=np.linalg.svd(M,compute_uv=False); rank=(s>1e-9).sum()
    print((p,q),"dim of K-fixed subspace of R^n:",n-rank)
