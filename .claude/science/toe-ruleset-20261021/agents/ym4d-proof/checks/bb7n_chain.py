"""bb7n: the nonabelian framed DD8 refinement chain R^{ax} (Construction GC, BFT_B §18.0), d = 2, SU(2) (lane B session 7).

Criteria: checks/bb7n_criteria.md (written before this script). Tests Theorem N2's depth uniformity of the coarse curvature.
Conventions: roots at block corners (fine site 3X), block of a fine site z = floor(z/3); fine 3X + r sits at coarse X + r/3.
Field arrays Z[x, y, a] = link (x, y) -> (x, y) + e_a. Quaternions (w, x, y, z); Lie algebra = R^3, exp(v) = (cos|v|, sin|v| v/|v|).
"""
import time

import numpy as np

T0 = time.time()
rng = np.random.default_rng(7474)
TK = 12
OFF = range(-4, 6)


# ---------- group backends ----------
def qmul(p, q):
    w1, x1, y1, z1 = np.moveaxis(p, -1, 0)
    w2, x2, y2, z2 = np.moveaxis(q, -1, 0)
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], axis=-1)


def qinv(q):
    return q * np.array([1.0, -1.0, -1.0, -1.0])


def qexp(v):
    th = np.linalg.norm(v, axis=-1, keepdims=True)
    sinc = np.where(th > 1e-15, np.sin(th) / np.where(th > 1e-15, th, 1.0), 1.0)
    return np.concatenate([np.cos(th), sinc * v], axis=-1)


def qlog(q):
    vn = np.linalg.norm(q[..., 1:], axis=-1, keepdims=True)
    th = np.arctan2(vn, q[..., :1])
    fac = np.where(vn > 1e-15, th / np.where(vn > 1e-15, vn, 1.0), 1.0)
    return fac * q[..., 1:]


class NA:
    mul, inv, exp, log = staticmethod(qmul), staticmethod(qinv), staticmethod(qexp), staticmethod(qlog)

    @staticmethod
    def one(shape):
        e = np.zeros(shape + (4,)); e[..., 0] = 1.0
        return e


class LIN:
    mul = staticmethod(lambda a, b: a + b)
    inv = staticmethod(lambda a: -a)
    exp = staticmethod(lambda v: v)
    log = staticmethod(lambda v: v)

    @staticmethod
    def one(shape):
        return np.zeros(shape + (3,))


# ---------- DD8 weights ----------
def lagrange_weights(p, t):
    nodes = np.arange(-p + 1, p + 1)
    w = np.ones(len(nodes))
    for a, qa in enumerate(nodes):
        for b, qb in enumerate(nodes):
            if a != b:
                w[a] *= (t - qb) / (qa - qb)
    return nodes, w


NODES = np.arange(-3, 5)
W0 = [dict(zip(*lagrange_weights(4, r / 3.0))) for r in range(3)]   # W0[r][q]
W0 = [{int(q): float(w) for q, w in d.items()} for d in W0]


def c1_weights():
    """fine link 3i+r -> 3i+r+1 of the derived scheme = sum_l C1[r][l] B(i + l)."""
    C1 = []
    for r in range(3):
        nxt = W0[r + 1] if r < 2 else {1: 1.0}
        coef = {}
        for q in set(list(nxt.keys()) + list(W0[r].keys())):
            dw = nxt.get(q, 0.0) - W0[r].get(q, 0.0)
            if q > 0:
                ls = range(0, q); sg = 1.0
            elif q < 0:
                ls = range(q, 0); sg = -1.0
            else:
                ls = []; sg = 0.0
            for l in ls:
                coef[l] = coef.get(l, 0.0) + sg * dw
        C1.append({l: c for l, c in coef.items() if abs(c) > 1e-15})
    return C1


C1 = c1_weights()


def sh(A, q0, q1):
    """value at X + (q0, q1)."""
    return np.roll(A, (-q0, -q1), axis=(0, 1))


