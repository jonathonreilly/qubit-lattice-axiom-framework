#!/usr/bin/env python3
"""One species, three couplings: packets of species (0,0,0) crossing a stretch gradient and a shear, frame (reach one), reach two,
reach three.  Worked computation, run 2 of 2.

As landed on main: block 69 (#8601) keeps the reach-three coupling sum sigma_a (1/2){C_a[B_a^j], P_j} and its common leading geometry
(1+B)^T(1+B) but claims NO integrated deflection; block 68 (#8599) the frame and reach-two couplings.  So the lattice factors below are
derived here from the exact uniform-strain symbols, and packets are compared with clouds of rays of the same symbols in the same fields.
Symbols (uniform strain B_a^j; s = sin k, c = cos k):  frame  h_a = s_a + sum_j B_a^j s_j;  reach two  h_a = s_a + c_a sum_j B_a^j s_j;
reach three  h_a = s_a + c_a sum_j B_a^j s_j c_j;  E = |h|.
Reduction (exact): fields depend on (x, y) only, so a packet uniform along z (k_z = 0) evolves in the k_z = 0 sector, where S_z = P_z = 0
and C_z = 1: the 96 x 64 x 64 torus reduces to the 96 x 64 slice with the same x-y operators.  Floating point for the evolutions.
"""
import sys, time
import numpy as np
import sympy as sp
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply

def out(s): print(s, flush=True)

# ------------------------------------------------------------------ exact factors
q, b, kx, ky = sp.symbols('q b k_x k_y', real=True)
def symb(kind, Bm, k):
    s = [sp.sin(k[0]), sp.sin(k[1]), 0]; c = [sp.cos(k[0]), sp.cos(k[1]), 1]
    h = []
    for a in range(3):
        if kind == "frame": h.append(s[a] + sum(Bm[a][j] * s[j] for j in range(3)))
        elif kind == "reach2": h.append(s[a] + c[a] * sum(Bm[a][j] * s[j] for j in range(3)))
        else: h.append(s[a] + c[a] * sum(Bm[a][j] * s[j] * c[j] for j in range(3)))
    return h
Bst = [[b, 0, 0], [0, 0, 0], [0, 0, 0]]
fac = {}
for kind in ("frame", "reach2", "reach3"):
    h = symb(kind, Bst, (q, 0))
    # at b = 0, h = (sin q, 0, 0) with sin q > 0 on (0, pi): dE/db = d h_x / db exactly (the other components vanish identically)
    assert all(sp.simplify(h[a]) == 0 for a in (1, 2))
    fac[kind] = sp.simplify(sp.diff(h[0], b) / sp.sin(q))
Bsh = [[0, b, 0], [b, 0, 0], [0, 0, 0]]
tilt = {}
for kind in ("frame", "reach2", "reach3"):
    h = symb(kind, Bsh, (kx, ky))
    E2 = sum(x ** 2 for x in h)
    vy = sp.diff(E2, ky).subs(ky, 0) / (2 * sp.sin(kx))          # E dE/dk_y / E, E = sin k_x at first order
    tilt[kind] = sp.simplify(sp.diff(vy, b).subs(b, 0) / 2)
okf = sp.simplify(fac["frame"] - 1) == 0 and sp.simplify(fac["reach2"] - sp.cos(q)) == 0 and sp.simplify(fac["reach3"] - sp.cos(q) ** 2) == 0
out("X exact: stretch B_x^x = b, k = (q,0,0): dE/db = sin q x {frame %s, reach two %s, reach three %s}: %s" % (fac["frame"], fac["reach2"], fac["reach3"], "PASS" if okf else "FAIL"))
out("X exact: symmetric shear B_x^y = B_y^x = b: velocity tilt dv_y/d(2b) per unit = {frame %s, reach two %s, reach three %s}" % (
    tilt["frame"], sp.simplify(tilt["reach2"]), tilt["reach3"]))
out("X hence at fixed time the stretch deflection scales 1 : cos q : cos^2 q (ray, first order); reach two and three differ by 10 per cent where cos q = 0.9, q = %.4f"
    % np.arccos(0.9))

# ------------------------------------------------------------------ lattice operators on the Lx x Ly slice (k_z = 0 sector)
Lx, Ly = 96, 64
N = Lx * Ly
idx = lambda x, y: (x % Lx) * Ly + (y % Ly)
X, Y = np.meshgrid(np.arange(Lx), np.arange(Ly), indexing='ij'); Xf, Yf = X.ravel(), Y.ravel()
def shift(dx, dy):
    rows = np.arange(N); cols = np.array([idx(x + dx, y + dy) for x, y in zip(Xf, Yf)])
    return sps.csr_matrix((np.ones(N), (rows, cols)), shape=(N, N))      # (T psi)(r) = psi(r + e)
