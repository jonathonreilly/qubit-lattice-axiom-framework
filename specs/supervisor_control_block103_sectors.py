"""Supervisor control for block 103 (independent method): the ordered sea on the sphere menu by a t-grid with the
azimuthal kernels K_m(t,t') = e^(b t t') I_m(b rho rho')/Z (Bessel form, no Legendre expansion), the per-neighbour
spectrum by sector, the turn at 1/6, the longitudinal mass and its law near the point; then the vacancy block at g = 1
(mass-channel strength, the point where the lean's birth turns abrupt, the massless surface for the density-lean block)."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import ive
from scipy.optimize import brentq

N = 120
t, w = leggauss(N)
w = w / 2  # probability weights for dt/2
rh = np.sqrt(1 - t * t)


def L1(b):
    return 1 / np.tanh(b) - 1 / b


def kernels(b, ms=(0, 1, 2, 3)):
    Z = np.sinh(b) / b
    X = b * np.outer(rh, rh)
    out = {}
    for m in ms:
        # e^(b t t') I_m(X) = e^(b t t' + X) ive(m, X)
        out[m] = np.exp(b * np.outer(t, t) + X) * ive(m, X) / Z
    return out


def sea(b, rho=1.0, K=None, tol=1e-15):
    K = K or kernels(b)
    G = 1 + 0.4 * t
    for _ in range(200000):
        bb = 1 - rho + rho * G
        F = bb ** 6
        F /= np.sum(w * F)
        Gn = K[0] @ (w * F)
        if np.abs(Gn - G).max() < tol:
            G = Gn
            break
        G = Gn
    bb = 1 - rho + rho * G
    F = bb ** 6
    F /= np.sum(w * F)
    return G, bb, F, K


def sector_top(b, G, bb, F, K, rho, m, k=2):
    # A eta = rho K_m(F eta)/b on the t-grid; self-adjoint in weight w F bb
    d = np.sqrt(w * F * bb)
    A = rho * K[m] * (w * F)[None, :] / bb[:, None]
    S = d[:, None] * A / d[None, :]
    S = (S + S.T) / 2
    ev = np.sort(np.linalg.eigvalsh(S))[::-1]
    return ev[:k]


print("check K_m against the sphere integral at one pair of points (b=1):")
b = 1.0
K = kernels(b)
t1, t2 = 0.3, -0.5
ph = np.linspace(0, 2 * np.pi, 20001)[:-1]
for m in (0, 1, 2):
    direct = np.mean(np.exp(b * (t1 * t2 + np.sqrt(1 - t1 ** 2) * np.sqrt(1 - t2 ** 2) * np.cos(ph))) * np.cos(m * ph)) / (np.sinh(b) / b)
    X = b * np.sqrt(1 - t1 ** 2) * np.sqrt(1 - t2 ** 2)
    print(f"  m={m}: direct {direct:.15f} bessel {np.exp(b * t1 * t2 + X) * ive(m, X) / (np.sinh(b) / b):.15f}")

bc = brentq(lambda x: 6 * L1(x) - 1, 0.4, 0.6, xtol=1e-16)
print(f"massless point 6 L = 1 at beta0 = {bc:.15f}")
print("\nno vacancies: M, per-neighbour tops by sector (x6), longitudinal mass")
print(" beta     M        6mu(m=1)          6mu(m=1,2nd)  6mu(m=0)  mL^2     6mu(m=2)  6mu(m=3)")
for b in (0.515, 0.52, 0.53, 0.6, 0.8, 1.0, 2.0, 4.0):
    G, bb, F, K = sea(b)
    M = np.sum(w * F * t)
    e1 = sector_top(b, G, bb, F, K, 1.0, 1)
    e0 = sector_top(b, G, bb, F, K, 1.0, 0, 3)
    e2 = sector_top(b, G, bb, F, K, 1.0, 2)
    e3 = sector_top(b, G, bb, F, K, 1.0, 3)
    mu = e0[1]  # e0[0] = 1 is the normalisation (constant) mode
    mL2 = (1 - 6 * mu) / mu
    print(f" {b:<6} {M:.6f} {6 * e1[0]:.15f} {6 * e1[1]:.4f}        {6 * mu:.4f}    {mL2:7.3f}  {6 * e2[0]:.4f}    {6 * e3[0]:.4f}   (m0 top {e0[0]:.12f})")

print("\nnear the point: mL^2/(12 eps) and M^2 against the third-order law")
for b in (0.509, 0.51, 0.512, 0.515):
    G, bb, F, K = sea(b)
    M = np.sum(w * F * t)
    l1 = L1(b)
    l2 = 1 - 3 * l1 / b
    eps = 6 * l1 - 1
    c3 = -6 * l1 ** 3 * (38 * l2 - 3) / (6 * l2 - 1)
    M2 = eps / (-c3) / 9
    e0 = sector_top(b, G, bb, F, K, 1.0, 0, 3)
    mL2 = (1 - 6 * e0[1]) / e0[1]
    print(f" b={b}: eps={eps:.3e}  M^2/law={M ** 2 / M2:.4f}  mL^2/(12 eps)={mL2 / (12 * eps):.4f}  screened m^2 at -eps: {6 * eps / (1 - eps):.3e}")

print("\nvacancies at g = 1: the point where the lean's birth turns abrupt")
f_t = lambda x: 12 * L1(x) ** 2 + 8 * L1(x) * (1 - 3 * L1(x) / x) - 5 * L1(x) + 5 * (1 - 3 * L1(x) / x)
bt = brentq(f_t, 0.8, 1.2, xtol=1e-15)
print(f" beta_t = {bt:.12f}, rho_t = {1 / (6 * L1(bt)):.12f}")
for b in (0.95, 0.96):
    rc = 1 / (6 * L1(b))
    G, bb, F, K = sea(b, rc * 1.001)
    logz = np.log(rc * 1.001 / (1 - rc * 1.001)) - np.log(np.sum(w * bb ** 6))
    print(f" b={b}: ordered branch at rho=1.001 rho_c needs log z - log z_c = {logz - np.log(rc / (1 - rc)):+.2e}")


def block(b, rho):
    G, bb, F, K = sea(b, rho)
    n = N
    h = (G - 1) / bb
    avgF = lambda f: np.sum(w * F * f)
    Keta = rho * K[0] * (w * F)[None, :] / bb[:, None]
    row = (w * F) @ Keta
    Mx = np.zeros((n + 1, n + 1))
    Mx[1:, 1:] = Keta - np.outer(np.ones(n), row)
    Mx[1:, 0] = h - avgF(h)
    Mx[0, 0] = rho * (1 - rho) * avgF(h)
    Mx[0, 1:] = rho * (1 - rho) * row
    strength = (1 - rho) * (1 - np.sum(w * bb ** 5) / np.sum(w * bb ** 6))
    turn = sector_top(b, G, bb, F, K, rho, 1)[0]
    M = np.sum(w * F * t)
    return Mx, strength, turn, M


print("\nvacancies: mass-channel strength (1-rho)(1-<b^5>/<b^6>) against the block's own entry; turn stays 1/6")
for b, r in [(1.0, 0.9), (2.0, 0.9), (4.0, 0.95), (0.7, 0.9)]:
    Mx, s, turn, M = block(b, r)
    top = max(np.linalg.eigvals(Mx).real)
    print(f" ({b},{r}): M={M:.4f} entry={Mx[0, 0]:.6e} formula={s:.6e} 6*turn={6 * turn:.13f} 6mu0={6 * top:.4f}")

print("\nmassless surface of the density-lean block (6 mu0 = 1), and the mass source's share on that mode")
for b in (1.0, 2.0, 4.0):
    rc = 1 / (6 * L1(b))
    f = lambda r: 6 * max(np.linalg.eigvals(block(b, r)[0]).real) - 1
    rs = np.linspace(rc * 1.01, 0.995, 40)
    vals = [f(r) for r in rs]
    signs = [(rs[i], rs[i + 1]) for i in range(len(rs) - 1) if vals[i] * vals[i + 1] < 0]
    roots = [brentq(f, a, c, xtol=1e-12) for a, c in signs]
    line = []
    for r0 in roots:
        Mx, s, turn, M = block(b, r0)
        ev, R = np.linalg.eig(Mx)
        k = int(np.argmax(ev.real))
        rv = R[:, k].real
        rv /= np.linalg.norm(rv)
        evl, Lv = np.linalg.eig(Mx.T)
        lf = Lv[:, int(np.argmax(evl.real))].real
        v = Mx[:, 0]
        share = abs((lf @ v) / (lf @ rv)) / np.linalg.norm(v)
        line.append(f"rho*={r0:.5f} (M={M:.4f}, share {share:.2f})")
    print(f" b={b}: ordering from rho_c={rc:.4f}; sign of 6mu0-1 at rho_c+ {vals[0]:+.3f}, at 0.995 {vals[-1]:+.3f}; " + "; ".join(line))
