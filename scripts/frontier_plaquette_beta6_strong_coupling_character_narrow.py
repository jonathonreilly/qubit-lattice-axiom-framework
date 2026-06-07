#!/usr/bin/env python3
"""Narrow runner for `PLAQUETTE_BETA6_STRONG_COUPLING_CHARACTER_NARROW_THEOREM_NOTE_2026-05-27`.

Verifies the standalone algebraic facts about the supplied strong-coupling
character coefficient packet evaluated at the supplied point u = 1/3. In the
standard convention u = beta/18 at beta = 6, but this runner does not derive
that convention from the framework. The conclusions are stated in layers:

  (C1) Supplied leading-order single-plaquette character context: at small beta,
       the strong-coupling expansion begins
            <P>(u) = u + O(u^4),
       with u(beta) := beta/18 the leading-order single-link fundamental
       character coefficient for SU(3) Wilson gauge action. This is context,
       not a retained conclusion of this runner.

  (T2) Truncated bounded series (Münster 1981, Drouffe-Zuber 1983
       coefficient table, cited as external coefficient providers only):
            <P>(u) = u + 4 u^4 + 24 u^6 - 24 u^7 + 100 u^8 + O(u^9).
       Substituting u = 1/3 (the leading-order value at beta = 6)
       produces the truncated SC numerical estimate.

  (T3) Padé[N/M] analytic-continuation table from the truncated series:
       the [3/3] Padé approximant lands at the closed-form rational
       value 3/5 = 0.6 exactly, in BOTH the plain u-expansion and under
       the conformal map z = u/(1 + 4 u) (i.e. u = z/(1-4 z)). The
       [4/4] Padé approximant lands at the closed-form 0.3974... and is
       NOT a stable continuation in either variable because the
       alternating sign at u^7 destabilizes it.

  (T4) Sensitivity audit: the Padé[3/3] value uses only the SC coefficients
       through u^6 (i.e. c_1, c_4, c_6); it is independent of c_7, c_8 and
       any higher-order coefficient. Perturbing c_6 destroys the close
       agreement with the MC value 0.5934 (the value 3/5 is rigid in c_6 = 24).

  (T5) Borel-Pade obstruction witness: building the Borel transform
       b_n := c_n / n! and applying Padé[3/3] to the Borel series followed
       by formal Borel-Laplace summation at u = 1/3 exposes a positive
       real pole on the Laplace contour. This proves only that this
       ordinary Padé[3/3] Borel route does not provide the same
       analytic continuation as direct Padé[3/3], not a universal Borel
       non-summability theorem.

The runner does NOT identify u = 1/3 with the framework's beta = 6 plaquette
value. It treats the coefficient table and u = 1/3 evaluation point as supplied
inputs for a pure Padé-algebra certificate. The 0.5934 Monte Carlo value enters
only as a comparison number to characterise the Padé[3/3] residual gap (-1.1%);
this is not a closure of <P>(beta=6) at the level of a retained-grade theorem.
"""
from __future__ import annotations

from pathlib import Path
import math
import sys

try:
    import sympy as sp
    from sympy import Rational, Symbol, sqrt, symbols, log, expand, simplify, Poly, factorial
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}  ({detail})")


def section(title):
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


# ============================================================================
section("Pattern A narrow theorem: SU(3) Wilson plaquette strong-coupling Pade[3/3]")
# ============================================================================

beta_sym = Symbol('beta', positive=True)
u = Symbol('u', positive=True)

# Strong-coupling character expansion coefficients for SU(3) Wilson plaquette,
# cited from Munster (1981) Nucl.Phys. B190 [FS3] 439 Table 1 and
# Drouffe-Zuber (1983) Phys.Rep. 102, 1 Section 4.5 Table 13 specialised to
# D=4 hypercubic, fundamental-rep character expansion.
#
# These reference values are coefficient PROVIDERS, not load-bearing axioms.
# The theorem-grade content of this note is the algebraic consequence of these
# coefficients under Pade[N/M] continuation, not a derivation of the
# coefficients themselves.
SC_COEFFS_PUBLISHED = {
    1: Rational(1),
    4: Rational(4),
    6: Rational(24),
    7: Rational(-24),
    8: Rational(100),
}
SUPPLIED_EVALUATION_POINT = Rational(1, 3)
MC_REFERENCE_SUPPLIED = Rational(5934, 10000)

