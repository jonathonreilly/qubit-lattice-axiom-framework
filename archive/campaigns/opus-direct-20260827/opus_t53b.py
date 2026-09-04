"""T53b - confirm T53's stationarity finding on an independent mesh family, and
on a second multiplet.
T53 resolved why the earlier attempts failed: at the round sphere lambda1 is
3-fold DEGENERATE (the l=1 harmonics), and a degenerate eigenvalue splits
LINEARLY under perturbation.  So E1 = min(multiplet) has a KINK at eps = 0 --
it falls linearly in both directions (slopes -0.40 oblate, -0.80 prolate), which
is exactly Hersch's theorem (lambda1 * Area is MAXIMISED by the round sphere) and
not a failure of stationarity at all.  The differentiable observable is the
MULTIPLET MEAN, and T53 measured it as clean and quadratic.
Here: the same test on octaspheres, and on the l=2 (5-fold) multiplet, to check
neither the mesh family nor the choice of multiplet is carrying the result."""
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
def levels(V,F):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    e=np.sort(np.clip(np.linalg.eigvalsh(A0.T@A0),0,None)); nz=e[e>1e-9]
    return float(np.mean(nz[:3])), float(np.mean(nz[3:8])), float(nz[0])
print("T53b  MULTIPLET MEANS on an exactly area-preserving spheroid family")
print("      (l=1 mean over 3 modes, l=2 mean over 5 modes, plus min for contrast)")
for name,gen,ks in (("icosphere",icosphere,(3,)),("octasphere",octasphere,(3,4))):
    for k in ks:
        V0,F=gen(k); r0=levels(V0,F)
        print(f"\n  {name} sub={k} ({len(V0)} verts):  l1mean={r0[0]:.7f} l2mean={r0[1]:.7f} min={r0[2]:.7f}")
        print(f"   {'eps':>7} {'d(l1mean)':>14} {'/eps^2':>10} {'d(l2mean)':>14} {'/eps^2':>10} {'d(min)':>14} {'/|eps|':>10}")
        for eps in (-0.08,-0.04,-0.02,-0.01,0.01,0.02,0.04,0.08):
            a,c=fixed_area(eps,4*np.pi)
            V=[np.array([p[0]*a,p[1]*a,p[2]*c]) for p in V0]
            r=levels(V,F)
            if r is None: print(f"   {eps:+7.3f}  degenerate"); continue
            d1=(r[0]-r0[0])/r0[0]; d2=(r[1]-r0[1])/r0[1]; dm=(r[2]-r0[2])/r0[2]
            print(f"   {eps:+7.3f} {d1:+14.6e} {d1/eps**2:10.4f} {d2:+14.6e} {d2/eps**2:10.4f}"
                  f" {dm:+14.6e} {dm/abs(eps):10.4f}", flush=True)
print()
print("  '/eps^2' columns constant and the values symmetric in +-eps  =>  the round")
print("  sphere is a genuine CRITICAL POINT of the multiplet means at fixed area.")
print("  '/|eps|' column constant but DIFFERENT for + and -  =>  the min has a kink,")
print("  because the degenerate level splits linearly.  Both behaviours are correct")
print("  and they are the same physics seen two ways.")
