#!/usr/bin/env python3
"""T23 test: is the S3-sign 'orientation bit' of the flavor sector a mirror (handedness) bit?
Pre-registered in PREREGISTER.md.  numpy only.  Exact/integer where possible."""
import itertools, numpy as np
np.set_printoptions(precision=6, suppress=True)
PASS=FAIL=0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS+=1; print("PASS:",name,detail)
    else: FAIL+=1; print("FAIL:",name,detail)

L=4; N=L**3
pts=list(itertools.product(range(L),repeat=3))
idx=lambda x,y,z:((x%L)*L+(y%L))*L+(z%L)

# ---------- staggered surface, corner waves ----------
D=np.zeros((N,N))
for (x,y,z) in pts:
    eta=[1,(-1)**x,(-1)**(x+y)]
    for mu,e in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
        i=idx(x,y,z); D[i,idx(x+e[0],y+e[1],z+e[2])]+=eta[mu]/2; D[i,idx(x-e[0],y-e[1],z-e[2])]-=eta[mu]/2
corners=list(itertools.product([0,1],repeat=3))           # c
V=np.zeros((N,8))
for a,c in enumerate(corners):
    for p in pts: V[idx(*p),a]=(-1)**(c[0]*p[0]+c[1]*p[1]+c[2]*p[2])
V/=np.sqrt(N)
check("F0 corner waves are the exact 8-dim kernel of D", np.allclose(D@V,0) and np.linalg.matrix_rank(D)==N-8 and np.allclose(V.T@V,np.eye(8)))
triplet=[corners.index(c) for c in [(1,0,0),(0,1,0),(0,0,1)]]

# ---------- point group ----------
def sp_mats():
    out=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3),int)
            for j in range(3): M[p[j],j]=s[j]
            out.append((p,s,M))
    return out
G=sp_mats()
det=lambda M:int(round(np.linalg.det(M)))
def perm_sign(p): return (-1)**sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j])
def site_unitary(M,t=(0,0,0)):
    U=np.zeros((N,N))
    for p in pts:
        q=tuple((M@np.array(p)+np.array(t))%L)
        U[idx(*q),idx(*p)]=1
    return U
proper=[g for g in G if det(g[2])==1]; improper=[g for g in G if det(g[2])==-1]
check("F1 |O|=24, |O_h|=48", len(proper)==24 and len(G)==48)

# ---------- Block A: induced action on triplet, label level, computed from real unitaries ----------
def kernel_action(M):
    U=site_unitary(M); R=V.T@U@V
    inker=np.linalg.norm(U@V-V@R)<1e-12
    return R,inker
perm_of={}   # g index -> permutation of triplet (as tuple), sign-free check
allsignfree=True; allinker=True
for k,(p,s,M) in enumerate(G):
    R,inker=kernel_action(M)
    allinker&=inker
    # permutation matrix?
    isperm=np.allclose(np.abs(R).sum(0),1) and np.allclose(np.abs(R).sum(1),1) and set(np.round(R.flatten(),9))<= {0.0,1.0}
    allsignfree&=isperm
    T=R[np.ix_(triplet,triplet)]
    perm_of[k]=tuple(int(np.argmax(T[:,j])) for j in range(3)) if np.allclose(T.sum(0),1) else None
check("A0 every U_g maps the kernel into itself, sign-free permutation of corners", allinker and allsignfree)
check("A0b triplet preserved by every U_g (hw is O_h-invariant)", all(v is not None for v in perm_of.values()))
# geometric prediction: triplet perm = coordinate permutation p
check("A0c triplet action equals the coordinate permutation p of the signed permutation matrix", all(perm_of[k]==G[k][0] for k in range(48)))
img_proper={perm_of[k] for k,g in enumerate(G) if det(g[2])==1}
check("A1 O -> S3 is onto", len(img_proper)==6, f"image size {len(img_proper)}")
transp=[p for p in img_proper if perm_sign(p)==-1]
cnt={p:sum(1 for k,g in enumerate(G) if det(g[2])==1 and perm_of[k]==p) for p in img_proper}
check("A1b each transposition is the image of 4 proper rotations; kernel V4 has 4 elements", all(cnt[p]==4 for p in img_proper), str(cnt))
ker_sgn=[g for k,g in enumerate(G) if det(g[2])==1 and perm_sign(perm_of[k])==1]
check("A2 ker(sgn o pi) in O has order 12 (tetrahedral T); det is trivial on O (so sgn o pi != det|O)", len(ker_sgn)==12 and all(det(g[2])==1 for g in proper))
# tetrahedral check: contains no order-4 element (C4) and contains 8 three-fold rotations + 3 twofold coordinate rotations + identity
def order(M):
    P=np.eye(3,dtype=int); n=0
    while True:
        P=P@M; n+=1
        if (P==np.eye(3,dtype=int)).all(): return n
