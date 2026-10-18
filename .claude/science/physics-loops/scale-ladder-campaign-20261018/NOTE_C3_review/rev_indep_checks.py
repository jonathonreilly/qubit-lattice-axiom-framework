#!/usr/bin/env python3
"""Reviewer's independent checks (fresh-context same-family reviewer; imports nothing from the runner).

R1  B4 sufficiency by a different path: realise sl2 |x (+V_m) as affine matrices on (+V_m) (+) C, with V_m =
    homogeneous polynomials of degree m in (x, y), E = x d/dy, F = y d/dx, H = x d/dx - y d/dy. Jacobi is automatic
    (matrix commutators); the load-bearing checks are the momentum grading ([X_a, X_b] in span X_(a+b), one generator
    per momentum), Lam_n = n - arc centre, and the Lam_2 set.
R2  necessity at L = 5, 6 by a non-Groebner path: sympy.solve of the cyclic Jacobi system under (S), all components;
    every solution's (Lam_2..Lam_(L-2)) must be an arc point.
R3  A1 sharpened: for each finite-range family, the y-values on the unit circle where all non-constant z-coefficients
    of d(zy) - d(z) vanish (where [D, X_p] in span X_p would hold at that single p).
R4  C3 in 2D (3x3 torus, xi = e_1 uniform): {G_m[e_1], (1/2) sum N pi^2} = (1/2) sum_x (N_(x+e1) - N_x) pi_x pi_(x+e1).
"""
import itertools
from fractions import Fraction as Fr
import sympy as sp

x, y = sp.symbols("x y")
P = 0


def ok(name, cond, msg=""):
    global P
    print(("[OK]  " if cond else "[BAD] ") + name + "  " + msg, flush=True)
    P += (not cond)


def partitions(L):
    path = list(range(2, L - 1))
    if not path:
        return [[]]
    res = []
    for cuts in itertools.product([False, True], repeat=len(path) - 1):
        arcs, cur = [], [path[0]]
        for i, c in enumerate(cuts):
            if c:
                arcs.append(cur); cur = []
            cur.append(path[i + 1])
        arcs.append(cur)
        res.append(arcs)
    return res


def R1(L):
    parts = partitions(L)
    lam2 = set()
    allgood = True
    for arcs in parts:
        # basis of V = (+) V_m: monomials x^(m-j) y^j of arc i; momentum n0 + m - j
        basis = []  # (arc index, m, j, momentum)
        for i, arc in enumerate(arcs):
            m = len(arc) - 1
            for j in range(m + 1):
                basis.append((i, m, j, arc[0] + m - j))
        dimV = len(basis)
        # matrix space: V (+) C (+) W, W = defining V_1 (faithful sl2 block, not part of the algebra's radical)
        N = dimV + 1 + 2
        pos = {(b[0], b[2]): k for k, b in enumerate(basis)}
        wb = [(-1, 1, 0), (-1, 1, 1)]

        def rho(op):
            M = sp.zeros(N, N)
            for k, (i, m, j, n) in enumerate(basis):
                mono = x ** (m - j) * y ** j
                img = sp.expand(op(mono))
                if img == 0:
                    continue
                for jj in range(m + 1):
                    co = sp.Poly(img, x, y).coeff_monomial(x ** (m - jj) * y ** jj)
                    if co != 0:
                        M[pos[(i, jj)], k] = co
            for k, (i, m, j) in enumerate(wb):
                img = sp.expand(op(x ** (m - j) * y ** j))
                for jj in range(2):
                    co = sp.Poly(img, x, y).coeff_monomial(x ** (m - jj) * y ** jj) if img != 0 else 0
                    if co != 0:
                        M[dimV + 1 + jj, dimV + 1 + k] = co
            return M
        E = rho(lambda f: x * sp.diff(f, y))
        F = rho(lambda f: y * sp.diff(f, x))
        H = rho(lambda f: x * sp.diff(f, x) - y * sp.diff(f, y))
        gens = {0: H / 2, 1 % L: E, (-1) % L: F / 2}
        for k, (i, m, j, n) in enumerate(basis):
            T = sp.zeros(N, N)
            T[k, dimV] = 1  # translation by basis vector k
            assert n % L not in gens
            gens[n % L] = T
        assert set(gens) == set(range(L))
        lam = {}
        good = True
        for a in range(L):
            for b in range(L):
                C = gens[a] * gens[b] - gens[b] * gens[a]
                tgt = gens[(a + b) % L]
                # C must be a scalar multiple of tgt
                nz = [(r, c) for r in range(N) for c in range(N) if tgt[r, c] != 0]
                sc = C[nz[0]] / tgt[nz[0]]
                if C - sc * tgt != sp.zeros(N, N):
                    good = False
                if a == 0:
                    lam[b] = sc
        good &= lam[1] == 1 and lam[L - 1] == -1
        cen = {n: Fr(arc[0] + arc[-1], 2) for arc in arcs for n in arc}
        good &= all(sp.Rational(lam[n]) == sp.Rational((Fr(n) - cen[n]).numerator, (Fr(n) - cen[n]).denominator) for n in cen)
        if L >= 4:
            lam2.add(sp.Rational(lam[2]))
        allgood &= good
    exp = {sp.Rational(-m, 2) for m in range(L - 3)} if L >= 4 else set()
    ok(f"R1_L{L}", allgood and lam2 == exp, f"{len(parts)} partitions as affine matrices: graded, Lam_n = n - centre; Lam_2 set {sorted(lam2)}")