# Source-boundary manifest: these are finite supplied inputs.  The runner proves
# only rational consequences of this tuple; it does not certify the coefficient
# table, beta-to-u convention, or MC comparison as framework-derived facts.
SUPPLIED_INPUT_PACKET = {
    "coefficients": SC_COEFFS_PUBLISHED,
    "evaluation_u": SUPPLIED_EVALUATION_POINT,
    "mc_reference": MC_REFERENCE_SUPPLIED,
}


def build_series_in_u(coeffs):
    """Build the symbolic SC series <P>(u) up to the maximum order in coeffs."""
    max_order = max(coeffs.keys())
    return sum(c * u**n for n, c in coeffs.items()), max_order


def coefficient_list(coeffs, max_n):
    """Return [a_0, a_1, ..., a_{max_n}] from a {n: a_n} dict."""
    return [coeffs.get(n, Rational(0)) for n in range(max_n + 1)]


def pade_NM(a, N, M):
    """Pade[N/M] approximant. Returns (P_coeffs, Q_coeffs) with Q_0=1.

    Solves the linear system
      sum_{j=0..M} b_j a_{N+i-j} = 0   for i = 1..M  with b_0 = 1.
    Then
      P_i = sum_{j=0..min(i,M)} b_j a_{i-j}.
    """
    assert len(a) >= N + M + 1, f"need >= {N+M+1} coeffs, got {len(a)}"
    if M == 0:
        return list(a[:N+1]), [Rational(1)]
    rows, rhs = [], []
    for i in range(M):
        row = []
        for j in range(1, M + 1):
            idx = N + i + 1 - j
            row.append(a[idx] if 0 <= idx < len(a) else Rational(0))
        rows.append(row)
        rhs.append(-a[N + i + 1])
    A_sys = sp.Matrix(rows)
    b_vec = sp.Matrix(rhs)
    sol = A_sys.solve(b_vec)
    Q = [Rational(1)] + [sol[j] for j in range(M)]
    P_out = []
    for i in range(N + 1):
        s = Rational(0)
        for j in range(min(i, M) + 1):
            s += Q[j] * a[i - j]
        P_out.append(s)
    return P_out, Q


# ----------------------------------------------------------------------------
section("Part 0: source-boundary manifest")
# ----------------------------------------------------------------------------
check("coefficient packet is an explicit finite supplied tuple",
      SUPPLIED_INPUT_PACKET["coefficients"] == {
          1: Rational(1),
          4: Rational(4),
          6: Rational(24),
          7: Rational(-24),
          8: Rational(100),
      },
      detail=f"orders={sorted(SUPPLIED_INPUT_PACKET['coefficients'])}")
check("beta=6 evaluation point enters only as supplied rational u=1/3",
      SUPPLIED_INPUT_PACKET["evaluation_u"] == Rational(1, 3),
      detail=f"u_eval={SUPPLIED_INPUT_PACKET['evaluation_u']}")
check("MC comparator is an explicit non-theorem comparison value",
      SUPPLIED_INPUT_PACKET["mc_reference"] == Rational(5934, 10000),
      detail=f"mc={float(SUPPLIED_INPUT_PACKET['mc_reference']):.4f}")

# ----------------------------------------------------------------------------
section("Part 1 (C1): supplied leading-order strong-coupling context")
# ----------------------------------------------------------------------------
# At small beta, <P>(beta) = beta/18 + O(beta^4) for SU(3) Wilson plaquette.
# The leading O(beta) coefficient equals 1 / (2 N^2) with N=3.

leading_coeff = Rational(1) / (2 * 3**2)
check("leading <P>/beta coefficient equals 1/(2 N^2) at N=3",
      leading_coeff == Rational(1, 18),
      detail=f"1/(2*3^2) = {leading_coeff}, expected 1/18")

# Substitute u = beta/18:
u_leading = beta_sym / 18
check("supplied leading-order convention gives u(beta)=beta/18 and beta=6 -> u=1/3",
      u_leading.subs(beta_sym, 6) == Rational(1, 3),
      detail=f"u(6) = {u_leading.subs(beta_sym, 6)}")

# ----------------------------------------------------------------------------
section("Part 2 (T2): truncated bounded series")
# ----------------------------------------------------------------------------
P_u_full, max_order = build_series_in_u(SC_COEFFS_PUBLISHED)
print(f"  <P>(u) (truncated at u^{max_order}) = {sp.expand(P_u_full)}")