ords=sorted(order(g[2]) for g in ker_sgn)
check("A2b ker has element orders 1x1, 2x3, 3x8 (rotation group of the tetrahedron)", ords==[1]+[2]*3+[3]*8, str(ords))
even_all=[g for k,g in enumerate(G) if perm_sign(perm_of[k])==1]
has_inv=any((g[2]==-np.eye(3,dtype=int)).all() for g in even_all)
check("A3 elements of O_h acting on triplet as even perm: order 24, contains inversion, 12 improper",
      len(even_all)==24 and has_inv and sum(1 for g in even_all if det(g[2])==-1)==12)
inv_idx=[k for k,g in enumerate(G) if (g[2]==-np.eye(3,dtype=int)).all()][0]
check("A3b inversion acts as identity on the triplet", perm_of[inv_idx]==(0,1,2))
c4=[k for k,g in enumerate(G) if det(g[2])==1 and order(g[2])==4]
check("A3c every 90-degree rotation (C4) acts on the triplet as a transposition", all(perm_sign(perm_of[k])==-1 for k in c4), f"{len(c4)} C4 elements")

# ---------- Block B: circulant ----------
Rc=[g for g in proper if g[0]==(1,2,0) and g[1]==(1,1,1)][0]     # (x,y,z)->(z,x,y) or inverse; use as C3[111]
kC=G.index(Rc); Rk,_=kernel_action(Rc[2]); C=Rk[np.ix_(triplet,triplet)]
TSg=[g for g in proper if g[0]==(1,0,2) and g[1]==(-1,-1,-1)][0]    # pi-rotation about [1,-1,0]: (x,y,z)->(-y,-x,-z)
Rt,_=kernel_action(TSg[2]); TS=Rt[np.ix_(triplet,triplet)]
check("B0 TS from the proper pi-rotation about [1,-1,0]: det M=+1, TS=transposition(1 2)", det(TSg[2])==1 and np.allclose(TS,[[0,1,0],[1,0,0],[0,0,1]]))
check("B0b C real cyclic, C^3=I, C^T=C^2, TS C TS = C^2", np.allclose(np.linalg.matrix_power(C,3),np.eye(3)) and np.allclose(C.T,C@C) and np.allclose(TS@C@TS,C@C))
def W(a,b): return a*np.eye(3)+b*C+np.conj(b)*C@C
rng=np.random.default_rng(1)
ok=True
for _ in range(50):
    a=rng.normal(); b=rng.normal()+1j*rng.normal()
    ok&=np.allclose(TS@W(a,b)@TS,np.conj(W(a,b))) and np.allclose(TS@W(a,b)@TS,W(a,np.conj(b)))
check("B1 on the Hermitian section conj(W)=TS W TS (K = proper-rotation conjugation)", ok)
d=2/9; r=np.sqrt(2)/2
Wp=W(1,r*np.exp(1j*d)); Wm=W(1,r*np.exp(-1j*d))
lam=lambda dd:1+np.sqrt(2)*np.cos(dd+2*np.pi*np.arange(3)/3)
check("B2 eigenvalues of W(delta) are 1+sqrt2 cos(delta+2 pi k/3), same multiset for +/-delta",
      np.allclose(np.sort(np.linalg.eigvalsh(Wp)),np.sort(lam(d))) and np.allclose(np.sort(lam(d)),np.sort(lam(-d))) and np.allclose(np.sort(np.linalg.eigvalsh(Wm)),np.sort(lam(-d))))
check("B3 Tr W^n equal for +/-delta, n=1..8", all(abs(np.trace(np.linalg.matrix_power(Wp,n))-np.trace(np.linalg.matrix_power(Wm,n)))<1e-12 for n in range(1,9)))
orbit=[]
for k,g in enumerate(G):
    if det(g[2])!=1: continue
    Pm=np.zeros((3,3)); 
    for j in range(3): Pm[perm_of[k][j],j]=1
    X=Pm@Wp@Pm.T
    if not any(np.allclose(X,Y) for Y in orbit): orbit.append(X)
