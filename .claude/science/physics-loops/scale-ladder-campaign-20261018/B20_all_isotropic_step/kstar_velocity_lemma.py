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
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
