#!/usr/bin/env python3
"""No factor per level in the nonlinear remainder of the composite block map. Consumer: Lemma AN1 of `library/analytic-lift.md`.

Written before running. The contour-free chain N^(n) = N_(n-1) o ... o N_0 has derivative Q^(o,(n)) at the base point. A generic iterate of quadratic maps would have a remainder growing by a factor per level. Lemma AN1 says that it does not: with theta the fine bond angles and, in d dimensions, ||theta||_crit(b')^2 := the critical norm squared on the two level-n blocks of b',

 | log N^(n)(e^theta)(b') - Q^(o,(n)) theta(b') | <= C(L) ||theta||_crit(b')^2,

uniformly in n, since averaging over a block gains 1/L per level in the critical norm. In d = 2 the critical norm is the L^2 norm of H, which is the sum over bonds of |theta_b|^2. So d = 2 tests the same mechanism in its own scaling. Base point U = 1, SU(2), L = 3, torus of 3 top cells per direction, n = 1, 2, 3, 4.

R_n := max over b' of | log N^(n)(b') - Q^(o,(n)) theta (b') | / S(b'), with S(b') the sum of |theta_b|^2 over the two level-n blocks of b', over b' with S(b') at least 1e-6 of its maximum, and with the amplitude scaled so that max S = sigma^2 := 0.02.

Families, each built for its n: random (i.i.d. Gaussian su(2) angles); line (one row of fine bonds on the centre line of one parent bond, with direction e_1 on the first half and e_2 on the second); bundle (all direction-0 bonds in one level-n block, with direction rotating from e_1 to e_2 along the bond's axis across the block); rotblock (constant angles on each level-1 block, in a direction fixed at random per block); nested (one row, with direction given by a hierarchical pattern: e_1, e_2, e_3 cycled by level of the first non-zero digit of the position in base L).

PRE-STATED criteria.
 J0. Control: for random theta at n = 1 and n = 2, halving the amplitude changes R_n by at most 10 percent (remainder quadratic), and the same chain at amplitude 1e-5 of the size has | log N - Q^o theta | / |Q^o theta| <= 1e-3 (first derivative is Q^o).
 J1. For each family: R_4 <= 1.5 max(R_1, R_2, R_3). This is the statement of no factor per level.
 J2. Reported: the largest R_n over all families and n. Expected of order one.
FAIL if J0 or J1 fails.

Limits. d = 2, U = 1, one contour per point (axis ordered), structured families and random draws: a search, not a supremum. Nothing on d = 4 except through the same recursion. RSS guard 2 GB.
"""
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


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


def contour(r):
    """Axis-ordered steps from y to y + r: list of (axis, sign)."""
    steps = []
    for ax in (0, 1):
        for _ in range(abs(r[ax])):
            steps.append((ax, 1 if r[ax] > 0 else -1))
    return steps


def one_level(V):
    """V: quaternions on bonds, shape (2, N, N, 4). Returns the level map N_j at base point 1, and the linear map on its log."""
    N = V.shape[1]
    nc = N // L
    I, J = np.meshgrid(h + L * np.arange(nc), h + L * np.arange(nc), indexing="ij")
    theta = qlog(V)

    def bond(ax, x0, x1):
        return V[ax, x0 % N, x1 % N]

    def th(ax, x0, x1):
        return theta[ax, x0 % N, x1 % N]

    rs = [(r0, r1) for r0 in range(-h, h + 1) for r1 in range(-h, h + 1)]
    Gamma, ThetaG = {}, {}
    for r in rs:
        x0, x1 = I.copy(), J.copy()
        q = np.zeros(I.shape + (4,))
        q[..., 0] = 1
        tsum = np.zeros(I.shape + (3,))
        for ax, sg in contour(r):
            if sg > 0:
                q = qmul(q, bond(ax, x0, x1))
                tsum += th(ax, x0, x1)
                if ax == 0:
                    x0 = x0 + 1
                else:
                    x1 = x1 + 1
            else:
                if ax == 0:
                    x0 = x0 - 1
                else:
                    x1 = x1 - 1
                q = qmul(q, qinv(bond(ax, x0, x1)))
                tsum -= th(ax, x0, x1)
        Gamma[r], ThetaG[r] = q, tsum
    Phi = sum(ThetaG[r] for r in rs) / len(rs)
    g = qexp(-Phi)
    out = np.zeros((2, nc, nc, 4))
    for mu in (0, 1):
        Om = {}
        for r in rs:
            x0, x1 = I + r[0], J + r[1]
            q = Gamma[r]
            for _ in range(L):
                q = qmul(q, bond(mu, x0, x1))
                if mu == 0:
                    x0 = x0 + 1
                else:
                    x1 = x1 + 1
            # Back from x + L e_mu to the centre of the next block, along the contour of that block.
            Gn = np.roll(Gamma[r], -1, axis=mu)
            Om[r] = qmul(q, qinv(Gn))
        Oc = Om[(0, 0)]
        tavg = sum(qlog(qmul(Om[r], qinv(Oc))) for r in rs) / len(rs)
        Vp = qmul(qexp(tavg), Oc)
        gn = np.roll(g, -1, axis=mu)
        out[mu] = qmul(qmul(g, Vp), qinv(gn))
    return out


