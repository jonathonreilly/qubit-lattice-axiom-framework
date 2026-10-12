# R11-2: which side carries the weak (non-character) invariance, and the TT dispersion it allows.
# Fields: symmetric h, E on Z^3 with midpoint symbols q_i = 2 sin(k_i/2) (09-14 note convention).
# Orthonormal symmetric-tensor basis (6 comps). Vector gauge h -> h + sym(q x a); scalar gauge E -> E + (q^2 I - q q) b.
import numpy as np, sympy as sp
rng = np.random.default_rng(7)
idx = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
def basis():
    B=[]
    for (i,j) in idx:
        M=np.zeros((3,3))
        if i==j: M[i,i]=1
        else: M[i,j]=M[j,i]=1/np.sqrt(2)
        B.append(M)
    return B
Bs=basis()
def vec(M): return np.array([np.sum(M*b) for b in Bs])
def mat(v): return sum(c*b for c,b in zip(v,Bs))
def Vmap(q):   # 6x3: a -> sym(q a)
    return np.column_stack([vec(0.5*(np.outer(q,e)+np.outer(e,q))) for e in np.eye(3)])
def Svec(q):   # scalar constraint row: S h = q^2 tr h - q.h.q  (as 6-vector, real inner product)
    return vec(np.dot(q,q)*np.eye(3)-np.outer(q,q))
eps=np.zeros((3,3,3))
for a,b,c in [(0,1,2),(1,2,0),(2,0,1)]: eps[a,b,c]=1; eps[a,c,b]=-1
def Rmap(q):   # R_ij = eps_iab eps_jcd q_a q_c h_bd  (sign irrelevant for |R|^2)
    cols=[]
    for b in Bs:
        R=np.einsum('iab,jcd,a,c,bd->ij',eps,eps,q,q,b)
        cols.append(vec(R))
    return np.column_stack(cols)
def Cmap(q):   # C_ij = eps_iab q_a (E_bj - delta_bj trE/2), symmetrized part
    cols=[]
    for b in Bs:
        Et=b-np.eye(3)*np.trace(b)/2
        C=np.einsum('iab,a,bj->ij',eps,q,Et); C=0.5*(C+C.T)
        cols.append(vec(C))
    return np.column_stack(cols)
trv=vec(np.eye(3))
KN=np.eye(6)-0.5*np.outer(trv,trv)          # E:E - (trE)^2/2
def QN(q): return -Rmap(q)                   # h:R(h) form; real-space R = eps eps d d h has Fourier symbol -eps eps q q h
def PTT(q):
    V=Vmap(q); s=Svec(q)[:,None]
    A=np.hstack([V,s])                        # TT = orthogonal complement of span(V, S-row) (trace lies in this span)
    Qo,_=np.linalg.qr(A)
    return np.eye(6)-Qo@Qo.T
