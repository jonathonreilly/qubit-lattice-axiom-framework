#!/usr/bin/env python3
r"""C3 check: Theorem C linear algebra (exact) and the FFZ 'O(a)' claim (numerical).

C1  Full support: lam(k1) + lam(k2) = lam'(k1+k2) for ALL k1,k2 in Z_L  =>  solution space is {lam = const, lam' = 2 const}
    (dim 1, exact rank over QQ).  So lam - lam(0) is the zero homomorphism; lam = 0 needs lam(0) = 0.
C2  No-wrap support (|kbar1|,|kbar2|,|kbar1+kbar2| <= L//2, i.e. anti-aliased product), L odd:
    solution space contains lam = i kbar (SLAC) and has dim 2 (const and kbar).
F1  FFZ sine algebra: with basis J_m = g^m1 h^m2 the structure constant kappa(w^{p2q1} - w^{p1q2}) deviates from
    p x q at O(1/N); with the Weyl-ordered basis J'_m = e^{i pi m1 m2/N} J_m (a rescaling X_m -> phase X_m, i.e. a
    coboundary) it is (N/pi) sin(pi s/N) and deviates at O(1/N^2).  So the O(a) in C3's E2 is a basis artefact.
"""
import numpy as np
import sympy as sp

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def nbar(n, L):
    r = n % L
    return r - L if r > L // 2 else r


def nullspace(L, allowed):
    lam = sp.symbols(f"a0:{L}")
    lamp = sp.symbols(f"b0:{L}")
    rows = []
    for k1 in range(L):
        for k2 in range(L):
            if allowed(k1, k2):
                rows.append([1 if j == k1 else 0 for j in range(L)])
                rows[-1] = [0] * L
                r = [0] * (2 * L)
                r[k1] += 1
                r[k2] += 1
                r[L + (k1 + k2) % L] -= 1
                rows[-1] = r
    M = sp.Matrix(rows)
    return M.nullspace()


if __name__ == "__main__":
    for L in (4, 5, 6, 7, 8, 9):
        ns = nullspace(L, lambda a, b: True)
        v = ns[0] if len(ns) == 1 else None
        ok = len(ns) == 1 and all(v[j] == v[0] for j in range(L)) and all(v[L + j] == 2 * v[0] for j in range(L))
        check(f"C1_L{L}", ok, f"full support: solutions of lam(k1)+lam(k2)=lam'(k1+k2) = span{{lam=1, lam'=2}} (dim {len(ns)}); lam(0)=0 => lam=0")
    for L in (5, 7, 9):
        m = L // 2
        allowed = lambda a, b: abs(nbar(a, L)) <= m and abs(nbar(b, L)) <= m and abs(nbar(a, L) + nbar(b, L)) <= m
        ns = nullspace(L, allowed)
        M = sp.Matrix.hstack(*ns)
        slac = sp.Matrix([nbar(j, L) for j in range(L)] + [nbar(j, L) for j in range(L)])
        in_span = M.rank() == sp.Matrix.hstack(M, slac).rank()
        check(f"C2_L{L}", len(ns) == 2 and in_span, f"no-wrap support: solution space dim {len(ns)}, contains SLAC lam = kbar: {in_span}")
    # FFZ
    p, q = (1, 2), (2, -1)
    s = p[1] * q[0] - p[0] * q[1]
    Ns = np.array([11, 21, 41, 81, 161, 321])
    e_raw, e_weyl = [], []
    for N in Ns:
        w = np.exp(2j * np.pi / N)
        kappa = N / (2j * np.pi)
        raw = kappa * (w ** (p[1] * q[0]) - w ** (p[0] * q[1]))
        # direct matrix computation of the Weyl-ordered structure constant for small N only (sanity), formula otherwise
        weyl = kappa * (np.exp(1j * np.pi * s / N) - np.exp(-1j * np.pi * s / N))
        e_raw.append(abs(raw - s) / abs(s))
        e_weyl.append(abs(weyl - s) / abs(s))
    sr = np.polyfit(np.log(Ns), np.log(e_raw), 1)[0]
    sw = np.polyfit(np.log(Ns), np.log(e_weyl), 1)[0]
    # matrix-level confirmation of the Weyl-basis constant at N = 7
    N = 7
    w = np.exp(2j * np.pi / N)
    g = np.roll(np.eye(N), 1, axis=0)
    h = np.diag(w ** np.arange(N))
    Jp = lambda m: np.exp(1j * np.pi * m[0] * m[1] / N) * np.linalg.matrix_power(g, m[0] % N) @ np.linalg.matrix_power(h, m[1] % N)
    r = (p[0] + q[0], p[1] + q[1])
    Cm = Jp(p) @ Jp(q) - Jp(q) @ Jp(p)
    cc = np.trace(Jp(r).conj().T @ Cm) / N
    mat_ok = np.linalg.norm(Cm - cc * Jp(r)) < 1e-10 and abs(cc - 2j * np.sin(np.pi * s / N)) < 1e-10
    check("F1", abs(sr + 1) < 0.1 and abs(sw + 2) < 0.1 and mat_ok,
          f"raw-basis deviation slope {sr:.2f} (O(a)); Weyl-basis deviation slope {sw:.2f} (O(a^2)); N=7 matrix check of 2i sin(pi s/N): {mat_ok}")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
