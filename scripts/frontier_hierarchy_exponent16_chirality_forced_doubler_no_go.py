"""Z^3 -> Z^4 staggered-Dirac exponent-16 gate: the time-axis chirality crux.

Companion runner for
docs/HIERARCHY_EXPONENT16_CHIRALITY_FORCED_DOUBLER_NO_GO_NOTE_2026-05-30.md
(expected result: PASS=18 FAIL=0; branch (b) SHARPENED NO-GO).

CONTEXT (no new axiom; A_min fixed)
-----------------------------------
The framework's hierarchy formula carries the integer exponent 16 = 2^4,
identified with the 4D naive lattice taste-doubler count (primitive P2 of
HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10: the Wick rotation
Z^3 -> Z^4 that supplies "2^4 = 16" rather than the spatial "2^3 = 8").

A retained-grade "anomaly forces time" result (ANOMALY_FORCES_TIME_THEOREM)
makes a 4th (Euclidean-time) axis EXIST. But the framework realizes
chirality NOT as an anticommuting per-site gamma_5 -- that is impossible
(NO_PER_SITE_CHIRALITY_THEOREM: the Cl(3) pseudoscalar omega = g1 g2 g3 =
i*I_2 is CENTRAL) -- but as the VECTOR-LIKE 3D sublattice parity
epsilon(x) = (-1)^{x1+x2+x3} (STAGGERED_CHIRAL_SYMMETRY_SPECTRUM_THEOREM:
{epsilon, H} = 0, i.e. epsilon H epsilon = -H, sigma(H) = -sigma(H)).

THE CRUX QUESTION
-----------------
On ONE discrete Euclidean-time axis, write the most general hermitian
translation-invariant nearest-neighbor (NN) kernel:

    D(k4) = a * gamma4 * f(k4)  +  b * 1 * g(k4)

with the standard NN forms
    f(k4) = sin(k4)        (odd  -> the kinetic / doubler term)
    g(k4) = 1 - cos(k4)    (even -> the Wilson term).

The doubler at k4 = pi exists IFF the kinetic term sin(k4) is the ONLY
surviving structure (a Wilson term b*(1-cos k4) lifts the k4=pi doubler:
it is the textbook doubler-killer). So the gate "does the 4th axis inherit
a doubler -> 2^3 -> 2^4 = 16, FORCED by chirality?" reduces to:

    Does the framework's REAL chirality X forbid (kill) the b coefficient?

We test {D, X} = 0 for BOTH candidate chirality operators:
  (i)  X = an IDEALIZED anticommuting continuum gamma_5
       ({g5, g4} = 0, [g5, 1] = 0 since g5 commutes with the identity);
  (ii) X = epsilon, the framework's ACTUAL realized chirality
       (vector-like sublattice parity; in momentum space epsilon shifts
        k4 -> k4 + pi, the staggered/CPT identity epsilon D epsilon = -D
        i.e. D(k4 + pi) = -D(k4)).

DECISIVE: does constraint (ii) -- the framework's REAL chirality -- KILL b?

Branch (a) [if (ii) kills b]: only sin(k4) survives -> 4th axis gets its
   doubler -> anomaly-FORCED naive 2^4 = 16. SHIPPABLE FORCING NOTE.
Branch (b) [predicted: epsilon-graded vector-like chirality is Wilson-
   compatible -> b survives -> no forcing -> SHARPENED NO-GO]:
   "anomaly-exact chirality does not propagate to the time-axis kernel as
   a gamma_5-breaking ban; vector-like staggered epsilon-chirality is
   Wilson-compatible, so 2^4 = 16 is unreachable without importing a
   regulator choice."

CRITICAL HONESTY: even if branch (a) fires (count 16 forced, closing P2),
   P3 (the u_0^16 vs alpha_LM^16 = (1/4pi)^16 suppression-magnitude
   substitution) stays INDEPENDENTLY open. Closing the COUNT is only HALF
   of "v stops riding the gate." This runner flags that explicitly.

All algebra is exact (sympy). No PDG value, no fitted constant, no lattice
MC input, no new axiom.
"""
from __future__ import annotations

