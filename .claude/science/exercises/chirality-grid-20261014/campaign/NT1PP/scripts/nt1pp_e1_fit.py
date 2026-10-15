"""NT-1'' E1 fit (PREREG section 5): WLS of ln(mean tau) vs Lx; L1 contrast. usage: python3 nt1pp_e1_fit.py"""
import numpy as np
for sizes in ((4, 6, 8, 10), (6, 8, 10)):
    L = np.array(sizes, float); y = []; s = []; P = []; n = []
    for Lx in sizes:
        R = np.load(f"e1_Lx{Lx}.npy"); m = R.mean(0); se = R.std(0, ddof=1) / np.sqrt(len(R))
        y.append(np.log(m[0])); s.append(se[0] / m[0]); P.append(m[3]); n.append(len(R))
    y, s, P = np.array(y), np.array(s), np.array(P)
    Wt = 1 / s**2; X = np.stack([np.ones_like(L), -L], 1)
    cov = np.linalg.inv(X.T @ (Wt[:, None] * X)); beta = cov @ X.T @ (Wt * y)
    chi2 = np.sum(Wt * (y - X @ beta) ** 2); dof = len(L) - 2
    sig_u = np.sqrt(cov[1, 1]); sig_s = sig_u * np.sqrt(max(1.0, chi2 / dof)) if dof > 0 else sig_u
    sig = max(sig_u, sig_s); nu = beta[1]
    LP = L * P; dev = np.abs(LP / LP.mean() - 1).max(); ratio = P / np.exp(y)
    print(f"sizes {sizes}: n per size {n}; nu = {nu:.3f} +- {sig:.3f} (unscaled {sig_u:.3f}, chi2/dof {chi2:.2f}/{dof}) -> nu/sigma = {nu/sig:.1f}")
    print(f"   L1 Lx*plateau {np.round(LP, 4)} max rel dev {dev:.3f}; ratio L1/11112 {np.round(ratio, 1)}")
    print(f"   fixed-wording items: sizes>=3 {len(L)>=3 and min(n)>=4}; nu>0 at >=3 sigma {nu > 0 and nu/sig >= 3}; L1 prop 1/Lx (+-20%) {dev <= 0.2}; "
          f"registered ratio>=10 at each size {bool(np.all(ratio >= 10))}")
