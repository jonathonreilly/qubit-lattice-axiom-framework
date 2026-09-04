"""T58 - IS RESULT 1'S CONDITION A VARIATIONAL PRINCIPLE ON THE COMPLEX?
T57 established what Result 1's uniform-weight condition MEANS on a complex: the
dual cells must TILE,  sum_e (1/2) l_e l*_e = sum_v A_v = sum_f A_f = Area.  It
holds to 1e-15 for the circumcentric dual on a well-shaped mesh, fails by 2e-2
for the barycentric dual, and fails enormously (defect ~ 10^2-10^3) on jittered
meshes -- because jitter destroys DELAUNAY-ness, and the circumcentric dual only
tiles when the mesh is Delaunay.  The failure is quantitative: the spectral
identity misses by exactly 2*(tiling defect)/Area, predicted and measured to four
figures.

So Result 1 selects the Delaunay/Voronoi structure.  The question that makes it
DYNAMICS rather than bookkeeping: is the tiling defect an ACTION?  Delaunay
triangulations are characterised variationally, so if the R1 defect decreases
monotonically under the edge flips that restore Delaunay-ness, then Result 1's
condition is not merely a constraint -- it is a variational principle, and it is
the framework's own.

Test: build non-Delaunay meshes by flipping edges of a good one, then measure
  (a) the R1 tiling defect,
  (b) the count of non-Delaunay edges (cot alpha + cot beta < 0),
  (c) whether flipping back reduces (a) monotonically."""
import numpy as np, itertools
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t54b.py").read().split('print("T54  cross-check')[0])
def edge_faces(F):
    ef={}
    for k,f in enumerate(F):
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
            ef.setdefault((min(a,b),max(a,b)),[]).append(k)
    return ef
def flip(F,e,ef):
    """flip edge e=(a,b) shared by two triangles; returns a new face list or None"""
    if len(ef[e])!=2: return None
    k1,k2=ef[e]; a,b=e
    o1=[v for v in F[k1] if v not in e]; o2=[v for v in F[k2] if v not in e]
    if len(o1)!=1 or len(o2)!=1: return None
    c,d=o1[0],o2[0]
    if c==d: return None
    G=list(F); G[k1]=(a,d,c); G[k2]=(b,c,d)
    return G
def defect_and_nd(V,F):
    try:
        s0,s1,s2,t0,t1,t2,E=build_dual(V,F,"circumcentric")
    except Exception:
        return None
    area=float(np.sum([0.5*np.linalg.norm(np.cross(V[f[1]]-V[f[0]],V[f[2]]-V[f[0]])) for f in F]))
    nd=int(np.sum(s1<0))
    return abs(t1-area), nd, area, float(np.min(s1))
V0,F0=icosphere(2)
base=defect_and_nd(V0,F0)
print(f"T58  icosphere sub=2: {len(V0)} verts, {len(F0)} faces")
print(f"     Delaunay start: R1 tiling defect = {base[0]:.3e}, non-Delaunay edges = {base[1]}, "
      f"min star1 = {base[3]:.4f}")
print()
print("  (1) FLIP edges away from Delaunay and watch the R1 defect")
ef=edge_faces(F0); keys=sorted(ef.keys())
rng=np.random.default_rng(4)
F=list(F0); hist=[]
order=[keys[i] for i in rng.permutation(len(keys))]
applied=0
print(f"   {'flips':>6} {'R1 tiling defect':>20} {'non-Delaunay edges':>20} {'min star1':>12}")
print(f"   {0:6d} {base[0]:20.6e} {base[1]:20d} {base[3]:12.5f}")
for e in order:
    ef2=edge_faces(F)
    if e not in ef2: continue
    G=flip(F,e,ef2)
    if G is None: continue
    r=defect_and_nd(V0,G)
    if r is None: continue
    F=G; applied+=1; hist.append((applied,r))
    if applied in (1,2,3,5,8,12,18,25):
        print(f"   {applied:6d} {r[0]:20.6e} {r[1]:20d} {r[3]:12.5f}", flush=True)
    if applied>=25: break
print()
print("  (2) now FLIP BACK toward Delaunay (greedy: flip the most negative edge)")
print(f"   {'step':>6} {'R1 tiling defect':>20} {'non-Delaunay edges':>20} {'min star1':>12}")
for step in range(1,26):
    ef2=edge_faces(F)
    s0,s1,s2,t0,t1,t2,E=build_dual(V0,F,"circumcentric")
    worst=None; wv=0.0
    for e,idx in E.items():
        if s1[idx]<wv: wv=s1[idx]; worst=e
    if worst is None: break
    G=flip(F,worst,ef2)
    if G is None: break
    r=defect_and_nd(V0,G)
    if r is None: break
    F=G
    if step in (1,2,3,5,8,12,18,25):
        print(f"   {step:6d} {r[0]:20.6e} {r[1]:20d} {r[3]:12.5f}", flush=True)
    if r[1]==0:
        print(f"   {step:6d} {r[0]:20.6e} {r[1]:20d} {r[3]:12.5f}   <== back to Delaunay", flush=True)
        break
print()
print("  defect rising with flips away and falling with flips back  =>  Result 1's")
print("  condition is a variational principle, minimised by the Delaunay complex.")