# Cross-check: substituting u = 1/3 gives a definite rational truncated value.
u_third = SUPPLIED_EVALUATION_POINT
P_trunc_third = P_u_full.subs(u, u_third)
check("truncated series <P>(u=1/3) is a definite rational number",
      P_trunc_third.is_rational,
      detail=f"<P>(u=1/3) = {P_trunc_third} = {float(P_trunc_third):.6f}")

# Bound on the MC comparison gap (NOT a closure claim, just a residual measurement):
mc_val = MC_REFERENCE_SUPPLIED  # 0.5934 as an exact rational comparison number
residual_trunc = float(mc_val - P_trunc_third)
check("truncated SC O(u^8) series leaves a sizeable residual to MC 0.5934 "
      "(NOT a closure)",
      residual_trunc > 0.15,
      detail=f"residual = {residual_trunc:.4f} ({100*residual_trunc/0.5934:.1f}%)")

# ----------------------------------------------------------------------------
section("Part 3 (T3): Pade[N/M] analytic-continuation table")
# ----------------------------------------------------------------------------
a_list = coefficient_list(SC_COEFFS_PUBLISHED, max_order)
print(f"  a_n series: {[(n, c) for n, c in enumerate(a_list)]}")


def eval_pade(a, N, M, u_val):
    """Return (rational value, P-polynomial, Q-polynomial) of Pade[N/M] at u_val."""
    P_c, Q_c = pade_NM(a, N, M)
    P_poly = sum(c * u**i for i, c in enumerate(P_c))
    Q_poly = sum(c * u**i for i, c in enumerate(Q_c))
    Pv = P_poly.subs(u, u_val)
    Qv = Q_poly.subs(u, u_val)
    return Pv / Qv, P_poly, Q_poly


# [3/3] Pade in u:
val33, P33, Q33 = eval_pade(a_list, 3, 3, u_third)
print(f"  Pade[3/3] in u:  P(u) = {sp.expand(P33)}")
print(f"                   Q(u) = {sp.expand(Q33)}")
print(f"                   value at u=1/3 = {val33} = {float(val33):.6f}")

check("Pade[3/3] at u=1/3 equals exactly 3/5",
      val33 == Rational(3, 5),
      detail=f"Pade[3/3](1/3) = {val33}")
match_residual = sp.expand(P_u_full * Q33 - P33)
check("Pade[3/3] matching equations vanish through order u^6",
      all(sp.expand(match_residual).coeff(u, n) == 0 for n in range(7)),
      detail="series*Q-P = O(u^7)")
check("Pade[3/3] denominator is nonzero at supplied u=1/3",
      Q33.subs(u, u_third) != 0,
      detail=f"Q(1/3)={Q33.subs(u, u_third)}")

# Residual gap to MC value 0.5934:
gap_33 = float(mc_val - val33)
check("Pade[3/3] residual to MC value 0.5934 is small (NOT zero -- no closure)",
      abs(gap_33) < 0.02 and gap_33 < 0,
      detail=f"gap = {gap_33:+.4f} ({100*gap_33/0.5934:+.2f}%)")
check("MC comparator is not consumed as a theorem equality",
      mc_val != val33,
      detail=f"mc={mc_val}, Pade[3/3]={val33}")

# Pade[4/4]:
val44, P44, Q44 = eval_pade(a_list, 4, 4, u_third)
check("Pade[4/4] at u=1/3 is rational",
      val44.is_rational,
      detail=f"Pade[4/4](1/3) = {val44} = {float(val44):.6f}")
gap_44 = float(mc_val - val44)
check("Pade[4/4] does NOT improve over Pade[3/3] (alternation destabilizes)",
      abs(gap_44) > abs(gap_33),
      detail=f"|gap_44|={abs(gap_44):.4f} > |gap_33|={abs(gap_33):.4f}")

# Pade[1/1]:
val11, _, _ = eval_pade(a_list, 1, 1, u_third)
check("Pade[1/1] at u=1/3 = 1/3 (just the leading-order linear value)",
      val11 == Rational(1, 3),
      detail=f"Pade[1/1](1/3) = {val11}")

