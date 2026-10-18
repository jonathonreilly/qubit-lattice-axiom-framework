import numpy as np, sys
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
U = np.ones(4)
B, W, *_ = R.census(2, 2, R.GROUPS['K48']); W, _ = np.linalg.qr(W)
for b in (0.3, 0.05):
    g0 = np.eye(4) + b*np.outer(U, U); Qe, Mh = R.regge(g0); C = R.compl(Mh(np.zeros(4)))
    seff = lambda k: R.schur(Qe(k), Mh(k), Mh(-k), C)
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
    for s in (0.05, 0.01, 0.002):
        D = C.T @ Qe(s*kd) @ C; sd = np.sort(np.abs(np.linalg.eigvals(D)))
        print(f"b={b} s={s}: |D| smallest eigen {sd[0]:.2e}; |Seff|/s^2 = {np.abs(seff(s*kd)).max()/s**2:.3e}")
    def FS(x, h, k):
        a = [seff(e*k)/e**2 for e in (2e-3, 1e-3)]; S2 = (4*a[1]-a[0])/3
        return float(np.real(x @ (0.5*(S2+S2.T)) @ x))
    cS, res = R.fit(FS, B, nsamp=450); cE, _ = R.fit(lambda x, h, k: R.EH(h, k, g0), B, nsamp=450)
    lam = (cS@cE)/(cE@cE)
    print(f"b={b}: Schur O(k^2) symbol: outside K48 span {np.linalg.norm(cS - W@(W.T@cS))/np.linalg.norm(cS):.1e}; = {lam:+.6f} EH_g0, misfit {np.linalg.norm(cS-lam*cE)/np.linalg.norm(cS):.2e}; (-1/4 sqrt det = {-0.25*np.sqrt(1+4*b):+.6f})")
