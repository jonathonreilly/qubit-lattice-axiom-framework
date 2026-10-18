import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
us = np.array([1, 1, 1, 0.0]); q = np.array([0.3, -0.2, 0.25, 0.15])
for c in (0.0, 0.05, 0.2, -0.2):
    g0 = np.eye(4) + c*np.outer(us, us)
    Qe, Mh = R.regge(g0); s = np.sort(np.linalg.svd(Qe(q), compute_uv=False)); s /= s[-1]
    ks = 0.6*np.array([0.48, 0.6, 0.64]); kt = R.newton(lambda t: R.scalar(np.array([*ks, t]), g0), 0.6j)
    # Schur symbol vs EH_g0 (only meaningful when eliminated block is stiff)
    C = R.compl(Mh(np.zeros(4))); kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
    soft = np.min(np.abs(np.linalg.eigvals(C.T @ Qe(0.01*kd) @ C)))
    print(f"c={c:+.2f}: sv5..6 {s[4]:.1e} {s[5]:.1e}; scalar-shell k_t = {kt:.6f} (real part {abs(kt.real):.1e}); smallest eliminated eigenvalue {soft:.2e}")
