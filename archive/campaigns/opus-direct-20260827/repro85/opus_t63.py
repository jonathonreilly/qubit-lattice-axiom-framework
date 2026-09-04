"""T63 - is the -1/2 ratio universal, or was T62 under-resolved?
T62 measured the orientation ratio (x-aligned / z-aligned matter) across six
observables at icosphere sub=3 and got -0.506, -0.470, -0.435, -0.462, +0.206,
-0.287.  The first is right on the predicted -1/2 and the rest degrade -- and the
degradation tracks how far each observable reaches toward the MESH CUTOFF
('sum of lowest 40' at 642 vertices is well into the badly-resolved modes).

So: refine.  If the l=2 and l=3 ratios converge to -1/2 as the mesh refines, the
tensor structure IS universal and T62 was simply under-resolved.  If they sit
still, the ratio is genuinely observable-dependent and only the lowest multiplet
carries it.  Either answer is worth having; the point is not to guess."""
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
OBS={"l=1 mean": lambda e: float(np.mean(e[1:4])),
     "l=2 mean": lambda e: float(np.mean(e[4:9])),
     "l=3 mean": lambda e: float(np.mean(e[9:16])),
     "l=4 mean": lambda e: float(np.mean(e[16:25]))}
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
zf=lambda mu:(lambda p: mu*(3*p[2]**2-1.0))
xf=lambda mu:(lambda p: mu*(3*p[0]**2-1.0))
print("T63  orientation ratio x/z vs MESH REFINEMENT.  predicted -1/2.")
print(f"   {'observable':>10}" + "".join(f"{'sub='+str(k):>14}" for k in (2,3,4)) + f"{'trend':>22}")
store={}
for key in OBS:
    row=f"   {key:>10}"; vals=[]
    for k in (2,3,4):
        V0,F=icosphere(k)
        cz=crit(V0,F,zf(0.10),key); cx=crit(V0,F,xf(0.10),key)
        r=(cx/cz) if (cz and cx and abs(cz)>1e-9) else float('nan')
        vals.append(r); row+=f"{r:14.5f}"
    store[key]=vals
    if not any(np.isnan(vals)):
        d2=abs(vals[1]+0.5); d3=abs(vals[2]+0.5)
        row+=f"   |err| {abs(vals[0]+0.5):.3f}->{d2:.3f}->{d3:.3f}"
    print(row, flush=True)
print()
print("  |err| shrinking toward zero  =>  universal -1/2, T62 was under-resolved.")
print("  |err| flat or growing        =>  only the lowest multiplet carries the ratio.")
