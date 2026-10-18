import numpy as np, sys
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
U = np.ones(4); q = np.array([0.3, -0.2, 0.25, 0.0])
Q0 = R.regge(np.eye(4))[0](q)
for b in (1e-12, 1e-9, 1e-6, 1e-4, 1e-3):
    Q = R.regge(np.eye(4) + b*np.outer(U, U))[0](q)
    s = np.sort(np.linalg.svd(Q, compute_uv=False))
    print(f"b={b:.0e}: sv5={s[4]:.3e}  |Q(b)-Q(0)|={np.abs(Q-Q0).max():.3e}")
# also a different deformation direction: diagonal anisotropy of the tick only (not K48)
for e in (1e-9, 1e-6, 1e-3):
    g = np.eye(4); g[3, 3] += e
    s = np.sort(np.linalg.svd(R.regge(g)[0](q), compute_uv=False)); print(f"tick-stretch e={e:.0e}: sv5={s[4]:.3e}")