def refine(Z, G, stats=None):
    """One step of R^{ax}: level-(j+1) field Z (T, T, 2, *) -> level-j field (3T, 3T, 2, *)."""
    T = Z.shape[0]
    one = G.one((T, T))
    Z0, Z1 = Z[:, :, 0], Z[:, :, 1]
    g = {(0, 0): one}
    for q0 in range(1, 6):
        g[(q0, 0)] = G.mul(g[(q0 - 1, 0)], sh(Z0, q0 - 1, 0))
    for q0 in range(-1, -5, -1):
        g[(q0, 0)] = G.mul(g[(q0 + 1, 0)], G.inv(sh(Z0, q0, 0)))
    for q0 in OFF:
        for q1 in range(1, 6):
            g[(q0, q1)] = G.mul(g[(q0, q1 - 1)], sh(Z1, q0, q1 - 1))
        for q1 in range(-1, -5, -1):
            g[(q0, q1)] = G.mul(g[(q0, q1 + 1)], G.inv(sh(Z1, q0, q1)))
    A0, A1 = {}, {}
    for q0 in range(-4, 5):
        for q1 in OFF:
            A0[(q0, q1)] = G.log(G.mul(G.mul(g[(q0, q1)], sh(Z0, q0, q1)), G.inv(g[(q0 + 1, q1)])))
    for q0 in OFF:
        for q1 in range(-4, 5):
            A1[(q0, q1)] = G.log(G.mul(G.mul(g[(q0, q1)], sh(Z1, q0, q1)), G.inv(g[(q0, q1 + 1)])))
    if stats is not None:
        stats.append(max(np.linalg.norm(v, axis=-1).max() for v in list(A0.values()) + list(A1.values())))

    out = np.zeros((3 * T, 3 * T, 2, Z.shape[-1]))
    for r0 in range(3):
        for r1 in range(3):
            # x-link with tail 3X + (r0, r1)
            s = sum(C1[r0][l] * W0[r1][q] * A0[(l, q)] for l in C1[r0] for q in W0[r1])
            if r0 == 2:  # face link into X' = X + e0; mu(z'), z' = 3X' + (0, r1)
                mu = 0.0
                for q1, wq in W0[r1].items():
                    if q1 > 0:
                        psi = -sum(A1[(1, m)] for m in range(0, q1))
                    elif q1 < 0:
                        psi = sum(A1[(1, m)] for m in range(q1, 0))
                    else:
                        psi = 0.0
                    mu = mu + wq * psi
                s = s + mu
                val = G.mul(G.exp(s), Z0)
            else:
                val = G.exp(s)
            out[r0::3, r1::3, 0] = val
            # y-link with tail 3X + (r0, r1)
            s = sum(W0[r0][q] * C1[r1][l] * A1[(q, l)] for l in C1[r1] for q in W0[r0])
            if r1 == 2:
                mu = 0.0
                for q0, wq in W0[r0].items():
                    if q0 > 0:
                        psi = -sum(A0[(m, 1)] for m in range(0, q0))
                    elif q0 < 0:
                        psi = sum(A0[(m, 1)] for m in range(q0, 0))
                    else:
                        psi = 0.0
                    mu = mu + wq * psi
                s = s + mu
                val = G.mul(G.exp(s), Z1)
            else:
                val = G.exp(s)
            out[r0::3, r1::3, 1] = val
    return out


def hol(Z, G):
    return G.mul(G.mul(Z[:, :, 0], sh(Z[:, :, 1], 1, 0)), G.mul(G.inv(sh(Z[:, :, 0], 0, 1)), G.inv(Z[:, :, 1])))


def curv_profile(Z, G):
    return np.linalg.norm(G.log(hol(Z, G)), axis=-1)


def chain(V, G, k, stats=None):
    levels = [V]
    for _ in range(k):
        levels.append(refine(levels[-1], G, stats))
    return levels  # levels[m] = level k - m


out = []
# L0 structure (linear)
b = rng.standard_normal((TK, TK, 2, 3))
Rb = refine(b, LIN)
qax = np.stack([Rb[0::3, 0::3, 0] + Rb[1::3, 0::3, 0] + Rb[2::3, 0::3, 0],
                Rb[0::3, 0::3, 1] + Rb[0::3, 1::3, 1] + Rb[0::3, 2::3, 1]], axis=2)
l0a = np.abs(qax - b).max() / np.abs(b).max()
nu = rng.standard_normal((TK, TK, 3))
dnu = np.stack([sh(nu, 1, 0) - nu, sh(nu, 0, 1) - nu], axis=2)
Rd = refine(dnu, LIN)
C0nu = np.repeat(np.repeat(nu, 3, axis=0), 3, axis=1)
dC0 = np.stack([sh(C0nu, 1, 0) - C0nu, sh(C0nu, 0, 1) - C0nu], axis=2)
l0b = np.abs(Rd - dC0).max() / np.abs(nu).max()
L0 = l0a <= 1e-12 and l0b <= 1e-12
out.append(f"L0 linear structure: max|Q_ax R b - b|/max|b| = {l0a:.1e}; max|R(d nu) - dC_0 nu|/max|nu| = {l0b:.1e}: "
           f"{'PASS' if L0 else 'FAIL'}")

