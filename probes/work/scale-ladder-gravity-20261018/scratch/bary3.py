import sys, pickle, numpy as np
sys.path.insert(0, '.'); sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import regge_generic as RG
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
B = pickle.load(open('bary.pkl', 'rb'))
def extras(k):
    Q = B.Q(k); _, s, vh = np.linalg.svd(Q); N = vh[-80:].conj().T; G = B.gauge(k)
    r = N - G @ np.linalg.pinv(G, rcond=1e-9) @ N
    u, ss, _ = np.linalg.svd(r); return u[:, :16], ss[:18]
for k in [np.array([0.02, 0.01, -0.015, 0.012]), np.array([0.3, -0.2, 0.25, 0.1])]:
    X, ss = extras(k); M = B.line_map(k)
    # metric share of each extra (component in im M modulo gauge)
    G = B.gauge(k); Pg = np.eye(B.E) - G @ np.linalg.pinv(G, rcond=1e-9)
    Mm = Pg @ M; Pm = Mm @ np.linalg.pinv(Mm, rcond=1e-9)
    sh = np.linalg.svd(Pm @ X, compute_uv=False)
    print(f"|k|={np.linalg.norm(k):.3f}: extras-vs-gauge singular values {ss[14]:.1e},{ss[15]:.1e},{ss[16]:.1e}; metric-share singular values of the 16 extras:", " ".join(f"{x:.2f}" for x in sh[:6]))
