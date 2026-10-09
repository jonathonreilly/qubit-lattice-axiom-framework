#!/usr/bin/env python3
"""K3 (kill agent, route F2): reflection positivity forces a power-law floor on zone-face flatness.

Lemma N (proof in the report). Free field on Z_tau, translation-invariant quadratic action,
positive transfer matrix (site + link RP <=> G(n) = int lambda^|n| dm(lambda), m >= 0 on [0,1]).
Write z = cos q0 and D(z) = 1/S(z) for the inverse propagator. Then -D is Nevanlinna:
    D(z) = a - b z - int_{t>1} dnu(t)/(t - z),  b >= 0, nu >= 0,
and with  sigma^2 := -4 c4/c2  (D = c0 + c2 q0^2 + c4 q0^4 + ...; sigma = s for the Gaussian
kernel (2/s^2)(1-exp(-s^2 q^2/2))),  the face-to-origin curvature ratio obeys
    R := |d2D/dq0^2 (pi)| / |d2D/dq0^2 (0)| = |D'(-1)|/|D'(1)|  >=  1/(sigma^2 + 2/3)^2,
with equality iff b = 0 and nu is one atom (the rational kernel S/(1+s^2 S)).
With hypercubic W(B4) symmetry the same bound holds along every spatial axis.

Checks:
 (1) random positive measures on (0,1): min of R*(sigma^2+2/3)^2 over samples (expect >= 1, ~1 at one atom);
 (2) same with atoms at lambda < 0 allowed (site RP only): is the bound still respected?
 (3) Gaussian time kernel: R vs sigma (exponentially small) and Hankel RP test (expect violation);
 (4) converse sanity: random Nevanlinna-form D -> Hankel matrix of G(n) is PSD.
"""
import numpy as np

rng = np.random.default_rng(20261009)


def S_and_derivs(z, lam, m):
    # S(z) = sum m (1-lam^2)/(1+lam^2-2 lam z)
    den = 1 + lam ** 2 - 2 * lam * z
    S = (m * (1 - lam ** 2) / den).sum()
    S1 = (m * (1 - lam ** 2) * 2 * lam / den ** 2).sum()
    S2 = (m * (1 - lam ** 2) * 8 * lam ** 2 / den ** 3).sum()
    return S, S1, S2


def D_derivs(z, lam, m):
    S, S1, S2 = S_and_derivs(z, lam, m)
    D1 = -S1 / S ** 2
    D2 = (2 * S1 ** 2 - S * S2) / S ** 3
    return D1, D2


def ratio(lam, m):
    D1p, D2p = D_derivs(1.0, lam, m)
    D1m, _ = D_derivs(-1.0, lam, m)
    R = abs(D1m) / abs(D1p)
    sig2 = 1.0 / 3.0 + D2p / D1p  # D2/D1 >= 0 when both negative
    return R, sig2, D1p, D2p


def sample(neg=False):
    k = rng.integers(1, 6)
    if neg:
        lam = rng.uniform(-0.999, 0.999, size=k)
    else:
        lam = 1 - 10 ** rng.uniform(-4, 0, size=k)  # spread toward lambda -> 1 (wide kernels)
        lam = np.clip(lam, 1e-6, 1 - 1e-9)
    m = 10 ** rng.uniform(-3, 0, size=k)
    return lam, m


