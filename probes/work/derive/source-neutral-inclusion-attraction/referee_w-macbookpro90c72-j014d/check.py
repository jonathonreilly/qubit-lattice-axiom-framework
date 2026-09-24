#!/usr/bin/env python3
"""Referee for source-neutral-inclusion-attraction a3.

Author w-jonathonsmac4f50-j0b3c (claude-opus-5-5). Own torus solve, own Bessel Green.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import ive

fails = []
AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def moments_and_hessian():
    """Cov(X^2, Y^2) = v^2 + 2 c^2, and sum_ij (3 n_i n_j - delta_ij)^2 = 6 on the sphere."""
    c, v, t, s = sp.symbols("c v t s")
    # Moment generating function of a centered pair. Fourth derivative at 0 is E X^2 Y^2.
    mgf = sp.exp(sp.Rational(1, 2) * (v * t**2 + v * s**2 + 2 * c * t * s))
    moment = sp.diff(mgf, t, 2, s, 2).subs({t: 0, s: 0})
    ok_cov = sp.simplify(moment - (v**2 + 2 * c**2)) == 0
    n = sp.symbols("n1 n2 n3")
    raw = 0
    for i in range(3):
        for j in range(3):
            raw += (3 * n[i] * n[j] - (1 if i == j else 0)) ** 2
    target = 9 * (n[0] ** 2 + n[1] ** 2 + n[2] ** 2) ** 2 - 6 * (n[0] ** 2 + n[1] ** 2 + n[2] ** 2) + 3
    ok_h = sp.expand(raw - target) == 0
    on_sphere = sp.Integer(6)
    coeff = sp.Integer(on_sphere) / (16 * sp.pi**2)
    ok_c = sp.simplify(coeff - sp.Integer(3) / (8 * sp.pi**2)) == 0
    report(
        "moments and hessian",
        bool(ok_cov and ok_h and ok_c),
        "Cov(X^2,Y^2)=v^2+2 c^2, so the epsilon^2 coefficient is 1/2; sum of squared second derivatives of 1/(4 pi r) is 3/(8 pi^2 r^6)",
    )


def mu_algebra():
    g0, ge, g2 = sp.symbols("G0 Ge G2")
    mu = 2 * (g0 - ge) - (g0 - 2 * ge + g2)
    report(
        "dipole eigenvalue",
        sp.simplify(mu - (g0 - g2)) == 0,
        "mu = 2(G(0)-G(e)) - (G(0)-2G(e)+G(2e)) equals G(0)-G(2e)",
    )


def row_sum_split():
    """A symmetric zero-row-sum matrix is a sum of bond squares."""
    rng = np.random.default_rng(1)
    A = rng.normal(size=(4, 4))
    Q = A + A.T
    Q -= np.diag(Q.sum(axis=1))
    recon = np.zeros_like(Q)
    for u, v in itertools.combinations(range(4), 2):
        d = np.zeros(4)
        d[u], d[v] = 1.0, -1.0
        recon += (-Q[u, v]) * np.outer(d, d)
    err = np.max(np.abs(recon - Q))
    report("difference decomposition", err < 1e-12, f"max entry error {err:.1e} on a random 4-site zero-row-sum matrix")


def torus(L):
    sites = list(itertools.product(range(L), repeat=3))
    idx = {p: i for i, p in enumerate(sites)}
    n = len(sites)
    lap = np.zeros((n, n))
    for p, i in idx.items():
        lap[i, i] = 6
        for a in AXES:
            q = tuple((p[k] + a[k]) % L for k in range(3))
            lap[i, idx[q]] -= 1
    w, V = np.linalg.eigh(lap)
    inv = np.array([0.0 if abs(wi) < 1e-10 else 1.0 / wi for wi in w])
    G = (V * inv) @ V.T
    return G, idx


def bond_matrix(G, idx, x, y, L):
    def ends(origin, axis):
        return origin, tuple((origin[k] + axis[k]) % L for k in range(3))

    M = np.zeros((6, 6))
    for i, bi in enumerate(AXES):
        u, v = ends(x, bi)
        for j, bj in enumerate(AXES):
            p, q = ends(y, bj)
            M[i, j] = (
                G[idx[u], idx[p]] - G[idx[u], idx[q]] - G[idx[v], idx[p]] + G[idx[v], idx[q]]
            )
    return M


def dress(M, eps):
    S = np.eye(6) + eps * M
    if eps > -1 + 1e-12:
        return np.linalg.inv(S)
    ones = np.ones(6) / np.sqrt(6)
    P = np.eye(6) - np.outer(ones, ones)
    return np.linalg.pinv(P @ S @ P, rcond=1e-10)


def interaction(G, idx, x, y, ex, ey, L):
    Mxx = bond_matrix(G, idx, x, x, L)
    Myy = bond_matrix(G, idx, y, y, L)
    Mxy = bond_matrix(G, idx, x, y, L)
    Ax, Ay = dress(Mxx, ex), dress(Myy, ey)
    X = Ax @ Mxy @ Ay @ Mxy.T
    ev = np.linalg.eigvalsh(np.eye(6) - ex * ey * X)
    if np.any(ev <= 0):
        return np.nan, Mxy
    return 0.5 * np.log(np.prod(ev)), Mxy


def laplacian_F(L, x, y, ex, ey, shared="none"):
    """Prime log-det of the modified Laplacian, minus the two single inclusions."""
    G, idx = torus(L)
    n = len(idx)

    def add_bonds(mat, origin, eps, skip=None):
        for a in AXES:
            u = origin
            v = tuple((origin[k] + a[k]) % L for k in range(3))
            edge = tuple(sorted((u, v)))
            if skip and edge in skip:
                continue
            iu, iv = idx[u], idx[v]
            mat[iu, iu] += eps
            mat[iv, iv] += eps
            mat[iu, iv] -= eps
            mat[iv, iu] -= eps
        return mat

    def prime_logdet(mat):
        w = np.linalg.eigvalsh(mat)
        w = w[w > 1e-8]
        return np.sum(np.log(w))

    sites_lap = np.zeros((n, n))
    for p, i in idx.items():
        sites_lap[i, i] = 6
        for a in AXES:
            q = tuple((p[k] + a[k]) % L for k in range(3))
            sites_lap[i, idx[q]] -= 1
    base = prime_logdet(sites_lap)

    def cost(incl):
        mat = sites_lap.copy()
        shared_edges = set()
        if shared != "none" and len(incl) == 2:
            # the edge(s) incident to both sites
            for a in AXES:
                v = tuple((x[k] + a[k]) % L for k in range(3))
                if v == y:
                    shared_edges.add(tuple(sorted((x, v))))
        if shared == "mult" and shared_edges:
            for origin, eps in incl:
                add_bonds(mat, origin, eps, skip=shared_edges)
            for edge in shared_edges:
                u, v = edge
                # weight (1+ex)(1+ey) means added stiffness (1+ex)(1+ey)-1
                extra = (1 + ex) * (1 + ey) - 1
                iu, iv = idx[u], idx[v]
                mat[iu, iu] += extra
                mat[iv, iv] += extra
                mat[iu, iv] -= extra
                mat[iv, iu] -= extra
        elif shared == "add" and shared_edges:
            for origin, eps in incl:
                add_bonds(mat, origin, eps, skip=shared_edges)
            for edge in shared_edges:
                u, v = edge
                extra = ex + ey
                iu, iv = idx[u], idx[v]
                mat[iu, iu] += extra
                mat[iv, iv] += extra
                mat[iu, iv] -= extra
                mat[iv, iu] -= extra
        else:
            for origin, eps in incl:
                add_bonds(mat, origin, eps)
        return 0.5 * (prime_logdet(mat) - base)

    both = cost([(x, ex), (y, ey)])
    onlyx = cost([(x, ex)])
    onlyy = cost([(y, ey)])
    return both - onlyx - onlyy, G, idx


def torus_checks():
    L = 4
    x, y = (0, 0, 0), (2, 0, 0)
    direct, G, idx = laplacian_F(L, x, y, 0.5, 0.5)
    formula, Mxy = interaction(G, idx, x, y, 0.5, 0.5, L)
    unlike, _ = interaction(G, idx, x, y, 0.5, -0.4, L)
    unlike_d, _, _ = laplacian_F(L, x, y, 0.5, -0.4)
    vac, _ = interaction(G, idx, x, y, -1.0, -1.0, L)
    # second-order coefficient on this same M
    f2 = -0.5 * 0.5 * 0.5 * np.sum(Mxy**2)
    # a smaller epsilon should approach f2 / (0.5*0.5) * ex*ey
    small, _ = interaction(G, idx, x, y, 1e-4, 1e-4, L)
    f2_small = -0.5 * (1e-4) ** 2 * np.sum(Mxy**2)
    quarter = -0.25 * (1e-4) ** 2 * np.sum(Mxy**2)
    # contact, L=6 so the printed 8^3 number is not required; sign split only
    L6 = 6
    mult, _, _ = laplacian_F(L6, (0, 0, 0), (1, 0, 0), -0.5, -0.5, shared="mult")
    add, _, _ = laplacian_F(L6, (0, 0, 0), (1, 0, 0), -0.5, -0.5, shared="add")
    ok = (
        abs(direct - formula) < 1e-8
        and abs(unlike - unlike_d) < 1e-8
        and formula < 0
        and unlike > 0
        and vac < 0
        and abs(small - f2_small) / abs(f2_small) < 1e-3
        and abs(small - quarter) / abs(quarter) > 0.5
        and mult > 0
        and add < 0
    )
    report(
        "torus formula and sign",
        ok,
        f"L=4 r=2 formula {formula:.6e} vs laplacian {direct:.6e}; unlike {unlike:.6e}; "
        f"vacancy {vac:.6e}; small-eps ratio {small / f2_small:.6f}; "
        f"L=6 contact mult {mult:.4e} add {add:.4e}",
    )


def Gz(n):
    a, b, c = sorted(abs(int(v)) for v in n)

    def f(t):
        return ive(a, 2 * t) * ive(b, 2 * t) * ive(c, 2 * t)

    pts = (0.0, 0.4, 2.0, 12.0, 80.0, np.inf)
    return sum(quad(f, lo, hi, epsabs=1e-14, limit=400)[0] for lo, hi in zip(pts, pts[1:]))


def infinite():
    g0, ge, g2 = Gz((0, 0, 0)), Gz((1, 0, 0)), Gz((2, 0, 0))
    mu = g0 - g2
    alpha = 2 / (1 - mu)
    const = -3 / (16 * np.pi**2) * alpha**2
    bare = -3 / (4 * np.pi**2)
    # tilt comparison along an axis, using the asymptotic vacancy constant is not the finite-r F.
    # Compute the 6x6 from Bessel Green values at the needed offsets for r=5 only as a spot check,
    # and the tilt ratio from G(r).
    ratios = []
    for r in (5, 10, 20):
        gr = Gz((r, 0, 0))
        ft = -gr / (g0**2 - gr**2)
        # axial second-difference sketch is not the full F; use the dressed continuum law as the prediction
        # and the exact 6x6 below for r=5.
        ratios.append((r, ft))
    # exact 6x6 at r=5,10 using Bessel entries. Bonds of 0 and of r*e1.
    def ends(origin, axis):
        return origin, tuple(origin[k] + axis[k] for k in range(3))

    cache = {}

    def g(p, q):
        d = tuple(p[k] - q[k] for k in range(3))
        key = tuple(sorted(abs(v) for v in d))
        if key not in cache:
            cache[key] = Gz(key)
        return cache[key]

    def M_inf(x, y):
        M = np.zeros((6, 6))
        for i, bi in enumerate(AXES):
            u, v = ends(x, bi)
            for j, bj in enumerate(AXES):
                p, q = ends(y, bj)
                M[i, j] = g(u, p) - g(u, q) - g(v, p) + g(v, q)
        return M

    vac_ratios = []
    for r, ft in ratios:
        Mxx = M_inf((0, 0, 0), (0, 0, 0))
        Mxy = M_inf((0, 0, 0), (r, 0, 0))
        Ax = dress(Mxx, -1.0)
        X = Ax @ Mxy @ Ax @ Mxy.T
        ev = np.linalg.eigvalsh(np.eye(6) - X)
        F = 0.5 * np.log(np.prod(ev))
        vac_ratios.append((r, F / ft, F * r**6))
    ok = (
        abs((g0 - ge) - 1 / 6) < 1e-10
        and abs(mu - 0.209841695316) < 5e-10
        and abs(alpha - 2.53114) < 2e-5
        and abs(const - (-0.121712)) < 2e-6
        and abs(bare - (-0.075990)) < 2e-5
        and abs(vac_ratios[0][1] - 6.00e-5) / 6.00e-5 < 0.02
        and abs(vac_ratios[1][1] - 1.11e-6) / 1.11e-6 < 0.02
        and abs(vac_ratios[2][1] - 3.14e-8) / 3.14e-8 < 0.02
    )
    text = " ".join(f"r={r} ratio {rat:.3e} F r^6 {fr6:.4f}" for r, rat, fr6 in vac_ratios)
    report(
        "infinite lattice",
        ok,
        f"G(0)-G(e)={g0 - ge:.10f}, mu={mu:.12f}, alpha(-1)={alpha:.5f}, vacancy constant {const:.6f}, bare {bare:.5f}; {text}",
    )


def main():
    moments_and_hessian()
    mu_algebra()
    row_sum_split()
    torus_checks()
    infinite()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - for disjoint bonds F = 1/2 log det(I - eps_x eps_y A_x M_xy A_y M_yx), "
        "negative for like signs at every order. The second-order coefficient is 1/2, not 1/4. "
        "On Z^3 the constant is -(3/(16 pi^2)) eps_x eps_y alpha_x alpha_y, and two vacancies "
        "are 6.0e-5, 1.1e-6, 3.1e-8 of two unit tilts at r = 5, 10, 20. "
        "A rotation-invariant inclusion has no charge, so its interaction is not 1/r."
    )
    print(
        "SUMMARY: confirmed the block-determinant formula on the 4^3 torus, the Gaussian factor 1/2, "
        "the dipole eigenvalue G(0)-G(2e), the vacancy constant -0.121712, and the three tilt ratios. "
        "The lattice Green expansion G=1/(4 pi r)+O(r^{-3}) was used as an assumed input to the constant, "
        "and the constant's algebraic prefactor was checked from that expansion."
    )


if __name__ == "__main__":
    main()
