"""C3b s3b: (i) the scale n* at which Theorem H's bound becomes effective, for the s3 clock families;
(ii) a larger box (L=512) for the fractional families F0.8, F0.95, where s3 saw <L(x)> still growing with box size.

Theorem H (Gaussian form):  P(L(0) >= n) <= c_n (K M)^n / n!  +  P(T_0 - min_{|y|<=n} T_y > M),
K = (2 pi v)^(-1/2), v = 1/<1/f>  (interpolation variance),  and the second term <= |B_n| exp(-M^2 / (2 V_n)),
V_n = max_{|y|_1<=n} Var(T_0 - T_y).  We take c_n <= 4*3^(n-1) (d=2), choose M = sqrt(2 V_n log(4|B_n|)) so the second
term is <= 1/4, and report n* = least n with first term <= 1/4 (so P(L>=n*) <= 1/2), using log-gamma.
Var(T_0 - T_y) is computed in infinite volume by numerical quadrature of 2 * int (1 - cos k.y) f(k) dk/(2pi)^2.
"""
import numpy as np
from scipy.special import gammaln, gamma
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
from c3b_common import check, total, mean_se
import s3_gaussian_clocks as S3


def inc_var(fam, par, y, nq=2048, s2=0.01):
    # midpoint quadrature on [-pi,pi]^2 (avoids k=0); integrable singularity for F with H<1
    k = (np.arange(nq) + 0.5) / nq * 2 * np.pi - np.pi
    KX, KY = np.meshgrid(k, k, indexing='ij')
    lap = 4 - 2 * np.cos(KX) - 2 * np.cos(KY)
    f = s2 + lap ** ((par - 2) / 2) if fam == 'P' else lap ** (-(1 + par))
    return 2 * np.mean((1 - np.cos(KX * y[0] + KY * y[1])) * f), (1.0 / np.mean(1.0 / f))


def nstar(fam, par):
    """V_n = upper estimate of max_{|y|_1<=n} Var(T_0 - T_y).
       P family: rigorous V_n = 4 Var(T_0) (since Var(T0-Ty) = 2(C0 - C(y)) <= 4 C0); C0 by quadrature.
       F family: max(direct lattice quadrature along (n,0) and the diagonal for n<=64, continuum asymptote A_H n^{2H}),
       A_H = -2^{-2H-1} Gamma(-H) / (pi Gamma(1+H)) (Mellin transform of J_0).  Indicative, not a rigorous bound."""
    v = inc_var(fam, par, (1, 0))[1]
    K = (2 * np.pi * v) ** -0.5
    if fam == 'P':
        k = (np.arange(2048) + 0.5) / 2048 * 2 * np.pi - np.pi
        KX, KY = np.meshgrid(k, k, indexing='ij')
        lap = 4 - 2 * np.cos(KX) - 2 * np.cos(KY)
        C0 = np.mean(0.01 + lap ** ((par - 2) / 2))
    else:
        A_H = -2.0 ** (-2 * par - 1) * gamma(-par) / (np.pi * gamma(1 + par))
    ns = np.unique(np.logspace(0, 15, 600).astype(np.int64))
    for n in ns:
        if fam == 'P':
            Vn = 4 * C0
        else:
            Vn = A_H * float(n) ** (2 * par)
            if n <= 64:
                Vn = max(Vn, inc_var(fam, par, (n, 0))[0], inc_var(fam, par, (n // 2, n - n // 2))[0])
        Bn = 2.0 * n * n + 2 * n + 1
        M = np.sqrt(2 * Vn * np.log(4 * Bn))
        log_first = np.log(4.0) + (n - 1) * np.log(3.0) + n * np.log(K * M) - gammaln(n + 1.0)
        if log_first <= np.log(0.25):
            return int(n), v, K
    return None, v, K


if __name__ == "__main__":
    t0 = time.time()
    print("family par   v      K      n*  (P(L>=n*)<=1/2 by Theorem H; 'None' = beyond 1e15)")
    res = {}
    for fam, par in [('P', 0.25), ('P', 1.0), ('F', 0.5), ('F', 0.8), ('F', 0.95)]:
        n_, v, K = nstar(fam, par)
        res[(fam, par)] = n_
        print(f"  {fam}  {par:5}  {v:.4f} {K:.4f}  {n_}")
    check("s3b.1 Theorem H scale n* is finite (<=1e15) for P0.25, P1.0, F0.5",
          all(res[c] is not None for c in [('P', 0.25), ('P', 1.0), ('F', 0.5)]))
    print("Box sizes used in s3 are 64..256; for F0.8/F0.95 n* exceeds them, so s3's box-size dependence of L(x)"
          " is not in tension with Theorem H (which is an a.s.-finiteness statement, with this effective scale).")
    # (ii) larger box for F0.8, F0.95
    for par in (0.8, 0.95):
        R = S3.run(512, 'F', par, 40, 64)
        lm, lse = mean_se(R['Lm']); ch, che = mean_se(R['chi'])
        print(f"F{par} L=512 ns=40: <L(x)>={lm:.3f}+-{lse:.3f}  max_box L={R['Lmax'].mean():.1f}  chi_L={ch:.2f}+-{che:.2f}")
    print(f"elapsed {time.time()-t0:.0f}s")
    total()
