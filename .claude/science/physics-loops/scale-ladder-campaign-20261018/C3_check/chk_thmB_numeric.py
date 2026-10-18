#!/usr/bin/env python3
r"""C3 check, route 3 (numerical, different method from Groebner): random-start Levenberg-Marquardt on the graded
Jacobi system for Z_L (complex structure constants, (S) normalised Lam_1 = 1, c(1,-1) = 1, nothing else imposed).

For every converged solution (max |Jacobi| < 1e-11) the checker tests:
  T1  2 Lam_n integer for all n (Theorem B (i));
  T2  Lam_n not in n + L Z for n not in {0,+-1} (Theorem B (ii));
  T3  the checker's arc lemma: {2..L-2} splits into arcs [n0, n0+m] with Lam_n = n - (n0+m/2) (implies Lam_2 <= 0).
Also reports the set of Lam_2 values reached and the smallest Jacobi residual reachable with Lam_2 pinned to 2.
Floating point; this is evidence, not proof.
"""
import sys

import numpy as np
from scipy.optimize import least_squares

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def make(L, pin2=None):
    pairs = [(a, b) for a in range(L) for b in range(a + 1, L) if (a, b) not in ((0, 1), (1, L - 1))]
    if pin2 is not None:
        pairs.remove((0, 2))
    idx = {p: i for i, p in enumerate(pairs)}
    nv = len(pairs)

    def cmat(z):
        C = np.zeros((L, L), complex)
        for (a, b), i in idx.items():
            C[a, b] = z[i]
            C[b, a] = -z[i]
        C[0, 1], C[1, 0] = 1, -1
        C[1, L - 1], C[L - 1, 1] = 1, -1
        if pin2 is not None:
            C[0, 2], C[2, 0] = pin2, -pin2
        return C
    A, B, E = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")

    def jac(C):
        return (C[A, B] * C[(A + B) % L, E] + C[B, E] * C[(B + E) % L, A] + C[E, A] * C[(E + A) % L, B]).ravel()

    def fun(x):
        z = x[:nv] + 1j * x[nv:]
        r = jac(cmat(z))
        return np.concatenate([r.real, r.imag])
    return nv, cmat, fun


def arc_ok(L, lam, tol=1e-6):
    """greedy arc decomposition of 2..L-2 using Lam_n - Lam_{n-1} = 1 inside an arc; arcs start at n0 with
    Lam_{n0} = -m/2 and end with Lam = +m/2."""
    n = 2
    while n <= L - 2:
        start = n
        m2 = -2 * lam[start]  # = m
        m = int(round(m2.real))
        if abs(m2 - m) > tol or m < 0 or start + m > L - 2:
            return False
        for j in range(m + 1):
            if abs(lam[start + j] - (j - m / 2)) > tol:
                return False
        n = start + m + 1
    return True


if __name__ == "__main__":
    rng = np.random.default_rng(181026)
    Ls = [int(a) for a in sys.argv[1:]] or [5, 6, 7, 8]
    for L in Ls:
        nv, cmat, fun = make(L)
        sols = []
        tries = 400
        for _ in range(tries):
            x0 = rng.normal(scale=rng.choice([0.3, 1.0, 2.0]), size=2 * nv)
            r = least_squares(fun, x0, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
            if np.max(np.abs(r.fun)) < 1e-11:
                C = cmat(r.x[:nv] + 1j * r.x[nv:])
                sols.append(C[0].copy())
        ok1 = all(np.max(np.abs(2 * lam - np.round(2 * lam.real))) < 1e-6 for lam in sols)
        bad2 = 0
        for lam in sols:
            for n in range(2, L - 1):
                q = lam[n] - n
                if abs(q / L - np.round(q.real / L)) < 1e-6:
                    bad2 += 1
        ok3 = all(arc_ok(L, lam) for lam in sols)
        l2 = sorted({round(lam[2].real * 2) / 2 for lam in sols})
        check(f"N_L{L}_count", len(sols) >= 20, f"L={L}: {len(sols)}/{tries} random starts converged to exact graded Lie algebras with (S)")
        check(f"N_L{L}_T1", ok1, "2 Lam_n / Lam_1 integer on every solution (Theorem B (i))")
        check(f"N_L{L}_T2", bad2 == 0, "Lam_n/Lam_1 not in n + LZ for n not in {0,+-1} on every solution (Theorem B (ii))")
        check(f"N_L{L}_T3", ok3, f"arc formula Lam_n = n - centre(arc) holds on every solution; Lam_2/Lam_1 values reached: {l2}")
        # pinned Lam_2 = 2: best residual
        nvp, cmatp, funp = make(L, pin2=2.0)
        best = np.inf
        for _ in range(100):
            x0 = rng.normal(size=2 * nvp)
            r = least_squares(funp, x0, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
            best = min(best, np.max(np.abs(r.fun)))
        check(f"N_L{L}_pin2", best > 1e-3, f"Lam_2 = 2 pinned: smallest max|Jacobi| over 100 starts = {best:.3e} (no solution found)")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
