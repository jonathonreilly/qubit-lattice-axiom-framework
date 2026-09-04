"""T56 - is the exact identity real?  Test it where it should hold and where it must not.
T55 found: with the dual that Result 1's condition selects (circumcentric), the
Rayleigh quotient of the LINEAR coordinate functions on a sphere-inscribed mesh is
   lambda = sum_edges star1_e (x_j - x_i)^2  /  sum_vertices A_v x_v^2  =  2.000000000
exactly, at every refinement.  That is the discrete form of  int |grad x|^2 =
2 int x^2  on the unit sphere (x is an l=1 harmonic, l(l+1)=2).

An exact number wants breaking.  Four ways:
  (B1) a DIFFERENT mesh family (octahedral) -- must still be exactly 2;
  (B2) a RANDOMLY PERTURBED but still inscribed mesh (vertices jittered then
       re-projected onto the sphere) -- must STILL be exactly 2 if the identity
       is about the sphere and the dual, not about mesh symmetry;
  (B3) a sphere of RADIUS R -- must be exactly 2/R^2;
  (B4) an ELLIPSOID, where x is NOT an eigenfunction -- must NOT be exact.
The barycentric dual is run alongside every time as the control."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t54b.py").read().split('print("T54  cross-check')[0])
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
def rayleigh(V,F,kind):
    if kind=="barycentric":
        _,s1,_,_,_,_,E=build_dual(V,F,"barycentric"); s0=bary_star0(V,F)
    else:
        s0,s1,_,_,_,_,E=build_dual(V,F,"circumcentric")
    d0,_=incidence(V,F,E)
    out=[]
    for a in range(3):
        X=np.array([p[a] for p in V]); dX=d0@X
        out.append(float(np.sum(s1*dX*dX)/np.sum(s0*X*X)))
    return out
def jitter(V,eps,seed):
    rng=np.random.default_rng(seed)
    return [ (p+eps*rng.normal(size=3))/np.linalg.norm(p+eps*rng.normal(size=3)*0) for p in V ]
def jitter_proj(V,eps,seed):
    rng=np.random.default_rng(seed); out=[]
    for p in V:
        q=p+eps*rng.normal(size=3); out.append(q/np.linalg.norm(q))
    return out
print("T56  Rayleigh quotient of the linear functions x,y,z.  'want' = 2/R^2 on a sphere.")
print(f"   {'case':>34} {'circumcentric (mean, spread)':>34} {'barycentric':>16}")
def show(label,V,F,want):
    c=rayleigh(V,F,"circumcentric"); b=rayleigh(V,F,"barycentric")
    print(f"   {label:>34}   {np.mean(c):.10f}  spread {max(c)-min(c):.1e}   {np.mean(b):16.8f}"
          f"    |c-want| = {abs(np.mean(c)-want):.2e}", flush=True)
print("  (B1) different mesh family")
for k in (2,3,4):
    V,F=octasphere(k); show(f"octasphere sub={k} ({len(V)}v)",V,F,2.0)
print("  (B2) randomly jittered, still inscribed")
for eps in (0.05,0.15,0.35):
    V0,F=icosphere(3); V=jitter_proj(V0,eps,7)
    show(f"icosphere sub=3 jitter {eps}",V,F,2.0)
print("  (B3) sphere of radius R (want 2/R^2)")
for R in (0.5,2.0,3.0):
    V0,F=icosphere(3); V=[p*R for p in V0]; show(f"radius R={R}",V,F,2.0/R**2)
print("  (B4) ELLIPSOID - x is not an eigenfunction, so this MUST break")
for axes in ((1.0,1.0,0.8),(1.0,1.0,0.5),(1.0,0.7,0.5)):
    V0,F=icosphere(3); V=[np.array([p[0]*axes[0],p[1]*axes[1],p[2]*axes[2]]) for p in V0]
    c=rayleigh(V,F,"circumcentric")
    print(f"   {'ellipsoid '+str(axes):>34}   per-axis: {[f'{v:.6f}' for v in c]}"
          f"   spread {max(c)-min(c):.3e}", flush=True)
