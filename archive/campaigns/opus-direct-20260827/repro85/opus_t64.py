"""T64 - the mu -> 0 limit: is the l=1 orientation ratio exactly -1/2 or not?
T63: the ratio converges under mesh refinement to STABLE observable-dependent
values (-0.506, -0.470, -0.438, -0.397 for l=1..4) -- the errors are flat, not
shrinking, so the deviation is not a discretisation artefact.  The remaining
possibility for l=1 is finite-mu nonlinearity: every ratio so far was measured at
mu = 0.10, which is not small.  Extrapolate mu -> 0.

Also measured: the (x^2-y^2) profile, which the analytic argument says is
orthogonal to an axisymmetric deformation and should give exactly zero.  T62
measured 0.0124 for it.  If that leakage also survives mu -> 0, then the
deviation from -1/2 and the non-zero orthogonal response are the same effect, and
the honest statement is that the response is quadrupolar but not exactly the
naive tensor contraction."""
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
def crit(V0,F,mfun):
    EPS=np.array([-0.04,-0.02,0.0,0.02,0.04]); y=[]
    for eps in EPS:
        a,c=fixed_area(eps,4*np.pi)
        V=[np.array([p[0]*a,p[1]*a,p[2]*c]) for p in V0]
        d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
        if np.any(s1<=1e-12): return None
        A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
        L=A0.T@A0+np.diag(np.array([mfun(p) for p in V]))
        e=np.sort(np.clip(np.linalg.eigvalsh(L),-1e9,None))
        y.append(float(np.mean(e[1:4])))
    c2,c1,c0=np.polyfit(EPS,np.array(y),2)
    return -c1/(2*c2)
V0,F=icosphere(3)
print("T64  l=1 mean, icosphere sub=3.  slope = crit/mu; ratio = x-slope / z-slope")
print(f"   {'mu':>7} {'z slope':>12} {'x slope':>12} {'ratio':>11} {'(x2-y2) slope':>16} {'/z slope':>11}")
for mu in (0.20,0.10,0.05,0.025,0.0125):
    cz=crit(V0,F,(lambda m:(lambda p: m*(3*p[2]**2-1.0)))(mu))
    cx=crit(V0,F,(lambda m:(lambda p: m*(3*p[0]**2-1.0)))(mu))
    co=crit(V0,F,(lambda m:(lambda p: m*(p[0]**2-p[1]**2)))(mu))
    print(f"   {mu:7.4f} {cz/mu:12.6f} {cx/mu:12.6f} {cx/cz:11.6f} {co/mu:16.6f} {co/cz:11.6f}", flush=True)
print()
print("  ratio -> -0.5 exactly as mu -> 0  =>  the naive tensor contraction is right")
print("  and everything above was finite-mu nonlinearity.  ratio settling elsewhere")
print("  =>  the response is quadrupolar but not the naive contraction, and the")
print("  (x^2-y^2) leakage is the same effect seen directly.")
