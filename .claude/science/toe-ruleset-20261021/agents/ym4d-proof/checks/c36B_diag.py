# post-run diagnostic (disclosed, not a criterion): contraction convergence of c36 B vs background size
import sys, numpy as np
sys.path.insert(0, "/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks")
import c36_nah1 as M
m = M.Model2(1.0); G = m.G
rng = np.random.default_rng(36002)
_ = M.su2_exp(0.05 * rng.standard_normal((m.nc, 3))); _ = M.haar(rng, G.nb)  # same stream position as B's second background
for t in (0.15, 0.06, 0.08, 0.10, 0.12):
    r2 = np.random.default_rng(int(t * 1000) + 7)
    V = M.su2_exp(t * r2.standard_normal((m.nc, 3)))
    ang = 0.0
    for iX, X in enumerate(G.blocks):
        Xm = M.coarse_plus(G, X, 0); Xn = M.coarse_plus(G, X, 1)
        VP = V[iX*2] @ V[G.bidx[Xm]*2+1] @ M.dag(V[G.bidx[Xn]*2]) @ M.dag(V[iX*2+1])
        ang = max(ang, np.linalg.norm(M.su2_log(VP)))
    with np.errstate(all="ignore"):
        try:
            U, A, U0, ops0, hist = M.branch(m, V, maxit=60)
            res = hist[-1]
        except Exception as e:
            res = float("nan")
    print(f"t={t}: max |log V_P| = {ang:.3f}; final residual {res:.1e} after {len(hist)} its; first {hist[:4]}")
