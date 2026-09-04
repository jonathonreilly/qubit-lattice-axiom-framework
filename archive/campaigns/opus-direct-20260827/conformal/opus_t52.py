"""T52 - second independent route to T51's gauge/shape separation.
T51 measured, with E1 (first nonzero 0-form eigenvalue) on icospheres sub=2,3,4:
    GAUGE (slide vertices along the sphere): -1.58e-4, -4.16e-5, -1.05e-5
           ratios 3.80, 3.95  ->  O(h^2), dying
    SHAPE (l=2 deformation at fixed area) : -7.69e-2, -8.06e-2, -8.15e-2
           converging to a nonzero limit
Before that is called verified, change everything that could be carrying it:
  * a DIFFERENT tangential slide field (azimuthal rather than the sin(3 theta)
    one), and a random tangential field;
  * DIFFERENT shape deformations (l=3 and l=4 rather than l=2);
  * a DIFFERENT observable -- the mean of the l=2 eigenvalue CLUSTER (the 3-fold
    level near 2) instead of E1;
  * a DIFFERENT mesh family (octahedral rather than icosahedral).
The separation has to survive all four."""
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
def spec0(V,F):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    e=np.sort(np.clip(np.linalg.eigvalsh(A0.T@A0),0,None))
    return e, float(np.sum(s0))
def obs(e):
    nz=e[e>1e-9]
    E1=float(nz[0])
    cl=[z for z in nz if abs(z-nz[0])<0.35*max(1.0,nz[0])]     # the 3-fold l=1 level
    lvl2=[z for z in nz if 4.0<z<8.5]                           # the 5-fold l=2 level
    return E1, float(np.mean(cl)), (float(np.mean(lvl2)) if lvl2 else float('nan'))
def slide(V,eps,kind):
    out=[]
    rng=np.random.default_rng(5)
    R=rng.normal(size=(len(V),3))
    for i,p in enumerate(V):
        if kind=="polar":   t=np.cross(p,np.array([0.,0.,1.])); w=np.sin(3*np.arccos(np.clip(p[2],-1,1)))
        elif kind=="azim":  t=np.cross(p,np.array([1.,0.,0.])); w=1.0
        else:               t=R[i]-p*np.dot(R[i],p); w=1.0
        n=np.linalg.norm(t); t=t/n if n>1e-9 else np.array([1.,0.,0.])
        q=p+eps*t*w; out.append(q/np.linalg.norm(q))
    return out
def shape(V,F,eps,l,area0):
    def h(p):
        x,y,z=p
        return {2:3*z*z-1.0, 3:z*(5*z*z-3.0), 4:35*z**4-30*z*z+3.0}[l]
    Vd=[p*(1.0+eps*h(p)/(3.0 if l>2 else 1.0)) for p in V]
    r=spec0(Vd,F)
    if r is None: return None
    f=np.sqrt(area0/r[1])
    return [p*f for p in Vd]
print("T52  eps = 0.05.  relative change in three observables; ratio = previous/current")
for meshname,gen,subs in (("icosphere",icosphere,(2,3,4)),("octasphere",octasphere,(2,3,4))):
    print(f"\n  === {meshname}")
    print(f"   {'sub':>4} {'verts':>6} {'perturbation':>16} {'dE1/E1':>13} {'ratio':>7}"
          f" {'d(l=1 lvl)':>13} {'d(l=2 lvl)':>13}")
    prev={}
    for k in subs:
        V,F=gen(k); r=spec0(V,F)
        if r is None: continue
        e0,area=r; b=obs(e0)
        rows=[("GAUGE polar",slide(V,0.05,"polar")),("GAUGE azimuthal",slide(V,0.05,"azim")),
              ("GAUGE random",slide(V,0.05,"rand"))]
        for l in (2,3,4):
            Vd=shape(V,F,0.05,l,area)
            if Vd is not None: rows.append((f"SHAPE l={l}",Vd))
        for nm,Vp in rows:
            rp=spec0(Vp,F)
            if rp is None:
                print(f"   {k:4d} {len(V):6d} {nm:>16}   degenerate"); continue
            a=obs(rp[0])
            d1=(a[0]-b[0])/b[0]; d2=(a[1]-b[1])/b[1]; d3=(a[2]-b[2])/b[2]
            rt=prev.get(nm,None); prev[nm]=abs(d1)
            print(f"   {k:4d} {len(V):6d} {nm:>16} {d1:+13.3e} "
                  f"{(rt/abs(d1) if rt else float('nan')):7.2f} {d2:+13.3e} {d3:+13.3e}", flush=True)
print()
print("  GAUGE rows: ratio ~4 per refinement (O(h^2)) and magnitude collapsing.")
print("  SHAPE rows: ratio ~1 (converged) and magnitude staying put.")