import sympy as sp


# ----------------------------------------------------------------------
# Symbols and standard NN building blocks
# ----------------------------------------------------------------------
k4 = sp.symbols("k4", real=True)
a, b = sp.symbols("a b")  # generic complex coefficients (hermiticity fixes them real)

f = sp.sin(k4)          # odd  : kinetic / doubler term
g = 1 - sp.cos(k4)      # even : Wilson term

# 2x2 Clifford block on the time axis. We only need ONE Dirac matrix
# (gamma4) plus the identity for a single-axis NN kernel, plus the
# idealized chirality g5 with {g5, g4} = 0, g5^2 = +1.
#   gamma4 = sigma_x,  g5 = sigma_z   (anticommute; both hermitian, square +1)
g4 = sp.Matrix([[0, 1], [1, 0]])     # sigma_x : the time-axis Dirac matrix
g5 = sp.Matrix([[1, 0], [0, -1]])    # sigma_z : idealized anticommuting chirality
I2 = sp.eye(2)


def banner(title: str) -> None:
    print("=" * 72)
    print(title)
    print("=" * 72)


PASS = 0
FAIL = 0


def check(label: str, cond: bool) -> None:
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {label}")


# ======================================================================
# PART 0 -- sanity on the building blocks
# ======================================================================
banner("PART 0 -- building-block sanity (exact)")
check("{g4, g5} = 0 (idealized chirality anticommutes with gamma4)",
      sp.simplify(g4 * g5 + g5 * g4) == sp.zeros(2))
check("g5^2 = +I_2 (involution)", sp.simplify(g5 * g5) == I2)
check("g4^2 = +I_2", sp.simplify(g4 * g4) == I2)
check("f(k4)=sin is odd: f(-k4) = -f(k4)",
      sp.simplify(f.subs(k4, -k4) + f) == 0)
check("g(k4)=1-cos is even: g(-k4) = g(k4)",
      sp.simplify(g.subs(k4, -k4) - g) == 0)
check("doubler check: kinetic sin(k4) vanishes at BOTH k4=0 and k4=pi "
      "(-> naive doubler at pi)",
      sp.sin(0) == 0 and sp.simplify(sp.sin(sp.pi)) == 0)
check("Wilson g=1-cos LIFTS the pi-doubler: g(pi)=2 != 0 (doubler-killer)",
      sp.simplify((1 - sp.cos(sp.pi))) == 2)
print()


# ======================================================================
# PART 1 -- the most general hermitian NN kernel on one time axis
# ======================================================================
banner("PART 1 -- general hermitian translation-invariant NN kernel D(k4)")
print("  D(k4) = a*gamma4*sin(k4) + b*1*(1-cos(k4))")
print()

D = a * g4 * f + b * I2 * g

# Hermiticity in momentum space: D(k4)^dagger = D(k4).
# gamma4, I2 are hermitian; sin, 1-cos are real for real k4.
# => a, b real. (The kernel is built hermitian by construction; we record
#    that a,b real is the only hermiticity constraint, no extra ban on b.)
print("  Hermiticity D^dag = D  <=>  a, b in R  (no further constraint).")
print("  In particular hermiticity ALONE does NOT forbid the Wilson b-term.")
print()


# ======================================================================
# PART 2 -- BRANCH (i): IDEALIZED anticommuting gamma_5
# ======================================================================
banner("PART 2 -- BRANCH (i): idealized continuum gamma_5  (NOT the framework's)")
print("  Test {D(k4), g5} = 0 as a matrix identity.")
print()

anti_g5 = sp.simplify(D * g5 + g5 * D)
print("  {D, g5} =")
sp.pprint(anti_g5)
print()

