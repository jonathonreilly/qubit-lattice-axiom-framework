import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
U = np.ones(4); us = np.array([1, 1, 1, 0.0]); n = np.array([0.48, 0.6, 0.64])
g0 = np.eye(4) + 0.3*np.outer(U, U)
for km in (0.2, 0.1, 0.05):
    ks = km*n; kt = R.newton(lambda t: R.scalar(np.array([*ks, t]), g0), 1j*km); print(f"b=0.3: |k|={km} Re k_t/|k| = {abs(kt.real)/km:.4e}")
g0 = np.eye(4) + 0.2*np.outer(us, us); Qe, Mh = R.regge(g0); C = R.compl(Mh(np.zeros(4)))
B, W, *_ = R.census(2, 2, R.GROUPS['K48'])
def FS(x, h, k):
    a = [R.schur(Qe(e*k), Mh(e*k), Mh(-e*k), C)/e**2 for e in (2e-3, 1e-3)]; S2 = (4*a[1]-a[0])/3
    return float(np.real(x @ (0.5*(S2+S2.T)) @ x))
cS, _ = R.fit(FS, B, nsamp=700); cE, _ = R.fit(lambda x, h, k: R.EH(h, k, g0), B, nsamp=700)
lam = (cS@cE)/(cE@cE); print(f"c=0.2 full form = {lam:+.6f} EH_g0 (target {-0.25*np.sqrt(np.linalg.det(g0)):+.6f}), misfit {np.linalg.norm(cS-lam*cE)/np.linalg.norm(cS):.1e}")
