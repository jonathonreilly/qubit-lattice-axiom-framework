"""Kill-round checks for T11 (Claude Sonnet 5.5, same family as attacker).
K1 replication of landed census on the 2x3 rectangle with the attack's rule (landed: 98 orientations, 28 laws).
K2 second clock: formed-record odds under precession depend on f/omega, invariant under common rescale.
K3 tick fixed as unit: parallel-kernel two-site correlation vs q (attack's closed form) -> H1 == (q->0) premise.
"""
import itertools, numpy as np, sys
sys.path.insert(0,'.')
import test_T11 as T
# K1
E=[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)]
n=6; A=T.adj_of(n,E)
perms=list(itertools.permutations(range(n)))
sigs={}
for p in perms: sigs.setdefault(T.orientation_sig(p,E),[]).append(p)
laws={sg:tuple(np.round(T.law_float_all(n,A,ps[0]),12)) for sg,ps in sigs.items()}
print("K1 2x3 rectangle: orientations",len(sigs),"| acyclic count |chi(-1)|",abs(T.chi_at(n,E,-1)),"| distinct laws",len(set(laws.values())),"(landed 2026-09-13 note: 98 and 28)")
# K2
from scipy.integrate import quad
def odds(f,w):
    # formation density f e^{-ft}; perpendicular Bloch component cos(wt); P(+)=(1+<cos>)/2
    val,_=quad(lambda t: f*np.exp(-f*t)*np.cos(w*t),0,np.inf,limit=500)
    return (1+val)/2
print("K2 P(+ on perpendicular menu):")
for f,w in [(0.1,1),(1,1),(10,1),(0.5,5),(5,50),(100,100)]:
    print(f"  f={f:>5} omega={w:>5} f/omega={f/w:>6.2f}  P+={odds(f,w):.6f}  closed={(1+f*f/(f*f+w*w))/2:.6f}")
# K3
print("K3 two adjacent sites, tick = unit, per-tick formation prob q: E[st] absorbed =")
for q in [1,2/3,1/2,1/3,0.1,0.01,0.001]:
    print(f"  q={q:<8.4g} E={0.6*2*(1-q)/(2-q):.4f}")