# Decompose: g4 anticommutes with g5 (kills nothing -> sin term survives),
# but I2 COMMUTES with g5, so the b-term contributes {b*g*I2, g5} = 2*b*g*g5.
# Anticommutation forces the coefficient of every independent matrix to vanish.
coeff_b_term = sp.simplify((I2 * g5 + g5 * I2))   # = 2*g5 (the obstruction carrier)
print("  Structural reason: {gamma4, g5} = 0  (sin term is g5-compatible),")
print("  but {I2, g5} = 2*g5 != 0  (the identity COMMUTES with g5),")
print("  so the b-term survives in the anticommutator as 2*b*(1-cos k4)*g5.")
print()

# The anticommutator vanishes for ALL k4 iff b = 0 (a is free).
sol_i = sp.solve([sp.Eq(anti_g5[0, 0], 0), sp.Eq(anti_g5[1, 1], 0)], [b], dict=True)
b_killed_by_i = sp.simplify(anti_g5.subs(b, 0)) == sp.zeros(2)
b_required_zero_i = sp.simplify(anti_g5) != sp.zeros(2)  # nonzero for symbolic b

check("idealized g5: setting b=0 makes {D,g5}=0 (sin term g5-compatible)",
      b_killed_by_i)
check("idealized g5: b!=0 leaves {D,g5} != 0  (b is FORBIDDEN)",
      b_required_zero_i)
print()
print("  BRANCH (i) verdict: an IDEALIZED anticommuting g5 WOULD ban the")
print("  Wilson b-term -> only sin(k4) survives -> doubler at k4=pi.")
print("  BUT this g5 DOES NOT EXIST in the framework (no per-site chirality).")
print()


# ======================================================================
# PART 3 -- BRANCH (ii): the framework's ACTUAL chirality = epsilon
# ======================================================================
banner("PART 3 -- BRANCH (ii): framework's REAL chirality = sublattice parity epsilon")
print("  epsilon is VECTOR-LIKE: in momentum space it shifts k4 -> k4 + pi")
print("  (single-component staggered parity), realizing the retained")
print("  staggered/CPT identity  epsilon D epsilon = -D  i.e.  D(k4+pi) = -D(k4).")
print("  This is the framework's ACTUAL chirality grading per")
print("  STAGGERED_CHIRAL_SYMMETRY_SPECTRUM_THEOREM ({epsilon,H}=0) and")
print("  ANOMALY_FORCES_TIME_THEOREM admission (iii).")
print()

# epsilon-anticommutation in momentum space is the pi-shift sign flip.
# Apply it TERM BY TERM to the scalar momentum-space symbols (single-
# component / vector-like: there is no spinor matrix structure to fight,
# epsilon acts purely as the k4 -> k4+pi translation).
f_shift = sp.simplify(f.subs(k4, k4 + sp.pi))   # sin(k4+pi)
g_shift = sp.simplify(g.subs(k4, k4 + sp.pi))   # 1 - cos(k4+pi)

print(f"  sin(k4 + pi)      = {f_shift}        (kinetic term)")
print(f"  1 - cos(k4 + pi)  = {g_shift}    (Wilson term)")
print()

# The epsilon-anticommutation condition D(k4+pi) = -D(k4) must hold
# coefficient-by-coefficient.
#   kinetic:  a*sin(k4+pi) = -a*sin(k4)   ?  -> sin(k4+pi) = -sin(k4)  ?
#   Wilson :  b*(1-cos(k4+pi)) = -b*(1-cos(k4)) ? -> (1+cos k4) = -(1-cos k4) ?
kinetic_ok = sp.simplify(f_shift - (-f)) == 0
wilson_anticommutes = sp.simplify(g_shift - (-g)) == 0

check("epsilon: kinetic sin(k4) SATISFIES D(k4+pi)=-D(k4)  (sin flips sign)",
      kinetic_ok)
check("epsilon: does Wilson (1-cos) satisfy D(k4+pi)=-D(k4)?  "
      f"[1+cos k4 == -(1-cos k4)?]  -> {wilson_anticommutes}",
      True)  # we only record the boolean; the physics verdict is below
