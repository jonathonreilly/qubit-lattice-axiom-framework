"""T111 - IS THE u(4) FLAVOUR SYMMETRY RESTORED IN THE CONTINUUM LIMIT?
Result 55's prediction, and it is the one that decides whether the framework has
a flavour symmetry at all.  The flat operator is

     D(q) = sum_a (cos q_a - 1) gamma_a  +  sum_a (i sin q_a) gamma_bar_a

with gamma_bar_a = eps_a - iota_a a SECOND Clifford set.  The u(4) flavour algebra
is the 16-dimensional commutant of {gamma_bar_a}; it is an exact symmetry of the
kinetic (sin q) part and is broken ONLY by the Wilson term (cos q - 1), whose
relative weight is O(|q|).

So the prediction is sharp: measure the breaking as a function of |q|.  If it
scales as |q| and vanishes at small momentum, the u(4) is a genuine continuum
symmetry of the framework, broken by discretisation alone -- which is a completely
different statement from Result 41's 'the framework has no non-abelian internal
symmetry'.

Measured: for each generator X of the 16-dim commutant of {gamma_bar}, the
relative breaking   ||[X, D(q)]|| / ||D(q)||   as |q| -> 0."""
import numpy as np, itertools
d=4
BAS=[]
for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
def epsm(a):
    M=np.zeros((NF,NF))
    for S in BAS:
        if a in S: continue
        T=tuple(sorted(S+(a,))); M[IDX[T],IDX[S]]=(-1)**sum(1 for i in S if i<a)
    return M
def iotam(a):
    M=np.zeros((NF,NF))
    for S in BAS:
        for pos,i in enumerate(S):
            if i!=a: continue
            T=tuple(x for x in S if x!=i); M[IDX[T],IDX[S]]+=(-1)**pos
    return M
gam=[epsm(a)+iotam(a) for a in range(d)]
gbar=[epsm(a)-iotam(a) for a in range(d)]
print("T111  the two Clifford sets")
print(f"   {{gamma_a,gamma_b}} = 2 delta: "
      f"{all(np.allclose(gam[a]@gam[b]+gam[b]@gam[a],2*(a==b)*np.eye(NF)) for a in range(d) for b in range(d))}")
print(f"   {{gbar_a,gbar_b}} = -2 delta: "
      f"{all(np.allclose(gbar[a]@gbar[b]+gbar[b]@gbar[a],-2*(a==b)*np.eye(NF)) for a in range(d) for b in range(d))}")
print(f"   {{gamma_a, gbar_b}} = 0:      "
      f"{all(np.allclose(gam[a]@gbar[b]+gbar[b]@gam[a],0) for a in range(d) for b in range(d))}")
# the flavour algebra: commutant of all gbar
A=np.vstack([np.kron(np.eye(NF),g)-np.kron(g.T,np.eye(NF)) for g in gbar])
u,s,vh=np.linalg.svd(A,full_matrices=False)
tol=1e-9*s.max(); nul=int(np.sum(s<tol))+(A.shape[1]-len(s))
print(f"   commutant of {{gbar_a}} has dimension {nul}   (u(4) is 16)")
B=vh[len(s)-nul:].conj().reshape(nul,NF,NF)
def Dq(q):
    return sum((np.cos(q[a])-1.0)*gam[a] for a in range(d)) + \
           sum(1j*np.sin(q[a])*gbar[a] for a in range(d))
print()
print("   relative breaking ||[X, D(q)]|| / ||D(q)|| for the flavour generators,")
print("   as the momentum is scaled down (continuum limit)")
print(f"   {'|q| scale':>11} {'max over X':>14} {'mean over X':>14} {'ratio to previous':>19}")
rng=np.random.default_rng(1)
dirn=rng.normal(size=d); dirn/=np.linalg.norm(dirn)
prev=None
for sc in (1.0,0.5,0.25,0.125,0.0625,0.03125):
    q=sc*dirn
    D=Dq(q); nD=np.linalg.norm(D)
    vals=[np.linalg.norm(X@D-D@X)/nD for X in B]
    mx=max(vals); mn=float(np.mean(vals))
    r=(prev/mx) if prev else float('nan'); prev=mx
    print(f"   {sc:11.5f} {mx:14.6e} {mn:14.6e} {r:19.3f}", flush=True)
print()
print("   breaking falling linearly with |q| (ratio ~2 per halving) means the u(4)")
print("   is EXACT in the continuum and broken only by the lattice Wilson term --")
print("   so the framework does have a non-abelian flavour symmetry, and Result 41's")
print("   'commutant is only the phase' is a statement about the lattice operator.")
print()
print("   control: the same measurement for the KINETIC part alone (should be 0)")
for sc in (1.0,0.25):
    q=sc*dirn
    Dk=sum(1j*np.sin(q[a])*gbar[a] for a in range(d))
    vals=[np.linalg.norm(X@Dk-Dk@X)/max(np.linalg.norm(Dk),1e-30) for X in B]
    print(f"   |q|={sc}: max breaking of the kinetic part = {max(vals):.3e}")
