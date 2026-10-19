"""Reviewer r2: Theorem H and Corollary H-G.

(a) Kolmogorov interpolation variance, closed form for AR(1) on Z: v = s^2(1-rho^2)/(1+rho^2) = [int 1/f]^-1;
    dense-matrix check at an interior site; det Cov(T_S|T_0) >= v^|S| for random S (sup of conditional density).
(b) Theorem H-a on Z^2 with T = T1 + Y, T1 = beta*(x1+x2) DETERMINISTIC NON-STATIONARY tilt, Y iid N(0,1)
    (premise (i), K = (2 pi)^-1/2).  MC of P(L(0)>=n) against c_n (KM)^n/n! + psi_n(M), psi computed by quadrature,
    exact SAW counts c_n on Z^2; for a grid of M.  Also a steep tilt where the bound is useless but still valid.
(c) H-b arithmetic: c_n (K eta n)^n / n! <= (D/(D-1)) (e (D-1) K eta)^n.
(d) Fractional clocks, d=2: f_H = lap^-(1+H) >= 8^-(1+H) (so T = T1 + white noise with the residual spectral weight
    f_H - 8^-(1+H) >= 0 realises premise (i)); increment variance exponent ~ 2H on a large torus (FFT, not quadrature).
(e) SCOPE: a stationary Gaussian clock with power-law covariance but int 1/f = infinity:
    T_x = W_x - W_{x+e1}, W power-law; f_T = (2-2cos k1) f_W vanishes on k1=0.  Interpolation variance -> 0 with
    grid refinement, while C_T(r) decays as a power law.  So 'including ALL power-law covariances' is too broad.
"""
import math
import numpy as np
from scipy.stats import norm
from scipy.special import gammaln
from rv_common import check, total

rng = np.random.default_rng(4242)

# ---------- (a) ----------
for rho, s in [(0.9, 1.0), (0.5, 2.0), (-0.7, 1.0)]:
    n = 401
    i = np.arange(n)
    Sig = s ** 2 * rho ** np.abs(i[:, None] - i[None, :])
    Q = np.linalg.inv(Sig)
    c = n // 2
    v_dense = 1 / Q[c, c]
    v_cf = s ** 2 * (1 - rho ** 2) / (1 + rho ** 2)
    k = (np.arange(1 << 16) + 0.5) / (1 << 16) * 2 * np.pi
    fk = s ** 2 * (1 - rho ** 2) / np.abs(1 - rho * np.exp(1j * k)) ** 2
    v_spec = 1 / np.mean(1 / fk)
    check(f"a1 AR(1) rho={rho}: 1/Q_cc = closed form = 1/mean(1/f)", abs(v_dense / v_cf - 1) < 1e-10 and abs(v_spec / v_cf - 1) < 1e-8,
          f"{v_dense:.10f} {v_cf:.10f} {v_spec:.10f}")
    worst = np.inf
    for rep in range(300):
        m = rng.integers(1, 15)
        S = c + rng.choice(np.r_[-100:0, 1:101], size=m, replace=False)
        Aidx = np.r_[c, S]
        Sub = Sig[np.ix_(Aidx, Aidx)]
        cond = Sub[1:, 1:] - np.outer(Sub[1:, 0], Sub[0, 1:]) / Sub[0, 0]
        worst = min(worst, np.linalg.slogdet(cond)[1] / m - np.log(v_cf))
    check(f"a2 AR(1) rho={rho}: det Cov(T_S|T_0)^(1/|S|) >= v (300 random S)", worst >= -1e-10, f"min log-margin {worst:.4f}")

# ---------- (b) ----------
cn = [1, 4, 12, 36, 100, 284, 780, 2172, 5916, 16268, 44100]  # SAWs on Z^2 (OEIS A001411)
W = 14
side = 2 * W + 1
xs = np.indices((side, side)).reshape(2, -1).T - W
Nn = len(xs)
id_ = {tuple(p): k for k, p in enumerate(xs)}
nb = -np.ones((Nn, 4), np.int64)
for k, p in enumerate(xs):
    for j, d in enumerate(((1, 0), (-1, 0), (0, 1), (0, -1))):
        q_ = (p[0] + d[0], p[1] + d[1])
        if q_ in id_:
            nb[k, j] = id_[q_]
c0 = id_[(0, 0)]
dist1 = np.abs(xs).sum(1)


import numba as _nb


