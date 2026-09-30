"""C: (i) how wide is the chart's preimage of the full repo-quoted NuFIT-6.1 3sigma box (near basin)?
(ii) mechanical look-elsewhere: every library triple (a,b,c) for the equations Tr H = a, delta q_+ = b, det H = c;
how many have a chamber solution inside the box?  Library is mechanical (all p/q with q<=6, plus the square-root forms
sqrt(n)/q for n in {2,3,6,8}, q in {1,2,3}); NOT built around the proposal's constants."""
import math, itertools, numpy as np
from scipy import optimize
from common import BOX61, BOX53, observables
E1=math.sqrt(8/3); E2=math.sqrt(8)/3; GAMMA=0.5
T_M=np.array([[1,0,0],[0,0,1],[0,1,0]],dtype=complex)
T_D=np.array([[0,-1,1],[-1,1,0],[1,0,-1]],dtype=complex)
T_Q=np.array([[0,1,1],[1,0,1],[1,1,0]],dtype=complex)
HB=np.array([[0,E1,-E1-1j*GAMMA],[E1,0,-E2],[-E1+1j*GAMMA,-E2,0]],dtype=complex)
def H(m,d,q): return HB+m*T_M+d*T_D+q*T_Q
def obs(x):
    w,V=np.linalg.eigh(H(*x)); o=np.argsort(w.real); return observables(V[o][[2,1,0],:] if False else V[:,o][[2,1,0],:])
def inb(o,B): return B["s12"][0]<=o[0]<=B["s12"][1] and B["s13"][0]<=o[1]<=B["s13"][1] and B["s23"][0]<=o[2]<=B["s23"][1]
rng=np.random.default_rng(5)
# ---- (i) preimage of the full 3-sigma box, near basin (vectorised)
N=6_000_000
m=rng.uniform(-1.2,1.6,N); d=rng.uniform(0.4,1.8,N); q=rng.uniform(0.2,1.6,N)
k=(q+d>=E1); m,d,q=m[k],d[k],q[k]
Hs=HB[None]+m[:,None,None]*T_M[None]+d[:,None,None]*T_D[None]+q[:,None,None]*T_Q[None]
w,V=np.linalg.eigh(Hs); P=V[:,[2,1,0],:]; a=np.abs(P)**2
s13=a[:,0,2]; c13=1-s13; s12=a[:,0,1]/c13; s23=a[:,1,2]/c13
ok=(w>0).sum(1)==1
for nm,B in (("NuFIT-6.1 3sigma",BOX61),("NuFIT-5.3 3sigma (lane)",BOX53)):
    b=ok&(s12>=B["s12"][0])&(s12<=B["s12"][1])&(s13>=B["s13"][0])&(s13<=B["s13"][1])&(s23>=B["s23"][0])&(s23<=B["s23"][1])
    print(f"\n(i) {nm}: in-box samples {b.sum()} of {ok.sum()} baseline-signature chamber samples")
    if b.sum():
        det=np.linalg.det(Hs[b]).real
        for lab,arr,ref in (("m",m[b],2/3),("delta",d[b],None),("q_+",q[b],None),("delta*q_+",(d*q)[b],2/3),("det H",det,E2)):
            lo,hi=arr.min(),arr.max(); ctr=(lo+hi)/2
            print(f"    {lab:10s} range [{lo:.4f},{hi:.4f}]  half-width/centre = {(hi-lo)/2/abs(ctr)*100:5.1f}%")
        print(f"    proposal values: Tr H=2/3 inside range? {m[b].min()<=2/3<=m[b].max()};  delta*q_+=2/3 inside? {(d*q)[b].min()<=2/3<=(d*q)[b].max()};  det H=sqrt8/3={E2:.4f} inside? {det.min()<=E2<=det.max()}")
# ---- (ii) mechanical library look-elsewhere
lib={}
for q_ in range(1,7):
    for p_ in range(1,2*q_+1):
        lib[f"{p_}/{q_}"]=p_/q_
for n in (2,3,6,8):
    for q_ in (1,2,3):
        lib[f"sqrt{n}/{q_}"]=math.sqrt(n)/q_
vals={}
for kx,v in lib.items():
    key=round(v,9)
    if key not in vals: vals[key]=kx
lib=dict(vals)     # {value: name}, unique values
print(f"\n(ii) mechanical library: {len(lib)} distinct constants; triples = {len(lib)**3}")
# prune each equation's constants to the ranges realised in the (looser) NuFIT-5.3 box preimage +-20% to keep it fast
b=ok&(s12>=BOX53["s12"][0])&(s12<=BOX53["s12"][1])&(s13>=BOX53["s13"][0])&(s13<=BOX53["s13"][1])&(s23>=BOX53["s23"][0])&(s23<=BOX53["s23"][1])
det=np.linalg.det(Hs[b]).real
rng_m=(m[b].min()*0.8,m[b].max()*1.2); rng_dq=((d*q)[b].min()*0.8,(d*q)[b].max()*1.2); rng_det=(det.min()-0.3*abs(det.min()),det.max()+0.3*abs(det.max()))
A=[v for v in lib if rng_m[0]<=v<=rng_m[1]]; Bv=[v for v in lib if rng_dq[0]<=v<=rng_dq[1]]; Cv=[v for v in lib if rng_det[0]<=v<=rng_det[1]]
print(f"    constants within loose coordinate ranges: Tr H:{len(A)}  delta*q:{len(Bv)}  det:{len(Cv)}  -> {len(A)*len(Bv)*len(Cv)} triples to solve")
starts=[np.array([m0,d0,q0]) for m0 in (0.0,0.4,0.7) for d0 in (0.7,0.95,1.2) for q0 in (0.5,0.75,1.0)]
hit1=set(); hit3=set(); hit3_53=set()
BOX53_1={"s12":(0.295,0.318),"s13":(0.02063,0.02297),"s23":(0.530,0.558)}
for ca,cb,cc in itertools.product(A,Bv,Cv):
    def res(x): return [x[0]-ca, x[1]*x[2]-cb, np.linalg.det(H(*x)).real-cc]
    found=[]
    for x0 in starts:
        try: x,info,ier,msg=optimize.fsolve(res,x0,xtol=1e-12,full_output=True)
        except Exception: continue
        if ier!=1 or max(abs(r) for r in res(x))>1e-9 or x[1]+x[2]<E1-1e-9: continue
        if not any(np.allclose(x,f,atol=1e-6) for f in found): found.append(x)
    for x in found:
        w_,V_=np.linalg.eigh(H(*x))
        if (w_>0).sum()!=1: continue
        o=observables(V_[:,np.argsort(w_)][[2,1,0],:])
        if inb(o,BOX61): hit3.add((lib[ca],lib[cb],lib[cc]))
        if inb(o,BOX53): hit3_53.add((lib[ca],lib[cb],lib[cc]))
        if inb(o,BOX53_1): hit1.add((lib[ca],lib[cb],lib[cc]))
print(f"    triples with a baseline-signature chamber solution inside NuFIT-6.1 3sigma box: {len(hit3)}")
print(f"    triples with a baseline-signature chamber solution inside NuFIT-5.3 3sigma box: {len(hit3_53)}")
print(f"    triples inside the NuFIT-5.3 1sigma box (the proposal's own claim): {len(hit1)}")
for t in sorted(hit1): print("      5.3 1sigma hit:",t)
for t in sorted(hit3): print("      6.1 hit:",t)
print("    (the lane's proposal is ('2/3','2/3','sqrt8/3') -- present among the hits above iff it is in the library and the box)")