Tx, Ty = shift(1, 0), shift(0, 1)
I = sps.identity(N, format='csr')
S = [(Tx - Tx.T) / 2j, (Ty - Ty.T) / 2j]
C = [(Tx + Tx.T) / 2, (Ty + Ty.T) / 2]
P = [S[0] @ C[0], S[1] @ C[1]]
SIG = [sps.csr_matrix(np.array([[0, 1], [1, 0]], complex)), sps.csr_matrix(np.array([[0, -1j], [1j, 0]])), sps.csr_matrix(np.array([[1, 0], [0, -1]], complex))]
def Cw(a, v):     # symmetric hop along a weighted by the bond function v (value at the bond's first site)
    D = sps.diags(v); Ta = [Tx, Ty][a]
    return (D @ Ta + Ta.T @ D) / 2
def ham(kind, Bf):
    """Bf[a][j]: site array (bond or site placement as the coupling needs), a, j in {0 (x), 1 (y)}; z components absent."""
    H = sps.kron(S[0], SIG[0]) + sps.kron(S[1], SIG[1])
    for a in range(2):
        for j in range(2):
            v = Bf[a][j]
            if v is None: continue
            if kind == "frame":
                D = sps.diags(v); term = (D @ S[j] + S[j] @ D) / 2
            elif kind == "reach2":
                term = (Cw(a, v) @ S[j] + S[j] @ Cw(a, v)) / 2
            else:
                term = (Cw(a, v) @ P[j] + P[j] @ Cw(a, v)) / 2
            H = H + sps.kron(term, SIG[a])
    return H.tocsr()
def packet(q, x0, y0, w):
    dx = (Xf - x0 + Lx / 2) % Lx - Lx / 2; dy = (Yf - y0 + Ly / 2) % Ly - Ly / 2       # periodic distances (the packet straddles y = 0)
    env = np.exp(-((dx ** 2 + dy ** 2) / (2 * w ** 2)) + 1j * q * dx)
    u = np.array([1.0, 1.0]) / np.sqrt(2)        # positive eigenvector of sigma_x sin q (q in (0, pi))
    psi = (env[:, None] * u[None, :]).ravel(); return psi / np.linalg.norm(psi)
def mean_y(psi):
    rho = (np.abs(psi.reshape(N, 2)) ** 2).sum(1)
    yc = Yf.astype(float); yc = np.where(yc > Ly / 2, yc - Ly, yc)          # centred coordinate around y = 0
    return float((rho * yc).sum() / rho.sum())

# ------------------------------------------------------------------ rays of the same symbols in the same fields
def E_sym(kind, k, B):       # numeric symbol, 2D, B[a][j]
    s = np.sin(k); c = np.cos(k); h = np.zeros(2)
    for a in range(2):
        if kind == "frame": h[a] = s[a] + sum(B[a][j] * s[j] for j in range(2))
        elif kind == "reach2": h[a] = s[a] + c[a] * sum(B[a][j] * s[j] for j in range(2))
        else: h[a] = s[a] + c[a] * sum(B[a][j] * s[j] * c[j] for j in range(2))
    return np.hypot(h[0], h[1])
def ray_cloud(kind, Bfun, q, x0, y0, w, T, n=400, seed=1):
    rng = np.random.default_rng(seed)
    xs = rng.normal(x0, w / np.sqrt(2), n); ys = rng.normal(y0, w / np.sqrt(2), n)
    kxs = rng.normal(q, 1 / (np.sqrt(2) * w), n); kys = rng.normal(0, 1 / (np.sqrt(2) * w), n)
    h = 1e-5; dt = 0.1; Y_end = []
    for x, y, kxx, kyy in zip(xs, ys, kxs, kys):
        st = np.array([x, y, kxx, kyy])
        def f(st):
            x, y, k1, k2 = st
            E = lambda kk, xx, yy: E_sym(kind, np.array(kk), Bfun(xx, yy))
            vx = (E((k1 + h, k2), x, y) - E((k1 - h, k2), x, y)) / (2 * h)
            vy = (E((k1, k2 + h), x, y) - E((k1, k2 - h), x, y)) / (2 * h)
            fx = -(E((k1, k2), x + h, y) - E((k1, k2), x - h, y)) / (2 * h)
            fy = -(E((k1, k2), x, y + h) - E((k1, k2), x, y - h)) / (2 * h)
            return np.array([vx, vy, fx, fy])
        for _ in range(int(round(T / dt))):
            k1 = f(st); k2 = f(st + dt / 2 * k1); k3 = f(st + dt / 2 * k2); k4 = f(st + dt * k3)
            st = st + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        Y_end.append(st[1])
    return float(np.mean(Y_end))

