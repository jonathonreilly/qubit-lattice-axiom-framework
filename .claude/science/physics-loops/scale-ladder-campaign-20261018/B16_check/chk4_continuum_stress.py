"""B16 check, item 4: continuum leading-order {G[xi], C(N)} at order (h^0, E^2, F^2).

Own implementation: sympy Functions of (x0,x1,x2), Euler operators by differentiation w.r.t. Derivative
objects, local Poisson bracket {int f, int g} = int sum_(q,p) (E_q f E_p g - E_p f E_q g).
"mod Gauss" is imposed by substituting E^i = eps^{ijk} d_j W_k AFTER the bracket (div E = 0 identically),
then requiring the density to be a total divergence (all Euler operators w.r.t. A, W, N, xi vanish).

Premises (as B16): P_A[xi] = int xi^i E^j F_ij; G_g[xi] = int sum_{i<=j} P_ij (d_i xi_j + d_j xi_i);
H_EM(N) = int N[(g2/2) E.E + (cB/(2 g2)) sum_{i<j} F_ij^2]; coupling int N sum_{i<=j} h_ij Q_ij(E,F) with Q_ij a
GENERAL quadratic form in (E1,E2,E3,F01,F02,F12): 6 x 21 = 126 unknowns; RHS H_EM(s1 xi.grad N + s2 N div xi).

C4a  solution space = one-parameter family: Q = (metric stress of H_EM(g), E a vector density, A a one-form)
     + lam tr h (H_EM density), with s1 = 1, s2 = -2 lam.
C4b  without Gauss (E unrestricted) the gauge-covariant P_A does NOT close (Gauss needed with an E-dependent
     multiplier), while the pure Lie generator G_Lie[xi] = int E^j (xi^i d_i A_j + A_i d_j xi^i) closes with the
     same coupling and no Gauss term.
"""
import itertools
import sys
import time

import sympy as sp

X = sp.symbols("x0 x1 x2")
DIM = 3
g2, cB = sp.symbols("g2 cB", positive=True)
A = [sp.Function(f"A{i}")(*X) for i in range(3)]
Ef = [sp.Function(f"E{i}")(*X) for i in range(3)]
W = [sp.Function(f"W{i}")(*X) for i in range(3)]
N = sp.Function("N")(*X)
XI = [sp.Function(f"xi{i}")(*X) for i in range(3)]
PAIRS = [(0, 1), (0, 2), (1, 2)]
SYMP = [(i, j) for i in range(3) for j in range(i, 3)]
H = {ij: sp.Function(f"h{ij[0]}{ij[1]}")(*X) for ij in SYMP}
PP = {ij: sp.Function(f"P{ij[0]}{ij[1]}")(*X) for ij in SYMP}


def hsym(i, j):
    return H[(min(i, j), max(i, j))]


def d(f, i):
    return sp.diff(f, X[i])


def Fij(i, j):
    return d(A[j], i) - d(A[i], j)


def euler(f, u):
    """Euler operator E_u(f) = sum_alpha (-D)^alpha df/du_alpha (f polynomial in jets of Function u)."""
    f = sp.expand(f)
    out = 0
    ders = set(a for a in f.atoms(sp.Derivative) if a.expr == u)
    jets = [u] + sorted(ders, key=sp.default_sort_key)
    for jet in jets:
        df = sp.diff(f, jet)
        if df == 0:
            continue
        if jet == u:
            out += df
        else:
            vars_ = jet.variables
            term = df
            for v in vars_:
                term = -sp.diff(term, v)
            out += term
    return sp.expand(out)


CANON = [(A[i], Ef[i]) for i in range(3)] + [(H[ij], PP[ij]) for ij in SYMP]


def bracket(f, g):
    out = 0
    for q, p in CANON:
        fq, fp = euler(f, q), euler(f, p)
        if fq == 0 and fp == 0:
            continue
        gq, gp = euler(g, q), euler(g, p)
        out += fq * gp - fp * gq
    return sp.expand(out)