# ----------------------------------------------------------------------------
section("Part 4 (T4): sensitivity audit on Pade[3/3]")
# ----------------------------------------------------------------------------
# Pade[3/3] uses only coefficients up to u^(3+3)=u^6.
# Verify independence from c_7 and c_8:
for c7_alt in [Rational(0), Rational(-24), Rational(100), Rational(-1000)]:
    for c8_alt in [Rational(0), Rational(100), Rational(-1000), Rational(10000)]:
        coeffs_alt = dict(SC_COEFFS_PUBLISHED)
        coeffs_alt[7] = c7_alt
        coeffs_alt[8] = c8_alt
        a_alt = coefficient_list(coeffs_alt, 8)
        v, _, _ = eval_pade(a_alt, 3, 3, u_third)
        if v != Rational(3, 5):
            check(f"Pade[3/3] invariance under (c_7,c_8)=({c7_alt},{c8_alt})",
                  False, detail=f"value changed to {v}")
            break
    else:
        continue
    break
else:
    check("Pade[3/3](u=1/3) is invariant under arbitrary changes of (c_7, c_8)",
          True, detail="checked 16 (c_7,c_8) perturbation pairs")

# Verify dependence on c_6 (rigidity audit):
for c6_alt, expected_pade_three in [
    (Rational(24), Rational(3, 5)),    # baseline (Munster 1981)
    (Rational(12), Rational(3, 7)),    # half-cube-corner counterfactual
    (Rational(0), Rational(9, 23)),    # cube-corner removed: distinct Pade[3/3] value
]:
    coeffs_alt = dict(SC_COEFFS_PUBLISHED)
    coeffs_alt[6] = c6_alt
    a_alt = coefficient_list(coeffs_alt, 8)
    v, _, _ = eval_pade(a_alt, 3, 3, u_third)
    check(f"Pade[3/3](u=1/3) with c_6={c6_alt} equals {expected_pade_three}",
          v == expected_pade_three,
          detail=f"got {v} = {float(v):.6f}")

# ----------------------------------------------------------------------------
section("Part 5 (T3 cont.): conformal-mapping cross-check")
# ----------------------------------------------------------------------------
# u -> z := u/(1 + alpha*u), i.e. u = z/(1 - alpha*z).
# Substitute into <P>(u) and re-expand in z, then build Pade[3/3] in z and
# evaluate at z(u=1/3) = 1/(3 + alpha).
z = Symbol('z', positive=True)
alpha = 4  # nominal conformal parameter; the result is invariant for moderate alpha
u_of_z = z / (1 - alpha * z)
P_in_z = P_u_full.subs(u, u_of_z)
P_z_series = sp.series(P_in_z, z, 0, max_order + 1).removeO()
P_z_poly = sp.Poly(P_z_series, z)
coeffs_z_list = list(reversed(P_z_poly.all_coeffs()))
while len(coeffs_z_list) < max_order + 1:
    coeffs_z_list.append(Rational(0))

# Pade[3/3] in z, evaluated at z(u=1/3) = 1/7:
z_val = Rational(1, 3) / (1 + alpha * Rational(1, 3))
check(f"conformal z(u=1/3, alpha={alpha}) = 1/(3+alpha) = 1/{3+alpha}",
      z_val == Rational(1, 3 + alpha),
      detail=f"z = {z_val}")


def eval_pade_in(var_sym, a, N, M, val):
    P_c, Q_c = pade_NM(a, N, M)
    P_poly = sum(c * var_sym**i for i, c in enumerate(P_c))
    Q_poly = sum(c * var_sym**i for i, c in enumerate(Q_c))
    return (P_poly.subs(var_sym, val) / Q_poly.subs(var_sym, val))


val_z33 = eval_pade_in(z, coeffs_z_list, 3, 3, z_val)
check("Pade[3/3] in conformally-mapped z (alpha=4) at z=1/7 equals 3/5",
      val_z33 == Rational(3, 5),
      detail=f"Pade[3/3]_z(z=1/7) = {val_z33}")

# Also alpha=2:
alpha2 = 2
u_of_z2 = z / (1 - alpha2 * z)
P_in_z2 = P_u_full.subs(u, u_of_z2)
P_z2_series = sp.series(P_in_z2, z, 0, max_order + 1).removeO()
P_z2_poly = sp.Poly(P_z2_series, z)
coeffs_z2_list = list(reversed(P_z2_poly.all_coeffs()))
while len(coeffs_z2_list) < max_order + 1:
    coeffs_z2_list.append(Rational(0))
z_val2 = Rational(1, 3) / (1 + alpha2 * Rational(1, 3))  # = 1/5
val_z33_alpha2 = eval_pade_in(z, coeffs_z2_list, 3, 3, z_val2)
check("Pade[3/3] in conformally-mapped z (alpha=2) at z=1/5 equals 3/5",
      val_z33_alpha2 == Rational(3, 5),
      detail=f"Pade[3/3]_z(z=1/5, alpha=2) = {val_z33_alpha2}")

