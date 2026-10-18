#!/usr/bin/env python3
"""B20 lemma: the k* doublet velocity of ANY word in S^{+-1}, S^{+-2}, R_L and symmetric on-site unitaries.
Statement (exact; proof in FINDINGS): let W = F_1 ... F_n, and D an exactly 2-fold level of W(k*) (+-k*).
D is the E1/2 or the E5/2 isotypic space (each occurs once), so every letter acts on D as a scalar at k*, and
  P_D W^dag dW P_D = sum_i lambda_i^{-1} P_D dF_i P_D.
Letters with k-independent spectrum (R_L = 1 - 2P(k), on-site) contribute 0 (P dP P = 0); S^p contributes
i p P_D diag(f_c . dk) P_D (S(k*) = 1).  Hence h(q) = n_S <f>_D . q with n_S the total S-power of the word,
<f>_D = P_D diag(f_c) P_D = eps_D (sqrt2/3) sigma (isotropic, untilted), eps_{E1/2} = -eps_{E5/2}:
  speed |n_S| sqrt2/3, chirality sign(n_S) eps_D, and zero velocity when n_S = 0.
Checked here on random words with random symmetric on-site unitaries.  Prints PASS/FAIL, TOTAL."""
import time
exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
t0=time.time(); PASS=FAIL=0
def check(name,ok,detail=""):
    global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}",flush=True)
check("S(k*) = S(-k*) = 1 exactly (k*.f_c in {0, +-pi} and the gauge signs compensate)",np.allclose(SK(kst),np.eye(12)) and np.allclose(SK(-kst),np.eye(12)))
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1])
def isotypic(k0):
    M=0.37*Hon0+0.11*Lam+0.05*(Hon0@Lam+Lam@Hon0)+0.23*RL(k0)+0.07*(RL(k0)@Lam+Lam@RL(k0))
    w,V=np.linalg.eigh((M+M.conj().T)/2); out=[]; i=0
    while i<12:
        j=i
        while j<12 and abs(w[j]-w[i])<1e-7: j+=1
        out.append(V[:,i:j]); i=j
    return out
def fmat(P):
    h=[P.conj().T@np.diag(F[:,j])@P for j in range(3)]
    return np.array([[np.trace(x@s).real/2 for s in (sx,sy,sz)] for x in h]),np.array([np.trace(x).real/2 for x in h])
EPS={}
for lab,k0 in (("k*",kst),("-k*",-kst)):
    blocks=isotypic(k0); dims=sorted(b.shape[1] for b in blocks)
    ds=[b for b in blocks if b.shape[1]==2]; info=[]
    for b in ds:
        M,a=fmat(b); sv=np.linalg.svd(M,compute_uv=False); info.append((sv,int(np.sign(np.linalg.det(M))),np.abs(a).max()))
    EPS[lab]=[(b,i[1]) for b,i in zip(ds,info)]
    check(f"at {lab}: a generic symmetric operator has isotypic blocks 2+2+4+4; <f>_D is isotropic sqrt2/3 with zero tilt on both doublets and opposite det signs",
          dims==[2,2,4,4] and all(np.allclose(i[0],np.sqrt(2)/3) and i[2]<1e-12 for i in info) and info[0][1]==-info[1][1],
          f"det signs {[i[1] for i in info]}")
# random words
rng=np.random.default_rng(42)
def ronsite():
    U=sum(np.exp(1j*rng.uniform(0,2*np.pi))*P for P in Ps)
    V=sum(np.exp(1j*rng.uniform(0,2*np.pi))*P for P in Qs)
    return U@V if rng.random()<0.5 else V@U
kletters=['S','Si','S2','S2i','R']; nS={'S':1,'Si':-1,'S2':2,'S2i':-2,'R':0}
nd=0; okall=True; worst=0; zerov=0
for t in range(300):
    n=rng.integers(1,5); w=[]
    for _ in range(n): w+=[kletters[rng.integers(5)],ronsite()]
    ns=sum(nS[L] for L in w if isinstance(L,str))
    for lab,k0 in (("k*",kst),("-k*",-kst)):
        for E,m in node_levels(w,k0):
            if m!=2: continue
            v=vel_matrix(w,k0,E); P=None
            # which isotypic doublet?
            W0=Wk(w,k0); import scipy.linalg as sl
            T,Zs=sl.schur(W0,output='complex'); idx=np.argsort(np.abs(wrap(np.angle(np.diag(T))-E)))[:2]; Pd=Zs[:,idx]
            ov=[np.linalg.norm(b.conj().T@Pd) for b,_ in EPS[lab]]; eps=EPS[lab][int(np.argmax(ov))][1]
            pred=abs(ns)*np.sqrt(2)/3
            nd+=1; err=np.abs(v['sv']-pred).max(); worst=max(worst,err)
            good=err<1e-9 and v['tilt']<1e-9 and (ns==0 or v['chi']==np.sign(ns)*eps) and max(ov)>1-1e-9
            okall&=good; zerov+=(ns==0)
