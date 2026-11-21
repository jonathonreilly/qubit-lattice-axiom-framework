#!/usr/bin/env python3
"""W3: the fibre split in the limit n -> infinity of the map (B-1).

Level-j lattice spacing 1, coarse spacing L. In Fourier, with k = theta + l, l in (2 pi / L) Z^4,
  M_mu(theta) = sum_l L^2 |a_mu(L k)|^2 / |k|^2,
  S^p_mu(theta) = sum_l conj(j^p_mu(k)) L a_mu(L k) / |k|^2,
  delta_pq = int_BZ dtheta / (2 pi)^4 conj[ S^q . J*_p ],
  J*_p = M^-1 [ conj(S^p) - conj(w) (w . M^-1 conj(S^p)) / (w . M^-1 conj(w)) ],
with w_mu = 1 - exp(-i L theta_mu), the conservation of a coarse closed current.
1/|k|^2 is written by Schwinger parameter, so each sum factorizes over axes.
"""
import json, os, resource, sys
import numpy as np

LIM = 2 * 1024**3


def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    if rss > LIM:
        sys.exit("rss limit")


def s(u):
    u = np.asarray(u, float)
    out = np.ones_like(u)
    m = np.abs(u) > 1e-12
    out[m] = 2 * np.sin(u[m] / 2) / u[m]
    return out


def tnodes():
    x, w = np.polynomial.legendre.leggauss(12)
    ts, wt = [], []
    for dk in range(-6, 8):
        a, b = 10.0**dk, 10.0 ** (dk + 1)
        ts.append(0.5 * (b - a) * x + 0.5 * (b + a))
        wt.append(0.5 * (b - a) * w)
    return np.concatenate(ts), np.concatenate(wt)


class Tables:
    def __init__(self, L, Mgrid, xs, N):
        self.L, self.Mgrid = L, Mgrid
        self.ts, self.wt = tnodes()
        h = 2 * np.pi / L / Mgrid
        self.theta = -np.pi / L + h * (np.arange(Mgrid) + 0.5)
        self.h = h
        m = np.arange(-N, N + 1)
        self.xs = list(xs)
        nt = len(self.ts)
        self.m0 = np.zeros((Mgrid, nt))
        self.m1 = np.zeros((Mgrid, nt))
        self.E0 = {x: np.zeros((Mgrid, nt), complex) for x in xs}
        self.E1 = {x: np.zeros((Mgrid, nt), complex) for x in xs}
        for it, th in enumerate(self.theta):
            k = th + 2 * np.pi * m / L
            sL = s(L * k)
            sj = s(k)
            base0 = sj * sL
            base1 = (sj * sL) ** 2 * np.exp(1j * k / 2 - 1j * L * k / 2)
            e = np.exp(-np.outer(self.ts, k**2))
            self.m0[it] = (e * sL**2).sum(1)
            self.m1[it] = (e * sL**4).sum(1)
            for x in xs:
                ph = np.exp(1j * k * x)
                self.E0[x][it] = (e * (base0 * ph)).sum(1)
                self.E1[x][it] = (e * (base1 * ph)).sum(1)
        guard()


def outer4(a, b, c, d):
    return np.einsum("i,j,k,l->ijkl", a, b, c, d, optimize=True)


def mats(T):
    """M_mu on the theta grid."""
    nt = len(T.ts)
    G = T.Mgrid
    M = np.zeros((4, G, G, G, G))
    for i in range(nt):
        m0 = T.m0[:, i]
        m1 = T.m1[:, i]
        w = T.wt[i]
        M[0] += w * outer4(m1, m0, m0, m0)
        M[1] += w * outer4(m0, m1, m0, m0)
        M[2] += w * outer4(m0, m0, m1, m0)
        M[3] += w * outer4(m0, m0, m0, m1)
    return M * T.L**2