out=[]
def p(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
p("== 1. identities (random k) ==")
for t in range(3):
    k=rng.normal(size=3); q=2*np.sin(k/2)
    V=Vmap(q); s=Svec(q); R=Rmap(q)
    p(f"k#{t}: |S.V|={np.linalg.norm(s@V):.1e}  |R V|={np.linalg.norm(R@V):.1e}  |R-R^T|={np.linalg.norm(R-R.T):.1e}  tr-check |trv.R - S|={np.linalg.norm(trv@R - s):.1e}")
    # weak S-invariance of K_N:  K_N s must lie in Im(V) (=Im G^dagger); strong would need K_N s = 0
    Ks=KN@s; coef,res,_,_=np.linalg.lstsq(V,Ks,rcond=None)
    p(f"      K_N S^T: norm={np.linalg.norm(Ks):.3e} (nonzero => NOT strongly S-invariant), residual off Im(V)={np.linalg.norm(V@coef-Ks):.1e}  s^T K_N s={s@KN@s:.1e}")
    # h:R exactly vector-gauge invariant as a global quadratic form
    p(f"      Q_N V = {np.linalg.norm(QN(q)@V):.1e}  (global form invariant, density not)")
p('|C S^T| (random k) =', np.linalg.norm(Cmap(2*np.sin(rng.normal(size=3)/2))@Svec(2*np.sin(rng.normal(size=3)/2))))
p("== 2. polynomial-system check: no O(1)/O(k) invariant characters ==")
ks=sp.symbols('k1:4'); kv=sp.Matrix(ks)
# h-side: m(k)=A + sum_l B_l k_l (symmetric), condition V(k)^T m(k)=0 identically (divergence-free)
Aa=sp.symbols('a0:6'); Bb=sp.symbols('b0:18')
def smat(c): return sp.Matrix([[c[0],c[3],c[5]],[c[3],c[1],c[4]],[c[5],c[4],c[2]]])
M=smat(Aa)+sum((smat(Bb[6*l:6*l+6])*ks[l] for l in range(3)),sp.zeros(3))
div=M*kv   # q_i m_ij
eqs=[]
for comp in div:
    eqs+=sp.Poly(sp.expand(comp),*ks).coeffs()
sol=sp.solve(eqs,list(Aa)+list(Bb),dict=True)
free=set(Aa+Bb)-set(sol[0].keys())
p("h-side deg<=1 divergence-free symbols: free params =",len(free), "(0 => every invariant h-character is O(k^2))")
# E-side: r(k)=A constant, condition S(k) r = k^2 tr r - k.r.k = 0 identically
r=smat(Aa); Sr=sp.expand((kv.T*kv)[0]*r.trace()-(kv.T*r*kv)[0])
sol2=sp.solve(sp.Poly(Sr,*ks).coeffs(),list(Aa),dict=True)
p("E-side constant S-invariant symbols: free params =",6-len(sol2[0]), "(0 => every invariant E-character is O(k))")
p("== 3. TT dispersion by realization class (random cubic-generic allowed terms) ==")
def rand_div_free_stencil():
    # general local divergence-free symmetric symbol: m = R(chi) for local chi (Kroner); chi random trig polynomial
    c=rng.normal(size=(6,)); ph=rng.normal(size=(6,3))
    return lambda q,k: Rmap(q).T@(c*np.cos(ph@k))   # m = R^T chi => V^T m = 0
def rand_Sinv_E_stencil():
    c=rng.normal(size=(6,)); ph=rng.normal(size=(6,3))
    return lambda q,k: Cmap(q).T@(c*np.cos(ph@k))   # r = C^T chi  => S r = 0 since C S^T = 0
mh=[rand_div_free_stencil() for _ in range(4)]
rE=[rand_Sinv_E_stencil() for _ in range(4)]
K0=rng.normal(size=(6,6)); K0=K0@K0.T+np.eye(6)
def blocks(cls,k):
    q=2*np.sin(k/2); P=PTT(q)
    Hhh_char=sum(np.outer(m(q,k),m(q,k)) for m in mh)      # strongly invariant h-characters
    HEE_char=sum(np.outer(r(q,k),r(q,k)) for r in rE)      # strongly S-invariant E-characters
    if cls=='L (both compact)':      HEE,Hhh=HEE_char,Hhh_char
    if cls=='A (E integer, h compact)': HEE,Hhh=K0+HEE_char,Hhh_char        # polynomial E-side allowed weakly
    if cls=='B (h integer, E compact)': HEE,Hhh=HEE_char,QN(q)+Hhh_char     # polynomial h:R allowed
    if cls=='N (both polynomial; not a rotor/qubit class)': HEE,Hhh=K0,QN(q)+Hhh_char
    return P@HEE@P,P@Hhh@P,P
for cls in ['L (both compact)','A (E integer, h compact)','B (h integer, E compact)','N (both polynomial; not a rotor/qubit class)']:
    d=rng.normal(size=3); d/=np.linalg.norm(d)
    ws=[];kk=[];allpos=True
    for kmag in [0.04,0.02,0.01,0.005]:
        k=kmag*d; HEE,Hhh,P=blocks(cls,k)
        U,sv,_=np.linalg.svd(P); U=U[:,:2]   # TT basis
        M=(U.T@HEE@U)@(U.T@Hhh@U)
        w2=np.sort(np.linalg.eigvals(M).real); allpos=allpos and bool(np.all(w2>0)); ws.append(np.sqrt(np.abs(w2))); kk.append(kmag)
    ws=np.array(ws); slope=np.polyfit(np.log(kk),np.log(ws[:,1]),1)[0]; slope0=np.polyfit(np.log(kk),np.log(ws[:,0]),1)[0]
    p(f"{cls:48s}: omega_TT exponents p = {slope0:.3f}, {slope:.3f}   (omega ~ k^p); all omega^2 > 0: {allpos}")
p("NOTE: in N, K_N on TT = |E_TT|^2 and h:R on TT = q^2|h_TT|^2 > 0 (09-14 note); here random positive K0 stands in for K_N on TT.")

p("== 4. dressing identities on TT (H_N|TT = H_L|TT composed with (-Delta)^-1, both sides) ==")
for t in range(3):
    k=rng.normal(size=3)*0.7; q=2*np.sin(k/2); P=PTT(q); U,_,_=np.linalg.svd(P); U=U[:,:2]; q2=q@q
    Rt=U.T@Rmap(q).T@Rmap(q)@U; Ct=U.T@Cmap(q).T@Cmap(q)@U; Kt=U.T@KN@U; Qt=U.T@QN(q)@U
    p(f"k#{t}: |K_N - |C|^2/q^2|_TT = {np.linalg.norm(Kt-Ct/q2*np.trace(Kt)/np.trace(Ct/q2)):.1e} (ratio const={np.trace(Ct)/q2/np.trace(Kt):.6f}),  |h:R - |R|^2/q^2|_TT = {np.linalg.norm(Qt-Rt/q2):.1e}, sign of h:R on TT: {np.sign(np.linalg.eigvalsh(Qt)).tolist()}")

open(__file__.replace('.py','.out'),'w').write('\n'.join(out)+'\n')
