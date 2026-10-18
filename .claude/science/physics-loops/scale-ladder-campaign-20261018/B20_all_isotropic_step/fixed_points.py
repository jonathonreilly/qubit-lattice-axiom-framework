#!/usr/bin/env python3
"""B20 part 4 support: points whose little group forces isotropy.  A linear Weyl cone at k is forced isotropic
(and untilted) by its little group iff the little group's rotation parts contain T (the only subgroups of O acting
irreducibly on R^3 are T and O).  The affine PSG action is k -> R k + pi s_R (s_R measured here as the unique
shift with spec W(Rk + pi s_R) = spec W(k) for a generic symmetric word; one per rotation, as in the note).
We list the T-fixed and O-fixed points modulo three translation groups:
  (a) 2pi Z^3 (any word), (b) + pi(1,1,1) (exact period of S, hence of words without R_L),
  (c) (pi/2) Z^3 (the corner-plane tastes Z_i of S^2 words whose last on-site factor commutes with the Z_i).
Exhaustive over k in (pi/8) Z^3, which contains every solution (the fixed-point congruences have
denominators dividing 4 for (a),(b) and 8 for (c)).  Prints PASS/FAIL, TOTAL."""
import itertools, time, numpy as np
exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
t0=time.time(); PASS=FAIL=0
def check(name,ok,detail=""):
    global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}",flush=True)
rots=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product((1,-1),repeat=3):
        M=np.zeros((3,3))
        for i in range(3): M[i,p[i]]=s[i]
        if np.linalg.det(M)>0: rots.append(M)
rng=np.random.default_rng(0); KS=rng.uniform(-np.pi,np.pi,(3,3))
w=['S',onH(1,2,unit=1),'R',onL(1,5,2,unit=1),'S2',onH(3,7,unit=1)]
def same(a,b):
    e1=np.linalg.eigvals(a); e2=np.linalg.eigvals(b); used=np.zeros(12,bool)
    for x in e1:
        d=np.abs(e2-x); d[used]=9; j=np.argmin(d)
        if d[j]>1e-7: return False
        used[j]=True
    return True
SR=[]
for R in rots:
    ss=[np.array(s) for s in itertools.product((0,1),repeat=3) if all(same(Wk(w,R@k+np.pi*np.array(s)),Wk(w,k)) for k in KS)]
    SR.append(ss)
check("each of the 24 rotations has exactly one shift class s_R (generic symmetric word), all 8 classes occur",
      all(len(s)==1 for s in SR) and len({tuple(s[0]) for s in SR})==8)
SR=[s[0] for s in SR]
isT=[abs(np.trace(R)-3)<1e-9 or abs(np.trace(R)+1)<1e-9 and np.allclose(np.abs(np.diag(R)),1) or abs(np.trace(R))<1e-9 and np.allclose(np.diag(R),0) for R in rots]
assert sum(isT)==12
def inlat(v,lat):
    v=np.asarray(v)/np.pi
    if lat=='a': return np.allclose(np.mod(v+1e-9,2),0,atol=1e-7) or np.allclose(np.mod(v+1e-9,2),2,atol=1e-7)
    if lat=='b': return inlat(v*np.pi,'a') or inlat(v*np.pi-np.pi*np.ones(3),'a')
    if lat=='c': x=np.mod(v*2+1e-9,1); return np.all((x<1e-7)|(x>1-1e-7))
def fixed(k,group,lat): return all(inlat(R@k+np.pi*s-k,lat) for R,s,t in zip(rots,SR,isT) if (t or group=='O'))
def reduce(k,lat):
    if lat=='c': return tuple(np.round(np.mod(k/np.pi+1e-9,0.5),4))
    v=np.mod(k/np.pi+1e-9,2)
    if lat=='b':
        v2=np.mod(v+1,2); v=min(tuple(np.round(v,4)),tuple(np.round(v2,4))); return v
    return tuple(np.round(v,4))
pts=[np.array(p)*np.pi/8 for p in itertools.product(range(16),repeat=3)]
res={}
for lat in 'abc':
    for grp in 'TO':
        res[(lat,grp)]=sorted({reduce(k,lat) for k in pts if fixed(k,grp,lat)})
        print(f"  lattice ({lat}), {grp}-fixed points (k/pi, reduced):",res[(lat,grp)])
check("(a) modulo 2pi Z^3 the O-fixed and the T-fixed points are exactly +-k* = +-(pi/2)(1,-1,1)",
      res[('a','O')]==res[('a','T')] and set(res[('a','O')])=={(0.5,1.5,0.5),(1.5,0.5,1.5)})
check("(b) modulo 2pi Z^3 + pi(1,1,1)Z (words without R_L) the T-fixed set is the single class k* = -k*",len(res[('b','T')])==1 and res[('b','T')]==res[('b','O')])
check("(c) modulo (pi/2) Z^3 the T-fixed set is {0 (= k*), (pi/4)(1,1,1)}, both O-fixed",
      set(res[('c','T')])=={(0,0,0),(0.25,0.25,0.25)} and res[('c','T')]==res[('c','O')])
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
