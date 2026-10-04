
# Explicit bounded execution cap; scientific content is unchanged by this metadata.
AUDIT_TIMEOUT_SEC = 120
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp
# Sakharov induced gravity from W = log|det D|: the metric effective action's leading terms are the
# heat-kernel (Seeley-DeWitt) coefficients of the Dirac operator D. a_0 -> cosmological const (~Lambda^4),
# a_1 -> Einstein-Hilbert (~Lambda^2 R) => 1/(16 pi G) ~ Lambda^2 => G ~ 1/Lambda^2 ~ a^2 (lattice scale).
# Gilkey: for P = -(nabla^2 + E), a_k(x) = (4pi)^{-d/2} * b_k ; b_0 = tr(I), b_1 = (1/6) tr(6E + R*I).
# Dirac (Lichnerowicz): D^2 = -nabla^2 + R/4  => E = -R/4 ; spinor bundle dim in d=4 is 4.
d=4; spin_dim=4
print("=== Seeley-DeWitt coefficients of the Dirac operator (induced gravity) ===")
b0 = spin_dim                              # tr(I)
print(f"  a0 ~ (4pi)^-2 * {b0}    -> induced COSMOLOGICAL CONSTANT, magnitude ~ Lambda^4  (the dominant divergence)")
# b1 = (1/6) tr(6E + R I), E=-R/4:
E_coeff = F(-1,4)
b1 = F(1,6)*(6*E_coeff*spin_dim + spin_dim)   # coefficient of R
print(f"  a1 ~ (4pi)^-2 * ({b1}) R  -> induced EINSTEIN-HILBERT term (coeff of R), magnitude ~ Lambda^2")
print(f"     a1 R-coefficient = {b1}  ( = -R/3 per Dirac spinor content )  -> nonzero, definite magnitude")
print()
print("=== G_Newton is INDUCED (not a free parameter) ===")
print("  Matching  S_ind ⊃ [(4pi)^-2 |a1| Lambda^2] ∫R√g  to  S_EH = (1/16piG) ∫R√g :")
print("    1/(16 pi G)  ~  (4pi)^-2 * (1/3) * Lambda^2 * N_f     (N_f = fermion species)")
# Corrigendum 2026-09-30: this line used to print the typed coefficient 48 pi^3, which is (4pi)^2 times the
# coefficient that the matching line above gives. The coefficient is now SOLVED from the matching line.
G_sym, Lam_sym, Nf_sym = sp.symbols("G Lambda N_f", positive=True)
matching_line = sp.Eq(1 / (16 * sp.pi * G_sym), (4 * sp.pi) ** -2 * sp.Rational(1, 3) * Lam_sym ** 2 * Nf_sym)
G_solved = sp.solve(matching_line, G_sym)[0]
G_coeff = sp.simplify(G_solved * Nf_sym * Lam_sym ** 2)      # G = G_coeff / (N_f Lambda^2)
print(f"    =>  G ~ {str(G_coeff).replace('**', '^').replace('*', ' ')} / (N_f Lambda^2)  ~  a^2 / N_f        (Lambda ~ 1/a, the lattice cutoff)")
print("  CONDITIONAL RESULT: the supplied matching equation fixes G = 3*pi/(N_f*Lambda^2).")
print("  Determinant normalization, cutoff scheme, physical metric and attractive source sign remain unsupplied.")
print("  This runner does not establish a graviton, TT positivity, a Ward identity or an exhaustive gravity wall.")

# ---------------------------------------------------------------------------
# Corrigendum 2026-09-30: coefficient consistency check (PASS/FAIL).  Added after the wall-campaign check
# (L14-W11) found that the previously printed G ~ 48 pi^3/(N_f Lambda^2) was inconsistent with the matching
# line.  Checks are same-model-family; the O(1) coefficient below is the coefficient OF THE MATCHING LINE only.
# ---------------------------------------------------------------------------
print("=== COEFFICIENT CONSISTENCY CHECK (corrigendum 2026-09-30) ===")
results = []
def check(name, ok):
    results.append((name, bool(ok)))
    print(("PASS" if ok else "FAIL"), name)

old_coeff = 48 * sp.pi ** 3                                    # the coefficient printed before the correction
# C1: solving the note's own matching line gives 3 pi, not 48 pi^3
check("C1 matching line 1/(16 pi G) = (4pi)^-2 (1/3) Lambda^2 N_f solves to G = 3 pi/(N_f Lambda^2)",
      sp.simplify(G_coeff - 3 * sp.pi) == 0)
