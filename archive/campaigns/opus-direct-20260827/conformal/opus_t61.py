"""T61 - second route to T60, including the sharpest available check: ORIENTATION.
T60: on the covariant arena, an inhomogeneous matter profile m ~ mu(3z^2-1) shifts
the shape that extremises the spectral functional, linearly in mu and tracking its
sign (critical eps = -0.081, -0.157, -0.302 for mu = 0.05, 0.10, 0.20; mirrored
for negative mu).  Before that is written down, change everything that could be
carrying it:

 (1) ORIENTATION.  The deformation family is a spheroid along z.  Matter aligned
     with it, (3z^2-1), versus matter aligned with x, (3x^2-1).  Since
     3x^2-1 = -(1/2)(3z^2-1) + (3/2)(x^2-y^2) and the (x^2-y^2) part is orthogonal
     to an axisymmetric deformation, the x-aligned matter must produce a shift of
     EXACTLY -1/2 the z-aligned one.  That is a quantitative tensor prediction,
     not a sign check.
 (2) a different MESH FAMILY (octahedral);
 (3) a different OBSERVABLE (the l=2 multiplet mean instead of l=1);
 (4) an l=4 matter profile, which has no l=2 content aligned with the family and
     so must produce a much smaller shift."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def octasphere(nsub):
    V=[np.array(v,dtype=float) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    F=[(0,2,4),(2,1,4),(1,3,4),(3,0,4),(2,0,5),(1,2,5),(3,1,5),(0,3,5)]
    for _ in range(nsub):
        mid={}; NF=[]
        def m(i,j):
            k=(min(i,j),max(i,j))
            if k not in mid: V.append((V[i]+V[j])/2); mid[k]=len(V)-1
            return mid[k]
        for (a,b,c) in F:
            ab,bc,ca=m(a,b),m(b,c),m(c,a); NF+=[(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
        F=NF
    return [v/np.linalg.norm(v) for v in V],F
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
def level(V,F,mfun,which):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    L=A0.T@A0+np.diag(np.array([mfun(p) for p in V]))
    e=np.sort(np.clip(np.linalg.eigvalsh(L),-1e9,None))
    return float(np.mean(e[1:4])) if which==1 else float(np.mean(e[4:9]))
EPS=np.array([-0.06,-0.04,-0.02,0.0,0.02,0.04,0.06])
def crit(V0,F,mfun,which=1):
    y=[]
    for eps in EPS:
        a,c=fixed_area(eps,4*np.pi)
        V=[np.array([p[0]*a,p[1]*a,p[2]*c]) for p in V0]
        v=level(V,F,mfun,which)
        if v is None: return None
        y.append(v)
    c2,c1,c0=np.polyfit(EPS,np.array(y),2)
    return -c1/(2*c2)
PROF={"z-aligned (3z^2-1)": lambda mu:(lambda p: mu*(3*p[2]**2-1.0)),
      "x-aligned (3x^2-1)": lambda mu:(lambda p: mu*(3*p[0]**2-1.0)),
      "x^2-y^2 (orthogonal)": lambda mu:(lambda p: mu*(p[0]**2-p[1]**2)),
      "l=4 (35z^4-30z^2+3)": lambda mu:(lambda p: mu*(35*p[2]**4-30*p[2]**2+3.0)/6.0)}
for meshname,gen,k in (("icosphere sub=3",icosphere,3),("octasphere sub=3",octasphere,3),
                       ("octasphere sub=4",octasphere,4)):
    V0,F=gen(k)
    print(f"\n  === {meshname} ({len(V0)} verts)")
    print(f"   {'profile':>22} {'mu=0.05':>12} {'mu=0.10':>12} {'slope':>10} {'ratio to z':>12}")
    base=None
    for nm,mk in PROF.items():
        vals=[]
        for mu in (0.05,0.10):
            c=crit(V0,F,mk(mu))
            vals.append(c if c is not None else float('nan'))
        sl=np.mean([vals[0]/0.05, vals[1]/0.10])
        if base is None: base=sl
        print(f"   {nm:>22} {vals[0]:12.6f} {vals[1]:12.6f} {sl:10.4f} {sl/base:12.4f}", flush=True)
V0,F=icosphere(3)
print(f"\n  === observable check: l=2 multiplet mean instead of l=1 (icosphere sub=3)")
print(f"   {'profile':>22} {'mu=0.10 crit':>14} {'slope':>10}")
for nm in ("z-aligned (3z^2-1)","x-aligned (3x^2-1)"):
    c=crit(V0,F,PROF[nm](0.10),which=2)
    print(f"   {nm:>22} {c:14.6f} {c/0.10:10.4f}", flush=True)
print()
print("  PREDICTION: x-aligned / z-aligned = -1/2 exactly (tensor structure).")
print("  x^2-y^2 must give ~0 (orthogonal to an axisymmetric family).")
print("  l=4 must give a much smaller shift than l=2.")