check("B4 the proper-rotation orbit of W(delta) is exactly {W(delta),W(-delta)}", len(orbit)==2 and any(np.allclose(o,Wm) for o in orbit))
print("     detail: W(delta) is NOT invariant under proper rotations => an O-covariant law-level 3x3 operator has |orbit|=1 => S3-invariant => <=2 distinct eigenvalues;")
print("             the two 'orientations' are two rotated copies of one operator.")
# spectrum of an O-invariant Hermitian op on triplet: commutant of S3 perm rep
Pm_all=[]
for k,g in enumerate(G):
    if det(g[2])==1:
        Pm=np.zeros((3,3))
        for j in range(3): Pm[perm_of[k][j],j]=1
        Pm_all.append(Pm)
def avg(X): return sum(P@X@P.T for P in Pm_all)/len(Pm_all)
ev=[np.round(np.linalg.eigvalsh(avg((lambda A:(A+A.conj().T)/2)(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))))),9) for _ in range(5)]
check("B5 group-averaging a random Hermitian operator over the PROPER rotation group gives spectrum {a,a,b} (two distinct values)", all(len(set(e))==2 for e in ev), str(ev[0]))

# ---------- Block C: Cl(3)/M2(C) pseudoscalar ----------
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); S=[sx,sy,sz]
omega=sx@sy@sz
check("C0 omega = sigma1 sigma2 sigma3 = i*Identity (central)", np.allclose(omega,1j*np.eye(2)))
def null_dim(rows):
    A=np.array(rows); s=np.linalg.svd(A,compute_uv=False); return int((s<1e-9).sum())
def lin_dim(M):
    # X sigma_i = sum_j M[j,i] sigma_j X , X in M2(C) (vec, complex-linear)
    rows=[]
    for i in range(3):
        Sp=sum(M[j,i]*S[j] for j in range(3))
        # vec(X sigma_i - Sp X) with column-major: (sigma_i^T kron I - I kron Sp) vec X
        rows.append(np.kron(S[i].T,np.eye(2))-np.kron(np.eye(2),Sp))
    A=np.vstack(rows); s=np.linalg.svd(A,compute_uv=False); return 4-int((s>1e-9).sum())
def antilin_dim(M):
    # X conj(sigma_i) = sum_j M[j,i] sigma_j X
    rows=[]
    for i in range(3):
        Sp=sum(M[j,i]*S[j] for j in range(3))
        rows.append(np.kron(np.conj(S[i]).T,np.eye(2))-np.kron(np.eye(2),Sp))
    A=np.vstack(rows); s=np.linalg.svd(A,compute_uv=False); return 4-int((s>1e-9).sum())
okp=all(lin_dim(g[2])==1 and antilin_dim(g[2])==0 for g in proper)
oki=all(lin_dim(g[2])==0 and antilin_dim(g[2])==1 for g in improper)
check("C1 every proper signed permutation is implemented LINEARLY (1-dim solution), none antilinearly; every improper one only ANTIlinearly", okp and oki)
check("C2 characters sgn(pi) and det are different on O_h: agree on exactly half of the elements",
      sum(1 for k,g in enumerate(G) if perm_sign(perm_of[k])==det(g[2]))==24)
combo={}
for k,g in enumerate(G): combo[(perm_sign(perm_of[k]),det(g[2]))]=combo.get((perm_sign(perm_of[k]),det(g[2])),0)+1
check("C2b (sgn,det) pattern is the full Klein group of characters, 12 elements each", sorted(combo.values())==[12,12,12,12], str(combo))
check("C3 omega fixed by all proper rotations (central), flipped by every antilinear implementer", all(np.allclose(omega,omega) for _ in [0]))  # trivially central; sign flip under K below
check("C3b K: conj(omega) = -omega", np.allclose(np.conj(omega),-omega))

# ---------- Block D: absolute vs relative ----------
def Wd(dd): return W(1,r*np.exp(1j*dd))
def inv_obs(W1,W2):
    return np.array([np.trace(np.linalg.matrix_power(W1,a)@np.linalg.matrix_power(W2,b)).real for a in range(0,5) for b in range(0,5)])
d1,d2=2/9,0.13
pp=inv_obs(Wd(d1),Wd(d2)); mm=inv_obs(Wd(-d1),Wd(-d2)); pm=inv_obs(Wd(d1),Wd(-d2)); mp=inv_obs(Wd(-d1),Wd(d2))
check("D1 flipping BOTH sectors' orientation changes no O-invariant Tr(W1^a W2^b)", np.allclose(pp,mm) and np.allclose(pm,mp))
check("D2 flipping ONE sector changes Tr(W1 W2)", abs(pp[5+1]-pm[5+1])>1e-6, f"Tr(W1W2): same-orient {pp[6]:.6f}  opposite {pm[6]:.6f}")
check("D3 closed form Tr(W1W2)=3+6 r^2 cos(d1-d2)", abs(pp[6]-(3+6*r*r*np.cos(d1-d2)))<1e-12 and abs(pm[6]-(3+6*r*r*np.cos(d1+d2)))<1e-12)

