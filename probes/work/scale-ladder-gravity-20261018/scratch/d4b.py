import sys, pickle, numpy as np
sys.path.insert(0, '.'); sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import regge_generic as RG
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
C = pickle.load(open('d4.pkl', 'rb'))
def basis_split(k):
    M = C.line_map(k); G = C.gauge(k)
    A = np.hstack([M, G]); u, s, vh = np.linalg.svd(A.real if np.isrealobj(k) else A)
    r = int((s > 1e-9*s[0]).sum()); return M, u[:, r:], r
M0, Cc, r = basis_split(np.zeros(4)); print("dim(im M + im G) at k=0:", r, " complement:", Cc.shape[1])
# use a fixed real complement of im M(0) + im G(0)
def seff(k):
    Q = C.Q(k); Mp, Mm = C.line_map(k), C.line_map(-k)
    D = Cc.T @ Q @ Cc
    return Mm.T @ Q @ Mp - (Mm.T @ Q @ Cc) @ np.linalg.solve(D, Cc.T @ Q @ Mp), D
kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
for s in (0.05, 0.02, 0.01):
    S, D = seff(s*kd); print(f"s={s}: min|eig D| {np.min(np.abs(np.linalg.eigvals(D))):.2e};  |Seff|/s^2 {np.abs(S).max()/s**2:.4f}")
B, W, *_ = R.census(2, 2, R.GROUPS['B4'])
def FS(x, h, k):
    a = [seff(e*k)[0]/e**2 for e in (2e-2, 1e-2)]; S2 = (4*a[1]-a[0])/3
    return float(np.real(x @ (0.5*(S2+S2.T)) @ x))
cS, res = R.fit(FS, B, nsamp=700); cE, _ = R.fit(lambda x, h, k: R.EH(h, k, np.eye(4)), B, nsamp=700)
lam = (cS@cE)/(cE@cE); print(f"D4-cone full form O(k^2) = {lam:+.6f} EH, misfit {np.linalg.norm(cS-lam*cE)/np.linalg.norm(cS):.2e} (fit residual {res:.1e})")
# pullback too
def FP(x, h, k):
    a = [(C.line_map(-e*k).T @ C.Q(e*k) @ C.line_map(e*k))/e**2 for e in (2e-2, 1e-2)]; S2 = (4*a[1]-a[0])/3
    return float(np.real(x @ (0.5*(S2+S2.T)) @ x))
cP, _ = R.fit(FP, B, nsamp=700); lp = (cP@cE)/(cE@cE); print(f"D4-cone pullback O(k^2) = {lp:+.6f} EH, misfit {np.linalg.norm(cP-lp*cE)/np.linalg.norm(cP):.2e}")
