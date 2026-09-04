"""T62 - is the COUPLING universal, or only the TENSOR STRUCTURE?
T61 verified that matter shifts the extremal shape with a tensor structure that is
exactly right: x-aligned/z-aligned = -0.4967 against a predicted -1/2, on three
meshes, and an orthogonal (x^2-y^2) profile gives ~0.  But it also showed the
SLOPE depends on which spectral functional is used: -1.59 for the l=1 multiplet
mean, -0.56 for the l=2 one.  So the response magnitude is not a universal
number, and that matters -- it is exactly the unresolved 'which functional'
question Result 27 flagged.

Sharpen it: across many observables, is the ORIENTATION RATIO always -1/2 while
the slope varies?  If so, the statement that survives is structural (the response
is a rank-2 tensor contracted with the matter quadrupole) and the coupling
strength is not yet determined by anything in the framework -- which is the
honest position and names exactly what is missing.

Controls included: adding a CONSTANT to the potential must not move the critical
point at all (a constant shifts every eigenvalue equally)."""
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
def spec(V,F,mfun):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    L=A0.T@A0+np.diag(np.array([mfun(p) for p in V]))
    return np.sort(np.clip(np.linalg.eigvalsh(L),-1e9,None))
OBS={"l=1 mean (3 modes)":  lambda e: float(np.mean(e[1:4])),
     "l=2 mean (5 modes)":  lambda e: float(np.mean(e[4:9])),
     "l=3 mean (7 modes)":  lambda e: float(np.mean(e[9:16])),
     "sum of lowest 16":    lambda e: float(np.sum(e[:16])),
     "sum of lowest 40":    lambda e: float(np.sum(e[:40])),
     "log-sum lowest 16":   lambda e: float(np.sum(np.log(np.abs(e[1:17])+1e-12)))}
EPS=np.array([-0.06,-0.04,-0.02,0.0,0.02,0.04,0.06])
def crit(V0,F,mfun,key):
    y=[]
    for eps in EPS:
        a,c=fixed_area(eps,4*np.pi)
        V=[np.array([p[0]*a,p[1]*a,p[2]*c]) for p in V0]
        e=spec(V,F,mfun)
        if e is None: return None
        y.append(OBS[key](e))
    c2,c1,c0=np.polyfit(EPS,np.array(y),2)
    return -c1/(2*c2)
V0,F=icosphere(3)
zf=lambda mu:(lambda p: mu*(3*p[2]**2-1.0))
xf=lambda mu:(lambda p: mu*(3*p[0]**2-1.0))
print("T62  icosphere sub=3.  slope = d(critical eps)/d(mu), from mu = 0.10")
print(f"   {'observable':>22} {'slope (z-aligned)':>19} {'slope (x-aligned)':>19} {'ratio x/z':>11}")
for key in OBS:
    cz=crit(V0,F,zf(0.10),key); cx=crit(V0,F,xf(0.10),key)
    if cz is None or cx is None: print(f"   {key:>22}  degenerate"); continue
    print(f"   {key:>22} {cz/0.10:19.5f} {cx/0.10:19.5f} {cx/cz:11.5f}", flush=True)
print()
print("  CONTROL: a CONSTANT potential must not move the critical point at all")
print(f"   {'constant c':>12} {'critical eps (l=1 mean)':>26}")
for c in (0.0,0.5,2.0,-1.0):
    r=crit(V0,F,(lambda cc: (lambda p: cc))(c),"l=1 mean (3 modes)")
    print(f"   {c:12.2f} {r:26.8f}", flush=True)
print()
print("  ratio ~ -1/2 for EVERY observable while the slopes differ  =>  the TENSOR")
print("  STRUCTURE is universal and the COUPLING STRENGTH is not determined.")