if __name__ == "__main__":
    print("(1) lambda in (0,1), 200000 random measures")
    worst = np.inf
    worst_case = None
    bad_sign = 0
    for _ in range(200000):
        lam, m = sample()
        R, sig2, D1p, D2p = ratio(lam, m)
        if D1p >= 0 or D2p > 1e-12 * abs(D1p):
            bad_sign += 1
        q = R * (sig2 + 2.0 / 3.0) ** 2
        if q < worst:
            worst, worst_case = q, (len(lam), sig2)
    print(f"   min R*(sigma^2+2/3)^2 = {worst:.12f}  (atoms, sigma^2) at min = {worst_case}; sign violations = {bad_sign}")
    for lam1 in (0.5, 0.9, 0.99, 0.999):
        R, sig2, _, _ = ratio(np.array([lam1]), np.array([1.0]))
        print(f"   one atom lambda={lam1}: sigma^2={sig2:.4f} R={R:.4e} bound={1/(sig2+2/3)**2:.4e}")

    print("(2) atoms at lambda < 0 allowed (site RP, transfer matrix not positive), 200000 samples")
    worst = np.inf
    viol = 0
    nonmono = 0
    for _ in range(200000):
        lam, m = sample(neg=True)
        R, sig2, D1p, D2p = ratio(lam, m)
        if D1p >= 0:
            nonmono += 1
            continue
        if sig2 <= 0:
            continue
        q = R * (sig2 + 2.0 / 3.0) ** 2
        worst = min(worst, q)
        if q < 1 - 1e-9:
            viol += 1
    print(f"   min R*(sigma^2+2/3)^2 = {worst:.6f}; violations = {viol}; samples with D'(1) >= 0 skipped = {nonmono}")

    print("(3) Gaussian time kernel K(q0) = sum_n W(n)(1-cos q0 n), W ~ exp(-n^2/2s^2), normalized to q0^2")
    for s in (0.5, 1.0, 1.5, 2.0, 3.0):
        n = np.arange(1, int(14 * s) + 3)
        W = np.exp(-n ** 2 / (2 * s * s))
        W = W / (W * n ** 2).sum()
        c2 = (W * n ** 2).sum() / 2 * 2 / 2  # K ~ sum W n^2 q^2/2 *2 (both signs) -> normalized to 1
        curv0 = (2 * W * n ** 2).sum() / 2      # d2K/dq0^2 at 0  (sum over +-n)
        curvpi = (2 * W * n ** 2 * np.cos(np.pi * n)).sum() / 2
        c4 = -(2 * W * n ** 4).sum() / 24 / 2
        sig2 = -4 * c4 / (curv0 / 2)
        # Hankel RP test (as R2_c4) with M = 0.3
        Nq = 1 << 15
        qq = 2 * np.pi * np.arange(Nq) / Nq
        Kq = (2 * W[None, :] * (1 - np.cos(np.outer(qq, n)))).sum(1) / 2
        G = np.fft.ifft(1.0 / (0.09 + Kq)).real
        T = 10
        H = np.array([[G[i + j] for j in range(T + 1)] for i in range(T + 1)])
        ev = np.linalg.eigvalsh(H)
        print(f"   s={s:3.1f} sigma^2={sig2:7.3f}  R={abs(curvpi)/curv0:.3e}  RP bound={1/(sig2+2/3)**2:.3e}  Hankel min/max={ev.min()/ev.max():+.2e}")

    print("(4) converse: Nevanlinna-form D = a - b z - sum nu/(t - z) -> Hankel PSD?")
    worst = np.inf
    for _ in range(300):
        k = rng.integers(1, 4)
        t = 1 + 10 ** rng.uniform(-3, 1, size=k)
        nu = 10 ** rng.uniform(-3, 0, size=k)
        b = rng.uniform(0, 1)
        Nq = 1 << 14
        z = np.cos(2 * np.pi * np.arange(Nq) / Nq)
        Dz = -b * z - (nu[None, :] / (t[None, :] - z[:, None])).sum(1)
        Dz = Dz - Dz.min() + 0.05  # choose a so D > 0 on [-1,1]
        G = np.fft.ifft(1.0 / Dz).real
        T = 8
        H = np.array([[G[i + j] for j in range(T + 1)] for i in range(T + 1)])
        Hl = np.array([[G[i + j + 1] for j in range(T + 1)] for i in range(T + 1)])
        ev = min(np.linalg.eigvalsh(H).min() / np.linalg.eigvalsh(H).max(),
                 np.linalg.eigvalsh(Hl).min() / np.linalg.eigvalsh(Hl).max())
        worst = min(worst, ev)
    print(f"   worst min/max eigenvalue over site and link Hankel matrices = {worst:+.2e} (>= -1e-12 means RP holds)")
