"""T165 - RECORD GROWTH AS A CAUSAL PROCESS: does information propagate, and how far?

The axioms leave the record FORMATION SITE and RATE downstream, so any simulation
must supply them and say so.  I supply the simplest possible one and flag it:
   ASSUMPTION (not axiom content): at each step, every unrecorded site with at
   least one recorded neighbour forms a record simultaneously.
Everything else is derived: the distribution comes from the R94 channel at the
R99 optimum (alpha = 1/3, delta = 1/sqrt(3)), applied to RECORDED neighbours only,
because the Record axiom says an unrecorded site cannot be read.

The question is whether the seed's state influences distant records -- i.e.
whether information propagates at all through record growth, and with what
profile.  The record FRONT advances one site per step by construction; the
INFORMATION need not keep up.

Measurement: run the growth twice from the same seed site with two ANTIPODAL seed
states, everything else (random draws) held identical by seeding the RNG the same
way.  The difference between the two runs at distance r is the causal influence of
the seed.  A sharp cutoff = a light cone.  Exponential decay = a correlation
length.  No difference = the seed does not propagate at all.

CONTROL: with delta = 0 (no curl channel) and alpha = 0 there is no channel at all
and the influence must be exactly zero everywhere beyond the seed."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
DIRS=[np.array(d) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
def cross(a,b): return np.cross(a,b)
def rule(nbrs,al,de):
    """nbrs: list of (n_hat, v) for RECORDED neighbours only.  Returns v_out."""
    if not nbrs: return np.zeros(3)
    V=sum(v for _,v in nbrs); C=sum(cross(nh,v) for nh,v in nbrs)
    return (al*V+de*C)/6.0
def grow(L,seed_v,al,de,steps,rng_seed=0):
    rng=np.random.default_rng(rng_seed)
    c=L//2
    rec={}; rec[(c,c,c)]=np.array(seed_v,dtype=float)
    for step in range(steps):
        front=set()
        for x in rec:
            for d in DIRS:
                y=tuple(np.array(x)+d)
                if all(0<=t<L for t in y) and y not in rec: front.add(y)
        new={}
        for y in sorted(front):
            nb=[]
            for d in DIRS:
                z=tuple(np.array(y)+d)
                if z in rec: nb.append((d.astype(float),rec[z]))
            v=rule(nb,al,de)
            # a record locks ONE possibility: project to the nearest pure state
            # (null vector), with a random draw when the rule gives no direction
            nrm=np.linalg.norm(v)
            if nrm<1e-12:
                u=rng.normal(size=3); u/=np.linalg.norm(u); v=0.5*u
            else:
                v=0.5*v/nrm
            new[y]=v
        rec.update(new)
        if not new: break
    return rec
L=25; STEPS=9
print("T165  does the seed's state propagate through record growth?")
print(f"      L={L}, {STEPS} steps, alpha=1/3, delta=1/sqrt(3) (the R99 optimum)")
print("      ASSUMPTION (not axiom content): all boundary sites record each step")
print()
for nm,al,de in (("R99 optimum  alpha=1/3, delta=1/sqrt3",1/3,1/np.sqrt(3)),
                 ("CONTROL      alpha=0,   delta=0",0.0,0.0)):
    A=grow(L,[0,0,0.5],al,de,STEPS,rng_seed=7)
    B=grow(L,[0,0,-0.5],al,de,STEPS,rng_seed=7)
    c=L//2
    print(f"   {nm}")
    print(f"      {'dist':>5} {'sites':>6} {'mean |v_A - v_B|':>18}")
    for r in range(1,STEPS+1):
        ds=[]
        for x in A:
            d=max(abs(np.array(x)-c))
            if d==r and x in B: ds.append(np.linalg.norm(A[x]-B[x]))
        if ds: print(f"      {r:5d} {len(ds):6d} {np.mean(ds):18.6f}")
    print()
print("   a profile falling with distance = a correlation length;")
print("   a sharp cutoff = a light cone;  all zeros in the CONTROL = the test works.")
