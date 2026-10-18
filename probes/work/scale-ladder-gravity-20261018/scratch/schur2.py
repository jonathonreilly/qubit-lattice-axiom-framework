import numpy as np, sys
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
Qe, Mh = R.regge(np.eye(4)); C = R.compl(Mh(np.zeros(4))); HC = R.HC
def seff(k): return R.schur(Qe(k), Mh(k), Mh(-k), C)
rng = np.random.default_rng(0)
for t in range(3):
    kd = rng.standard_normal(4); kd /= np.linalg.norm(kd)
    for s in (0.05, 0.01):
        k = s*kd; S = seff(k); D = C.T @ Qe(k) @ C
        sd = np.sort(np.linalg.svd(D, compute_uv=False))
        ss = np.sort(np.linalg.svd(S, compute_uv=False))
        print(f"s={s}: D sv min/max {sd[0]/sd[-1]:.1e}; Seff sv/max " + " ".join(f"{x/ss[-1]:.1e}" for x in ss[:6]))
# fit Seff O(k^2) symbol in the census basis, compare with EH and the K48 span
B, W, *_ = R.census(2, 2, R.GROUPS['K48']); W, _ = np.linalg.qr(W)
def FS(x, h, k):
    a = [seff(e*k)/e**2 for e in (2e-3, 1e-3)]; S2 = (4*a[1]-a[0])/3
    return float(np.real(x @ (0.5*(S2+S2.T)) @ x))
cS, res = R.fit(FS, B, nsamp=500); cE, _ = R.fit(lambda x, h, k: R.EH(h, k, np.eye(4)), B, nsamp=500)
lam = (cS@cE)/(cE@cE)
print(f"Schur O(k^2) symbol: fit residual {res:.1e}; outside K48 span {np.linalg.norm(cS - W@(W.T@cS))/np.linalg.norm(cS):.1e}; best EH multiple {lam:+.6f}, misfit {np.linalg.norm(cS-lam*cE)/np.linalg.norm(cS):.3e}")
