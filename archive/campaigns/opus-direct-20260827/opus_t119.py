"""T119 - THE HEAT TRACE: A COVARIANT REGULATOR, AND SAKHAROV'S COEFFICIENT.

R65 closed the Sakharov route as posed: regressing W = (1/2) logdet(Delta+m^2)
against curvature cannot separate induced gravity from mesh distortion, because
W is not diffeomorphism invariant.  It named the fix: "use a covariant regulator."

T118 says exactly which one.  The low spectrum IS diffeomorphism invariant at
O(h^2) (p = 1.85, 1.83, 1.86, 1.88 over four refinements, with the first-order
response vanishing identically -- 16.2x for a 4x amplitude).  What is NOT
invariant is any sum that keeps a fixed FRACTION of the modes, because that is a
cutoff in lattice units that rises without bound as the mesh refines.  So the
regulator must weight by a fixed PHYSICAL scale.  The canonical such object is

        K(tau) = Tr e^{-tau Delta} = sum_i e^{-tau lambda_i}

and its small-tau expansion is the Seeley-DeWitt series

        K(tau) ~ (4 pi tau)^{-d/2} [ Vol + (tau/6) int R sqrt(g) + O(tau^2) ]

whose tau^1 coefficient IS the induced Einstein-Hilbert term.  Sakharov's
mechanism is not something to regress for -- it is the a_1 coefficient, and it
can be read off directly.  This turns a failed fit into a measurement.

Observable:      F(tau) = [ (4 pi tau)^{d/2} K(tau) - Vol ] / tau  ->  (1/6) int R sqrt(g)

Three tests, in order of what they decide:
  (A) FLAT CONTROL: F(tau) -> 0 on a flat mesh (int R = 0).  Fixes the window in
      tau where the lattice heat trace is trustworthy: tau >> h^2 (UV modes are
      lattice artifacts) and tau << 1 (the expansion is asymptotic).
  (B) DIFFEOMORPHISM GATE: K(tau) must not move under a pure re-triangulation of
      flat space -- the exact test W failed in R65.
  (C) THE MEASUREMENT: on a conformally curved metric g = e^{2 phi} delta with
      phi = eps cos(2 pi n.x), continuum gives to O(eps^2)
          int R sqrt(g) = 6 int (grad phi)^2 = 12 pi^2 |n|^2 eps^2 .
      Does F(tau) reproduce it?"""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t116 import kuhn, positions, lengths_from_positions, spectrum, assemble

d=4
def vol_of(simp,l2list):
    t=0.0
    for l2 in l2list:
        G=np.empty((d,d))
        for a in range(d):
            for b in range(d): G[a,b]=0.5*(l2[0,a+1]+l2[0,b+1]-l2[a+1,b+1])
        t+=np.sqrt(max(np.linalg.det(G),0.0))/24.0
    return t

def l2_conformal(simp,L,eps,nvec):
    """g = e^{2 phi} delta,  phi = eps cos(2 pi n.x).  Edge length uses phi at the
    midpoint -- second-order accurate, which is what the O(h^2) window needs."""
    out=[]; h=1.0/L; kv=2*np.pi*np.asarray(nvec,dtype=float)
    for (ids,base,offs) in simp:
        X=(base[None,:]+offs)*h
        l2=np.zeros((5,5))
        for i,j in itertools.combinations(range(5),2):
            dx=X[i]-X[j]; mid=0.5*(X[i]+X[j])
            l2[i,j]=l2[j,i]=np.exp(2*eps*np.cos(float(mid@kv)))*float(dx@dx)
        out.append(l2)
    return out

def heat(lam,taus): return np.array([float(np.sum(np.exp(-t*lam))) for t in taus])
def F(lam,vol,taus): return ((4*np.pi*taus)**(d/2)*heat(lam,taus)-vol)/taus

TAUS=np.array([0.02,0.03,0.05,0.07,0.10,0.14,0.20,0.28])
print("T119  the heat trace as a covariant regulator")
print()
print("(A) FLAT CONTROL -- F(tau) must vanish; where it does is the usable window")
print(f"    {'L':>3} {'h^2':>8} |  " + "  ".join(f"t={t:<5g}" for t in TAUS))
flat={}
for L in (5,6,7,8):
    verts,vid,simp=kuhn(L); N=len(verts)
    l20=[lengths_from_positions(positions(s,lambda X:0.0*X,L)) for s in simp]
    lam=spectrum(simp,l20,N); v=vol_of(simp,l20); flat[L]=(simp,N,lam,v,l20)
    print(f"    {L:3d} {1.0/L**2:8.4f} |  "+"  ".join(f"{x:7.3f}" for x in F(lam,v,TAUS)),flush=True)
print()
print("(B) DIFFEOMORPHISM GATE -- pure re-triangulation of flat space, A=0.03")
kvec=2*np.pi*np.array([1.0,0,0,0])
def gauge(X):
    o=np.zeros_like(X); o[:,1]=0.03*np.sin(X@kvec); return o
print(f"    {'L':>3} |  " + "  ".join(f"t={t:<5g}" for t in TAUS) + "     <- |dK|/K")
for L in (5,6,7,8):
    simp,N,lam0,v0,_=flat[L]
    l2g=[lengths_from_positions(positions(s,gauge,L)) for s in simp]
    lg=spectrum(simp,l2g,N)
    r=np.abs(heat(lg,TAUS)-heat(lam0,TAUS))/heat(lam0,TAUS)
    print(f"    {L:3d} |  "+"  ".join(f"{x:7.1e}" for x in r),flush=True)
print("    (compare: the full logdet moved by O(1) in R65 -- that is the contrast)")
print()
print("(C) THE MEASUREMENT -- conformal phi = eps cos(2 pi x1), n=(1,0,0,0)")
EPS=0.05; NV=(1,0,0,0)
target=6.0*(2*np.pi**2*float(np.dot(NV,NV))*EPS**2)
print(f"    continuum target (1/6) int R sqrt(g) = int (grad phi)^2 = {target/6:.6f}")
print(f"                          [ int R sqrt(g) = {target:.6f} ]")
print(f"    {'L':>3} |  " + "  ".join(f"t={t:<5g}" for t in TAUS))
for L in (5,6,7,8):
    simp,N,lam0,v0,_=flat[L]
    l2c=l2_conformal(simp,L,EPS,NV)
    lc=spectrum(simp,l2c,N)
    if lc is None: print(f"    {L:3d} | degenerate"); continue
    vc=vol_of(simp,l2c)
    dF=F(lc,vc,TAUS)-F(lam0,v0,TAUS)     # subtract the flat lattice artifact
    print(f"    {L:3d} |  "+"  ".join(f"{x:7.4f}" for x in dF),flush=True)
print()
print(f"    a plateau near {target/6:.4f} inside the (A)-window is Sakharov's a_1,")
print("    i.e. an induced Einstein-Hilbert term with a computed coefficient.")
