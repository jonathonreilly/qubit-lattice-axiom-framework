"""T168 - the response under sampling, with the RIGHT estimator.

T167 measured the per-site difference between two arms sharing common random
numbers, and got essentially zero everywhere.  That was my probe failing: shared
uniforms make the ACCEPTED DRAW LITERALLY IDENTICAL in both arms whenever the
acceptance decision coincides, so the difference is zero by construction and only
a rare acceptance flip shows anything.  Variance reduction killed the signal.

The correct estimator for a linear response under a stochastic rule is the
ENSEMBLE-AVERAGED STATE: average v(x) over many independent runs in each arm, then
compare the averages.

There is also an exact fact worth having first.  Sampling from the Born measure on
pure states, P(n) ~ (1 + 2 v.n), has mean
   <0.5 n> = (|v|/3) v-hat = v/3
since <cos^2> = 1/3 on the sphere.  So THE RECORD DRAW CONTRACTS THE MEAN BY
EXACTLY 1/3, on top of whatever the channel does.  Verify that numerically, then
measure the profile."""
import numpy as np, sys
sys.path.insert(0,".")
from opus_t165 import DIRS
def rule(nbrs,al,de):
    if not nbrs: return np.zeros(3)
    V=sum(v for _,v in nbrs); C=sum(np.cross(nh,v) for nh,v in nbrs)
    return (al*V+de*C)/6.0
def draw(v,g):
    for _ in range(200):
        n=g.normal(size=3); n/=np.linalg.norm(n)
        if g.uniform()<=0.5*(1+2*np.dot(v,n)): return 0.5*n
    n=g.normal(size=3); return 0.5*n/np.linalg.norm(n)
print("T168  (1) does the record draw contract the mean by exactly 1/3?")
g=np.random.default_rng(5)
print(f"   {'|v| in':>8} {'<0.5 n> along v-hat':>22} {'|v|/3':>10} {'ratio':>8}")
for mag in (0.5,0.3,0.1):
    v=np.array([0,0,mag]); acc=np.zeros(3)
    N=200000
    for _ in range(N): acc+=draw(v,g)
    m=acc/N
    print(f"   {mag:8.3f} {m[2]:22.6f} {mag/3:10.6f} {m[2]/(mag/3):8.4f}")
print()
def grow(L,seed_v,al,de,steps,g):
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
            new[y]=draw(rule(nb,al,de),g)
        rec.update(new)
        if not new: break
    return rec
L=13; STEPS=5; NR=300
def rotz(v,th):
    c,s=np.cos(th),np.sin(th); return np.array([c*v[0]-s*v[1],s*v[0]+c*v[1],v[2]])
base=np.array([0.3,0.0,0.4]); base=0.5*base/np.linalg.norm(base)
print(f"(2) ensemble-averaged response, L={L}, {STEPS} steps, {NR} runs/arm, seed rotated 1.2 rad")
for nm,al,de in (("R99 optimum",1/3,1/np.sqrt(3)),("CONTROL alpha=delta=0",0.0,0.0)):
    S={}
    for arm,sv in (('A',base),('B',rotz(base,1.2))):
        g=np.random.default_rng(77 if arm=='A' else 78)
        tot={}
        for _ in range(NR):
            R=grow(L,sv,al,de,STEPS,g)
            for x,v in R.items(): tot[x]=tot.get(x,np.zeros(3))+v
        S[arm]={x:t/NR for x,t in tot.items()}
    c=L//2; acc={}
    for x in S['A']:
        if x not in S['B'] or x==(c,c,c): continue
        r=max(abs(np.array(x)-c)); acc.setdefault(r,[]).append(np.linalg.norm(S['A'][x]-S['B'][x]))
    print(f"   {nm}")
    print(f"      {'dist':>5} {'sites':>6} {'|<v>_A - <v>_B|':>17}")
    for r in sorted(acc): print(f"      {r:5d} {len(acc[r]):6d} {np.mean(acc[r]):17.6f}")
    print()
print("   a profile falling with distance now means a genuine correlation length;")
print("   the control bounds the sampling noise floor.")
