import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
us = np.array([1, 1, 1, 0.0])
for c in (0.2, 0.05):
    g0 = np.eye(4) + c*np.outer(us, us); n = np.array([0.48, 0.6, 0.64])
    prev = None
    for km in (0.4, 0.2, 0.1, 0.05):
        ks = km*n; kt = R.newton(lambda t: R.scalar(np.array([*ks, t]), g0), 1j*km)
        ratio = abs(kt.real)/km
        print(f"c={c}: |k|={km:.2f} Re k_t/|k| = {ratio:.3e}" + (f"  (halving ratio {prev/ratio:.2f})" if prev else ""))
        prev = ratio