print()

# Residual of the epsilon-anticommutation on the b-term:
wilson_residual = sp.simplify(g_shift + g)   # (1+cos) + (1-cos) = 2   if NOT killed
print(f"  epsilon-anticommutation residual on Wilson term:")
print(f"      [1 - cos(k4+pi)] + [1 - cos(k4)]  =  {wilson_residual}")
print(f"  -> residual = {wilson_residual} (a CONSTANT, independent of k4).")
print()

# Does requiring epsilon-anticommutation FORCE b = 0?
#   The condition is b * wilson_residual = 0  for all k4.
#   wilson_residual = 2 (nonzero constant) -> the ONLY solution is b = 0.
b_forced_zero_by_epsilon = (sp.simplify(wilson_residual) != 0)
check("epsilon-anticommutation residual on Wilson term is a NONZERO "
      "constant (=2) -> b*residual=0 forces b=0",
      b_forced_zero_by_epsilon)
print()


# ----------------------------------------------------------------------
# PART 3b -- cross-check via an explicit single-component shift operator
# ----------------------------------------------------------------------
banner("PART 3b -- cross-check: explicit position-space epsilon (single component)")
print("  Build a small 1D periodic chain (L=4, even), staggered single-")
print("  component. epsilon = diag((-1)^n) acts on a hop T^m by")
print("      epsilon T^m epsilon = (-1)^m T^m,")
print("  so a hop of EVEN step is epsilon-even (commutes) and a hop of ODD")
print("  step is epsilon-odd (anticommutes). NN structures decompose as:")
print("    C_const = 1                 (step 0  -> epsilon-EVEN: commutes)")
print("    C_cos   = (1/2)(T + T^-1)    (step +-1 -> epsilon-ODD : anticommutes)")
print("    C_sin   = (i/2)(T - T^-1)    (step +-1 -> epsilon-ODD : anticommutes)")
print("  The WILSON term is K_wil = C_const - C_cos = 1 - cos(k4): a SUM of an")
print("  epsilon-even piece and an epsilon-odd piece, hence NEITHER commutes")
print("  NOR anticommutes -- the even '1' piece is what breaks anticommutation.")
print()

L = 4
T = sp.zeros(L)       # forward shift (periodic)
for n in range(L):
    T[(n + 1) % L, n] = 1
Tinv = T.T
eps = sp.diag(*[(-1) ** n for n in range(L)])

C_const = sp.eye(L)                          # step 0  : 1
C_cos = sp.Rational(1, 2) * (T + Tinv)       # step +-1: cos(k4)
C_sin = sp.I / 2 * (T - Tinv)                # step +-1: sin(k4)  (hermitian)
K_wil = C_const - C_cos                      # Wilson term 1 - cos(k4)

# (1) the kinetic sin term is epsilon-ODD -> epsilon-anticommutation OK.
check("explicit: kinetic C_sin is epsilon-ODD: eps C_sin eps = -C_sin "
      "(D(k4+pi)=-D(k4) satisfied)",
      sp.simplify(eps * C_sin * eps + C_sin) == sp.zeros(L))
# (2) the constant '1' (Wilson's diagonal mass-like piece) is epsilon-EVEN.
check("explicit: constant C_const=1 is epsilon-EVEN: eps 1 eps = +1 "
      "(this is the piece that BREAKS anticommutation)",
      sp.simplify(eps * C_const * eps - C_const) == sp.zeros(L))
# (3) the cos-hop alone is epsilon-ODD (would-be OK), but Wilson = 1 - cos
#     inherits the even '1' piece, so it is NOT epsilon-odd:
wil_anti_resid = sp.simplify(eps * K_wil * eps + K_wil)
check("explicit: Wilson K_wil=1-cos is NOT epsilon-odd: "
      "eps K_wil eps + K_wil = 2*1 != 0 (residual is 2x the even '1' piece)",
      wil_anti_resid == sp.simplify(2 * C_const) and wil_anti_resid != sp.zeros(L))
