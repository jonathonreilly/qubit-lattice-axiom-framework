"""T59 - HOW MUCH DOES RESULT 1's CONDITION ACTUALLY SELECT?
T54b-T58 established that Result 1's uniform-weight condition, read on a complex,
is the TILING condition, and that it picks the circumcentric/Delaunay structure:
exact to 1e-15 there, violated by 2e-2 by the barycentric dual, and rising
monotonically as edges are flipped away from Delaunay.

The honest bound on that claim is the question of whether the condition sees the
GEOMETRY at all, or only the combinatorics.  If the tiling defect is zero for
EVERY Delaunay complex regardless of where the vertices sit, then Result 1
selects the dual structure and NOT the geometry -- which is a real limit on what
it can do, and it needs to be established rather than glossed.

Test: start from a Delaunay complex on a sphere and move the vertices in ways
that keep it Delaunay (small tangential slides, radial scalings, smooth
deformations), measuring the tiling defect throughout.  Compare against the
flips of T58, which changed combinatorics and did move it."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t54b.py").read().split('print("T54  cross-check')[0])
def defect(V,F):
    try: s0,s1,s2,t0,t1,t2,E=build_dual(V,F,"circumcentric")
    except Exception: return None,None
    area=float(np.sum([0.5*np.linalg.norm(np.cross(V[f[1]]-V[f[0]],V[f[2]]-V[f[0]])) for f in F]))
    return abs(t1-area), float(np.min(s1))
V0,F=icosphere(3)
d,mn=defect(V0,F)
print(f"T59  icosphere sub=3 ({len(V0)} verts).  round sphere: defect = {d:.3e}, min star1 = {mn:.4f}")
print()
print("  (a) SMALL TANGENTIAL SLIDES (geometry moves, combinatorics fixed, stays Delaunay)")
print(f"   {'eps':>8} {'R1 defect':>16} {'min star1':>12}")
for eps in (0.002,0.01,0.03,0.08):
    Vs=[]
    for p in V0:
        t=np.cross(p,np.array([0.,0.,1.])); n=np.linalg.norm(t)
        t=t/n if n>1e-9 else np.array([1.,0.,0.])
        q=p+eps*t*np.sin(3*np.arccos(np.clip(p[2],-1,1))); Vs.append(q/np.linalg.norm(q))
    dd,mm=defect(Vs,F); print(f"   {eps:8.3f} {dd:16.6e} {mm:12.5f}", flush=True)
print()
print("  (b) RADIAL SCALING (pure size change)")
for R in (0.4,1.0,2.5,7.0):
    dd,mm=defect([p*R for p in V0],F); print(f"   R={R:6.2f} {dd:16.6e} {mm:12.5f}", flush=True)
print()
print("  (c) SMOOTH SHAPE CHANGE - ellipsoids (genuinely different geometry)")
for axes in ((1.0,1.0,0.9),(1.0,1.0,0.7),(1.0,0.85,0.7),(1.0,1.0,0.45)):
    Vd=[np.array([p[0]*axes[0],p[1]*axes[1],p[2]*axes[2]]) for p in V0]
    dd,mm=defect(Vd,F)
    print(f"   {str(axes):>18} {dd:16.6e} {mm:12.5f}", flush=True)
print()
print("  (d) CONTROL - a single edge FLIP (combinatorics change, geometry identical)")
ef={}
for k,f in enumerate(F):
    for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])): ef.setdefault((min(a,b),max(a,b)),[]).append(k)
done=0
for e,ks in list(ef.items()):
    if len(ks)!=2: continue
    k1,k2=ks; a,b=e
    o1=[v for v in F[k1] if v not in e]; o2=[v for v in F[k2] if v not in e]
    if len(o1)!=1 or len(o2)!=1 or o1[0]==o2[0]: continue
    G=list(F); G[k1]=(a,o2[0],o1[0]); G[k2]=(b,o1[0],o2[0])
    dd,mm=defect(V0,G)
    if dd is None: continue
    print(f"   flip {str(e):>12} {dd:16.6e} {mm:12.5f}", flush=True)
    done+=1
    if done>=4: break
print()
print("  If (a)-(c) stay ~1e-15 while (d) jumps, then Result 1's condition is about")
print("  the COMBINATORIAL/dual structure and is blind to the geometry -- a real and")
print("  necessary limit on what the selector can be claimed to do.")
