"""
T318 - are the framework's monopoles free, or confined into pairs?

R199's charge-monopole route needs the monopole to be an independent excitation.
But the framework lives in the ORDERED phase (R175: the Born point is ~15% above
t_c), where the charge-1 matter field condenses and HIGGSES the Berry U(1). In a
Higgsed U(1), magnetic flux is squeezed into tubes and monopoles are linearly
confined into monopole-antimonopole pairs. If that is happening here, the
composite of R199 is not a viable excitation and the route closes.

Test: collect defect positions over many independent configurations and measure
the monopole-antimonopole pair correlation g(r) against the RANDOM-placement
expectation computed from the same lattice geometry.
  confined  -> g(r) strongly peaked at small r, falling fast
  free      -> g(r) ~ 1, i.e. positions uncorrelated
Control: the +/- counts must be equal in every configuration (total flux 0), and
the SAME-sign correlation is reported alongside -- a confining tube acts on
opposite signs, so if BOTH signs show the same peak the effect is not binding
but a density/locality artefact.
"""
import numpy as np
L=24; NCFG=120
def mc(rng,sweeps=1400):
    v=rng.normal(size=(L,L,L,3)); v/=np.linalg.norm(v,axis=-1,keepdims=True)
    for sw in range(sweeps):
        for _ in range(L**3):
            a,b,c=rng.integers(0,L,3)
            nbs=np.array([v[(a+1)%L,b,c],v[a-1,b,c],v[a,(b+1)%L,c],
                          v[a,b-1,c],v[a,b,(c+1)%L],v[a,b,c-1]])
            new=rng.normal(size=3); new/=np.linalg.norm(new); old=v[a,b,c]
            num=np.prod(1+(nbs@new)); den=np.prod(1+(nbs@old))
            if den<=0 or num<0: continue
            if num>=den or rng.random()<num/den: v[a,b,c]=new
    return v
def charges(v):
    th=np.arccos(np.clip(v[...,2],-1,1)); ph=np.arctan2(v[...,1],v[...,0])
    psi=np.stack([np.cos(th/2), np.sin(th/2)*np.exp(1j*ph)],axis=-1)
    lk=lambda a,b: np.sum(np.conj(a)*b,axis=-1)
    def pl(mu,nu):
        p1=psi; p2=np.roll(psi,-1,axis=mu)
        p3=np.roll(np.roll(psi,-1,axis=mu),-1,axis=nu); p4=np.roll(psi,-1,axis=nu)
        return np.angle(lk(p1,p2)*lk(p2,p3)*lk(p3,p4)*lk(p4,p1))
    F01,F12,F02=pl(0,1),pl(1,2),pl(0,2)
    tot=(F12-np.roll(F12,-1,axis=0)-F02+np.roll(F02,-1,axis=1)+F01-np.roll(F01,-1,axis=2))
    return np.round(tot/(2*np.pi)).astype(int)
def pbc(d): return np.minimum(d%L,(-d)%L)
opp=[]; same=[]; npos=0; bad=0
for c in range(NCFG):
    rng=np.random.default_rng(1000+c)
    n=charges(mc(rng))
    P=np.argwhere(n>0); M=np.argwhere(n<0)
    if len(P)!=len(M): bad+=1
    npos+=len(P)
    for a in P:
        for b in M: opp.append(np.linalg.norm(pbc(a-b)))
    for i,a in enumerate(P):
        for b in P[i+1:]: same.append(np.linalg.norm(pbc(a-b)))
opp=np.array(opp); same=np.array(same)
print(f"{NCFG} configs, L={L}.  total monopoles {npos}, mean per config {npos/NCFG:.2f}")
print(f"control: configs with unequal +/- counts = {bad}  (must be 0)\n")
# random expectation: pair separations of uniformly placed points on the torus
rr=np.random.default_rng(0)
A=rr.integers(0,L,size=(400000,3)); B=rr.integers(0,L,size=(400000,3))
rand=np.linalg.norm(pbc(A-B),axis=1)
bins=np.arange(0,L/2+1,1.5)
ho,_=np.histogram(opp,bins=bins); hs,_=np.histogram(same,bins=bins); hr,_=np.histogram(rand,bins=bins)
hr=hr/hr.sum()
print("     r range      g(r) opposite-sign    g(r) same-sign")
for i in range(len(bins)-1):
    if hr[i]<1e-6: continue
    go=(ho[i]/max(ho.sum(),1))/hr[i]; gs=(hs[i]/max(hs.sum(),1))/hr[i]
    print(f"   {bins[i]:4.1f}-{bins[i+1]:4.1f}      {go:8.3f}            {gs:8.3f}")
print("\n  confined -> opposite-sign g(r) sharply peaked at small r, same-sign flat")
print("  free     -> both ~ 1")