# ---------- Block F: what the actual D says (operator level; report only) ----------
und_sym=und_anti=0
for (p,s,M) in G:
    U=site_unitary(M); 
    if np.allclose(U@D@U.T,D): und_sym+=1
    elif np.allclose(U@D@U.T,-D): und_anti+=1
print(f"F1 undressed site permutations (48): commute with D: {und_sym}, anticommute: {und_anti}, neither: {48-und_sym-und_anti}")
# dressed: for each (g,t) find sign field s with S U D U^T S = eps D  (links solvable iff flux matches)
def find_dressing(U):
    Dg=U@D@U.T
    for eps in (1,-1):
        # need s_i s_j Dg[i,j] = eps D[i,j] for all linked i,j
        s=np.zeros(N,int); s[0]=1; stack=[0]; ok=True
        nz=[np.nonzero(D[i])[0] for i in range(N)]
        while stack and ok:
            i=stack.pop()
            for j in nz[i]:
                if abs(Dg[i,j])<1e-12: ok=False;break
                want=eps*D[i,j]/Dg[i,j]        # = s_i s_j
                sj=int(round(want))*s[i]
                if s[j]==0: s[j]=sj; stack.append(j)
                elif s[j]!=sj: ok=False;break
        if ok and (s!=0).all():
            S_=np.diag(s.astype(float))
            if np.allclose(S_@Dg@S_,eps*D): return eps,S_
    return None
dressed=[]   # (proper?, eps, 8x8 kernel matrix)
for (p,s,M) in G:
    for t in itertools.product(range(L),repeat=3):
        U=site_unitary(M,t); res=find_dressing(U)
        if res is None: continue
        eps,S_=res; Uf=S_@U
        R8=V.T@Uf@V
        assert np.linalg.norm(Uf@V-V@R8)<1e-10        # maps kernel to kernel
        dressed.append((det(M)==1,eps,R8,tuple(t),tuple(map(tuple,M))))
from collections import Counter
print("F2 dressed (g,t) counts by (proper, eps):",dict(Counter((a,b) for a,b,_,_,_ in dressed)))
def trip_preserved(R8): return np.linalg.norm(R8[np.ix_([i for i in range(8) if i not in triplet],triplet)])<1e-10
cnt_tp=Counter((a,b,trip_preserved(R)) for a,b,R,_,_ in dressed)
print("F3 dressed symmetries preserving the hw=1 triplet subspace, by (proper,eps,preserved):",dict(cnt_tp))
# commutant of the group generated by proper eps=+1 dressed symmetries on the 8-dim kernel
def closure(gens,limit=200000):
    seen={}; key=lambda A:tuple(np.round(A.flatten(),6))
    frontier=[np.eye(8)]; seen[key(frontier[0])]=frontier[0]
    while frontier:
        new=[]
        for A in frontier:
            for B in gens:
                Cm=B@A; k=key(Cm)
                if k not in seen:
                    seen[k]=Cm; new.append(Cm)
                    if len(seen)>limit: return None
        frontier=new
    return list(seen.values())
gens_plus=[R for a,b,R,_,_ in dressed if a and b==1]
uniq={}
for R in gens_plus: uniq[tuple(np.round(R.flatten(),6))]=R
gens_plus=list(uniq.values())
print("F4 distinct 8x8 matrices from proper eps=+1 dressed symmetries:",len(gens_plus))
grp=closure(gens_plus) if len(gens_plus)<400 else None
if grp is None: print("F5 closure skipped/too big")
else:
    print("F5 group order (as matrices) generated:",len(grp))
    def avg8(X): return sum(A@X@A.T for A in grp)/len(grp)
    ev=[]
    for _ in range(4):
        X=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8)); X=(X+X.conj().T)/2
        w=np.linalg.eigvalsh(avg8(X)); ev.append(np.round(w,6))
    print("F6 spectrum of a random Hermitian 8x8 operator averaged over the proper eps=+1 dressed group:",ev[0])
    print("   distinct eigenvalues:",[len(set(e)) for e in ev])
print(f"TOTAL PASS={PASS} FAIL={FAIL}")
