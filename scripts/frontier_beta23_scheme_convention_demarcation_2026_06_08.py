#!/usr/bin/env python3
"""Exact formal beta-coefficient reparametrization with supplied QCD polynomials.
Assume a same-theory, mass-independent, scale-independent analytic map with unit
leading coefficient. Nonzero b0 permits the fixed-c1 triangular solve (negative
b0 also works). At b0=0 only the tested c2/b2 and c3/b3 freedoms disappear;
other freedoms and special targets are not excluded. No physical HK matching,
framework running closure or sufficiency of two integrals is established.
"""

from __future__ import annotations

AUDIT_INPUT_PATHS = ["docs/BETA23_SCHEME_CONVENTION_DEMARCATION_FIXED_SPACING_BOUNDED_THEOREM_NOTE_2026-06-08.md", "docs/CLOSURE_C_L1_HK_MSBAR_3L_CONVERSION_NOTE_2026-05-10_cL1a.md"]
AUDIT_TIMEOUT_SECONDS = 120

import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


a = sp.symbols("alpha")
apr = sp.symbols("aprime")
c1, c2, c3 = sp.symbols("c1 c2 c3")
b0, b1, b2, b3 = sp.symbols("b0 b1 b2 b3")

# ===========================================================================
# Part 0.  The transformed coefficients, derived exactly (order-by-order inversion).
# ===========================================================================
print("=" * 78)
print("Part 0  Derive b_n' under a' = a + c1 a^2 + c2 a^3 + c3 a^4 (exact, symbolic)")
print("=" * 78)

beta = -(a ** 2) * (b0 + b1 * a + b2 * a ** 2 + b3 * a ** 3)
ap = a + c1 * a ** 2 + c2 * a ** 3 + c3 * a ** 4

# invert a(a') by ansatz, order by order (exact)
d1, d2, d3 = sp.symbols("d1 d2 d3")
ansatz = apr + d1 * apr ** 2 + d2 * apr ** 3 + d3 * apr ** 4
comp = sp.expand(ap.subs(a, ansatz)) - apr
inv = sp.solve([comp.coeff(apr, 2), comp.coeff(apr, 3), comp.coeff(apr, 4)],
               [d1, d2, d3], dict=True)[0]
a_of_ap = ansatz.subs(inv)
check("inverse series solved exactly: a = a' - c1 a'^2 + (2c1^2 - c2) a'^3 + ...",
      sp.expand(a_of_ap.coeff(apr, 2) + c1) == 0
      and sp.expand(a_of_ap.coeff(apr, 3) - (2 * c1 ** 2 - c2)) == 0)

beta_p = sp.expand((sp.diff(ap, a) * beta).subs(a, a_of_ap))
bp = [sp.expand(-beta_p.coeff(apr, k)) for k in (2, 3, 4, 5)]   # b0', b1', b2', b3'

# ===========================================================================
# Part 1.  (T1) UNIVERSALITY DERIVED: b0' = b0 and b1' = b1 identically.
# ===========================================================================
print("=" * 78)
print("Part 1  (T1) b0' == b0 and b1' == b1 IDENTICALLY (universality derived, not asserted)")
print("=" * 78)

check("b0' - b0 == 0 identically (no c-dependence at all)", sp.expand(bp[0] - b0) == 0)
check("b1' - b1 == 0 identically (no c-dependence at all)", sp.expand(bp[1] - b1) == 0)

# ===========================================================================
# Part 2.  (T2) b2, b3 are PURE CONVENTION: exact transformation laws + 't Hooft solve.
# ===========================================================================
print("=" * 78)
print("Part 2  (T2) b2', b3' transformation laws + 't Hooft scheme (b2'=b3'=0) exact solve")
print("=" * 78)

law2 = b2 - b1 * c1 + b0 * (c2 - c1 ** 2)
law3 = b3 - 2 * b2 * c1 + b1 * c1 ** 2 + b0 * (2 * c3 - 6 * c1 * c2 + 4 * c1 ** 3)
check("b2' = b2 - b1 c1 + b0 (c2 - c1^2) (exact)", sp.expand(bp[2] - law2) == 0,
      f"b2' = {sp.expand(bp[2])}")
check("b3' = b3 - 2 b2 c1 + b1 c1^2 + b0 (2 c3 - 6 c1 c2 + 4 c1^3) (exact)",
      sp.expand(bp[3] - law3) == 0)

# triangular solve: for ANY c1, set b2' = b3' = 0 by linear choice of c2, c3
c2_sol = sp.solve(sp.Eq(bp[2], 0), c2)[0]
c3_sol = sp.solve(sp.Eq(bp[3].subs(c2, c2_sol), 0), c3)[0]
check("'t Hooft scheme EXISTS for every c1: c2, c3 solve LINEARLY (b2'=b3'=0)",
      sp.simplify(bp[2].subs(c2, c2_sol)) == 0
      and sp.simplify(bp[3].subs({c2: c2_sol, c3: c3_sol})) == 0,
      f"c2 = {sp.simplify(c2_sol)}")
