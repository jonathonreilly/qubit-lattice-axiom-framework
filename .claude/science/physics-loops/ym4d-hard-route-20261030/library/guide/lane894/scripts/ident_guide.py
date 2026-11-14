"""GUIDE check of the identities of Steps 3, 5, 6c on random chains (refutes or guides only).
Criteria written first:
I1 Theorem A1 holds to 1e-10 for n = 1, 2, 3 (exact identity; E Delta^4 computed from the two-time law).
I2 Lemma R, Corollary A2 (a), (KE-ineq) hold.
I3 Lemma B4 (a), (b) hold for the top two odd eigenfunctions, and for the top with the third.
I4 Proposition B5: never both x, x2 < 0.3048; and (1-x-x2)(1-c) <= c/2 whenever x, x2 < 1.
I5 Proposition D: whenever a(1-rho) > M and kappa < 2, (WALL)_M fails (checked with random a, M).
"""
import numpy as np
rng = np.random.default_rng(894)
def chain(n, sharp):
    # symmetric PSD positive kernel with an involution sigma(i) = i + n mod 2n
    A = rng.random((2 * n, 2 * n)) ** sharp
    if rng.random() < 0.5:                      # make near-bit structure sometimes
        eps = 10 ** rng.uniform(-4, 0)
        blk = np.block([[np.ones((n, n)), eps * np.ones((n, n))], [eps * np.ones((n, n)), np.ones((n, n))]])
        A = A * blk
    S = np.roll(np.eye(2 * n), n, axis=0)
    A = A + S @ A @ S
    K = A @ A.T
    ev, U = np.linalg.eigh(K); om = np.abs(U[:, -1]); lam = ev[-1]
    P = K * om[None, :] / (lam * om[:, None]); nu = om ** 2 / (om ** 2).sum()
    return P, nu, S
worst = dict(A1=0.0); cnt = dict(R=0, A2=0, KE=0, B4a=0, B4b=0, B5=0, D=0, n=0, nearbit=0, both_small=0)
for trial in range(600):
    n = int(rng.integers(3, 9)); P, nu, S = chain(n, rng.uniform(0.5, 6))
    D = np.sqrt(nu); Sym = D[:, None] * P / D[None, :]; Sym = (Sym + Sym.T) / 2
    ev, V = np.linalg.eigh(Sym)
    odd, even = [], []
    for k in range(2 * n):
        f = V[:, k] / D
        (even if np.allclose(S @ f, f, atol=1e-7) else odd).append((ev[k], f))
    odd.sort(key=lambda t: -t[0]); even.sort(key=lambda t: -t[0])
    theta, g = odd[0]; rho = even[1][0]
    g = g / np.sqrt((nu * g * g).sum()); kappa = (nu * g ** 4).sum(); h = g * g - 1
    cnt['n'] += 1; cnt['nearbit'] += kappa < 1.2
    for nn in (1, 2, 3):
        Pn = np.linalg.matrix_power(P, nn)
        d4 = (nu[:, None] * Pn * (g[None, :] - g[:, None]) ** 4).sum()
        lhs = (nu * h * (h - Pn @ h)).sum(); rhs = 4 / 3 * kappa * (1 - theta ** nn) - d4 / 6
        worst['A1'] = max(worst['A1'], abs(lhs - rhs))
        cnt['A2'] += not (d4 <= 8 * kappa * (1 - theta ** nn) - 6 * (1 - rho ** nn) * (kappa - 1) + 1e-10)
    cnt['R'] += not ((kappa - 1) * (1 - rho) <= kappa * (1 - theta ** 2) + 1e-10)
    lamb_h = (nu * h * (h - P @ h)).sum()
    cnt['KE'] += not (lamb_h <= kappa * (1 - theta ** 2) + 1e-10)
    for k in (1, 2):
        if k >= len(odd): continue
        th2, f = odd[k]; f = f / np.sqrt((nu * f * f).sum()); kf = (nu * f ** 4).sum()
        g2f2 = (nu * g * g * f * f).sum(); f2Pg2 = (nu * f * f * (P @ (g * g))).sum()
        cnt['B4a'] += not ((theta + th2 - rho - 0.5) * g2f2 <= 0.5 * f2Pg2 + 1e-10)
        cnt['B4b'] += not (((1 - rho) - (1 - theta) - (1 - th2)) * g2f2 <= 0.5 * np.sqrt(kappa * kf * (1 - theta ** 2) * (1 - th2 ** 2)) + 1e-10)
        x = (1 - theta ** 2) / (1 - rho); x2 = (1 - th2 ** 2) / (1 - rho)
        if x < 1 and x2 < 1:
            c = np.sqrt(x * x2 / ((1 - x) * (1 - x2)))
            if c < 1: cnt['B5'] += not ((1 - x - x2) * (1 - c) <= c / 2 + 1e-10)
        cnt['both_small'] += (x < 0.3048 and x2 < 0.3048)
    a = rng.uniform(1, 200); M = rng.uniform(1, 100)
    if a * (1 - rho) > M and kappa < 2:
        cnt['D'] += (kappa - 1 >= min(1.0, a / M * kappa * (1 - theta ** 2)))
print('max |A1 residual| =', worst['A1']); print(cnt)
