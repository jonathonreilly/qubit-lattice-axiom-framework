"""C1: vacuum rate of a T-tick windowed formation weight in the 1D Dirac-step sea (supplied toy).

Step (A5 T2): U(k) = C(m) diag(e^{-ik}, e^{ik}), C(m) = [[cos m, -i sin m], [-i sin m, cos m]].
Quasi-energy theta: eigenvalue e^{-i theta}. Sea = every state with theta in (-pi, 0) filled.
Detector: listens at one site x (R component) for T ticks with taps f(t) = w(t) e^{-i Omega t}:
    w_hat = sum_t f(t) U^{-t} e_x^R ,  F = occupation of the normalised mode w_hat (a projector).
Its component on an eigenvector u_b(k) is W(theta - Omega) <u_b|e_x^R>, W(nu) = sum_t w(t) e^{i nu t}.
Vacuum rate eps = sum_k w_-(k)|W(theta_-(k)-Omega)|^2 / sum_{k,b} w_b(k)|W(theta_b(k)-Omega)|^2.
Windows: rect, Hann, C-infinity bump, DPSS (Slepian; optimal for m=0), Dolph-Chebyshev (closed form).
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.signal.windows import dpss

PI = np.pi
Omega = PI / 2                      # carrier: middle of the upper band


def windows(T):
    t = np.arange(T)
    v = 2 * (t + 1) / (T + 1) - 1
    out = {"rect": np.ones(T), "hann": np.sin(PI * (t + 1) / (T + 1)) ** 2,
           "bump": np.exp(-1.0 / (1.0 - v ** 2))}
    if T <= 48:
        out["dpss"] = dpss(T, T / 4.0)          # half-band concentration (W = 1/4)
    return out


def W_of(w, nu):
    """Direct DTFT W(nu) = sum_t w_t e^{i nu t}, chunked to bound memory."""
    out = np.empty(nu.shape, complex)
    t = np.arange(len(w))
    for a in range(0, len(nu), 2048):
        out[a:a + 2048] = np.exp(1j * np.outer(nu[a:a + 2048], t)) @ w
    return out


def lnT_cheb(n, y):
    """ln|T_n(y)| elementwise (robust for large n)."""
    y = np.asarray(y, float)
    out = np.empty_like(y)
    big = np.abs(y) > 1
    a = np.arccosh(np.abs(y[big]))
    out[big] = n * a + np.log1p(np.exp(-2 * n * a)) - np.log(2)
    c = np.cos(n * np.arccos(np.clip(y[~big], -1, 1)))
    out[~big] = np.log(np.abs(c) + 1e-300)
    return out


# ---------- spectral data of the seed e_x^R ----------
def band_data(m, Nk=2 ** 14):
    """k-grid, theta_b(k), weights w_b(k) for b = upper (0), lower (1)."""
    k = 2 * PI * (np.arange(Nk) + 0.5) / Nk - PI
    cm, sm = np.cos(m), np.sin(m)
    U = np.empty((Nk, 2, 2), complex)
    U[:, 0, 0] = cm * np.exp(-1j * k); U[:, 0, 1] = -1j * sm * np.exp(1j * k)
    U[:, 1, 0] = -1j * sm * np.exp(-1j * k); U[:, 1, 1] = cm * np.exp(1j * k)
    lam, vec = np.linalg.eig(U)
    th = -np.angle(lam)
    vec = vec / np.linalg.norm(vec, axis=1, keepdims=True)
    wR = np.abs(vec[:, 0, :]) ** 2            # weight of e^R on each eigenvector
    up = th > 0
    th_up = np.where(up[:, 0], th[:, 0], th[:, 1]); th_lo = np.where(up[:, 0], th[:, 1], th[:, 0])
    w_up = np.where(up[:, 0], wR[:, 0], wR[:, 1]); w_lo = np.where(up[:, 0], wR[:, 1], wR[:, 0])
    return th_up, th_lo, w_up, w_lo


def eps_window(w, m, bd):
    if m == 0:      # flat measure: theta uniform on the circle, half filled
        M = 2 ** 15
        th = -PI + 2 * PI * (np.arange(M) + 0.5) / M
        Wv = np.abs(W_of(w, th - Omega)) ** 2
        return Wv[th < 0].sum() / Wv.sum()
    th_up, th_lo, w_up, w_lo = bd
    lo = w_lo * np.abs(W_of(w, th_lo - Omega)) ** 2
    up = w_up * np.abs(W_of(w, th_up - Omega)) ** 2
    return lo.sum() / (lo.sum() + up.sum())


def ln_eps_dc(T, m, bd):
    """Dolph-Chebyshev window whose sidelobe arc is exactly the occupied arc [-pi+m, -m]."""
    n = T - 1
    th_e = PI / 2 + m                     # main-lobe half-width (centre Omega = pi/2)
    x0 = 1 / np.cos(th_e / 2)
    kap = np.arccosh(x0)
    scale = n * kap                        # ln of peak (up to log 2 terms), subtracted everywhere
    if m == 0:
        M = 4 * T + 4000
        th = -PI + 2 * PI * (np.arange(M) + 0.5) / M
        lw = 2 * (lnT_cheb(n, x0 * np.cos((th - Omega) / 2)) - scale)
        lo, al = th < 0, np.ones(M, bool)
        num = np.logaddexp.reduce(lw[lo]); den = np.logaddexp.reduce(lw[al])
        return num - den, kap
    th_up, th_lo, w_up, w_lo = bd
    l_lo = np.log(w_lo) + 2 * (lnT_cheb(n, x0 * np.cos((th_lo - Omega) / 2)) - scale)
    l_up = np.log(w_up) + 2 * (lnT_cheb(n, x0 * np.cos((th_up - Omega) / 2)) - scale)
    num = np.logaddexp.reduce(l_lo); den = np.logaddexp(num, np.logaddexp.reduce(l_up))
    return num - den, kap


for m in (0.0, 0.3):
    bd = None if m == 0 else band_data(m)
    if bd is not None:
        tot = bd[2] + bd[3]
        print(f"m={m}: weight check max|w_up+w_lo-1| = {np.abs(tot-1).max():.1e}; "
              f"upper band theta in [{bd[0].min():.4f}, {bd[0].max():.4f}] (expect [m, pi-m])")
    print(f"--- m = {m}: vacuum rate eps(T) of the windowed weight (carrier pi/2) ---")
    print(f"{'T':>5} {'rect':>10} {'hann':>10} {'bump':>10} {'dpss':>10} {'cheb':>12}")
    rows = []
    for T in (8, 16, 24, 32, 48, 64, 128, 256, 512, 1024):
        ws = windows(T)
        e = {name: eps_window(w, m, bd) for name, w in ws.items()}
        lde, kap = ln_eps_dc(T, m, bd)
        rows.append((T, e, lde))
        print(f"{T:5d} {e['rect']:10.3e} {e['hann']:10.3e} {e['bump']:10.3e} "
              f"{e.get('dpss', float('nan')):10.3e} {np.exp(lde) if lde > -700 else 0.0:12.3e}"
              f"  (ln cheb = {lde:9.2f})")
    # slopes
    Ts = np.array([r[0] for r in rows], float)
    for name in ("rect", "hann"):
        y = np.log([r[1][name] for r in rows])
        s = np.polyfit(np.log(Ts[-4:]), y[-4:], 1)[0]
        print(f"  {name}: d ln eps / d ln T (T=128..1024) = {s:+.3f}")
    yb = np.log([r[1]['bump'] for r in rows])
    sb = np.polyfit(np.sqrt(Ts[-5:]), yb[-5:], 1)[0]
    print(f"  bump: d ln eps / d sqrt(T) (T=64..1024) = {sb:+.3f}; local d ln eps/d ln T at 1024 = "
          f"{(yb[-1]-yb[-2])/np.log(2):+.2f} (keeps steepening => faster than any power)")
    yc = np.array([r[2] for r in rows])
    sc = np.polyfit(Ts[-4:], yc[-4:], 1)[0]
    print(f"  cheb: d ln eps / dT (T=128..1024) = {sc:+.4f}; predicted -2*kappa = {-2*kap:+.4f} "
          f"(kappa = arccosh(1/cos(pi/4+m/2)))")
    if m == 0:
        yd = np.log([r[1]['dpss'] for r in rows if 'dpss' in r[1] and r[0] <= 32])
        Td = np.array([r[0] for r in rows if 'dpss' in r[1] and r[0] <= 32], float)
        sd = np.polyfit(Td, yd, 1)[0]
        print(f"  dpss (true optimum for m=0; T=48 is at the 1e-30 double-precision floor): d ln eps/dT (T=8..32) = {sd:+.4f}; "
              f"Slepian ln((1+sin(pi/4))/(1-sin(pi/4))) = {-np.log((1+np.sin(PI/4))/(1-np.sin(PI/4))):+.4f}")
