"""T65b - full Kahler-Dirac operator, with the two defects of T65 repaired.
T65 gave erratic numbers (ratios 2.03, 0.18, 0.42, -0.50 across meshes and
amplitudes) for two identifiable reasons, both mine:

 (1) It sliced e[2:8] out of the spectrum.  The full D on a sphere has its lowest
     nonzero level at sqrt(l(l+1)) = sqrt2 with HIGH multiplicity, so a fixed
     slice cuts INTO a degenerate cluster instead of averaging over all of it --
     precisely the non-differentiable-observable mistake Result 27 diagnosed.
     Repair: detect the cluster and average over the whole of it.
 (2) Matter was added only on the 0-cells.  A scalar mass in a Kahler-Dirac
     theory multiplies the identity on EVERY degree.  Repair: put m(x) on
     vertices, on edges as the mean of their endpoints, on faces as the mean of
     their corners."""
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
def edges_of(F):
    E={}
    for f in F:
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
            E.setdefault((min(a,b),max(a,b)),len(E))
    return E
def Dspec(V,F,mfun):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    E=edges_of(F)
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    A1=np.diag(np.sqrt(s2))@d1@np.diag(1.0/np.sqrt(s1))
    N=nv+ne+nf; D=np.zeros((N,N))
    D[nv:nv+ne,0:nv]=A0; D[0:nv,nv:nv+ne]=A0.T
    D[nv+ne:,nv:nv+ne]=A1; D[nv:nv+ne,nv+ne:]=A1.T
    mv=np.array([mfun(p) for p in V])
    me=np.zeros(ne)
    for (a,b),i in E.items(): me[i]=0.5*(mv[a]+mv[b])         # scalar on edges
    mf=np.array([ (mv[f[0]]+mv[f[1]]+mv[f[2]])/3.0 for f in F])   # and on faces
    D += np.diag(np.concatenate([mv,me,mf]))                  # mass on EVERY degree
    return np.sort(np.abs(np.linalg.eigvalsh(D)))
def cluster_mean(e,tol=0.03):
    """mean of the FIRST COMPLETE degenerate cluster above zero"""
    nz=e[e>1e-7]
    if len(nz)==0: return None
    x0=nz[0]; grp=[z for z in nz if abs(z-x0)<tol*max(1.0,x0)]
    return float(np.mean(grp)), len(grp)
EPS=np.array([-0.04,-0.02,0.0,0.02,0.04])
def crit(V0,F,mfun):
    y=[]
    for eps in EPS:
        a,c=fixed_area(eps,4*np.pi)
        V=[np.array([p[0]*a,p[1]*a,p[2]*c]) for p in V0]
        e=Dspec(V,F,mfun)
        if e is None: return None,None
        r=cluster_mean(e)
        if r is None: return None,None
        y.append(r[0])
    c2,c1,c0=np.polyfit(EPS,np.array(y),2)
    return -c1/(2*c2), r[1]
for k in (2,3):
    V0,F=icosphere(k)
    e0=Dspec(V0,F,lambda p:0.0); cm=cluster_mean(e0)
    print(f"\n  icosphere sub={k} ({len(V0)} verts): {int(np.sum(e0<1e-7))} zero modes; "
          f"first cluster at {cm[0]:.6f} with multiplicity {cm[1]} (sqrt2 = {np.sqrt(2):.6f})")
    base,_=crit(V0,F,lambda p:0.0)
    print(f"   zero-matter baseline critical eps = {base:+.6f}")
    print(f"   {'profile':>14} {'mu':>6} {'crit-baseline':>15} {'slope':>11} {'ratio to z':>12}")
    for mu in (0.10,0.20):
        cz,_=crit(V0,F,(lambda m:(lambda p: m*(3*p[2]**2-1.0)))(mu))
        cx,_=crit(V0,F,(lambda m:(lambda p: m*(3*p[0]**2-1.0)))(mu))
        co,_=crit(V0,F,(lambda m:(lambda p: m*(p[0]**2-p[1]**2)))(mu))
        for nm,c in (("z-aligned",cz),("x-aligned",cx),("x^2-y^2",co)):
            if c is None: continue
            rt=((c-base)/(cz-base)) if (cz is not None and abs(cz-base)>1e-12) else float('nan')
            print(f"   {nm:>14} {mu:6.2f} {c-base:15.6f} {(c-base)/mu:11.4f} {rt:12.4f}", flush=True)
