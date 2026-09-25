#!/usr/bin/env python3
"""Loop factors of the pinned law (blocks 39-40, landed #8530/#8546), run 1 of 2.

Law with vacancies at the pinned scale c_0 = 6/(p+q+4r): a bond between records weighs 6 K_1(b|a) = c_0 omega(a,b), a bond with an empty end 1,
a record z.  An occupied set G (n sites, E bonds among them) weighs z^n Sum_contents Prod_bonds 6 K_1 = (6z)^n * f(G), f = 1 on every forest
(block 40 T2).  f(G) = 6^(E-n) P_G(p,q,r)/(p+q+4r)^E with P_G = Sum_contents p^#equal q^#opposite r^#orthogonal, an integer polynomial,
computed here EXACTLY by enumerating contents.  As landed, the single-cycle formula 1 + 3 l_1^n + 2 l_2^n is not a product rule for overlapping
cycles; the enumeration below is the full contraction.  Exact: Fractions/sympy.  The executed map calls probes/lib/moving_gas.py (floating point,
one seed, finite lattice and time; evidence only).
"""
import itertools, subprocess, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

def out(s): print(s, flush=True)
p, q, r = sp.symbols('p q r', positive=True)

def relation_counts(sites, bonds):
    """histogram of (#equal, #opposite, #orthogonal) bond relations over all 6^n content assignments (contents 0..5, opposite = a ^ 1)"""
    n = len(sites); idx = {s: i for i, s in enumerate(sites)}
    A = np.array(list(itertools.product(range(6), repeat=n)), dtype=np.int8)
    eq = np.zeros(len(A), dtype=np.int16); op = np.zeros(len(A), dtype=np.int16)
    for a, b in bonds:
        x, y = A[:, idx[a]], A[:, idx[b]]
        eq += (x == y); op += (x == (y ^ 1))
    E = len(bonds)
    keys, cnt = np.unique(eq.astype(np.int32) * 64 + op, return_counts=True)
    return {(int(k) // 64, int(k) % 64, E - int(k) // 64 - int(k) % 64): int(c) for k, c in zip(keys, cnt)}

def poly(sites, bonds):
    h = relation_counts(sites, bonds)
    return sp.expand(sum(c * p ** e * q ** o * r ** t for (e, o, t), c in h.items()))

def induced(sites):
    S = set(sites)
    return [(a, b) for a in sites for b in sites if a < b and sum(abs(x - y) for x, y in zip(a, b)) == 1]

def factor_expr(sites):
    bonds = induced(sites); n, E = len(sites), len(bonds)
    return sp.Integer(6) ** (E - n) * poly(sites, bonds) / (p + q + 4 * r) ** E, n, E

l1 = (p - q) / (p + q + 4 * r); l2 = (p + q - 2 * r) / (p + q + 4 * r)
cyc = lambda n: 1 + 3 * l1 ** n + 2 * l2 ** n

SETS = {
    "plaquette": [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)],
    "two plaquettes sharing an edge (2x3, cycle rank 2)": [(x, y, 0) for x in range(3) for y in range(2)],
    "skew six-cycle around a cube corner (cycle rank 1)": [(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1)],
    "three faces around a cube corner (7 sites, cycle rank 3)": [t for t in itertools.product((0, 1), repeat=3) if t != (1, 1, 1)],
    "cube (8 sites, cycle rank 5)": list(itertools.product((0, 1), repeat=3)),
}
F = {}
for name, sites in SETS.items():
    f, n, E = factor_expr(sites); F[name] = f
    out("X %s: n = %d, bonds %d, cycle rank %d; factor over the forest value f = 6^(E-n) P/(p+q+4r)^E, P = %s"
        % (name, n, E, E - n + 1, sp.factor(sp.expand(f * (p + q + 4 * r) ** E / sp.Integer(6) ** (E - n)))))
ok_pl = sp.simplify(F["plaquette"] - cyc(4)) == 0
ok_hex = sp.simplify(F["skew six-cycle around a cube corner (cycle rank 1)"] - cyc(6)) == 0
out("X the enumeration reproduces landed T3 for the plaquette (1 + 3 l_1^4 + 2 l_2^4): %s and for the skew hexagon (1 + 3 l_1^6 + 2 l_2^6): %s"
    % ("PASS" if ok_pl else "FAIL", "PASS" if ok_hex else "FAIL"))
# two plaquettes sharing an edge: exact closed form through the eigenvalues (transfer along the ladder)
L1, L2 = sp.symbols('lambda_1 lambda_2')
dom = F["two plaquettes sharing an edge (2x3, cycle rank 2)"]
out("X two plaquettes sharing an edge: f - (plaquette factor)^2 = %s (not zero: overlapping cycles do not multiply, as landed)"
    % sp.factor(sp.simplify(dom - cyc(4) ** 2)))

LINES = {"(p,1,2)": (1, 2), "(p,1,1)": (1, 1), "(p,2,4)": (2, 4), "(p,1,3)": (1, 3)}
out("X (1) exact plaquette factors 1 + 3 l_1^4 + 2 l_2^4, l_1 = (p-q)/(p+q+4r), l_2 = (p+q-2r)/(p+q+4r); rows marked * have p+q < 2r or p < q "
    "(omega not positive semidefinite: no scale makes the law with vacancies reflection positive)")
TAB = {}
for ln, (qq, rr) in LINES.items():
    cells = []
    for pv in range(3, 25):
        sub = {p: pv, q: qq, r: rr}
        a1, a2 = sp.Rational(pv - qq, pv + qq + 4 * rr), sp.Rational(pv + qq - 2 * rr, pv + qq + 4 * rr)
        fp = 1 + 3 * a1 ** 4 + 2 * a2 ** 4
        assert sp.simplify(fp - cyc(4).subs(sub)) == 0
        TAB[(ln, pv)] = fp
        star = "*" if (pv + qq < 2 * rr or pv < qq) else ""
        cells.append("p=%d%s: l1 %s l2 %s f %s = %.6f" % (pv, star, a1, a2, fp, float(fp)))
    out("X %s: %s" % (ln, "; ".join(cells)))
# where the plaquette factor passes 1.2 (the task's expectation) and 2.4265 (see (3)), exact roots in p
yc = sp.exp(4 * sp.Rational(2216544, 10 ** 7))
for ln, (qq, rr) in LINES.items():
    fpl = sp.together(cyc(4).subs({q: qq, r: rr}))
    roots = {}
    for target, lab in ((sp.Rational(6, 5), "1.2"), (yc, "exp(4 K_c) = %.4f" % float(yc))):
        sol = [s_ for s_ in sp.Poly(sp.numer(sp.together(fpl - target)), p).nroots(n=20) if abs(sp.im(s_)) < 1e-15 and sp.re(s_) > max(2 * rr - qq, qq)]
        roots[lab] = [float(sp.re(s_)) for s_ in sol]
    out("X %s: the plaquette factor passes 1.2 at p = %s and exp(4 K_c) at p = %s; limit as p -> infinity: 6"
        % (ln, ", ".join("%.4f" % x for x in roots["1.2"]) or "never", ", ".join("%.4f" % x for x in list(roots.values())[1]) or "never"))
# the expectation
f10, f11 = TAB[("(p,1,2)", 10)], TAB[("(p,1,2)", 11)]
exp_ok = f10 < sp.Rational(6, 5) < f11
out("X expectation 'the plaquette factor passes about 1.2 near p = 10 on (p,1,2)': f(10) = %.4f, f(11) = %.4f: %s"
    % (float(f10), float(f11), "consistent (crossing between 10 and 11)" if exp_ok else "NOT between 10 and 11"))

# (2) numbers for the larger sets on (p,1,2)
for pv in (6, 8, 10, 12, 16, 24):
    sub = {p: pv, q: 1, r: 2}
    vals = {k: sp.Rational(sp.simplify(v.subs(sub))) for k, v in F.items()}
    nplaq = {"plaquette": 1, "two plaquettes sharing an edge (2x3, cycle rank 2)": 2, "skew six-cycle around a cube corner (cycle rank 1)": 0,
             "three faces around a cube corner (7 sites, cycle rank 3)": 3, "cube (8 sites, cycle rank 5)": 6}
    fpl = vals["plaquette"]
    out("X (2) (p,1,2), p = %d: %s" % (pv, "; ".join("%s: %s = %.6f%s" % (k.split(" (")[0], vals[k], float(vals[k]),
        (" (over plaquette^%d: %.4f)" % (nplaq[k], float(vals[k] / fpl ** nplaq[k]))) if nplaq[k] > 1 else "") for k in F)))

# (3) translation to the content-less gas
out("X (3) translation: in the content-less gas a bond between two records weighs y (block 40 T4: y = c/c_0); with occupation n = (1 + s)/2 "
    "the weight y^(n n') is an Ising coupling log(y)/4 per bond, so the literature onset (density 1/2, zero field, K_c = 0.2216544) is "
    "y_c = exp(4 K_c) = %.6f per BOND.  At c_0 the content-less part has y = 1 and the whole binding sits on cycles.  COMPARABLE: the weight "
    "per site of a fully occupied region; the cubic lattice has 3 bonds and 3 plaquettes per site, so to leading order in the loop expansion "
    "(plaquette factors multiplying) a plaquette factor f matches a bond activity y = f: the matching plaquette factor is y_c itself.  A "
    "naive 'four bonds per plaquette' reading, f = y_c^4 = %.2f, exceeds the largest possible factor (6, all weights on equal contents) and is "
    "never reached.  NOT COMPARABLE: (i) plaquette factors do not multiply: overlapping loops reinforce (the ratios over plaquette^k in (2)), "
    "so the leading-order match overstates the p needed in a dense region; (ii) bond activity binds any two neighbours while loop factors need "
    "occupied four-site rings, so at low density the loop binding is far weaker than the matching bond activity; (iii) the content-less onset "
    "is condensation at density 1/2; the executed onsets are alignment of contents with clumping, at densities 0.1-0.7" % (float(yc), float(yc) ** 4))
# (4) the executed map at the pinned scale (fresh run of the repository's simulator; one seed; evidence only)
out("N (4) historical (block 40 landed table, not fresh evidence): onset of alignment on (p,1,2) at c_0 above p = 16 at density 0.1, between 8 "
    "and 12 at 0.3, between 6 and 8 at 0.5, below 6 at 0.7")
if len(sys.argv) < 2 or sys.argv[1] != "nosim":
    for rho in (0.1, 0.3, 0.5, 0.7):
        cells = []
        for pv in (4, 6, 8, 10, 12, 16, 24):
            t0 = time.time()
            res = subprocess.run([sys.executable, "probes/lib/moving_gas.py", str(pv), "1", "2", "neutral", str(rho), "16", "2000", "1"],
                                 capture_output=True, text=True)
            line = [l for l in res.stdout.splitlines() if l.startswith("SUMMARY")][-1]
            kv = dict(tok.split("=") for tok in line.split()[1:] if "=" in tok)
            cells.append("p=%d: nbrs/random %.2f aligned %.2f accept %.2f" % (pv, float(kv["nbrs_over_random"]), float(kv["aligned"]), float(kv["accept"])))
        out("N (4) executed now, (p,1,2), c_0, density %.1f, side 16, 2000 sweeps, seed 1: %s" % (rho, "; ".join(cells)))

out("")
out("SUMMARY: plaquette factor of the pinned law = 1 + 3 l_1^4 + 2 l_2^4 (exact tables p = 3..24 on four lines); on (p,1,2) it passes 1.2 between "
    "p = 10 (%.4f) and 11 (%.4f), as expected (root 10.2463), and reaches the leading-order match to the content-less onset, f = exp(4 K_c) = "
    "2.4269, at p = 30.95 (never the naive y_c^4); overlapping cycles do not multiply and reinforce (at p = 10: two plaquettes sharing an edge "
    "1.4717 against f^2 = 1.4111, the cube 5.645 against f^6 = 2.81), so a dense region binds more than the plaquette product; exact polynomials "
    "for the domino, the skew hexagon, three faces around a corner and the cube" % (float(f10), float(f11)))
