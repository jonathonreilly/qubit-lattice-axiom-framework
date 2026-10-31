#!/usr/bin/env python3
"""Lemma AN1 of `library/analytic-lift.md` in d = 4, where L^4 is the critical norm. Consumer: that lemma, and through it the closure of the one-step theorem.

Written before running. `checks/hard-core--mapped_composite_jet.py` tested d = 2 with structured families that do not sit on the contours. The proof's source term at one level comes from the comb: a stage-one contour bond lies on a fraction of order one of the paths of the level's block. So here there is a family made for it. Base point U = 1, SU(2), L = 3, one axis-ordered contour per point, torus of 2 top cells along direction 0 and 1 across, n = 1, 2, 3.

R_n := max over direction-0 parents of | log N^(n)(b') - Q^(o,(n)) theta(b') | / S, with S := ( sum over all bonds of |theta_b|^4 )^(1/2), the square of the L^4 norm of H, in scale-invariant form. The amplitude is scaled so that S = sigma2 := 0.02.

Families, built for each n, with B := 3^n: random, i.i.d. angles; bundle, all direction-0 bonds of block 0, with colour turning from e_1 to e_2 along direction 0; subbundle, the same on a cross section of side B/3 at the centre; rotblock, constant angles on each level-1 block, with a random colour per direction and block; comb, direction-0 bonds in the tube of cross section B/3 about the axis through a block centre, with colour e_1, together with all other direction-0 bonds of the block with colour e_2.

PRE-STATED criteria.
 K0. Control at n = 1, 2, random: halving S changes R_n by at most 10 percent, and at amplitude 1e-5 the relative difference between log N and Q^o theta is at most 1e-3.
 K1. For each family: R_3 <= 1.5 max(R_1, R_2). This is the statement of no factor per level, in the critical norm of d = 4.
 K2. Reported: the largest R_n, and the family that gives it. The proof allows a constant growing with L, at most L^2, so at L = 3 a value below about 10 is expected.
 K3. Control on the norm: with S replaced by the sum of |theta_b|^2 over all bonds, the L^2 norm squared in d = 4, the bundle's ratio must fall by about 9 per level, since that norm is not critical in d = 4: its ratio at n = 3 must be below 1/3 of its value at n = 2 times the L^4 ratio's change. Reported as a check that K1 has power, and FAIL only if the L^2 ratio does not fall.
FAIL if K0, K1 or K3 fails.

Limits. L = 3, n <= 3, U = 1, one contour per point, a search over structured families. RSS guard 2 GB.
"""
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


def qmul(a, b):
    w = a[..., 0] * b[..., 0] - np.sum(a[..., 1:] * b[..., 1:], axis=-1)
    v = a[..., 0, None] * b[..., 1:] + b[..., 0, None] * a[..., 1:] + np.cross(a[..., 1:], b[..., 1:])
    return np.concatenate([w[..., None], v], axis=-1)


def qinv(a):
    out = a.copy()
    out[..., 1:] *= -1
    return out


def qexp(t):
    n = np.linalg.norm(t, axis=-1, keepdims=True)
    s = np.where(n > 1e-12, np.sin(n) / np.where(n > 1e-12, n, 1.0), 1.0 - n * n / 6)
    return np.concatenate([np.cos(n), s * t], axis=-1)


def qlog(q):
    v = q[..., 1:]
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    ang = np.arctan2(n, q[..., 0, None])
    s = np.where(n > 1e-12, ang / np.where(n > 1e-12, n, 1.0), 1.0)
    return s * v


L = 3
h = (L - 1) // 2
D = 4


def contour(r):
    steps = []
    for ax in range(D):
        for _ in range(abs(r[ax])):
            steps.append((ax, 1 if r[ax] > 0 else -1))
    return steps


def all_r():
    grids = np.meshgrid(*[np.arange(-h, h + 1)] * D, indexing="ij")
    return [tuple(int(g.flat[i]) for g in grids) for i in range(grids[0].size)]


RS = all_r()


