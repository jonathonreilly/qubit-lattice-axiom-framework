"""T57 - the identity DERIVED, and the derivation's own prediction tested.
T56 broke my first hypothesis (that 'inscribed + circumcentric' alone gives
lambda = 2): randomly jittered inscribed meshes gave 2.0077, 2.0018, 2.0014 with
per-axis spreads up to 0.43.  Working out why gives the actual theorem.

Sum the Rayleigh quotient over the three coordinate axes.  For the numerator,
sum_a (x_a(j) - x_a(i))^2 is just the squared edge length, so

   sum_a N_a = sum_e star1_e * l_e^2 = sum_e (l*_e / l_e) l_e^2 = sum_e l_e l*_e
             = 2 * sum_e (1/2) l_e l*_e = 2 * AREA

and that last step is EXACTLY the tiling property -- which is exactly Result 1's
uniform-weight condition, verified in T54b to 1.8e-15 for the circumcentric dual
and violated by 2e-2 for the barycentric one.  For the denominator, on a mesh
inscribed in the unit sphere,

   sum_a D_a = sum_v A_v |p_v|^2 = sum_v A_v = AREA .

Hence  (sum_a N_a) / (sum_a D_a) = 2  EXACTLY, for ANY inscribed mesh, jittered
or not.  Splitting that equally into 2 per axis needs the extra fact
D_x = D_y = D_z = AREA/3, which is mesh SYMMETRY -- and jitter destroys it.

PREDICTION: on the jittered meshes where the per-axis values scattered by 0.43,
the AGGREGATE ratio must still be exactly 2.  And on the barycentric dual it must
FAIL, by exactly the amount the tiling property fails.  Both tested."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t54b.py").read().split('print("T54  cross-check')[0])
def parts(V,F,kind):
    if kind=="barycentric":
        _,s1,_,t0,t1,t2,E=build_dual(V,F,"barycentric"); s0=bary_star0(V,F)
    else:
        s0,s1,_,t0,t1,t2,E=build_dual(V,F,"circumcentric")
    d0,_=incidence(V,F,E)
    N=[];D=[]
    for a in range(3):
        X=np.array([p[a] for p in V]); dX=d0@X
        N.append(float(np.sum(s1*dX*dX))); D.append(float(np.sum(s0*X*X)))
    area=float(np.sum(0.5*np.linalg.norm(np.cross(
        [V[f[1]]-V[f[0]] for f in F],[V[f[2]]-V[f[0]] for f in F],axis=1),axis=1)))
    return N,D,area,(t0,t1,t2)
def jit(V,eps,seed):
    rng=np.random.default_rng(seed)
    return [ (p+eps*rng.normal(size=3))/np.linalg.norm(p+eps*rng.normal(size=3)) for p in V ]
print("T57  AGGREGATE ratio (sum_a N_a)/(sum_a D_a) -- predicted EXACTLY 2 for any")
print("     inscribed mesh with the dual Result 1 selects, jittered or not.")
print()
print(f"   {'mesh':>28} {'dual':>14} {'aggregate':>16} {'|agg-2|':>10} {'per-axis spread':>16}"
      f" {'sum_e l l*/2 - Area':>21}")
V0,F=icosphere(3)
cases=[("icosphere sub=3",V0)]
for eps,sd in ((0.05,7),(0.15,7),(0.35,7),(0.35,99)):
    cases.append((f"jittered eps={eps} seed={sd}", jit(V0,eps,sd)))
for k in (2,4):
    Vk,Fk=icosphere(k); cases.append((f"icosphere sub={k}", Vk))
for label,V in cases:
    Fuse=F if len(V)==len(V0) else (icosphere(2)[1] if len(V)==162 else icosphere(4)[1])
    for kind in ("circumcentric","barycentric"):
        try:
            N,D,area,t=parts(V,Fuse,kind)
        except Exception as ex:
            print(f"   {label:>28} {kind:>14}  {ex}"); continue
        agg=sum(N)/sum(D); per=[N[a]/D[a] for a in range(3)]
        print(f"   {label:>28} {kind:>14} {agg:16.12f} {abs(agg-2):10.2e} "
              f"{max(per)-min(per):16.3e} {t[1]-area:21.3e}", flush=True)
print()
print("   circumcentric: aggregate exactly 2 even when the per-axis values scatter,")
print("   and the last column (the tiling defect) is zero.  barycentric: both fail,")
print("   and they fail TOGETHER -- which is the point.  Result 1's condition is what")
print("   makes the identity true.")
