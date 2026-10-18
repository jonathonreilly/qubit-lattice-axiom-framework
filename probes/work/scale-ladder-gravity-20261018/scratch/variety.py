import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
Qe, _ = R.regge(np.eye(4)); rng = np.random.default_rng(42)
worst_on, best_off, n5 = 0, 1, []
for t in range(25):
    p3 = rng.standard_normal(3)*1.2 + 1j*rng.standard_normal(3)*0.5
    S3 = np.sum(4*np.sin(p3/2)**2)
    p4 = 2*np.arcsin(np.sqrt(-S3+0j)/2)            # 4 sin^2(p4/2) = -S3
    p = np.array([*p3, p4]); assert abs(np.sum(4*np.sin(p/2)**2)) < 1e-12
    s = R.sv(Qe(p)); so = R.sv(Qe(p*np.array([1, 1, 1, 1.03])))
    worst_on = max(worst_on, s[6]); best_off = min(best_off, so[5]); n5.append(int((so < 1e-12).sum()))
print(f"25 random complex points of the variety: 7th sv on shell <= {worst_on:.1e}; off-shell 6th sv >= {best_off:.1e}; off-shell nullities {sorted(set(n5))}")