def linear_level(theta):
    N = theta.shape[1]
    nc = N // L
    I, J = np.meshgrid(h + L * np.arange(nc), h + L * np.arange(nc), indexing="ij")
    out = np.zeros((2, nc, nc, 3))
    for mu in (0, 1):
        tot = np.zeros(I.shape + (3,))
        for r0 in range(-h, h + 1):
            for r1 in range(-h, h + 1):
                x0, x1 = I + r0, J + r1
                for _ in range(L):
                    tot += theta[mu, x0 % N, x1 % N]
                    if mu == 0:
                        x0 = x0 + 1
                    else:
                        x1 = x1 + 1
        out[mu] = tot / (L * L)
    return out


def composite(theta, n):
    V = qexp(theta)
    t = theta
    for _ in range(n):
        V = one_level(V)
        t = linear_level(t)
    return qlog(V), t


def S_of(theta, n):
    """Sum of |theta|^2 over each level-n block, and the two-block sum for each parent bond."""
    N = theta.shape[1]
    B = L**n
    a = np.sum(theta**2, axis=(0, 3))
    nc = N // B
    Sb = np.zeros((nc, nc))
    for i in range(nc):
        for j in range(nc):
            Sb[i, j] = np.sum(a[i * B : (i + 1) * B, j * B : (j + 1) * B])
    return np.stack([Sb + np.roll(Sb, -1, axis=0), Sb + np.roll(Sb, -1, axis=1)])


def ratio(theta, n, sigma2=0.02):
    S = S_of(theta, n)
    theta = theta * np.sqrt(sigma2 / np.max(S))
    S = S * sigma2 / np.max(S)
    logN, Qt = composite(theta, n)
    z = np.linalg.norm(logN - Qt, axis=-1)
    mask = S >= 1e-6 * np.max(S)
    return float(np.max(z[mask] / S[mask]))


def family(name, n, rng, nc=3):
    B = L**n
    N = nc * B
    t = np.zeros((2, N, N, 3))
    e = np.eye(3)
    if name == "random":
        t = rng.standard_normal(t.shape)
    elif name == "line":
        row = (B - 1) // 2
        for x in range(B):
            t[0, (row + x) % N, row] = e[0] if x < B // 2 else e[1]
    elif name == "bundle":
        for x0 in range(B):
            phi = (np.pi / 2) * x0 / max(B - 1, 1)
            t[0, x0, :B] = np.cos(phi) * e[0] + np.sin(phi) * e[1]
    elif name == "rotblock":
        for i in range(N // L):
            for j in range(N // L):
                u = rng.standard_normal((2, 3))
                u /= np.linalg.norm(u, axis=-1, keepdims=True)
                t[0, i * L : (i + 1) * L, j * L : (j + 1) * L] = u[0]
                t[1, i * L : (i + 1) * L, j * L : (j + 1) * L] = u[1]
    elif name == "nested":
        row = (B - 1) // 2
        for x in range(B):
            k = 0
            y = x
            while y > 0 and y % L == 0:
                y //= L
                k += 1
            t[0, (row + x) % N, row] = e[k % 3]
    return t


def main():
    ok = True
    rng = np.random.default_rng(11)
    print("J0", flush=True)
    for n in (1, 2):
        t = family("random", n, rng)
        r1, r2 = ratio(t, n, 0.02), ratio(t, n, 0.005)
        good = abs(r1 / r2 - 1) <= 0.1
        ok = ok and good
        S = S_of(t, n)
        small = t * 1e-5 * np.sqrt(0.02 / np.max(S))
        logN, Qt = composite(small, n)
        rel = float(np.max(np.linalg.norm(logN - Qt, axis=-1)) / np.max(np.linalg.norm(Qt, axis=-1)))
        good2 = rel <= 1e-3
        ok = ok and good2
        print(f" n={n}: R at sigma^2=0.02 {r1:.4f}, at 0.005 {r2:.4f}: {good}; first derivative, relative {rel:.1e}: {good2}", flush=True)
    print("J1", flush=True)
    best = 0.0
    for name in ("random", "line", "bundle", "rotblock", "nested"):
        vals = {}
        for n in (1, 2, 3, 4):
            vs = []
            for k in range(3 if name in ("random", "rotblock") else 1):
                vs.append(ratio(family(name, n, np.random.default_rng(100 + k)), n))
            vals[n] = max(vs)
            if rss_gb() > 2:
                raise SystemExit("RSS above 2 GB")
        good = vals[4] <= 1.5 * max(vals[1], vals[2], vals[3])
        ok = ok and good
        best = max(best, max(vals.values()))
        print(f" {name}: " + " ".join(f"R_{n}={vals[n]:.4f}" for n in vals) + f": {good} rss={rss_gb():.2f}GB", flush=True)
    print(f" J2 largest R_n={best:.4f}")
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
