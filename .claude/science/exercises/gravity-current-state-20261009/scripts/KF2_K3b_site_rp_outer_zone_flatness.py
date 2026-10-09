#!/usr/bin/env python3
"""K3b: (i) stable re-check of the sign claims in Lemma N (D'' <= 0 for lambda in [0,1]) via the
Lagrange identity; (ii) for site-RP-only measures (atoms at lambda < 0 allowed, transfer matrix not
positive), is the kernel genuinely flat in the outer zone, or only zero-curvature at one point?
Flatness measure: R_inf := max_{q0 in [pi/2, pi]} |dD/dq0| / max_{q0 in [0, pi/2]} |dD/dq0|  (grid).
For a Gaussian kernel of width s, R_inf ~ exp(-pi^2 s^2 / 8)-ish; for lambda >= 0 Lemma N gives a power floor.
"""
import numpy as np
rng = np.random.default_rng(7)

def poles(lam, m):
    # S(z) = c0 + sum mu/(zk - z) ; lam=0 atoms -> constant
    c0 = m[np.abs(lam) < 1e-12].sum()
    sel = np.abs(lam) >= 1e-12
    lam, m = lam[sel], m[sel]
    zk = (1 + lam ** 2) / (2 * lam)
    mu = m * (1 - lam ** 2) / (2 * lam)
    return c0, zk, mu

def check_sign(lam, m):
    c0, zk, mu = poles(lam, m)
    x = 1.0 / (zk - 1.0)
    S = c0 + (mu * x).sum(); S1 = (mu * x ** 2).sum(); S2 = 2 * (mu * x ** 3).sum()
    lag = (c0 * (mu * x ** 3).sum()) + 0.5 * sum(mu[i] * mu[j] * x[i] * x[j] * (x[i] - x[j]) ** 2
                                                   for i in range(len(x)) for j in range(len(x)))
    # 2 S1^2 - S S2 = -2 * lag  (exact identity)
    return -2 * lag <= 0, S1 > 0

def Dq(lam, m, q):
    z = np.cos(q)
    S = (m[None, :] * (1 - lam[None, :] ** 2) / (1 + lam[None, :] ** 2 - 2 * lam[None, :] * z[:, None])).sum(1)
    return 1.0 / S

q = np.linspace(0, np.pi, 4001)
def flatness(D):
    dD = np.abs(np.gradient(D, q))
    half = len(q) // 2
    return dD[half:].max() / dD[:half].max()

ok = 0
for _ in range(20000):
    k = rng.integers(1, 6)
    lam = np.concatenate([[0.0], 1 - 10 ** rng.uniform(-4, 0, size=k)])
    m = 10 ** rng.uniform(-3, 0, size=k + 1)
    a, b = check_sign(lam, m)
    ok += a and b
print(f"(i) lambda in [0,1]: D'(1)<0 and D''(1)<=0 via Lagrange identity in {ok}/20000 samples")

print("(ii) outer-zone flatness R_inf vs sigma^2; Lemma-N floor 1/(sigma^2+2/3)^2 shown for comparison")
best = []
for neg in (False, True):
    worst = np.inf; wc = None
    for _ in range(40000):
        k = rng.integers(1, 6)
        lam = rng.uniform(-0.999, 0.999, size=k) if neg else 1 - 10 ** rng.uniform(-4, 0, size=k)
        m = 10 ** rng.uniform(-3, 0, size=k)
        D = Dq(lam, m, q)
        c2 = (D[1] - D[0]) / q[1] ** 2
        if c2 <= 0:
            continue
        # sigma^2 from fit of first few points: D - D0 = c2 q^2 + c4 q^4
        qq = q[1:40]; yy = D[1:40] - D[0]
        A = np.stack([qq ** 2, qq ** 4], 1); c2f, c4f = np.linalg.lstsq(A, yy, rcond=None)[0]
        sig2 = -4 * c4f / c2f
        if sig2 <= 0.05:
            continue
        Rf = flatness(D)
        val = Rf * (sig2 + 2 / 3) ** 2
        if val < worst:
            worst, wc = val, (np.round(lam, 4), np.round(m, 4), round(sig2, 3), Rf)
    print(f"   {'site-RP only (lambda<0 allowed)' if neg else 'positive transfer (lambda>=0)'}: min R_inf*(sigma^2+2/3)^2 = {worst:.3e}")
    print(f"      worst case lam={wc[0]} m={wc[1]} sigma^2={wc[2]} R_inf={wc[3]:.3e}")
for s in (1.0, 1.5, 2.0):
    n = np.arange(1, int(14 * s) + 3); W = np.exp(-n ** 2 / (2 * s * s)); W /= (W * n ** 2).sum()
    D = (2 * W[None, :] * (1 - np.cos(np.outer(q, n)))).sum(1) / 2
    print(f"   Gaussian s={s}: R_inf={flatness(D):.3e}  floor={1/(s*s+2/3)**2:.3e}")