def cross(T, x, a, b):
    """S^p_mu for the plaquette in plane (a,b) with lower corner x."""
    nt = len(T.ts)
    G = T.Mgrid
    S = np.zeros((4, G, G, G, G), complex)
    others = [n for n in range(4) if n not in (a, b)]
    for i in range(nt):
        w = T.wt[i]
        fac = {n: T.E0[x[n]][:, i] for n in range(4)}
        # mu = a
        v = dict(fac)
        v[a] = T.E1[x[a]][:, i]
        v[b] = T.E0[x[b]][:, i] - T.E0[x[b] + 1][:, i]
        S[a] += w * outer4(v[0], v[1], v[2], v[3])
        # mu = b
        v = dict(fac)
        v[a] = T.E0[x[a] + 1][:, i] - T.E0[x[a]][:, i]
        v[b] = T.E1[x[b]][:, i]
        S[b] += w * outer4(v[0], v[1], v[2], v[3])
    return S * T.L


def delta(T, Mmu, Sp, Sq):
    G = T.Mgrid
    th = T.theta
    w = np.zeros((4, G, G, G, G), complex)
    for mu in range(4):
        sh = [1, 1, 1, 1]
        sh[mu] = G
        w[mu] = (1 - np.exp(-1j * T.L * th)).reshape(sh)
    Mi = 1.0 / Mmu
    a = (w * Mi * np.conj(Sp)).sum(0)
    b = (w * Mi * np.conj(w)).sum(0)
    Jp = Mi * (np.conj(Sp) - np.conj(w) * (a / b))
    I = np.conj((Sq * Jp).sum(0))
    vol = T.h**4 / (2 * np.pi) ** 4
    return float((I.sum() * vol).real), float(abs((I.sum() * vol).imag))


def run(L, Mgrid):
    # plaquettes in plane (0,1). Pair centred in the block: p at (-2,-2,-1,-1).
    conf = {
        "p": (-2, -2, -1, -1),
        "qn": (1, 1, 1, 1),      # offset (3,3,2,2)
        "qf": (1, 1, 1, 3),      # offset (3,3,2,4)
        "p0": (0, 0, 0, 0),      # block centre
        "q0": (3, 3, 2, 2),
    }
    xs = sorted({c for v in conf.values() for c in v} | {c + 1 for v in conf.values() for c in v})
    N = max(30, 8 * L)
    T = Tables(L, Mgrid, xs, N)
    Mmu = mats(T)
    guard()
    S = {k: cross(T, v, 0, 1) for k, v in conf.items()}
    guard()
    out = {"L": L, "Mgrid": Mgrid}
    for (a, b) in [("p", "p"), ("qn", "qn"), ("p", "qn"), ("p", "qf"), ("qf", "qf"), ("p0", "p0"), ("p0", "q0"), ("q0", "q0")]:
        d, im = delta(T, Mmu, S[a], S[b])
        out[f"d_{a}_{b}"] = d
        out[f"im_{a}_{b}"] = im
    # normalization: coarse plaquette variance from M, must equal P_infinity(p,p)
    th = T.theta
    Gg = T.Mgrid
    J0 = (1 - np.exp(-1j * L * th)).reshape(1, Gg, 1, 1)  # J_0 = 1 - e^{-i p_1}
    J1 = (np.exp(-1j * L * th) - 1).reshape(Gg, 1, 1, 1)  # J_1 = e^{-i p_0} - 1
    var = (np.abs(J0) ** 2 * Mmu[0] + np.abs(J1) ** 2 * Mmu[1]).sum() * T.h**4 / (2 * np.pi) ** 4
    out["coarse_plaquette_var"] = float(var)
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    res = []
    plan = [(1, 8), (1, 12), (3, 8), (3, 12), (5, 8), (5, 12), (7, 8), (7, 12), (9, 8), (9, 12), (15, 8), (15, 12), (21, 8), (21, 12)]
    for L, G in plan:
        r = run(L, G)
        res.append(r)
        print({k: (round(v, 10) if isinstance(v, float) and not k.startswith("im") else v) for k, v in r.items() if not k.startswith("im")}, flush=True)
        with open(os.path.join(here, "fibre_split.json"), "w") as f:
            json.dump(res, f, indent=1)


if __name__ == "__main__":
    main()