check("random words: every exactly 2-fold level at +-k* has speed |n_S| sqrt2/3 (isotropic, untilted) and chirality sign(n_S) eps_D",
      okall and nd>50,f"{nd} doublets checked ({zerov} with n_S = 0), max speed error {worst:.1e}")
# ---- bookkeeping of the two k* doublets (exact: each letter is a scalar on each isotypic doublet)
Dp={lab:[b for b,e in EPS[lab] if e==+1][0] for lab in EPS}; Dm={lab:[b for b,e in EPS[lab] if e==-1][0] for lab in EPS}
Q0,Q3=Qs[0],Qs[3]
def sc(U,b): return np.trace(b.conj().T@U@b)/2
ok=all(abs(sc(Ps[2],Dp[l])-1)<1e-12 and abs(sc(Ps[2],Dm[l])-1)<1e-12 and abs(sc(Q0,Dp[l])-1)<1e-12 and abs(sc(Q3,Dm[l])-1)<1e-12 for l in EPS)
rl=[round(sc(RL(kst),Dp['k*']).real),round(sc(RL(kst),Dm['k*']).real),round(sc(RL(-kst),Dp['-k*']).real),round(sc(RL(-kst),Dm['-k*']).real)]
check("doublets: D+ (eps=+1) = {H_on=2} cap {Lambda=-2sqrt2}, D- (eps=-1) = {H_on=2} cap {Lambda=+2sqrt2} at both +-k*; R_L = (-1,+1) on (D+,D-) at k* and (+1,-1) at -k*",
      ok and rl==[-1,1,1,-1],f"R_L scalars {rl}")
# random words: predicted doublet eigenvalues and the zero-net-chirality condition
rng=np.random.default_rng(7); okp=True; cnt=collections.Counter() if 'collections' in dir() else None
import collections; cnt=collections.Counter()
for t in range(400):
    n=rng.integers(1,5); w=[]
    for _ in range(n): w+=[kletters[rng.integers(5)],ronsite()]
    if rng.random()<0.5:   # tune: make every on-site letter have equal phases on Lambda = -+2sqrt2 (lambda_+ = lambda_-)
        w=[L if isinstance(L,str) else L for L in w]
        w=[L if isinstance(L,str) else (sum(np.exp(1j*rng.uniform(0,6.3))*P for P in Ps)@(np.exp(1j*0.7)*(Q0+Q3)+np.exp(1j*rng.uniform(0,6.3))*Qs[1]+np.exp(1j*rng.uniform(0,6.3))*Qs[2])) for L in w]
    nR=sum(1 for L in w if isinstance(L,str) and L=='R'); ns=sum(nS[L] for L in w if isinstance(L,str))
    if ns==0: continue
    lam={}
    for lab,k0 in (("k*",kst),("-k*",-kst)):
        for eps,b in ((1,Dp[lab]),(-1,Dm[lab])):
            pr=1
            for L in w:
                if isinstance(L,str): pr*= (sc(RL(k0),b) if L=='R' else 1.0)
                else: pr*=sc(L,b)
            lam[(lab,eps)]=pr
            W0=Wk(w,k0); okp&=np.allclose(W0@b,pr*b,atol=1e-9)
    lp=np.prod([sc(L,Dp['k*']) for L in w if not isinstance(L,str)]); lm=np.prod([sc(L,Dm['k*']) for L in w if not isinstance(L,str)])
    equal=abs(lp-lm)<1e-9
    # net chirality at the quasi-energy of the k* D+ doublet, from +-k*
    E=np.angle(lam[('k*',1)]); net=0
    for lab in ("k*","-k*"):
        for eps in (1,-1):
            if abs(lam[(lab,eps)]-np.exp(1j*E))<1e-9: net+=int(np.sign(ns))*eps
    if abs(lam[('k*',1)]-lam[('k*',-1)])<1e-9: cnt['4fold']+=1; continue   # D+ and D- degenerate: a 4-fold point, not a Weyl doublet
    cnt[(nR%2,equal,net)]+=1
check("random words: W(+-k*) acts on D+- as the product of the letter scalars (S -> 1, R_L -> the signs above, on-site -> its scalar)",okp)
check("(for an exactly 2-fold k* level at E) net +-k* chirality at E vanishes exactly when n_R is odd and lambda_+ = lambda_- (product of on-site scalars equal on D+ and D-); otherwise it is +-1 or +-2",
      all((key[2]==0)==(key[0]==1 and key[1]) for key in cnt if key!='4fold') and any(n==0 for (_,_,n) in cnt),dict(cnt))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
