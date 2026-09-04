"""T60 - DOES MATTER SOURCE THE GEOMETRY, ON THE ARENA THAT PASSES THE GATE?
This is Result 17's question -- the one whose gravitational reading Results 19-22
had to withdraw because the rigid lattice was not diffeomorphism invariant --
asked again on the arena that IS covariant (R23-R26), curved (R25), doubler-free
(R25), and carries a variational principle with a nontrivial solution (R27).

Result 27: with NO matter, the round sphere is a critical point of the multiplet
mean at fixed area (symmetric, quadratic, coefficient +0.223, mesh-independent).
So the free theory picks the round sphere.  The question now:

    put an INHOMOGENEOUS mass field on the sphere.  Does the critical shape MOVE?

If the critical eps stays 0 for uniform matter and shifts with the matter's own
quadrupole for l=2 matter -- tracking its sign and scaling with its amplitude --
that is matter sourcing geometry, measured on an arena where the gauge/shape
separation has already been verified (R26, factor 7760).

Family: exactly area-preserving spheroids (as in R27).  Matter: m(p) = m0 +
mu*(3z^2-1), an l=2 profile aligned with the deformation axis.  Observable: the
l=1 multiplet mean of (D+m)'s low spectrum, which R27 showed is the
differentiable one at a degenerate level."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def spheroid_area(a,c):
    if abs(c-a)<1e-12: return 4*np.pi*a*a
    if c<a:
        e=np.sqrt(1-(c*c)/(a*a)); return 2*np.pi*a*a*(1+((1-e*e)/e)*np.arctanh(e))
    e=np.sqrt(1-(a*a)/(c*c)); return 2*np.pi*a*a*(1+(c/(a*e))*np.arcsin(e))
def fixed_area(eps,A0):
    c=1.0+eps; lo,hi=0.2,3.0
    for _ in range(80):
        mid=(lo+hi)/2
        if spheroid_area(mid,c)<A0: lo=mid
        else: hi=mid
    return (lo+hi)/2,c
def lvl1(V,F,mfun):
    """l=1 multiplet mean of the 0-form operator with a position-dependent mass"""
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    L=A0.T@A0
    mv=np.array([mfun(p) for p in V])
    L=L+np.diag(mv)                                  # matter enters as a potential
    e=np.sort(np.clip(np.linalg.eigvalsh(L),-1e9,None))
    return float(np.mean(e[1:4]))
V0,F=icosphere(3)
A0=4*np.pi
EPS=np.array([-0.06,-0.04,-0.02,0.0,0.02,0.04,0.06])
def curve(mu,m0=0.0):
    mfun=lambda p: m0 + mu*(3*p[2]*p[2]-1.0)
    out=[]
    for eps in EPS:
        a,c=fixed_area(eps,A0)
        V=[np.array([p[0]*a,p[1]*a,p[2]*c]) for p in V0]
        out.append(lvl1(V,F,mfun))
    return np.array(out)
print("T60  l=1 multiplet mean vs shape parameter eps, at fixed area, sub=3")
print("     matter m(p) = mu * (3 z^2 - 1)   [mu = 0 reproduces Result 27]")
print()
print(f"   {'mu':>7} " + "".join(f"{e:>12.2f}" for e in EPS) + f"{'critical eps':>15}")
for mu in (0.0,0.05,0.10,0.20,-0.05,-0.10,-0.20):
    y=curve(mu)
    if any(v is None for v in y): print(f"   {mu:7.2f}   degenerate"); continue
    # fit a parabola and locate its vertex
    c2,c1,c0=np.polyfit(EPS,y,2)
    crit=-c1/(2*c2)
    print(f"   {mu:7.2f} " + "".join(f"{v:12.6f}" for v in y) + f"{crit:15.6f}", flush=True)
print()
print("   critical eps = 0 at mu = 0 (Result 27), and SHIFTING with mu, tracking its")
print("   sign, would mean the matter distribution selects the geometry.")
