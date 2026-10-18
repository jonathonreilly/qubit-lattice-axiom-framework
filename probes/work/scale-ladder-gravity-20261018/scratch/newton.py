import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
Qe, Mh = R.regge(np.eye(4)); C = R.compl(Mh(np.zeros(4)))
HC = R.HC; i00 = HC.index((3, 3))  # tick index 3
def seff(k):
    Q = Qe(k); Mp, Mm = Mh(k), Mh(-k)
    D = C.T @ Q @ C
    return Mm.T @ Q @ Mp - (Mm.T @ Q @ C) @ np.linalg.pinv(D, rcond=1e-10) @ (C.T @ Q @ Mp)
rng = np.random.default_rng(3)
print(" k-dir           |k|    h_tt*p3hat^2   h_tt*k^2    h_xx*p3hat^2 (trace part)")
for n in [(1,0,0), (1,1,0), (1,1,1), (3,1,2)]:
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.05, 0.5, 1.5):
        k = np.array([*(km*n), 0.0])
        S = seff(k)
        T = np.zeros(10); T[i00] = 1.0               # static T_tt source (bilinear coupling h.T)
        h = np.linalg.pinv(S, rcond=1e-9) @ T
        ph3 = np.sum(4*np.sin(km*n/2)**2)
        print(f" {tuple(n.round(2))!s:20s} {km:.2f}  {h[i00].real*ph3:+.6f}   {h[i00].real*km**2:+.6f}   {h[HC.index((0,0))].real*ph3:+.6f}")
