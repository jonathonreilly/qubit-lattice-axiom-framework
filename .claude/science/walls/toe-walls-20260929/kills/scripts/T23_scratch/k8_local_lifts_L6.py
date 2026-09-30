#!/usr/bin/env python3
"""K8 (replaces the L=4-only k2/k4/k7 search, whose 'solution' failed at L=6,8):
Search range<=1, period-2 UNITARY local operators A with (A P_g) D = eps * D (A P_g) that are exact on an unwrapped lattice.
 * intertwining space from explicit matrices on L=6 (no offset coincidences up to range 2);
 * unitarity imposed at COEFFICIENT level for all offsets |s|<=2 (valid on any large torus);
 * kernel action from the 8x8 unit-cell reduction.
Report, per rotation g: does a unitary lift exist, and what does its kernel action do to the hw=1 triplet?"""
import itertools, sys, numpy as np, torch
torch.set_default_dtype(torch.float64)
L=6; N=L**3
pts=list(itertools.product(range(L),repeat=3))
idx=lambda x,y,z:((x%L)*L+(y%L))*L+(z%L)
def Dmat(Lx):
    Nn=Lx**3; ptsn=list(itertools.product(range(Lx),repeat=3)); ix=lambda x,y,z:((x%Lx)*Lx+(y%Lx))*Lx+(z%Lx)
    Dn=np.zeros((Nn,Nn))
    for (x,y,z) in ptsn:
        eta=[1,(-1)**x,(-1)**(x+y)]
        for mu,e in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
            i=ix(x,y,z); Dn[i,ix(x+e[0],y+e[1],z+e[2])]+=eta[mu]/2; Dn[i,ix(x-e[0],y-e[1],z-e[2])]-=eta[mu]/2
    return Dn
D=Dmat(L)
offs=list(itertools.product([-1,0,1],repeat=3)); oi={t:i for i,t in enumerate(offs)}
par=list(itertools.product([0,1],repeat=3)); pi_={p:i for i,p in enumerate(par)}
def Pg(M,Lx=L):
    Nn=Lx**3; ptsn=list(itertools.product(range(Lx),repeat=3)); ix=lambda x,y,z:((x%Lx)*Lx+(y%Lx))*Lx+(z%Lx)
    U=np.zeros((Nn,Nn))
    for p in ptsn:
        q=tuple((M@np.array(p))%Lx); U[ix(*q),ix(*p)]=1
    return U
def basis(ti,pi):
    B=np.zeros((N,N)); t=offs[ti]; pr=par[pi]
    for p in pts:
        if (p[0]%2,p[1]%2,p[2]%2)==pr: B[idx(*p),idx(p[0]+t[0],p[1]+t[1],p[2]+t[2])]=1
    return B
BAS=[basis(ti,pi) for ti in range(27) for pi in range(8)]     # index = ti*8+pi
def sp(p,s):
    M=np.zeros((3,3),int)
    for j in range(3): M[p[j],j]=s[j]
    return M
GEN={'E':sp((0,1,2),(1,1,1)),'C2z':sp((0,1,2),(-1,-1,1)),'C4z':sp((1,0,2),(-1,1,1)),'C2d':sp((1,0,2),(-1,-1,-1)),'C3':sp((1,2,0),(1,1,1))}
def nullspace(M,eps):
    Dp=Pg(M)@D@Pg(M).T
    cols=[(B@Dp-eps*D@B).flatten() for B in BAS]
    A=np.array(cols).T
    u,s,vt=np.linalg.svd(A,full_matrices=False)
    return vt[int((s>1e-9).sum()):]                            # rows: coefficient vectors over (ti,pi)
# ---- coefficient-level unitarity ----
S_off=list(itertools.product(range(-2,3),repeat=3))
combos=[]   # (s_index, px_index, t1_index, t2_index, valid) with t2=t1+s
for si,s in enumerate(S_off):
    for pxi,px in enumerate(par):
        for t1 in offs:
            t2=(t1[0]+s[0],t1[1]+s[1],t1[2]+s[2])
            if t2 in oi:
                py=tuple((px[k]+t1[k])%2 for k in range(3))
                combos.append((si,pxi,oi[t1],oi[t2],pi_[py]))
combos=np.array(combos)
SI=torch.tensor(combos[:,0]); T1=torch.tensor(combos[:,2]); T2=torch.tensor(combos[:,3]); PY=torch.tensor(combos[:,4]); PX=torch.tensor(combos[:,1])
target=torch.zeros(len(S_off),8,dtype=torch.complex128)
target[S_off.index((0,0,0)),:]=1
def unit_residual(a):                                        # a: (27,8) complex
    terms=torch.conj(a[T1,PY])*a[T2,PY]
    out=torch.zeros(len(S_off),8,dtype=torch.complex128)
    out=out.index_put((SI,PX),terms,accumulate=True)
    return out-target