# ------------------------------------------------------------------ runs
T = 36.0; w = 9.0; x0, y0 = 20.0, 0.0
beta_s = 0.004                                    # stretch gradient d_y b at y = 0
beta_h = 0.0015                                   # shear ramp along x near x0
fs = (Ly / (2 * np.pi)) * np.sin(2 * np.pi * Yf / Ly)                    # f(y): slope 1 at y = 0, periodic
fsh = (Lx / (2 * np.pi)) * np.sin(2 * np.pi * (Xf - x0) / Lx)            # g(x): slope 1 at x = x0, periodic
stretch = lambda xx, yy: [[beta_s * (Ly / (2 * np.pi)) * np.sin(2 * np.pi * yy / Ly), 0.0], [0.0, 0.0]]
shear = lambda xx, yy: [[0.0, beta_h * (Lx / (2 * np.pi)) * np.sin(2 * np.pi * (xx - x0) / Lx)], [beta_h * (Lx / (2 * np.pi)) * np.sin(2 * np.pi * (xx - x0) / Lx), 0.0]]
H0 = ham("frame", [[None, None], [None, None]])
QS = (0.2, 0.4, 0.6, 0.8, 1.0, 1.2)
results = {}
t0 = time.time()
for field, Bsite, Bfun in (("stretch", [[beta_s * fs, None], [None, None]], stretch), ("shear", [[None, beta_h * fsh], [beta_h * fsh, None]], shear)):
    for qq in QS:
        psi0 = packet(qq, x0, y0, w)
        yref = mean_y(expm_multiply(-1j * H0 * T, psi0))
        rref = ray_cloud("frame", lambda xx, yy: [[0.0, 0.0], [0.0, 0.0]], qq, x0, y0, w, T)
        row = {}
        for kind in ("frame", "reach2", "reach3"):
            Hk = ham(kind, Bsite)
            yk = mean_y(expm_multiply(-1j * Hk * T, psi0))
            rk = ray_cloud(kind, Bfun, qq, x0, y0, w, T)
            row[kind] = (yk - yref, rk - rref)
        results[(field, qq)] = row
        out("N %-7s q=%.1f: packet deflection (ray cloud) frame %+.4f (%+.4f) | reach two %+.4f (%+.4f) | reach three %+.4f (%+.4f) | reach3/ray - 1 = %+.3f; "
            "reach2/frame %.3f (cos q %.3f), reach3/frame %.3f (cos^2 q %.3f)" % (field, qq, *row["frame"], *row["reach2"], *row["reach3"],
            row["reach3"][0] / row["reach3"][1] - 1, row["reach2"][0] / row["frame"][0], np.cos(qq), row["reach3"][0] / row["frame"][0], np.cos(qq) ** 2))
out("N elapsed %.0f s" % (time.time() - t0))
# where reach two and reach three differ by 10 per cent (stretch), packets and rays
def cross(vals):
    for (qa, ra), (qb, rb) in zip(vals[:-1], vals[1:]):
        if (ra - 0.9) * (rb - 0.9) <= 0: return qa + (0.9 - ra) * (qb - qa) / (rb - ra)
    return None
pk = [(qq, results[("stretch", qq)]["reach3"][0] / results[("stretch", qq)]["reach2"][0]) for qq in QS]
ry = [(qq, results[("stretch", qq)]["reach3"][1] / results[("stretch", qq)]["reach2"][1]) for qq in QS]
out("N stretch, reach3/reach2 by q: packets %s ; ray clouds %s -> 10 per cent at q = %s (packets), %s (rays), %.3f (first-order cos q = 0.9)" % (
    " ".join("%.1f:%.3f" % t for t in pk), " ".join("%.1f:%.3f" % t for t in ry), ("%.3f" % cross(pk)) if cross(pk) else "-", ("%.3f" % cross(ry)) if cross(ry) else "-", np.arccos(0.9)))
dev = {qq: results[("stretch", qq)]["reach3"][0] / results[("stretch", qq)]["reach3"][1] - 1 for qq in QS}
dev_first = {qq: results[("stretch", qq)]["reach3"][0] / (results[("stretch", qq)]["frame"][1] * np.cos(qq) ** 2) - 1 for qq in QS}
print()
print("SUMMARY: stretch gradient, species (0,0,0): packet deflections follow their own ray clouds (reach three: %s at q = 0.2..1.2); the reach-three/"
      "reach-two ratio falls below 0.9 near q = %s (first-order cos q = 0.9 at 0.451); against the frame ray times cos^2 q the reach-three packets deviate by %s"
      % (", ".join("%+.3f" % dev[qq] for qq in QS), ("%.2f" % cross(pk)) if cross(pk) else "-", ", ".join("%+.3f" % dev_first[qq] for qq in QS)))
bad = [qq for qq in QS if qq <= 0.6 + 1e-9 and abs(dev[qq]) > 0.05]
if bad:
    print("HIT: the reach-three packet deflection deviates from its ray prediction by more than 5 per cent at q = %s (%s)" % (
        ", ".join("%.1f" % qq for qq in bad), ", ".join("%+.3f" % dev[qq] for qq in bad)))