# top field
b = rng.standard_normal((TK, TK, 2, 3))
f_raw = curv_profile(qexp(b), NA).max()
res = {}
for tag, target in (("a", 0.10), ("2a", 0.20)):
    bb = b * (target / f_raw)
    V = qexp(bb)
    fk = curv_profile(V, NA).max()
    st = []
    levs = chain(V, NA, 3, st)
    levs_lin = chain(bb, LIN, 3)
    fl = [curv_profile(levs[m], NA).max() * 9 ** m for m in range(4)]     # f at level k - m (depth-3 chain)
    fl_lin = [np.linalg.norm(hol(levs_lin[m], LIN), axis=-1).max() * 9 ** m for m in range(4)]
    res[tag] = (fk, fl, fl_lin, st)
fk, fl, fl_lin, st = res["a"]
# R_k for depths 1, 2, 3: the depth-k chain is the first k refinements (same top): ratios over its levels
Rk = [max(fl[m] for m in range(k + 1)) / fk for k in (1, 2, 3)]
Na = Rk[2] <= 1.15 * max(Rk[0], Rk[1])
out.append(f"N-a depth uniformity (f_k = {fk:.4f}): R_1, R_2, R_3 = {Rk[0]:.4f}, {Rk[1]:.4f}, {Rk[2]:.4f}: {'PASS' if Na else 'FAIL'}")
nb = max(abs(fl[m] - fl_lin[m] * fk / fl_lin[0]) for m in range(4)) / fk
Nb = nb <= 0.25
out.append(f"N-b deviation from the linear chain (k = 3): max_j |f_j - f^lin_j f_k/f^lin_k|/f_k = {nb:.4f}: {'PASS' if Nb else 'FAIL'}")

# N-c covariance (k = 2), N-d control
fkA = res["a"][0]
V = qexp(b * (0.10 / f_raw))
h = rng.standard_normal((TK, TK, 4)); h /= np.linalg.norm(h, axis=-1, keepdims=True)
Vh = np.stack([qmul(qmul(h, V[:, :, a]), qinv(sh(h, *((1, 0) if a == 0 else (0, 1))))) for a in range(2)], axis=2)
c_plain = chain(V, NA, 2)
c_gauged = chain(Vh, NA, 2)
nc = max(np.abs(curv_profile(c_plain[m], NA) - curv_profile(c_gauged[m], NA)).max() for m in range(3))
Nc = nc <= 1e-10
out.append(f"N-c exact covariance under a Haar-random level-k gauge: max plaquette |log hol| difference = {nc:.1e}: "
           f"{'PASS' if Nc else 'FAIL'}")
blog = qlog(Vh)
c_ctrl = [qexp(x) for x in chain(blog, LIN, 2)]
nd = max(np.abs(curv_profile(c_plain[m], NA) - curv_profile(c_ctrl[m], NA)).max() * 9 ** m for m in range(3)) / fkA
blog0 = qlog(V)
c_ctrl0 = [qexp(x) for x in chain(blog0, LIN, 2)]
nd0 = max(np.abs(curv_profile(c_plain[m], NA) - curv_profile(c_ctrl0[m], NA)).max() * 9 ** m for m in range(3)) / fkA
Nd = nd >= 0.1
out.append(f"N-d control (global-log linear refinement of log V^h): max coarse curvature difference / f_k = {nd:.3f} "
           f"(>= 0.1 required: {'PASS' if Nd else 'FAIL'}); same on the ungauged log V: {nd0:.4f} (informational)")
out.append("N-e informational:")
for tag in ("a", "2a"):
    fk_, fl_, fll_, st_ = res[tag]
    out.append(f"  {tag}: f_k = {fk_:.4f}; f_j/f_k (j = k..k-3) = " + ", ".join(f"{x / fk_:.4f}" for x in fl_)
               + "; linear f^lin_j/f^lin_k = " + ", ".join(f"{x / fll_[0]:.4f}" for x in fll_))
    # axial stencil own size / (rho^2 f) at each step: step m uses level k - m field (rho = 3^-m)
    rat = [st_[m] / ((3.0 ** (-m)) ** 2 * fl_[m]) for m in range(3)]
    out.append(f"     max own|A^X| / (rho_(j+1)^2 f_(j+1)) per step = " + ", ".join(f"{x:.3f}" for x in rat))
allp = L0 and Na and Nb and Nc and Nd
out.append(f"VERDICT: {'ALL PASS' if allp else 'NOT ALL PASS'} (L0, N-a..N-d)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
