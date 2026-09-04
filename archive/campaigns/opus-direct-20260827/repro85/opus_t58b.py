"""T58b - STEEPEST DESCENT ON RESULT 1's OWN DEFECT.
T58 part (1): flipping edges away from the Delaunay complex raises the R1 tiling
defect monotonically (1.8e-15 -> 4.19 over 25 flips).  Part (2) found nothing to
flip back, because I used the PLANAR Delaunay criterion (cot a + cot b < 0) on a
mesh that lives on a curved surface, where it is not the right test -- the cotan
weights stayed positive throughout while the dual stopped tiling.

The right experiment does not need a separate Delaunay criterion at all: use
Result 1's defect AS the action and do steepest descent on it.  At each step try
every admissible edge flip, take the one that lowers the defect most, stop when
none does.  If that walks back to defect ~ 1e-15, then Result 1's condition is a
genuine variational principle whose minimiser is the Delaunay complex -- the
selection is DERIVED from the framework's own condition rather than imported."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t54b.py").read().split('print("T54  cross-check')[0])
def edge_faces(F):
    ef={}
    for k,f in enumerate(F):
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
            ef.setdefault((min(a,b),max(a,b)),[]).append(k)
    return ef
def flip(F,e,ef):
    if len(ef.get(e,[]))!=2: return None
    k1,k2=ef[e]; a,b=e
    o1=[v for v in F[k1] if v not in e]; o2=[v for v in F[k2] if v not in e]
    if len(o1)!=1 or len(o2)!=1: return None
    c,d=o1[0],o2[0]
    if c==d: return None
    if (min(c,d),max(c,d)) in ef: return None          # would duplicate an edge
    G=list(F); G[k1]=(a,d,c); G[k2]=(b,c,d)
    return G
def defect(V,F):
    try:
        s0,s1,s2,t0,t1,t2,E=build_dual(V,F,"circumcentric")
    except Exception:
        return None
    area=float(np.sum([0.5*np.linalg.norm(np.cross(V[f[1]]-V[f[0]],V[f[2]]-V[f[0]])) for f in F]))
    return abs(t1-area)
V0,F0=icosphere(2)
print(f"T58b  icosphere sub=2 ({len(V0)} verts, {len(F0)} faces)")
print(f"      Delaunay complex: R1 defect = {defect(V0,F0):.3e}")
rng=np.random.default_rng(4)
F=list(F0)
ef=edge_faces(F); keys=sorted(ef.keys())
n=0
for e in [keys[i] for i in rng.permutation(len(keys))]:
    G=flip(F,e,edge_faces(F))
    if G is None or defect(V0,G) is None: continue
    F=G; n+=1
    if n>=25: break
d0=defect(V0,F)
print(f"      after {n} random flips AWAY: R1 defect = {d0:.6f}")
print()
print("  STEEPEST DESCENT on the R1 defect (no Delaunay criterion used anywhere)")
print(f"   {'step':>5} {'best flip':>16} {'R1 defect':>16} {'drop':>14}")
cur=d0
for step in range(1,60):
    ef2=edge_faces(F); best=None; bd=cur
    for e in list(ef2.keys()):
        G=flip(F,e,ef2)
        if G is None: continue
        d=defect(V0,G)
        if d is not None and d<bd-1e-14: bd=d; best=(e,G)
    if best is None:
        print(f"   {step:5d} {'(none lowers it)':>16} {cur:16.6e}   -- local minimum reached")
        break
    F=best[1]; drop=cur-bd; cur=bd
    if step<=6 or step%5==0 or bd<1e-10:
        print(f"   {step:5d} {str(best[0]):>16} {cur:16.6e} {drop:14.6e}", flush=True)
    if cur<1e-12:
        print(f"   {step:5d} {'':>16} {cur:16.6e}   <== RECOVERED the tiling complex", flush=True)
        break
print()
print(f"  final R1 defect = {cur:.3e}   (Delaunay value was {defect(V0,F0):.3e})")
print("  same face set as the original? ", set(map(lambda t:tuple(sorted(t)),F))==set(map(lambda t:tuple(sorted(t)),F0)))