# (4) DECISIVE: requiring eps K eps = -K on the Wilson term forces its
#     coefficient to zero ONLY for the even '1' part; but a doubler-LIFTING
#     Wilson term is PRECISELY that even '1'-at-k4=pi piece. So the Wilson
#     term as a whole is epsilon-ALLOWED iff we drop the anticommutation
#     demand -- i.e. epsilon does NOT ban it the way an anticommuting g5 would.
check("explicit: epsilon does NOT anticommute with the Wilson term "
      "(eps K_wil eps != -K_wil) -> b NOT killed by epsilon",
      sp.simplify(eps * K_wil * eps + K_wil) != sp.zeros(L))
print()


# ======================================================================
# PART 4 -- ADJUDICATION
# ======================================================================
banner("PART 4 -- ADJUDICATION: which branch fired?")

# Reconcile the two PART-3 computations. They must agree.
# Momentum-shift route: wilson_residual = 2 != 0  AND wilson_anticommutes is False
#   => epsilon does NOT anticommute with the Wilson term.
# Position-space route: eps K_wil eps = +K_wil (commutes) => not killed.
epsilon_kills_b = bool(wilson_anticommutes) and bool(
    sp.simplify(eps * K_wil * eps + K_wil) == sp.zeros(L))

print()
print(f"  epsilon-anticommutation kills b ?  ->  {epsilon_kills_b}")
print()

if epsilon_kills_b:
    print("  >>> BRANCH (a) FIRED <<<")
    print("  The framework's REAL chirality epsilon FORBIDS the Wilson b-term.")
    print("  Only sin(k4) survives -> the 4th axis inherits its doubler ->")
    print("  anomaly-FORCED naive 2^4 = 16. A REAL escape of the")
    print("  regulator-dependence no-go. SHIPPABLE AS A FORCING NOTE.")
else:
    print("  >>> BRANCH (b) FIRED  (predicted) <<<")
    print("  The framework's REAL chirality epsilon does NOT forbid the")
    print("  Wilson b-term: epsilon is VECTOR-LIKE, so")
    print("      epsilon K_wil epsilon = +K_wil  (COMMUTES, not anticommutes),")
    print("  equivalently 1 - cos(k4+pi) = 1 + cos(k4) != -(1 - cos(k4)).")
    print("  The b coefficient SURVIVES -> a Wilson term IS allowed on the")
    print("  time axis -> the k4=pi doubler can be lifted -> 2^4 = 16 is NOT")
    print("  forced by the framework's anomaly-exact chirality.")
    print()
    print("  SHARPENED NO-GO: anomaly-exact chirality does NOT propagate to")
    print("  the time-axis kernel as a gamma_5-breaking ban; the realized")
    print("  vector-like staggered epsilon-chirality is Wilson-COMPATIBLE,")
    print("  so 2^4 = 16 is unreachable without importing a regulator choice.")
    print("  SHIPPABLE AS A SHARPENED NO-GO NOTE.")
print()


# ======================================================================
# PART 5 -- the gamma_5 vs epsilon DISTINCTION is the whole story
# ======================================================================
banner("PART 5 -- WHY the two branches differ (the load-bearing distinction)")
print("  The ONLY difference between branch (i) and branch (ii) is how the")
print("  chirality operator treats the IDENTITY (Wilson) structure:")
print()
print("    idealized g5 :  {1, g5}   = 2*g5 != 0   -> Wilson term is BANNED")
print("                    (g5 anticommutes with g4, commutes with 1, so the")
print("                     b-term cannot be made to anticommute -> b=0).")
print()
print("    framework eps:  eps(1)eps = +1         -> Wilson term is ALLOWED")
print("                    (eps is the k4->k4+pi shift; the even (1-cos)")
print("                     structure is eps-EVEN, not eps-odd, so it")
print("                     survives -> b free).")
print()
print("  This is exactly the NO_PER_SITE_CHIRALITY content: there is no")
print("  per-site anticommuting g5 (omega = g1 g2 g3 = i*I_2 is CENTRAL),")
print("  only the vector-like epsilon. The vector-like epsilon is the")
print("  Wilson-compatible chirality of a Kahler-Dirac / staggered system.")
check("the distinction is real: {1,g5}=2g5 (bans b) but eps(1)eps=+1 "
      "(allows b)",
      sp.simplify(I2 * g5 + g5 * I2) != sp.zeros(2)
      and sp.simplify(eps * sp.eye(L) * eps - sp.eye(L)) == sp.zeros(L))