def centres(shape):
    P = [s // L for s in shape]
    axes = [h + L * np.arange(p) for p in P]
    return np.meshgrid(*axes, indexing="ij")


def one_level(V):
    """V: quaternions on bonds, shape (D, N_0, ..., N_3, 4)."""
    shape = V.shape[1:-1]
    C = centres(shape)
    theta = qlog(V)

    def at(arr, ax, x):
        return arr[ax][tuple(x[i] % shape[i] for i in range(D))]

    Gamma, Tsum = {}, {}
    for r in RS:
        x = [c.copy() for c in C]
        q = np.zeros(C[0].shape + (4,))
        q[..., 0] = 1
        t = np.zeros(C[0].shape + (3,))
        for ax, sg in contour(r):
            if sg > 0:
                q = qmul(q, at(V, ax, x))
                t += at(theta, ax, x)
                x[ax] = x[ax] + 1
            else:
                x[ax] = x[ax] - 1
                q = qmul(q, qinv(at(V, ax, x)))
                t -= at(theta, ax, x)
        Gamma[r], Tsum[r] = q, t
    Phi = sum(Tsum.values()) / len(RS)
    g = qexp(-Phi)
    P = C[0].shape
    out = np.zeros((D,) + P + (4,))
    for mu in range(D):
        Oc = None
        tavg = np.zeros(P + (3,))
        Om = {}
        for r in RS:
            x = [C[i] + r[i] for i in range(D)]
            q = Gamma[r]
            for _ in range(L):
                q = qmul(q, at(V, mu, x))
                x[mu] = x[mu] + 1
            Om[r] = qmul(q, qinv(np.roll(Gamma[r], -1, axis=mu)))
        Oc = Om[(0,) * D]
        for r in RS:
            tavg += qlog(qmul(Om[r], qinv(Oc)))
        tavg /= len(RS)
        Vp = qmul(qexp(tavg), Oc)
        out[mu] = qmul(qmul(g, Vp), qinv(np.roll(g, -1, axis=mu)))
        del Om
    guard()
    return out


def linear_level(theta):
    shape = theta.shape[1:-1]
    C = centres(shape)
    P = C[0].shape
    out = np.zeros((D,) + P + (3,))
    for mu in range(D):
        tot = np.zeros(P + (3,))
        for r in RS:
            x = [C[i] + r[i] for i in range(D)]
            for _ in range(L):
                tot += theta[mu][tuple(x[i] % shape[i] for i in range(D))]
                x[mu] = x[mu] + 1
        out[mu] = tot / len(RS)
    return out


def composite(theta, n):
    V = qexp(theta)
    t = theta
    for _ in range(n):
        V = one_level(V)
        t = linear_level(t)
    return qlog(V), t


def ratio(theta, n, sigma2=0.02):
    S4 = float(np.sum(np.sum(theta**2, axis=-1) ** 2) ** 0.5)
    theta = theta * (sigma2 / S4) ** 0.5
    S2 = float(np.sum(theta**2))
    logN, Qt = composite(theta, n)
    z = float(np.max(np.linalg.norm(logN[0] - Qt[0], axis=-1)))
    return z / sigma2, z / S2


def family(name, n, rng):
    B = L**n
    shape = (2 * B, B, B, B)
    t = np.zeros((D,) + shape + (3,))
    e = np.eye(3)
    c0, c1 = (B - B // L) // 2, (B + B // L) // 2
    if name == "random":
        t = rng.standard_normal(t.shape)
    elif name in ("bundle", "subbundle"):
        for x0 in range(B):
            phi = (np.pi / 2) * x0 / max(B - 1, 1)
            col = np.cos(phi) * e[0] + np.sin(phi) * e[1]
            if name == "bundle":
                t[0, x0] = col
            else:
                t[0, x0, c0:c1, c0:c1, c0:c1] = col
    elif name == "rotblock":
        P = [s // L for s in shape]
        for mu in range(D):
            u = rng.standard_normal(tuple(P) + (3,))
            u /= np.linalg.norm(u, axis=-1, keepdims=True)
            t[mu] = np.kron(u, np.ones((L, L, L, L, 1)))
    elif name == "comb":
        t[0, :B] = e[1]
        t[0, :B, c0:c1, c0:c1, c0:c1] = e[0]
    return t


def main():
    ok = True
    rng = np.random.default_rng(21)
    print("K0", flush=True)
    for n in (1, 2):
        t = family("random", n, rng)
        r1, r2 = ratio(t, n, 0.02)[0], ratio(t, n, 0.005)[0]
        good = abs(r1 / r2 - 1) <= 0.1
        S4 = float(np.sum(np.sum(t**2, axis=-1) ** 2) ** 0.5)
        small = t * 1e-5 * (0.02 / S4) ** 0.5
        logN, Qt = composite(small, n)
        rel = float(np.max(np.linalg.norm(logN - Qt, axis=-1)) / np.max(np.linalg.norm(Qt, axis=-1)))
        good2 = rel <= 1e-3
        ok = ok and good and good2
        print(f" n={n}: R {r1:.4f} at 0.02, {r2:.4f} at 0.005: {good}; first derivative, relative {rel:.1e}: {good2} rss={rss_gb():.2f}GB", flush=True)
    print("K1", flush=True)
    best, who = 0.0, ""
    l2 = {}
    for name in ("random", "bundle", "subbundle", "rotblock", "comb"):
        vals = {}
        for n in (1, 2, 3):
            res = ratio(family(name, n, np.random.default_rng(5)), n)
            vals[n] = res[0]
            if name == "bundle":
                l2[n] = res[1]
            guard()
            print(f"  {name} n={n}: R={res[0]:.5f} L^2 ratio={res[1]:.3e} rss={rss_gb():.2f}GB", flush=True)
        good = vals[3] <= 1.5 * max(vals[1], vals[2])
        ok = ok and good
        if max(vals.values()) > best:
            best, who = max(vals.values()), name
        print(f" {name}: " + " ".join(f"R_{n}={vals[n]:.5f}" for n in vals) + f": {good}", flush=True)
    print(f" K2 largest R_n={best:.4f}, family {who}", flush=True)
    good3 = l2[3] < l2[2] / 3
    ok = ok and good3
    print(f" K3 bundle, L^2 ratio {l2[1]:.3e} {l2[2]:.3e} {l2[3]:.3e}: falls: {good3}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