# ---- unit cell reduction ----
H1=np.array([[1,1],[1,-1]])/np.sqrt(2); H=np.kron(np.kron(H1,H1),H1)        # corner-wave basis vs unit-cell sites, index bits (x,y,z)
def cell_ops(a,M):
    # A on 2-periodic functions f(p): (Af)(p)=sum_t a_t(p) f(p+t mod 2); P_g f(p) = f(M^-1 p) -> permutation of unit cell sites
    Ah=np.zeros((8,8),complex)
    for pi,p in enumerate(par):
        for ti,t in enumerate(offs):
            q=tuple((p[k]+t[k])%2 for k in range(3)); Ah[pi,pi_[q]]+=a[ti,pi]
    Ph=np.zeros((8,8))
    for pi,p in enumerate(par):
        q=tuple(int(v)%2 for v in (M@np.array(p))); Ph[pi_[q],pi]=1
    return H@Ah@Ph@H          # kernel action in corner basis (H symmetric orthogonal)
corner_idx={c:i for i,c in enumerate(par)}
triplet=[corner_idx[c] for c in [(1,0,0),(0,1,0),(0,0,1)]]; rest=[i for i in range(8) if i not in triplet]
def search(name,eps,ntry,mode,seed=0):
    M=GEN[name]; null=nullspace(M,eps); k=len(null)
    Nn=torch.tensor(null.reshape(k,27,8),dtype=torch.complex128)
    g=torch.Generator().manual_seed(seed); best=None; sols=[]
    Hh=torch.tensor(H,dtype=torch.complex128)
    Ph=np.zeros((8,8))
    for pi,p in enumerate(par):
        q=tuple(int(v)%2 for v in (M@np.array(p))); Ph[pi_[q],pi]=1
    Pht=torch.tensor(Ph,dtype=torch.complex128)
    # Ah as torch: Ah[pi, pi_[q]] += a[ti,pi]
    rows=[];cols=[];tis=[];pis=[]
    for pi,p in enumerate(par):
        for ti,t in enumerate(offs):
            q=tuple((p[kk]+t[kk])%2 for kk in range(3)); rows.append(pi); cols.append(pi_[q]); tis.append(ti); pis.append(pi)
    rows=torch.tensor(rows);cols=torch.tensor(cols);tis=torch.tensor(tis);pis=torch.tensor(pis)
    for tr in range(ntry):
        c=((torch.randn(k,generator=g)+1j*torch.randn(k,generator=g))*0.3).to(torch.complex128).requires_grad_(True)
        opt=torch.optim.LBFGS([c],lr=1,max_iter=300,tolerance_grad=1e-14,tolerance_change=1e-18,line_search_fn='strong_wolfe')
        def build():
            a=torch.einsum('k,kts->ts',c,Nn)
            Ah=torch.zeros(8,8,dtype=torch.complex128).index_put((rows,cols),a[tis,pis],accumulate=True)
            K=Hh@Ah@Pht@Hh
            return a,K
        def closure():
            opt.zero_grad(); a,K=build()
            loss=(unit_residual(a).abs()**2).sum()
            if mode=='triplet': loss=loss+(K[rest][:,triplet].abs()**2).sum()
            loss.backward(); return loss
        for _ in range(5): opt.step(closure)
        l=closure().item()
        if best is None or l<best[0]: best=(l,c.detach().clone())
        if l<1e-16: sols.append(best); break
    l,c=best
    a=torch.einsum('k,kts->ts',c,Nn).detach().numpy(); K=cell_ops(a,M)
    return l,a,K,k
if __name__=="__main__":
    name=sys.argv[1]; eps=int(sys.argv[2]); mode=sys.argv[3]; nt=int(sys.argv[4])
    l,a,K,k=search(name,eps,nt,mode)
    print(f"{name} eps={eps:+d} mode={mode}: dim intertwiners={k}  best loss={l:.3e}")
    if l<1e-12:
        T=K[np.ix_(triplet,triplet)]
        print("  kernel action unitary?",np.allclose(K.conj().T@K,np.eye(8),atol=1e-6)," triplet leakage",np.linalg.norm(K[np.ix_(rest,triplet)]).round(8))
        print("  |triplet block|:\n",np.round(np.abs(T),4))
        np.save(f"k8_{name}_{eps}_{mode}.npy",a)
