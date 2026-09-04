"""
T319 - are the framework's monopoles free, or confined into pairs?
(T318 was correct but scalar-looped: 2.3e9 Python site updates. Same physics,
checkerboard-vectorised -- Z^3 is bipartite, so given one sublattice every site
of the other is independent and they update simultaneously.)

Why this is the prerequisite for R199: the framework sits in the ORDERED phase
(R175: Born point ~15% above t_c), where the charge-1 field condenses and HIGGSES
the Berry U(1). In a Higgsed U(1) magnetic flux is squeezed into tubes and
monopoles are linearly CONFINED into monopole-antimonopole pairs. If so, R199's
charge-monopole composite is not a viable excitation.

  confined -> opposite-sign g(r) sharply peaked at small r
  free     -> g(r) ~ 1

CONTROL: the SAME-sign correlation is reported alongside. A confining tube acts
only between opposite charges, so if BOTH signs peak identically the signal is a
density/locality artefact, not binding.
"""
import numpy as np
L=24; NCFG=60; SWEEPS=900; BURN=300
idx=np.indices((L,L,L)); par=(idx.sum(axis=0)%2).astype(bool)
def sweep(v,rng):
    for sub in (True,False):
        m=(par==sub)
        nb=(np.roll(v,1,0)+np.roll(v,-1,0)+np.roll(v,1,1)+np.roll(v,-1,1)
            +np.roll(v,1,2)+np.roll(v,-1,2))
        nbs=np.stack([np.roll(v,s,ax) for ax in range(3) for s in (1,-1)],axis=0)
        new=rng.normal(size=v.shape); new/=np.linalg.norm(new,axis=-1,keepdims=True)
        do=np.einsum('n...c,...c->n...',nbs,v)      # 6 x L x L x L
        dn=np.einsum('n...c,...c->n...',nbs,new)
        wo=np.prod(1.0+do,axis=0); wn=np.prod(1.0+dn,axis=0)
        acc=(wn>=wo)|(rng.random(wo.shape)*wo<wn)
        acc&=m&(wo>0)&(wn>=0)
        v=np.where(acc[...,None],new,v)
    return v
def charges(v):
    th=np.arccos(np.clip(v[...,2],-1,1)); ph=np.arctan2(v[...,1],v[...,0])
    psi=np.stack([np.cos(th/2),np.sin(th/2)*np.exp(1j*ph)],axis=-1)
    lk=lambda a,b: np.sum(np.conj(a)*b,axis=-1)
    def pl(mu,nu):
        p1=psi; p2=np.roll(psi,-1,axis=mu)
        p3=np.roll(np.roll(psi,-1,axis=mu),-1,axis=nu); p4=np.roll(psi,-1,axis=nu)
        return np.angle(lk(p1,p2)*lk(p2,p3)*lk(p3,p4)*lk(p4,p1))
    F01,F12,F02=pl(0,1),pl(1,2),pl(0,2)
    tot=(F12-np.roll(F12,-1,axis=0)-F02+np.roll(F02,-1,axis=1)+F01-np.roll(F01,-1,axis=2))
    return np.round(tot/(2*np.pi)).astype(int)
def pbc(d): return np.minimum(d%L,(-d)%L)
opp=[];same=[];tot=0;bad=0
for c in range(NCFG):
    rng=np.random.default_rng(2000+c)
    v=rng.normal(size=(L,L,L,3)); v/=np.linalg.norm(v,axis=-1,keepdims=True)
    for s in range(SWEEPS): v=sweep(v,rng)
    n=charges(v); P=np.argwhere(n>0); M=np.argwhere(n<0)
    if len(P)!=len(M): bad+=1
    tot+=len(P)
    for a in P:
        opp.extend(np.linalg.norm(pbc(a-M),axis=1) if len(M) else [])
    for i,a in enumerate(P):
        if len(P)>i+1: same.extend(np.linalg.norm(pbc(a-P[i+1:]),axis=1))
opp=np.array(opp);same=np.array(same)
print(f"L={L}, {NCFG} configs.  monopoles found: {tot}  ({tot/NCFG:.2f}/config)")
print(f"control: configs with unequal +/- counts = {bad}  (must be 0)")
print(f"pairs: opposite-sign {len(opp)}, same-sign {len(same)}\n")
rr=np.random.default_rng(0)
A=rr.integers(0,L,size=(500000,3)); B=rr.integers(0,L,size=(500000,3))
rand=np.linalg.norm(pbc(A-B),axis=1)
bins=np.arange(0,L/2+0.1,2.0)
ho,_=np.histogram(opp,bins=bins); hs,_=np.histogram(same,bins=bins); hr,_=np.histogram(rand,bins=bins)
hr=hr/hr.sum()
print("     r range     g(r) OPPOSITE     g(r) SAME     (1.00 = uncorrelated)")
for i in range(len(bins)-1):
    if hr[i]<1e-6: continue
    go=(ho[i]/max(ho.sum(),1))/hr[i]; gs=(hs[i]/max(hs.sum(),1))/hr[i]
    print(f"   {bins[i]:4.1f}-{bins[i+1]:4.1f}     {go:8.3f}        {gs:8.3f}")