def hem(Nexpr, E=Ef):
    return Nexpr * (g2 / 2 * sum(e ** 2 for e in E) + cB / (2 * g2) * sum(Fij(i, j) ** 2 for (i, j) in PAIRS))


def curlW():
    eps = sp.LeviCivita
    return [sum(eps(i, j, k) * d(W[k], j) for j in range(3) for k in range(3)) for i in range(3)]


def to_symbols(expr):
    """replace Function/Derivative atoms by plain symbols for coefficient extraction."""
    atoms = sorted(expr.atoms(sp.Derivative), key=sp.default_sort_key) + sorted(expr.atoms(sp.core.function.AppliedUndef), key=sp.default_sort_key)
    rep = {a: sp.Symbol(f"j{n}") for n, a in enumerate(atoms)}
    # derivatives first so that Functions inside derivatives are not replaced prematurely
    e = expr.xreplace({a: rep[a] for a in atoms if isinstance(a, sp.Derivative)})
    e = e.xreplace({a: rep[a] for a in atoms if not isinstance(a, sp.Derivative)})
    return e, list(rep.values())


def coeff_eqs(expr, unknowns):
    expr = sp.expand(expr)
    if expr == 0:
        return []
    e, syms = to_symbols(expr)
    syms = [s for s in syms if e.has(s)]
    P = sp.Poly(e, *syms)
    return [c for c in P.coeffs() if c != 0]


def divergence_eqs(dens, fields, unknowns):
    eqs = []
    for u in fields:
        eqs += coeff_eqs(euler(dens, u), unknowns)
    return eqs


