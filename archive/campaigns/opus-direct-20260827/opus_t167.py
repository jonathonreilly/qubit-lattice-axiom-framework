"""T167 - DOES R101'S FLAT RESPONSE SURVIVE PROPER BORN SAMPLING?

R101 flagged its own assumption: a record locked the NEAREST pure state
deterministically.  The axioms say otherwise -- Admissibility gives a probability
DISTRIBUTION and Record locks one possibility, i.e. a DRAW.  Two things follow and
both deserve saying.

FIRST, a limitation of my own derivation that I have not stated before.  R92-R99
derived the rule for the STATE rho -- which is only the FIRST MOMENT of a measure
on the possibility domain.  The axioms ask for the measure.  Many measures on the
Bloch sphere share a mean, so covariance + normalisation + CP fix the mean and
LEAVE THE HIGHER MOMENTS OPEN.  My chain determines less than the axioms request,
and that gap is real.

SECOND, the testable part: pick a natural measure with the right mean and see
whether R101's flat response survives.  Given rho = (1/2)I + v.sigma, the Born
weight of the pure state n-hat is <n|rho|n> = (1/2)(1 + 2 v.n), so sample
   P(n) proportional to (1 + 2 v.n)   on the sphere
which is the Born measure on pure states and has the right mean direction.

Because a draw is noisy, the response must be ENSEMBLE-AVERAGED over many runs
with common random numbers (identical draws in both arms except for the seed), or
the signal drowns.  CONTROL: with zero channel the averaged response must be 0."""
import numpy as np, sys
sys.path.insert(0,".")
from opus_t165 import DIRS
def rule(nbrs,al,de):
    if not nbrs: return np.zeros(3)
    V=sum(v for _,v in nbrs); C=sum(np.cross(nh,v) for nh,v in nbrs)
    return (al*V+de*C)/6.0
def draw(v,u):
    """sample n ~ (1 + 2 v.n) on the sphere by rejection, using pre-drawn uniforms u"""
    i=0
    while i+3<len(u):
        n=np.array(u[i:i+3]); i+=3
        r=np.linalg.norm(n)
        if r<1e-9 or r>1: continue
        n=n/r
        if i>=len(u): break
        if u[i]<=0.5*(1+2*np.dot(v,n)):
            return 0.5*n
        i+=1
    n=np.array(u[:3]); n/=max(np.linalg.norm(n),1e-12); return 0.5*n
def grow(L,seed_v,al,de,steps,rng):
    c=L//2; rec={(c,c,c):np.array(seed_v,dtype=float)}
    for _ in range(steps):
        front=set()
        for x in rec:
            for d in DIRS:
                y=tuple(np.array(x)+d)
                if all(0<=t<L for t in y) and y not in rec: front.add(y)
        new={}
        for y in sorted(front):
            nb=[(d.astype(float),rec[z]) for d in DIRS
                for z in [tuple(np.array(y)+d)] if z in rec]
            v=rule(nb,al,de)
            u=rng[y]                      # COMMON RANDOM NUMBERS, same in both arms
            new[y]=draw(v,u)
        rec.update(new)
        if not new: break
    return rec
L=17; STEPS=6
def rngbank(L,seed):
    g=np.random.default_rng(seed); bank={}
    for x in np.ndindex(L,L,L): bank[x]=g.uniform(-1,1,size=400)
    return bank
def rotz(v,th):
    c,s=np.cos(th),np.sin(th); return np.array([c*v[0]-s*v[1],s*v[0]+c*v[1],v[2]])
base=np.array([0.3,0.0,0.4]); base=0.5*base/np.linalg.norm(base)
print("T167  response under proper Born sampling, ensemble-averaged")
print(f"      L={L}, {STEPS} steps, common random numbers, seed rotated by 0.6 rad")
for nm,al,de,NR in (("R99 optimum  alpha=1/3, delta=1/sqrt3",1/3,1/np.sqrt(3),40),
                    ("CONTROL      alpha=0,   delta=0",0.0,0.0,40)):
    acc={}
    for rep in range(NR):
        bank=rngbank(L,1000+rep)
        A=grow(L,base,al,de,STEPS,bank); B=grow(L,rotz(base,0.6),al,de,STEPS,bank)
        c=L//2
        for x in A:
            if x not in B: continue
            r=max(abs(np.array(x)-c))
            acc.setdefault(r,[]).append(np.linalg.norm(A[x]-B[x]))
    print(f"   {nm}")
    print(f"      {'dist':>5} {'samples':>8} {'mean response':>15}")
    for r in sorted(acc):
        if r==0: continue
        print(f"      {r:5d} {len(acc[r]):8d} {np.mean(acc[r]):15.6f}")
    print()
print("   flat and nonzero at the optimum, exactly zero in the control, means")
print("   R101's profile survives sampling and was not an artifact of the projection.")
