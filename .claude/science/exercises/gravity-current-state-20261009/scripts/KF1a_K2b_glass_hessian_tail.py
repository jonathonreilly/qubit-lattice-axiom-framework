"""K2b: per-configuration infinitesimal Hessian (glass branch) of the 2D liquid arm: step-size robustness and tail.
Same seed/model as K2 (abc); recompute H0 with steps 1e-4, 1e-5, 1e-6 on flip-free windows; report quantiles,
min triangle angle, max cotan weight per config, and the E_g mean with robust (median, trimmed) estimators."""
import numpy as np, sys
sys.argv = [sys.argv[0], '7', 'none']
exec(open('K2_delaunay_flip_kinks_2d.py').read().split("if __name__ == '__main__':")[0])
N = 400; L = np.sqrt(N); A0 = L*np.eye(2)
rows = []
for c in range(40):
    X = rng.uniform(0, L, (N, 2)); fr = periodic_delaunay(X, A0); es0 = edgeset(*fr)
    K0 = stiffness(X, A0, *fr); E0 = E_vac(K0)
    hs = []
    for h in (1e-4, 1e-5, 1e-6):
        Ep, Egp, frp = energies(X, A0, h, fr); Em, Egm, frm = energies(X, A0, -h, fr)
        ok = edgeset(*frp) == es0 and edgeset(*frm) == es0
        hs.append(((Egp + Egm - 2*E0)/h**2/N, ok))
    pos = X[fr[0]] + np.einsum("tvk,kl->tvl", fr[1], A0)
    ang = []
    for a in range(3):
        u = pos[:, (a+1) % 3] - pos[:, a]; v = pos[:, (a+2) % 3] - pos[:, a]
        ang.append(np.arccos(np.clip(np.einsum('ti,ti->t', u, v)/np.linalg.norm(u, axis=1)/np.linalg.norm(v, axis=1), -1, 1)))
    ang = np.array(ang)
    wmax = -np.min(K0 - np.diag(np.diag(K0)))
    rows.append([hs[0][0], hs[1][0], hs[2][0], hs[0][1], hs[1][1], hs[2][1], ang.min(), np.pi - ang.max(), wmax])
r = np.array(rows)
np.set_printoptions(linewidth=160, precision=4, suppress=True)
print("glass-branch Hessian per site, steps 1e-4 / 1e-5 / 1e-6 (flip-free flags), min angle, pi - max angle, max weight")
for x in r[np.argsort(-np.abs(r[:, 2]))][:8]: print(x)
for k, h in enumerate((1e-4, 1e-5, 1e-6)):
    x = r[:, k]; q = np.quantile(x, [0.1, 0.25, 0.5, 0.75, 0.9])
    xs = np.sort(x)[4:-4]
    print(f"step {h:.0e}: mean {x.mean():+.4f}  median {np.median(x):+.4f}  10/25/50/75/90% {q}  trimmed(10%) mean {xs.mean():+.4f} +- {xs.std(ddof=1)/np.sqrt(len(xs)):.4f}")
print("corr(|H0|, 1/min angle) =", np.corrcoef(np.abs(r[:, 1] - np.median(r[:, 1])), 1/np.minimum(r[:, 6], r[:, 7]))[0, 1])
