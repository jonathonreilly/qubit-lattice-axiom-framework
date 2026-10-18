import sys, time, pickle, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
import regge_generic as RG
t0 = time.time(); OFF, S = RG.barycentric(); B = RG.Complex(OFF, S)
print("barycentric:", len(S), "simplices,", B.E, "edge classes,", len(B.terms), "hinge classes,", len(B.types), "vertex types", f"{time.time()-t0:.0f}s")
pickle.dump(B, open('bary.pkl', 'wb'))
rng = np.random.default_rng(0)
for _ in range(3):
    k = rng.standard_normal(4)*0.5
    Q = B.Q(k); s = np.sort(np.linalg.svd(Q, compute_uv=False)); s /= s[-1]
    G = B.gauge(k); rg = np.linalg.matrix_rank(G, tol=1e-9)
    print(f"|k|={np.linalg.norm(k):.2f}: |QG|/|Q| {np.abs(Q@G).max()/np.abs(Q).max():.1e}; gauge rank {rg}; singular values 60..72:", " ".join(f"{x:.1e}" for x in s[60:72]))