# C2: substituting the solved G back into the matching line gives an identity
resid_new = sp.simplify(matching_line.lhs.subs(G_sym, G_solved) - matching_line.rhs)
check("C2 the solved G satisfies the matching line identically (residual 0)", resid_new == 0)
# C3: the previously printed coefficient does NOT satisfy the matching line
resid_old = sp.simplify(matching_line.lhs.subs(G_sym, old_coeff / (Nf_sym * Lam_sym ** 2)) - matching_line.rhs)
check("C3 the former coefficient 48 pi^3 does not satisfy the matching line (residual nonzero)", resid_old != 0)
# C4: the former coefficient is exactly (4pi)^2 = 16 pi^2 times the correct one
check("C4 48 pi^3 / (3 pi) = (4 pi)^2 = 16 pi^2 = %.6f" % float(sp.N(old_coeff / G_coeff)),
      sp.simplify(old_coeff / G_coeff - (4 * sp.pi) ** 2) == 0)
# C5: 48 pi^3 is what a (4pi)^-4 prefactor (not the (4pi)^-2 of the Gilkey line) would give
check("C5 48 pi^3 corresponds to a (4pi)^-4 loop prefactor: 1/(16 pi * 48 pi^3) = (4pi)^-4 * (1/3)",
      sp.simplify(1 / (16 * sp.pi * old_coeff) - (4 * sp.pi) ** -4 * sp.Rational(1, 3)) == 0)
# C6: the d=4 one-loop prefactor really is (4 pi)^-2 (flat heat kernel), so no d=4 scheme supplies (4pi)^-4
s_sym, p_sym = sp.symbols("s p", positive=True)
heat_kernel = sp.integrate(2 * sp.pi ** 2 * p_sym ** 3 * sp.exp(-s_sym * p_sym ** 2) / (2 * sp.pi) ** 4, (p_sym, 0, sp.oo))
check("C6 flat d=4 heat kernel: int d^4p/(2pi)^4 exp(-s p^2) = (4 pi s)^-2  (prefactor (4pi)^-2)",
      sp.simplify(heat_kernel - (4 * sp.pi * s_sym) ** -2) == 0)
# C7: proper-time integral with cutoff 1/Lambda^2 gives Lambda^2 (4pi)^-2 |b1|, |b1| = 1/3 from the block above
t_sym = sp.symbols("t", positive=True)
pt = sp.integrate((4 * sp.pi * t_sym) ** -2 / t_sym * t_sym, (t_sym, 1 / Lam_sym ** 2, sp.oo))
check("C7 proper-time cutoff integral gives Lambda^2/(4pi)^2, so the EH weight is (4pi)^-2 (1/3) Lambda^2 (b1 = -1/3)",
      sp.simplify(pt - Lam_sym ** 2 / (4 * sp.pi) ** 2) == 0 and b1 == F(-1, 3))
# C8: rational scheme factors (1/2 from det D = (det D^2)^(1/2), 2, 4, 8, ...) multiply 3 pi by a rational q, so they
#     can reach 48 pi^3 only if q = 16 pi^2, which is irrational: no rational rescaling of the matching line
#     turns 3 pi into 48 pi^3.  (Only a change of the loop prefactor, C5, supplies the missing pi^2.)
needed = sp.simplify(old_coeff / G_coeff)                      # 16 pi^2
check("C8 needed rescaling 16 pi^2 is irrational, so no rational scheme factor (1/2, 2, 4, 8, ...) gives 48 pi^3",
      needed.is_rational is False and sp.simplify(needed / sp.pi ** 2) == 16)
# C9: numeric size of the difference for the illustrative species count N_f = 8, Lambda = 1/a
nf_demo = 8
lp_new = math.sqrt(float(G_coeff) / nf_demo)
lp_old = math.sqrt(float(old_coeff) / nf_demo)
print(f"  info: N_f = {nf_demo}, Lambda = 1/a:  l_P/a = sqrt(G/a^2) = {lp_new:.4f} (matching line), {lp_old:.4f} (former printed value)")
check("C9 former implied l_P/a is 4 pi times the matching-line value (sqrt of the (4pi)^2 ratio)",
      abs(lp_old / lp_new - 4 * math.pi) < 1e-12)
print("  NOTE: 3 pi is the coefficient of the matching line only.  The 1/2 in det D = (det D^2)^(1/2), the fermion")
print("        sign, and the cutoff scheme (Lambda = 1/a vs pi/a) are O(1) factors this note does not evaluate;")
print("        the claim remains the scaling G ~ a^2/N_f, not a value of l_P/a.")

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
raise SystemExit(1 if n_fail else 0)
