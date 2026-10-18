import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
Qe, Mh = R.regge(np.eye(4)); HC = R.HC; itt = HC.index((3, 3)); ixx = HC.index((0, 0))
def Qh(k): return Mh(-k).T @ Qe(k) @ Mh(k)
def EH_matrix(k):
    Mx = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            ei = np.zeros(10); ej = np.zeros(10); ei[i] = 1; ej[j] = 1
            f = lambda x: R.EH(R.hfull(x), k, np.eye(4))
            Mx[i, j] = 0.25*(f(ei+ej) - f(ei-ej))
    return Mx
print(" dir        |k|   Q_h nullity  h_tt*k^2 (Q_h)   h_tt*p3hat^2 (Q_h)   h_tt*k^2 continuum(-EH/4)")
for n in [(1,0,0), (1,1,0), (1,1,1), (3,1,2)]:
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.05, 0.5, 1.5):
        k = np.array([*(km*n), 0.0]); S = Qh(k)
        s = R.sv(S); nul = int((s < 1e-10).sum())
        T = np.zeros(10); T[itt] = 1.0
        h = np.linalg.pinv(S, rcond=1e-9) @ T
        hc = np.linalg.pinv(-0.25*EH_matrix(k), rcond=1e-9) @ T
        ph3 = np.sum(4*np.sin(km*n/2)**2)
        print(f" {str(tuple(n.round(2))):18s} {km:.2f}   {nul}   {h[itt].real*km**2:+.6f}   {h[itt].real*ph3:+.6f}   {hc[itt].real*km**2:+.6f}")