@_nb.njit(cache=True)
def _L_all(T, nb):
    order = np.argsort(T)
    L = np.zeros(T.shape[0], np.int64)
    for x in order:
        best = -1
        for j in range(4):
            y = nb[x, j]
            if y >= 0 and T[y] < T[x] and L[y] > best:
                best = L[y]
        L[x] = best + 1
    return L


def L_of_0(T):
    return _L_all(T, nb)[c0]


def psi(n, M, beta):
    """P(T_0 - min_{|y|<=n, y!=0} T_y > M), T = beta*(x1+x2) + Y, by quadrature over Y_0."""
    ys = xs[(dist1 <= n) & (dist1 > 0)]
    tilt = beta * ys.sum(1)
    u = np.linspace(-9, 9, 4001)
    du = u[1] - u[0]
    # P(all T_y >= u - M) = prod_y P(Y_y >= u - M - tilt_y)
    logp = norm.logsf((u[:, None] - M - tilt[None, :])).sum(1)
    return float(np.sum(norm.pdf(u) * (1 - np.exp(logp))) * du)


K = (2 * np.pi) ** -0.5
for beta, R in [(0.15, 40000), (1.5, 20000)]:
    Ls = np.empty(R, np.int64)
    tilt_all = beta * xs.sum(1)
    for r in range(R):
        Ls[r] = L_of_0(tilt_all + rng.standard_normal(Nn))
    allok = True
    rep = []
    for n in range(1, 11):
        p = (Ls >= n).mean(); se = math.sqrt(max(p * (1 - p), 1e-12) / R)
        best = np.inf
        for M in np.linspace(0.5, 12, 24):
            b = cn[n] * (K * M) ** n / math.factorial(n) + psi(n, M, beta)
            best = min(best, b)
            allok &= (p - 4 * se <= b)
        rep.append(f"n={n}:P={p:.3g},minbound={best:.3g}")
    check(f"b1 beta={beta}: P(L(0)>=n) <= c_n(KM)^n/n! + psi_n(M) for n=1..10, 24 values of M (T1 non-stationary)", allok,
          "; ".join(rep[::3]))
    # {L(0) >= n} depends only on B(0,n); n <= 10 < W = 14, so the open box computes these events exactly.

# ---------- (c) ----------
ok = True
for D in (2, 4, 6, 8):
    for Kc in (0.3, 1.0, 3.0):
        for eta in np.linspace(0.01, 1, 15):
            for n in range(1, 60):
                c_n = D * (D - 1) ** (n - 1)
                lhs = math.log(c_n) + n * math.log(Kc * eta * n) - gammaln(n + 1)
                rhs = math.log(D / (D - 1)) + n * math.log(math.e * (D - 1) * Kc * eta)
                ok &= lhs <= rhs + 1e-12
check("c1 c_n (K eta n)^n/n! <= (D/(D-1)) (e(D-1)K eta)^n on a grid", ok)

# ---------- (d) ----------
Lt = 4096
k = 2 * np.pi * np.fft.fftfreq(Lt)
KX, KY = np.meshgrid(k, k, indexing='ij')
lap = 4 - 2 * np.cos(KX) - 2 * np.cos(KY)
TORUS = {}
SHAPE = {}
for H in (0.5, 0.8, 0.95):
    lap1 = lap.copy(); lap1[0, 0] = 1.0
    fH = lap1 ** (-(1 + H)); fH[0, 0] = 0.0
    floor = 8.0 ** (-(1 + H))
    resid_min = (fH - floor)[lap > 0].min()
    check(f"d1 H={H}: f_H - 8^-(1+H) >= 0 off the zero mode (white-noise component of variance 8^-(1+H) exists)",
          resid_min >= -1e-15, f"min residual {resid_min:.3e}")
    # continuum constant: int_R2 2(1-cos k.r)|k|^-(2+2H) d2k/(2pi)^2 = A_H r^(2H); A_H by direct Bessel quadrature
    from scipy.integrate import quad
    from scipy.special import j0, gamma as Gm
    I1 = quad(lambda u: (1 - j0(u)) * u ** (-1 - 2 * H), 0, 50, limit=400)[0]
    I2 = quad(lambda u: (1 - j0(u)) * u ** (-1 - 2 * H), 50, np.inf, limit=400)[0] if H < 0.9 else \
        quad(lambda u: u ** (-1 - 2 * H), 50, np.inf)[0] - quad(lambda u: j0(u) * u ** (-1 - 2 * H), 50, 5e4, limit=4000)[0]
    A_num = (I1 + I2) / np.pi
    A_author = -2.0 ** (-2 * H - 1) * Gm(-H) / (np.pi * Gm(1 + H))
    check(f"d2 H={H}: continuum increment constant A_H (Bessel quadrature) equals s3b's closed form", abs(A_num / A_author - 1) < 2e-3,
          f"{A_num:.5f} vs {A_author:.5f}")
    # torus deficit at fixed r=8 for the author's box sizes: Var_torus,L(8) / (A_H 8^(2H))
    rat = []
    for Ls_ in (64, 128, 256, 512, 4096):
        kq = 2 * np.pi * np.fft.fftfreq(Ls_)
        B1, B2 = np.meshgrid(kq, kq, indexing='ij')
        lq = 4 - 2 * np.cos(B1) - 2 * np.cos(B2); lq[0, 0] = 1.0
        fq = lq ** (-(1 + H)); fq[0, 0] = 0.0
        rat.append(2 * np.mean((1 - np.cos(B1 * 8)) * fq) / (A_author * 8 ** (2 * H)))
        SHAPE.setdefault(H, []).append(np.mean((1 - np.cos(B1 * 32)) * fq) / np.mean((1 - np.cos(B1 * 1)) * fq))
    TORUS[H] = rat
    print(f"  INFO H={H}: Var_torus(r=8)/(A_H 8^2H) for L=64,128,256,512,4096: " + " ".join(f"{x:.3f}" for x in rat))
    check(f"d3 H={H}: torus increment variance increases monotonically with box size (IR cutoff)", np.all(np.diff(rat) > 0))