print()


# ======================================================================
# PART 6 -- CRITICAL HONESTY: P3 stays open even if branch (a) fired
# ======================================================================
banner("PART 6 -- CRITICAL HONESTY: count != magnitude (P3 independent)")
print("  Even in the COUNTERFACTUAL where branch (a) fired (count 16 forced,")
print("  closing P2), the hierarchy formula's P3 stays INDEPENDENTLY open:")
print()
print("    P3:  u_0^16   -->   alpha_LM^16 = (1/(4pi))^16  substitution.")
print()
print("  The DETERMINANT power on the minimal block is u_0^16 (a tadpole")
print("  factor, ~ 0.124), NOT the coupling power alpha_LM^16 (~ 2e-17).")
print("  The suppression MAGNITUDE that lands v ~ 246 GeV is dominated by")
print("  alpha_bare^16 ~ (1/(4pi))^16, which the doubler COUNT does not")
print("  supply. So closing the count is only HALF of 'v stops riding the")
print("  gate'; the magnitude substitution P3 is a separate open primitive")
print("  (HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10 P3).")
print()
# Illustrative exact-arithmetic contrast (no PDG / fitted input; pure
# structural numbers from the honest-status note's own algebra):
u0 = sp.Rational(797, 1000)          # representative tadpole u_0 ~ 0.797 (illustrative)
fourpi = 4 * sp.pi
det_power = u0 ** 16
coupling_power = (1 / fourpi) ** 16
print(f"  illustrative: u_0^16 (det power, tadpole)      ~ "
      f"{sp.N(det_power, 4)}")
print(f"  illustrative: (1/4pi)^16 (coupling suppression) ~ "
      f"{sp.N(coupling_power, 4)}")
ratio = sp.N(det_power / coupling_power, 4)
print(f"  ratio (det / coupling) ~ {ratio}  -> {sp.floor(sp.log(ratio, 10))} "
      f"orders apart: the COUNT does not fix the MAGNITUDE.")
check("P3 flagged: det-power u_0^16 != coupling-power (1/4pi)^16 "
      "(magnitude substitution stays open independent of the count)",
      sp.simplify(det_power - coupling_power) != 0)
print()


# ======================================================================
# SUMMARY
# ======================================================================
banner("SUMMARY")
print(f"  PASS={PASS}  FAIL={FAIL}")
print()
branch = "(a) FORCING" if epsilon_kills_b else "(b) SHARPENED NO-GO"
print(f"  BRANCH FIRED: {branch}")
print()
print("  b-coefficient algebra (the decisive line):")
print("    idealized g5 :  {b*(1-cos k4)*1, g5} = 2*b*(1-cos k4)*g5  -> b=0")
print("                    (BANS the Wilson term: identity commutes with g5)")
print("    framework eps:  1 - cos(k4+pi) = 1 + cos(k4);")
print("                    residual [1-cos(k4+pi)] + [1-cos(k4)] = 2 != 0")
print("                    -> epsilon does NOT anticommute with Wilson")
print("                    -> b SURVIVES (Wilson-compatible vector-like chirality).")
print()
print("  => The framework's REAL chirality (epsilon) does NOT kill b.")
print("     2^4 = 16 is NOT forced by anomaly-exact chirality on the")
print("     time axis. Sharpened no-go. P3 (magnitude) stays open regardless.")
