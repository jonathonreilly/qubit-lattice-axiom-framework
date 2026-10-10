# R1 check: gapless mode counts, helicities and dispersion order for rank-2 tensor gauge classes
# on Z^3 lattice symbols (midpoint differences q_i = 2 sin(k_i/2)). Exact linear algebra, double precision.
import numpy as np, itertools
np.set_printoptions(precision=4, suppress=True)
IDX = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
def t2v(T):  # symmetric 3x3 -> orthonormal 6-vector
    s=np.sqrt(2); return np.array([T[0,0],T[1,1],T[2,2],s*T[0,1],s*T[1,2],s*T[0,2]])
def v2t(v):
    s=np.sqrt(2); T=np.zeros((3,3))
    T[0,0],T[1,1],T[2,2]=v[0],v[1],v[2]; T[0,1]=T[1,0]=v[3]/s; T[1,2]=T[2,1]=v[4]/s; T[0,2]=T[2,0]=v[5]/s; return T
eps=np.zeros((3,3,3))
for (a,b,c),sg in [((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)]: eps[a,b,c]=sg
def lin(f, nin):  # matrix of linear map from R^nin
    cols=[f(np.eye(nin)[i]) for i in range(nin)]; return np.array(cols).T
def ops(q):
    # vector gauge  dh = q_i l_j + q_j l_i   (linearized diffeo / relabelling)
    Gt = lin(lambda l: t2v(np.outer(q,l)+np.outer(l,q)), 3)
    # scalar-charge (fracton) gauge dh = q_i q_j a
    Ft = lin(lambda a: t2v(np.outer(q,q)*a[0]), 1)
    # scalar (Hamiltonian) constraint on h: S = q^2 tr h - q.h.q ; its gauge acts on E
    S  = lin(lambda v: np.array([q@q*np.trace(v2t(v)) - q@v2t(v)@q]), 6)
    # linearized curvature R_ij = eps_iab eps_jcd q_a q_c h_bd (vector-gauge invariant, symmetric)
    R  = lin(lambda v: t2v(np.einsum('iab,jcd,a,c,bd->ij',eps,eps,q,q,v2t(v))), 6)
    # fracton magnetic field B_ij = eps_iab q_a h_bj (9 comps)
    B  = lin(lambda v: np.einsum('iab,a,bj->ij',eps,q,v2t(v)).ravel(), 6)
    # Cotton-like electric invariant C_ij = eps_iab q_a (E_bj - delta_bj trE/2)
    C  = lin(lambda v: np.einsum('iab,a,bj->ij',eps,q,v2t(v)-np.eye(3)*np.trace(v2t(v))/2).ravel(), 6)
    trv = t2v(np.eye(3))
    DeW = np.eye(6) - 0.5*np.outer(trv,trv)
    return dict(Gt=Gt,Ft=Ft,S=S,R=R,B=B,C=C,DeW=DeW)
def phys_basis(cols):
    M=np.hstack(cols) if cols else np.zeros((6,0))
    U,s,Vt=np.linalg.svd(M, full_matrices=True)
    r=(s>1e-10*max(1,s.max() if s.size else 1)).sum()
    return U[:,r:]
def freqs(model, k):
    q=2*np.sin(np.asarray(k)/2); o=ops(q)
    if model=='V_compact':   W=phys_basis([o['Gt']]);            K=np.eye(6);  V=o['R'].T@o['R']
    if model=='VS_compact':  W=phys_basis([o['Gt'],o['S'].T]);   K=o['C'].T@o['C']; V=o['R'].T@o['R']
    if model=='F_compact':   W=phys_basis([o['Ft']]);            K=np.eye(6);  V=o['B'].T@o['B']
    if model=='V_EH':        W=phys_basis([o['Gt']]);            K=o['DeW'];   V=o['R']
    if model=='VS_EH':       W=phys_basis([o['Gt'],o['S'].T]);   K=o['DeW'];   V=o['R']
    Kp=W.T@K@W; Vp=W.T@V@W
    w2=np.linalg.eigvals(Kp@Vp)
    return np.sort_complex(w2), W
nhat=np.array([0.31,0.52,0.79]); nhat/=np.linalg.norm(nhat)
print("model        n_phys   omega^2 at k=1e-2 n   slope d log|omega^2| / d log k (per mode)")
for m in ['V_compact','VS_compact','F_compact','V_EH','VS_EH']:
    a,W=freqs(m,1e-2*nhat); b,_=freqs(m,1e-3*nhat)
    sl=np.log(np.abs(a)/np.abs(b))/np.log(10)
    print(f"{m:12s} {W.shape[1]:3d}   {np.real_if_close(a)}   slopes(omega^2)={np.round(sl,2)}")
# helicity content of physical modes at k along z: rotation generator about z acting on symmetric tensors
def hel_content(model):
    k=np.array([0,0,1e-2]); _,W=freqs(model,k)
    Lz=np.array([[0,-1,0],[1,0,0],[0,0,0]])
    J=lin(lambda v: t2v(Lz@v2t(v)-v2t(v)@Lz), 6)  # generator (antisymmetric real)
    P=W@W.T; Jp=W.T@J@W
    ev=np.linalg.eigvals(1j*Jp)  # helicities
    return np.round(np.sort(np.real(ev)),6)
for m in ['V_compact','VS_compact','F_compact']:
    print(m,'helicities of physical subspace (k||z):',hel_content(m))
# per-helicity speeds for fracton class (generic compact H=E^2+B^2)
k=np.array([0,0,1e-3]); w2,W=freqs('F_compact',k); print('F_compact omega^2/k^2 per mode:',np.round(np.real(w2)/1e-6,4))
# VS_EH: TT speed; V_EH: sign of scalar mode
k=1e-3*nhat; w2,W=freqs('V_EH',k); print('V_EH omega^2/k^2:',np.round(np.real_if_close(w2)/1e-6,4))
w2,W=freqs('VS_EH',k); print('VS_EH omega^2/k^2:',np.round(np.real_if_close(w2)/1e-6,4))
# Exact lattice identities at a random lattice momentum
rng=np.random.default_rng(1)
for _ in range(3):
    q=2*np.sin(rng.uniform(-np.pi,np.pi,3)/2); o=ops(q)
    print('identities |R Gt|=%.1e |S Gt|=%.1e |B Ft|=%.1e |C S^T|=%.1e |Gt^T R|=%.1e'%(
        np.abs(o['R']@o['Gt']).max(),np.abs(o['S']@o['Gt']).max(),np.abs(o['B']@o['Ft']).max(),
        np.abs(o['C']@o['S'].T).max(), np.abs(o['Gt'].T@o['R']).max()))
# Mass term: does tr h^2 (identity on h) survive projection as a k->0 nonzero term? It is not gauge invariant:
for name,key in [('vector gauge','Gt'),('fracton gauge','Ft')]:
    q=2*np.sin(1e-3*nhat/2); o=ops(q); g=o[key]
    print(name,': mass form h.h changes under gauge: max |g^T g| =',np.abs(g.T@g).max(), '(nonzero -> mass forbidden by the redundancy)')