# NOTE (reviewer): a first version of d4 compared absolute variances; that is ill-posed because a global rescaling of T
# does not change the record (Lemma 0).  The scale-free quantity is the SHAPE Var(32)/Var(1).
for H in (0.5, 0.8, 0.95):
    sh_ = np.array(SHAPE[H]) / SHAPE[H][-1]
    print(f"  INFO H={H}: shape Var(32)/Var(1) on torus L=64..512, relative to L=4096: " + " ".join(f"{x:.3f}" for x in sh_[:-1]))
d95 = 1 - SHAPE[0.95][3] / SHAPE[0.95][-1]; d05 = 1 - SHAPE[0.5][3] / SHAPE[0.5][-1]
check("d4 at L=512 the clock's large/small-scale shape is still far from converged for H=0.95, not for H=0.5",
      d95 > 0.2 and d05 < 0.05, f"shape deficit H=0.95: {d95:.3f}, H=0.5: {d05:.3f}")

# ---------- (e) ----------
alpha = 1.0
vs = []
for Lg in (64, 256, 1024):
    kk = (np.arange(Lg) + 0.5) / Lg * 2 * np.pi - np.pi       # midpoint grid: avoids exact zeros
    A1, A2 = np.meshgrid(kk, kk, indexing='ij')
    lp = 4 - 2 * np.cos(A1) - 2 * np.cos(A2)
    fW = 0.01 + lp ** ((alpha - 2) / 2)
    fT = (2 - 2 * np.cos(A1)) * fW
    vs.append(1 / np.mean(1 / fT))
check("e1 T = W - W(.+e1): interpolation variance v -> 0 under refinement (int 1/f_T = inf, so (H1) via Gaussian route fails)",
      vs[2] < vs[1] < vs[0] and vs[2] < 0.1 * vs[0], " ".join(f"{v:.3e}" for v in vs))
# covariance of T is a power law: C_T(x) = 2C_W(x)-C_W(x+e1)-C_W(x-e1); compute C_W on a big torus by FFT
Lc = 2048
k = 2 * np.pi * np.fft.fftfreq(Lc)
A1, A2 = np.meshgrid(k, k, indexing='ij')
lp = 4 - 2 * np.cos(A1) - 2 * np.cos(A2); lp[0, 0] = 1
fT = (2 - 2 * np.cos(A1)) * (0.01 + lp ** ((alpha - 2) / 2))
CT = np.real(np.fft.ifft2(fT))
rr = np.array([8, 16, 32, 64])
vals = np.abs(CT[0, rr])  # along e2 direction
sl = np.polyfit(np.log(rr), np.log(vals), 1)[0]
check("e2 that clock has power-law covariance along e2 (|C_T(r)| ~ r^-p, p finite, fitted)", -6 < sl < -1 and np.all(vals > 0),
      f"exponent {sl:.2f}")
total()