# ----------------------------------------------------------------------------
section("Part 6 (T5): Borel-Pade obstruction witness")
# ----------------------------------------------------------------------------
# Borel transform B(t) := sum (c_n / n!) t^n. Apply Pade[3/3] to the Borel
# series and check whether the ordinary Borel-Laplace contour is unobstructed.
b_coeffs = [SC_COEFFS_PUBLISHED.get(n, Rational(0)) / factorial(n) for n in range(max_order + 1)]
print(f"  Borel-transformed coefficients b_n: "
      f"{[(n, c) for n, c in enumerate(b_coeffs) if c != 0]}")

t = Symbol('t', positive=True)
P_b_c, Q_b_c = pade_NM(b_coeffs, 3, 3)
P_b_poly = sum(c * t**i for i, c in enumerate(P_b_c))
Q_b_poly = sum(c * t**i for i, c in enumerate(Q_b_c))
roots = [complex(root) for root in sp.nroots(Q_b_poly)]
positive_roots = [root.real for root in roots if abs(root.imag) < 1e-10 and root.real > 0]
u_float = 1.0 / 3.0
laplace_poles = [root / u_float for root in positive_roots]
print(f"  Borel-Pade[3/3] denominator Q(t) = {sp.factor(Q_b_poly)}")
print(f"  positive Borel-plane roots: {[f'{root:.6f}' for root in positive_roots]}")
print(f"  corresponding Laplace-contour poles at u=1/3: {[f'{pole:.6f}' for pole in laplace_poles]}")
check("Borel-Pade[3/3] has a positive real pole in the Borel plane",
      bool(positive_roots),
      detail=f"roots={positive_roots}")
check("ordinary Borel-Laplace integral at u=1/3 is obstructed by a positive-contour pole",
      any(0.0 < pole < 80.0 for pole in laplace_poles),
      detail=f"t_poles={laplace_poles}")

# ----------------------------------------------------------------------------
section("Part 7: comparison summary (NOT a closure)")
# ----------------------------------------------------------------------------
# This part records the numerical layout. None of these are retained-grade
# closure claims; they describe the algebraic position of the SC route at u=1/3.
mc_float = 0.5934
trunc_O8 = float(P_trunc_third)
pade33_float = float(val33)
pade44_float = float(val44)
print(f"  Truncated SC series O(u^8) at u=1/3   : {trunc_O8:.6f}   gap = {mc_float-trunc_O8:+.4f} ({100*(mc_float-trunc_O8)/mc_float:+.2f}%)")
print(f"  Pade[3/3] in u                        : {pade33_float:.6f}   gap = {mc_float-pade33_float:+.4f} ({100*(mc_float-pade33_float)/mc_float:+.2f}%)")
print(f"  Pade[3/3] in conformal z (alpha=4)    : {float(val_z33):.6f}   gap = {mc_float-float(val_z33):+.4f}")
print(f"  Pade[3/3] in conformal z (alpha=2)    : {float(val_z33_alpha2):.6f}   gap = {mc_float-float(val_z33_alpha2):+.4f}")
print(f"  Pade[4/4] in u                        : {pade44_float:.6f}   gap = {mc_float-pade44_float:+.4f}")
print(f"  Borel-Pade[3/3]+Borel-Laplace         : obstructed by positive-contour pole")
print(f"  MC reference value                    : {mc_float:.6f}")

# Sanity: the closeness of Pade[3/3] = 3/5 to MC 0.5934 is real but conditional:
#   - on the c_6 = 24 coefficient as published in Munster (1981),
#   - on u = 1/3 being the correct leading-order substitution at beta = 6.
# The note explicitly does NOT claim closure.
check("Pade[3/3] in u and in z (alpha=4) agree exactly",
      val33 == val_z33,
      detail=f"u-form = {val33}, z-form = {val_z33}")
check("Pade[3/3] in u and in z (alpha=2) agree exactly",
      val33 == val_z33_alpha2,
      detail=f"u-form = {val33}, z-form_alpha2 = {val_z33_alpha2}")

# ----------------------------------------------------------------------------
section(f"TOTAL: PASS={PASS} FAIL={FAIL}")
# ----------------------------------------------------------------------------

if FAIL > 0:
    sys.exit(1)
sys.exit(0)