# and (b2', b3') can be set to ANY prescribed pair (t2, t3), not just zero:
t2, t3 = sp.symbols("t2 t3")
c2_any = sp.solve(sp.Eq(bp[2], t2), c2)[0]
c3_any = sp.solve(sp.Eq(bp[3].subs(c2, c2_any), t3), c3)[0]
check("(b2', b3') reach ANY prescribed (t2, t3) — the pair carries NO invariant content",
      sp.simplify(bp[2].subs(c2, c2_any) - t2) == 0
      and sp.simplify(bp[3].subs({c2: c2_any, c3: c3_any}) - t3) == 0)

# ===========================================================================
# Part 3.  (T3) Nonzero b0 permits the fixed-c1 triangular solve.
# ===========================================================================
print("=" * 78)
print("Part 3  (T3) solvability denominators are exactly b0 and 2 b0 (nonzero b0; no sign requirement)")
print("=" * 78)

den2 = sp.denom(sp.together(c2_sol))
den3 = sp.denom(sp.together(c3_sol))
check("denominator of the c2 solve is b0; of the c3 solve is 2 b0",
      sp.simplify(den2 - b0) == 0 and sp.simplify(den3 - 2 * b0) == 0,
      f"den(c2)={den2}, den(c3)={den3}")
# degenerate control: at b0 = 0 b2' loses c2 dependence and b3' loses c3 dependence
check("CONTROL: at b0 = 0 the c2-dependence of b2' vanishes (freedom lost; prescription "
      "unreachable unless b2' = b2 - b1 c1 happens to hit the target)",
      sp.expand(sp.diff(bp[2].subs(b0, 0), c2)) == 0
      and sp.expand(sp.diff(bp[3].subs(b0, 0), c3)) == 0)

# ===========================================================================
# Part 4.  (T4) Supplied QCD coefficient polynomials in the formal invariant positions.
# ===========================================================================
print("=" * 78)
print("Part 4  (T4) inherited b0 = 7, b1 = 26 (N_f=6, bounded QCD context) = invariant set")
print("=" * 78)

CA, CF, TF, Nf = sp.Integer(3), sp.Rational(4, 3), sp.Rational(1, 2), sp.Integer(6)
b0_fw = (11 * CA - 4 * TF * Nf) / 3
b1_fw = sp.Rational(34, 3) * CA ** 2 - 4 * CF * TF * Nf - sp.Rational(20, 3) * CA * TF * Nf
check("b0 = (11 C_A - 4 T_F N_f)/3 = 7 exactly (supplied QCD polynomial, N_f = 6)",
      b0_fw == 7, f"b0 = {b0_fw}")
check("b1 = (34/3)C_A^2 - 4 C_F T_F N_f - (20/3) C_A T_F N_f = 26 exactly",
      b1_fw == 26, f"b1 = {b1_fw}")
check("AF: b0 = 7 > 0 -> the inherited QCD-running context supplies the "
      "solvability condition (T3) for its scheme freedom",
      b0_fw > 0)
# exact rational 't Hooft data at the framework point (c1 = 0 representative):
c2_fw = c2_sol.subs({c1: 0, b0: 7, b1: 26})
c3_fw = c3_sol.subs({c1: 0, b0: 7, b1: 26})
check("at (b0,b1) = (7,26), c1 = 0: c2 = -b2/7 and c3 = -b3/14 — exact rationals in "
      "(b2, b3); the scheme reaching (b2',b3') = (0,0) is explicit",
      sp.simplify(c2_fw + b2 / 7) == 0 and sp.simplify(c3_fw + b3 / 14) == 0,
      f"c2 = {sp.simplify(c2_fw)}, c3 = {sp.simplify(c3_fw)}")

# ===========================================================================
# Part 5.  (T5) Teeth: b1 not adjustable; leading rescaling is a DIFFERENT layer.
# ===========================================================================
print("=" * 78)
print("Part 5  (T5) teeth: the demarcation line cannot be moved; rescaling is not a scheme")
print("=" * 78)

check("b1' has ZERO dependence on (c1, c2, c3): d(b1')/dc_i == 0 for all i "
      "(the demarcation sits exactly at n >= 2, not movable)",
      all(sp.expand(sp.diff(bp[1], c)) == 0 for c in (c1, c2, c3)))
# leading rescaling a' = lambda a changes b0 -> b0/lambda: that is the coupling
# NORMALIZATION (g_bare convention) layer, excluded from scheme transformations here.
lam = sp.symbols("lam", positive=True)
beta_resc = sp.expand((lam * beta).subs(a, apr / lam))
b0_resc = sp.expand(-beta_resc.coeff(apr, 2))
check("a leading rescaling a' = lam*a sends b0 -> b0/lam (lam != 1 changes b0): that "
      "freedom is the separate g_bare NORMALIZATION convention, NOT a scheme map "
      "(normalization-preserving maps fix the leading coefficient = 1)",
      sp.simplify(b0_resc - b0 / lam) == 0)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: same-theory scale-independent formal maps with unit leading coefficient.")
print("b0,b1 are invariant; the fixed-c1 solve for b2,b3 works for nonzero b0, of either sign.")
print("Supplied QCD polynomials give (7,26); they do not prove framework running or matching.")
print("Physical HK coupling, continuum identification, normalization, vertices and fermion matching remain open.")
if FAIL:
    raise SystemExit(1)