def main():
    t0 = time.time()
    RES = {"pass": 0, "fail": 0}

    def check(tag, ok, msg):
        RES["pass" if ok else "fail"] += 1
        print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)

    vars6 = Ef + [Fij(*ij) for ij in PAIRS]
    quad = [(a, b) for a in range(6) for b in range(a, 6)]
    unk = {}
    Q = {}
    for ij in SYMP:
        Q[ij] = 0
        for (a, b) in quad:
            s = sp.Symbol(f"q{ij[0]}{ij[1]}_{a}{b}")
            unk[s] = (ij, a, b)
            Q[ij] += s * vars6[a] * vars6[b]
    s1, s2 = sp.symbols("s1 s2")
    unknowns = list(unk) + [s1, s2]
    coupling = N * sum(H[ij] * Q[ij] for ij in SYMP)
    PA = sum(XI[i] * Ef[j] * Fij(i, j) for i in range(3) for j in range(3) if i != j)
    GLie = sum(Ef[j] * (sum(XI[i] * d(A[j], i) + A[i] * d(XI[i], j) for i in range(3))) for j in range(3))
    Gg = sum(PP[(i, j)] * (d(XI[j], i) + d(XI[i], j)) for (i, j) in SYMP)
    divxi = sum(d(XI[i], i) for i in range(3))
    rhs = hem(s1 * sum(XI[i] * d(N, i) for i in range(3)) + s2 * N * divxi)
    results = {}
    for gname, Gm in (("P_A", PA), ("G_Lie", GLie)):
        lhs = bracket(Gm + Gg, hem(N) + coupling)
        # keep order h^0 (coupling contributes via G_g only)
        lhs0 = sp.expand(lhs.subs({H[ij]: 0 for ij in SYMP}).doit())
        dens = sp.expand(lhs0 - rhs)
        for gauss in (True, False):
            dd = dens
            fields = A + Ef + [N] + XI
            if gauss:
                cw = curlW()
                dd = sp.expand(dens.subs({Ef[i]: cw[i] for i in range(3)}).doit())
                fields = A + W + [N] + XI
            eqs = divergence_eqs(dd, fields, unknowns)
            sol = sp.solve(eqs, unknowns, dict=True)
            results[(gname, gauss)] = sol
            print(f"  [{gname}, mod Gauss={gauss}] #eqs {len(eqs)}, #solutions {len(sol)}, t={time.time() - t0:.0f}s", flush=True)
    # comparator: metric stress
    hm = sp.Matrix(3, 3, lambda i, j: hsym(i, j))
    epsl = sp.Symbol("epsl")
    gmat = sp.eye(3) + epsl * hm
    ginv = sp.eye(3) - epsl * hm  # O(eps)
    sqrtg = 1 + epsl * hm.trace() / 2
    Fm = sp.Matrix(3, 3, lambda i, j: Fij(i, j) if i != j else 0)
    Ev = sp.Matrix(Ef)
    dens_g = g2 / 2 * (Ev.T * gmat * Ev)[0] * (1 - epsl * hm.trace() / 2) + cB / (4 * g2) * sqrtg * sum(
        ginv[i, k] * ginv[j, l] * Fm[i, j] * Fm[k, l] for i in range(3) for j in range(3) for k in range(3) for l in range(3))
    stress = sp.expand(sp.diff(sp.expand(dens_g), epsl).subs(epsl, 0))
    lam = sp.Symbol("lam")
    hdens = g2 / 2 * sum(e ** 2 for e in Ef) + cB / (2 * g2) * sum(Fij(i, j) ** 2 for (i, j) in PAIRS)
    expected = sp.expand(stress + lam * sum(H[(i, i)] for i in range(3)) * hdens)

    def coupling_of(sol):
        cpl = sp.expand(sum(H[ij] * Q[ij] for ij in SYMP).xreplace(sol))
        return cpl

    sol = results[("P_A", True)]
    ok = False
    if len(sol) == 1:
        cpl = coupling_of(sol[0])
        free = sorted((cpl.free_symbols | {sol[0].get(s1, s1), sol[0].get(s2, s2)}.__class__()) & set(unknowns), key=str)
        free = [s for s in unknowns if s not in sol[0]]
        print("  free parameters:", free, " s1 =", sol[0].get(s1, s1), " s2 =", sol[0].get(s2, s2))
        # match to expected with lam = free param relation
        if len(free) == 1:
            fp = free[0]
            lamv = sp.solve(sp.Eq(sol[0].get(s2, s2), -2 * lam), fp) if sol[0].get(s2, s2).has(fp) else None
            diff = sp.expand(cpl - expected)
            # find lam(fp) by matching
            eqsl = coeff_eqs(diff, [lam])
            sl = sp.solve(eqsl, [lam], dict=True)
            ok = (len(sl) == 1) and sp.simplify(sol[0].get(s1, s1) - 1) == 0 and sp.simplify(sol[0].get(s2, s2) + 2 * sl[0][lam]) == 0
            print("  lam in terms of free parameter:", sl)
    check("C4a", ok, "P_A + G_g, mod Gauss (E = curl W), 126-coefficient general coupling: ONE-parameter solution = metric stress of H_EM(g) + lam tr h H_EM, s1 = 1, s2 = -2 lam")
    solL = results[("G_Lie", False)]
    okL = len(solL) == 1 and len([s for s in unknowns if s not in solL[0]]) == 1
    noP = len(results[("P_A", False)]) == 0
    if okL:
        diff = sp.expand(coupling_of(solL[0]) - expected)
        sl = sp.solve(coeff_eqs(diff, [lam]), [lam], dict=True)
        okL = len(sl) == 1 and sp.simplify(solL[0].get(s1, s1) - 1) == 0
    check("C4b", noP and okL and len(results[("G_Lie", True)]) == 1,
          f"without restricting E: P_A has NO solution (Gauss needed, field-dependent multiplier) [{len(results[('P_A', False)])} solutions]; "
          f"G_Lie closes with the same one-parameter metric-stress family and no Gauss term")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")


if __name__ == "__main__":
    main()