def R2(L):
    # (S): Lam_1 = 1, c(1,-1) = 1; unknowns: c(a,b) for 0 <= a < b < L except the two fixed
    sym = {}
    for a in range(L):
        for b in range(a + 1, L):
            sym[(a, b)] = sp.Symbol(f"c{a}_{b}")
    sym[(0, 1)] = sp.Integer(1)
    sym[(1, L - 1)] = sp.Integer(1)

    def c(a, b):
        a, b = a % L, b % L
        if a == b:
            return 0
        return sym[(a, b)] if a < b else -sym[(b, a)]
    eqs = set()
    for a, b, e in itertools.combinations(range(L), 3):
        J = sp.expand(c(a, b) * c(a + b, e) + c(b, e) * c(b + e, a) + c(e, a) * c(e + a, b))
        if J != 0:
            eqs.add(J)
    # also triples with repeats
    for a, b in itertools.product(range(L), repeat=2):
        for e in (a, b):
            J = sp.expand(c(a, b) * c(a + b, e) + c(b, e) * c(b + e, a) + c(e, a) * c(e + a, b))
            if J != 0:
                eqs.add(J)
    unk = sorted({s for q in eqs for s in q.free_symbols}, key=str)
    sols = sp.solve(list(eqs), unk, dict=True)
    arcpts = set()
    for arcs in partitions(L):
        cen = {n: Fr(arc[0] + arc[-1], 2) for arc in arcs for n in arc}
        arcpts.add(tuple(Fr(n) - cen[n] for n in range(2, L - 1)))
    got, free = set(), False
    for s in sols:
        vals = []
        for n in range(2, L - 1):
            v = sp.sympify(c(0, n)).subs(s)
            if not v.is_number:
                free = True
                break
            vals.append(Fr(str(sp.nsimplify(v))))
        else:
            got.add(tuple(vals))
    ok(f"R2_L{L}", not free and got == arcpts, f"sympy.solve: {len(sols)} solution components; Lam points {sorted(got)} == arc points {sorted(arcpts)}")


def R3():
    z, yy = sp.symbols("z y")
    fams = {"B14_central": {(0, 1): Fr(1, 2), (0, 0): Fr(-1, 2), (1, 1): Fr(1, 2), (1, 0): Fr(-1, 2)}}
    imp = {}
    for (r, c_, v) in [(0, 1, Fr(9, 8)), (0, 0, Fr(-9, 8)), (0, 2, Fr(-1, 24)), (0, -1, Fr(1, 24))]:
        for rr in (r, r + 1):
            imp[(rr, c_)] = imp.get((rr, c_), 0) + v / 2
    fams["imp4"] = imp
    for nm, A in fams.items():
        d = lambda zz: sum(sp.Rational(v.numerator, v.denominator) * zz ** (c_ - r) for (r, c_), v in A.items())
        g = sp.expand((d(z * yy) - d(z)) * z ** 6)
        Pz = sp.Poly(g, z)
        coeffs = [sp.factor(co) for mon, co in zip(Pz.monoms(), Pz.coeffs()) if mon[0] != 6]
        common = sp.gcd_list([sp.numer(sp.together(cf)) for cf in coeffs])
        print(f"  R3 {nm}: d(z) = {sp.simplify(d(z))}; non-constant z-coeffs gcd in y: {sp.factor(common)}")
        roots = sp.Poly(common, yy).all_roots() if sp.Poly(common, yy).degree() > 0 else []
        ok(f"R3_{nm}", all(sp.nsimplify(r) == 1 for r in roots), f"common roots {roots} (only y = 1 allowed)")


def R4():
    n = 3
    sites = [(i, j) for i in range(n) for j in range(n)]
    ph = {s: sp.Symbol(f"f{s[0]}{s[1]}") for s in sites}
    pi = {s: sp.Symbol(f"p{s[0]}{s[1]}") for s in sites}
    Nn = {s: sp.Symbol(f"N{s[0]}{s[1]}") for s in sites}
    sh = lambda s: ((s[0] + 1) % n, s[1])
    G = sum((ph[sh(s)] - ph[s]) * (pi[s] + pi[sh(s)]) / 2 for s in sites)
    Hh = sum(Nn[s] * pi[s] ** 2 / 2 for s in sites)
    br = sp.expand(sum(sp.diff(G, ph[s]) * sp.diff(Hh, pi[s]) - sp.diff(G, pi[s]) * sp.diff(Hh, ph[s]) for s in sites))
    tgt = sp.expand(sum((Nn[sh(s)] - Nn[s]) * pi[s] * pi[sh(s)] / 2 for s in sites))
    diag = sum(sp.Poly(br, *pi.values()).coeff_monomial(pi[s] ** 2) for s in sites)
    ok("R4_2D", br == tgt and sp.expand(diag) == 0, "2D 3x3, xi = e_1: bracket = (1/2) sum (N_(x+e1)-N_x) pi_x pi_(x+e1), no diagonal part")


if __name__ == "__main__":
    for L in range(3, 10):
        R1(L)
    for L in (5, 6):
        R2(L)
    R3()
    R4()
    print("BAD count:", P)
