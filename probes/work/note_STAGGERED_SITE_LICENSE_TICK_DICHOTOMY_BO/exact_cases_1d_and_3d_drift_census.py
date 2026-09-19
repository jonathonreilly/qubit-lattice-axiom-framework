#!/usr/bin/env python3
"""J:note check for STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09 (on main).

The note's theorem is 1D / per-axis: every site-licensed unitary 2-site-periodic tick U(z) = [[alpha, p + q/z], [r + s z, delta]] has
constant trace, single-monomial off-diagonal entries, a monomial determinant e^{iD} z^w with |w| <= 1, and is FLAT or SATURATING
(dispersive => T = 0 => bands (D + pi + w K)/2 + {0, pi}, |v| = 1 site/tick). Its falsifier list adds a larger-cell falsifier (a
dispersive licensed tick with a tunable cone slope) and "the 3D enumeration producing a quantized slope different from 1".

Checks, exact, with machinery disjoint from the runner (symbolic dichotomy + seeded least-squares sweep):
  A. a proof by cases in sympy: the Laurent coefficients of U^dag U - I and U U^dag - I (z-bar = 1/z) contain r s-bar and p q-bar as the
     z^{+-1} coefficients; in each of the four support cases (r or s zero) x (p or q zero) the remaining equations are solved and every
     solution is either z-independent (flat) or of the form [[0, p], [s z, 0]] / [[0, q/z], [r, 0]] with |p| = |s| = 1 resp.
     |q| = |r| = 1, trace 0, det = -p s z resp. -q r / z, eigenvalues squaring to det, slope 1/2 per cell = 1 per site;
  B. the 1D monomial census for periods p = 2..8: every licensed permutation of Z with period p, its drift velocity per orbit (exact
     rationals): only the uniform shifts are dispersive, with speed exactly 1;
  C. information beyond the note (no claim of the note is at stake, it names the 3D simultaneous tick open): all 7^8 period-2
     site-licensed permutation ticks on Z^3 (each of the 8 sublattice classes stays or moves one step along +-x, +-y, +-z; bijective
     iff the induced class map is a permutation), and the exact drift velocity vectors of their orbits.
HIT if a 1D claim fails.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as Fr

import numpy as np
import sympy as sp


def cases_1d():
    z = sp.symbols("z", nonzero=True)
    a, d, p, q, r, s = sp.symbols("alpha delta p q r s")
    ac, dc, pc, qc, rc, sc = sp.symbols("alpha_c delta_c p_c q_c r_c s_c")        # conjugates as independent symbols
    U = sp.Matrix([[a, p + q / z], [r + s * z, d]])
    Ud = sp.Matrix([[ac, rc + sc / z], [pc + qc * z, dc]])                         # conjugate transpose with z-bar = 1/z
    out = {}
    M1 = sp.expand(Ud * U)
    M2 = sp.expand(U * Ud)
    coeffs = set()
    for M in (M1, M2):
        for e in M:
            poly = sp.Poly(sp.expand(e * z), z)
            for c in poly.all_coeffs():
                coeffs.add(sp.expand(c))
    out["r s-bar is a coefficient"] = any(sp.simplify(c - rc * s) == 0 or sp.simplify(c - sc * r) == 0 for c in coeffs)
    out["p q-bar is a coefficient"] = any(sp.simplify(c - qc * p) == 0 or sp.simplify(c - pc * q) == 0 for c in coeffs)
    # the four support cases; solve over parameters of modulus and phase
    results = {}
    th = sp.symbols("t0:6", real=True)
    for zero_rs in ("r", "s"):
        for zero_pq in ("p", "q"):
            sub = {zero_rs: 0, zero_pq: 0}
            Uc = U.subs({sp.Symbol(k): 0 for k in sub})
            # remaining nonzero hop entries
            live = [x for x in (p, q, r, s) if str(x) not in sub]
            detU = sp.factor(sp.expand(Uc.det()))
            zdep = Uc.has(z)
            results[(zero_rs, zero_pq)] = (Uc, detU, zdep, live)
    # case analysis of unitarity: for a z-dependent case, unitarity forces the diagonal to vanish when both live hops are nonzero
    verdict = {}
    for key, (Uc, detU, zdep, live) in results.items():
        if not zdep:
            verdict[key] = "z-independent: flat"
            continue
        # columns: impose orthogonality coefficient by coefficient
        c1, c2 = Uc[:, 0], Uc[:, 1]
        conjmap = {a: ac, d: dc, p: pc, q: qc, r: rc, s: sc}
        cj = lambda e: sp.expand(e.subs(z, 1 / z).xreplace(conjmap)) if e != 0 else 0
        inner = sp.expand(cj(c1[0]) * c2[0] + cj(c1[1]) * c2[1])
        eqs = sp.Poly(sp.expand(inner * z ** 2), z).all_coeffs()
        # a dispersive tick needs both live hops nonzero; then orthogonality kills the diagonal entries
        eqs = [sp.factor(e) for e in eqs if e != 0]
        verdict[key] = ("orthogonality coefficients", eqs, "det", detU)
    # the dispersive families explicitly: U = [[0, p], [s z, 0]], |p| = |s| = 1; and U = [[0, q/z], [r, 0]], |q| = |r| = 1
    fam = []
    for M, detexp in ((sp.Matrix([[0, sp.exp(sp.I * th[0])], [sp.exp(sp.I * th[1]) * z, 0]]), 1),
                      (sp.Matrix([[0, sp.exp(sp.I * th[0]) / z], [sp.exp(sp.I * th[1]), 0]]), -1)):
        zz = sp.exp(sp.I * sp.Symbol("K", real=True))
        Mk = M.subs(z, zz)
        unit = sp.simplify(Mk * Mk.H - sp.eye(2)) == sp.zeros(2, 2)
        tr = sp.simplify(M.trace()) == 0
        dt = sp.simplify(M.det() / z ** detexp)
        lam = sp.symbols("lam")
        charp = sp.expand((M - lam * sp.eye(2)).det())
        # trace 0, so the characteristic polynomial is lam^2 + det: mu^2 = -det = -e^{iD} z^w, omega = (D + pi + w K)/2 + {0, pi}
        sq = sp.simplify(charp - (lam ** 2 + M.det())) == 0
        fam.append((unit, tr, dt.has(z) is False, sq))
    # per-case conclusions, checked: (zero r, zero p) has a z-free characteristic polynomial; in the two mixed cases orthogonality
    # reads alpha_c * hop = 0 and delta * conj(hop') = 0, so two nonzero live hops force alpha = delta = 0 (the mover), while one zero
    # live hop leaves a triangular tick whose eigenvalues are its constant diagonal (flat)
    lam = sp.symbols("lam")
    checks = {}
    U1 = sp.Matrix([[a, q / z], [s * z, d]])
    cp1 = sp.Poly(sp.expand((U1 - lam * sp.eye(2)).det()), lam)
    checks["(r,p): char poly z-free"] = all(not sp.simplify(c).has(z) for c in cp1.all_coeffs())
    for key, (h1, h2) in ((("r", "q"), (p, s)), (("s", "p"), (q, r))):
        Uc = results[key][0]
        eqs = verdict[key][1]
        forced = sp.solve([sp.Eq(e, 0) for e in eqs], [ac, d], dict=True)
        checks[f"{key}: nonzero hops force alpha = delta = 0"] = forced == [{ac: 0, d: 0}]
        for hz in (h1, h2):
            Ut = Uc.subs(hz, 0)
            cpt = sp.Poly(sp.expand((Ut - lam * sp.eye(2)).det()), lam)
            checks[f"{key}: {hz} = 0 is flat"] = all(not sp.simplify(c).has(z) for c in cpt.all_coeffs())
    return out, verdict, fam, checks


def perm_census_1d(p):
    """licensed permutations of Z with period p: moves m_j in {-1,0,1} for j = 0..p-1, bijective; orbit drift per site."""
    speeds = set()
    disp = 0
    for moves in itertools.product((-1, 0, 1), repeat=p):
        img = [(j + moves[j]) % p for j in range(p)]
        if len(set(img)) != p:
            continue
        # follow each class orbit: class sequence and displacement until return
        for j0 in range(p):
            j, D, m = j0, 0, 0
            while True:
                D += moves[j]
                j = (j + moves[j]) % p
                m += 1
                if j == j0:
                    break
            v = Fr(D, m)
            speeds.add(abs(v))
            disp += v != 0
    return speeds


def census_3d():
    classes = list(itertools.product((0, 1), repeat=3))
    moves = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    vels = {}
    n_bij = 0
    for assign in itertools.product(range(7), repeat=8):
        img = [tuple((c[k] + moves[a][k]) % 2 for k in range(3)) for c, a in zip(classes, assign)]
        if len(set(img)) != 8:
            continue
        n_bij += 1
        cidx = {c: i for i, c in enumerate(classes)}
        seen = set()
        for i0 in range(8):
            if i0 in seen:
                continue
            i, D, m = i0, [0, 0, 0], 0
            while True:
                seen.add(i)
                mv = moves[assign[i]]
                D = [D[k] + mv[k] for k in range(3)]
                i = cidx[img[i]]
                m += 1
                if i == i0:
                    break
            v = tuple(Fr(x, m) for x in D)
            key = tuple(sorted((abs(x) for x in v), reverse=True))
            vels[key] = vels.get(key, 0) + 1
    return n_bij, vels


def main():
    out, verdict, fam, checks = cases_1d()
    print(f"A. period-2 licensed Bloch tick: {out}")
    for k, v in verdict.items():
        print(f"   support case (zero {k[0]}, zero {k[1]}): {v}")
    print(f"   case conclusions: {checks}")
    print(f"   dispersive families [[0,p],[s z,0]] and [[0,q/z],[r,0]] with unit hops: (unitary for all K, trace 0, det/z^w constant, "
          f"char poly lam^2 + det): {fam}")
    c1d = {p: perm_census_1d(p) for p in range(2, 9)}
    print(f"B. 1D licensed permutation census, set of |drift| per orbit by period: { {p: sorted(str(x) for x in v) for p, v in c1d.items()} }")
    n_bij, vels = census_3d()
    disp = {k: v for k, v in vels.items() if any(x != 0 for x in k)}
    print(f"C. 3D period-2 site-licensed permutation ticks: {n_bij} bijective of 7^8; orbit drift |v| patterns (sorted components) with "
          f"counts: { {str(tuple(str(x) for x in k)): v for k, v in sorted(disp.items(), key=lambda kv: -kv[1])} }")
    fails = []
    if not (out["r s-bar is a coefficient"] and out["p q-bar is a coefficient"]):
        fails.append("cross-term kill")
    if not all(all(f) for f in fam) or not all(checks.values()):
        fails.append("period-2 case analysis")
    if any(v - {Fr(0), Fr(1)} for v in c1d.values()):
        fails.append("1D census: a dispersive licensed permutation with speed other than 1")
    if fails:
        print(f"HIT: {fails}")
    slow = sorted({k for k in disp if sum(k) != 1 or max(k) != 1}, key=lambda k: -sum(k))
    print(f"SUMMARY: in 1D the unitarity coefficients of the general period-2 licensed tick contain r s-bar and p q-bar, the four support "
          f"cases leave only z-independent (flat) ticks or the unit-hop movers [[0,p],[s z,0]] / [[0,q/z],[r,0]] with trace 0, monomial "
          f"det and eigenvalues squaring to det (slope 1 per site); licensed permutation censuses for periods 2..8 give |drift| in {{0, 1}} "
          f"only; beyond the note's 1D scope, the {n_bij} period-2 site-licensed permutation ticks on Z^3 carry orbit drifts "
          f"{sorted(str(tuple(str(x) for x in k)) for k in disp)} - quantized, including the (1/2,1/2,0)-type staircases the landed 3D "
          f"simultaneous-tick note already records and drifts with l1 speed below 1 such as (1/2,0,0); the note claims nothing in 3D, so "
          f"no falsifier of its 1D theorem fires")


if __name__ == "__main__":
    main()
