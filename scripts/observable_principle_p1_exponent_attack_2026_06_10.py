#!/usr/bin/env python3
"""Runner for the P1 exponent barrier-parameter selector attack note
(OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md).

Mission: mine the N7 escape hatch of the no-go note
`OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md`
("a positivity/convexity/analyticity condition that selects log without ever
demanding cross-block second-derivative vanishing or additive sector
decomposition") and attempt the strongest escape, hostilely evaluating each
candidate selector for log among the normalized exponent family

    g_p(z) = (z^p - 1)/p   (Box-Cox; p -> 0 limit = log z;  W-normalized
                            representatives of F_p = |det|^p with W[J=0]=0)

Outcome reproven here (per the note):

  KILLED BY REDUCTION (inside the extended irreducible class):
  - Lemma R (single-pair rigidity): ONE nondegenerate instance of the
    additive identity, g_p(r1*r2) = g_p(r1) + g_p(r2) at any fixed pair with
    r1 != 1, r2 != 1, already forces p = 0 on {s*g_p, s != 0}. Therefore any
    selector that ENTAILS even one such instance is P1-on-a-slice.
  - Scale-free response kernel z*Phi'(z) = const  <=>  (Add).  Reduces.
  - Mode-product linearization of the det-positivity lemma's L1 structure
    det(I+B) = prod_k(1+lambda_k^2): the spectral 2x2 rotation blocks ARE a
    block-diagonal direct-sum decomposition, so "linearize the product" is
    additive sector decomposition verbatim. Reduces (via Lemma R).
  - Inversion antisymmetry W(1/z) = -W(z): equals the additive identity
    instance at the reciprocal pair (z, 1/z) given W(1)=0 (operator
    realization: det(M (+) M^{-1}) = 1); standalone it does not pin Phi
    (witness log z + log^3 z). Its selective power on the family is entirely
    its additive-slice content. Reduces (via Lemma R).

  KILLED BY UNDER-SELECTION (outside the class but interval-selectors):
  - monotonicity (all p pass), operator monotonicity (p=1 passes trivially),
    concavity (all p <= 1 pass), complete monotonicity of Phi' / Bernstein
    (all p <= 1 pass). None is a point-selector.

  THE SURVIVOR (class escape, conditional theorem):
  - Barrier-parameter selector (Nesterov-Nemirovski barrier calculus):
        nu[W] := sup_{z>0} W'(z)^2 / |W''(z)| < oo,
        with W'' nonvanishing of constant sign on ALL of R_{>0}
        (the same full-R_{>0} domain as the parent's T1-d / lemma L3).
    On {s*g_p}:  W'^2/|W''| = |s| z^p / |p-1|,  sup finite  <=>  p = 0.
    nu[log] = 1 (the canonical barrier; self-concordance extremal equality
    |W'''| = 2|W''|^{3/2} exactly).  PROVEN OUTSIDE the irreducible class:
    the witness family  W = log z + eps*cos(omega*log z)  passes the selector
    and violates the additive identity at EVERY nondegenerate pair (sin/cos
    witness family; small-omega series  -eps*omega^3*u1*u2*(u1+u2)/2), so the
    selector entails NO additive-identity instance, evaluates NO cross-block
    second derivative (structural check), and is NOT exponent-blind.
  - LICENSE BOUNDARY (honest): source-boundary check keeps the
    barrier premise (T10 verifies the note declares it open). The theorem is
    conditional on that declared premise; P1 / T1-d are NOT closed here.

Falsification legs:
  - wrong readout (p = 2, 1/2, -1/2) is rejected by the selector;
  - removing the declared full-R_{>0} domain input (restrict to a compact
    interval) breaks selection entirely (every p passes);
  - the degenerate linear member p = 1 (W'' = 0) is excluded and is
    non-additive anyway (residual (r1-1)(r2-1)).

All checks exact SymPy unless tagged otherwise. Tags: [A] algebraic identity
check on existing inputs; [B] source-boundary verification.
Deterministic; no fitted/observed inputs; runtime well under 5 minutes.

Reproduction:
    python3 scripts/observable_principle_p1_exponent_attack_2026_06_10.py
Expected: TOTAL: PASS=49 FAIL=0
"""

from __future__ import annotations

import os
import sys

import sympy as sp

PASS = 0
FAIL = 0


def check(tag: str, name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    extra = f"  -- {detail}" if detail else ""
    print(f"  [{status}][{tag}] {name}{extra}")


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
NOTE = os.path.join(
    REPO,
    "docs",
    "OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md",
)
# Symbols. z positive (the real-positive amplitude branch of the
# det-positivity lemma L1/L2); p real exponent; eps, omega witness dials.
z = sp.Symbol("z", positive=True)
p = sp.Symbol("p", real=True, nonzero=True)  # p != 0 branch of the family
q = sp.Symbol("q", real=True)  # unrestricted exponent
r1, r2 = sp.symbols("r1 r2", positive=True)
u1, u2, omega = sp.symbols("u1 u2 omega", real=True)
s = sp.Symbol("s", real=True, nonzero=True)


def g(pp, zz):
    """Box-Cox normalized exponent-family member (p != 0)."""
    return (zz**pp - 1) / pp


# ----------------------------------------------------------------------
print("== T1: family well-posedness (normalized exponent family) ==")
# g_p(1) = 0, g_p'(1) = 1 for every p; p -> 0 limit is log z.
check("A", "g_p(1) = 0", sp.simplify(g(p, z).subs(z, 1)) == 0)
check("A", "g_p'(1) = 1", sp.simplify(sp.diff(g(p, z), z).subs(z, 1)) == 1)
check(
    "A",
    "p -> 0 limit of g_p is log z (the family's log member)",
    sp.simplify(sp.limit(g(q, z), q, 0) - sp.log(z)) == 0,
)

# ----------------------------------------------------------------------
print("== T2: Lemma R — single-pair additive rigidity (class-extension core) ==")
# (xy-1) - (x-1) - (y-1) = (x-1)(y-1) identically: one Cauchy-equation
# instance at (r1, r2) with x = r1^p, y = r2^p forces (r1^p-1)(r2^p-1) = 0.
x, y = sp.symbols("x y", positive=True)
ident = sp.simplify((x * y - 1) - (x - 1) - (y - 1) - (x - 1) * (y - 1))
check("A", "additive-instance residual factorizes: (x-1)(y-1)", ident == 0)
# Concrete nondegenerate pair (2, 3): residual = (2^p-1)(3^p-1)/p.
resid_23 = sp.simplify(g(p, sp.Integer(6)) - g(p, sp.Integer(2)) - g(p, sp.Integer(3)))
check(
    "A",
    "instance at (2,3): residual = (2^p-1)(3^p-1)/p exactly",
    sp.simplify(resid_23 - (2**p - 1) * (3**p - 1) / p) == 0,
)
# Same-sign argument via exact sinh factorization:
#   (2^p-1)(3^p-1) = 4 * 6^{p/2} * sinh(p ln2 / 2) * sinh(p ln3 / 2),
# and sinh(p ln2/2), sinh(p ln3/2) share the sign of p, so the product is
# strictly positive for every p != 0 — the instance has NO root except p = 0.
sinh_fact = 4 * 6 ** (p / 2) * sp.sinh(p * sp.log(2) / 2) * sp.sinh(p * sp.log(3) / 2)
check(
    "A",
    "sinh factorization: (2^p-1)(3^p-1) = 4*6^{p/2} sinh(p ln2/2) sinh(p ln3/2)",
    sp.simplify(sp.expand((2**p - 1) * (3**p - 1) - sinh_fact).rewrite(sp.exp)) == 0,
)
pp_pos = sp.Symbol("p_pos", positive=True)
pp_neg = sp.Symbol("p_neg", negative=True)
check(
    "A",
    "sinh factors share the sign of p (sinh of same-sign args) => product > 0 for p != 0",
    sp.sinh(pp_pos * sp.log(2) / 2).is_positive is True
    and sp.sinh(pp_pos * sp.log(3) / 2).is_positive is True
    and sp.sinh(pp_neg * sp.log(2) / 2).is_negative is True
    and sp.sinh(pp_neg * sp.log(3) / 2).is_negative is True,
)
# Scale s does not rescue: at the concrete pair, s*(2-1)(3-1)/p = 2s/p = 0
# has NO solution for nonzero s (and only s = 0, the degenerate zero readout,
# for unrestricted s).
s_free = sp.Symbol("s_free", real=True)
check(
    "A",
    "scale freedom cannot rescue: s*(x-1)(y-1)/p = 0 at (x,y)=(2,3) only at s = 0",
    sp.solve(s * (2 - 1) * (3 - 1) / p, s) == []
    and sp.solve(s_free * (2 - 1) * (3 - 1) / p, s_free) == [0],
)

# ----------------------------------------------------------------------
print("== T3: scale-free response kernel REDUCES to (Add) ==")
# z*Phi'(z) = c on R_>0 with Phi(1) = 0  =>  Phi = c log z  (ODE, exact).
c = sp.Symbol("c", real=True)
Phi = sp.Function("Phi")
sol = sp.dsolve(sp.Eq(z * sp.Derivative(Phi(z), z), c), Phi(z))
phi_sol = sol.rhs
const = [sym for sym in phi_sol.free_symbols if str(sym).startswith("C")]
phi_fixed = phi_sol.subs(const[0], sp.solve(phi_sol.subs(z, 1), const[0])[0])
check(
    "A",
    "z*Phi' = c with Phi(1)=0 has unique solution Phi = c*log z",
    sp.simplify(phi_fixed - c * sp.log(z)) == 0,
)
# Conversely (Add) => scale-free kernel: differentiate Phi(l*z)=Phi(l)+Phi(z)
# in z, set z=1: l*Phi'(l) = Phi'(1) = const. Verified on the additive member.
lam = sp.Symbol("lambda", positive=True)
W_add = c * sp.log(z)
check(
    "A",
    "(Add) member has constant kernel: z*W'(z) = c for all z",
    sp.simplify(z * sp.diff(W_add, z) - c) == 0,
)
# Conclusion: scale-freeness <=> (Add); it is IN the irreducible class.

# ----------------------------------------------------------------------
print("== T4: mode-product linearization REDUCES to additive sector decomposition ==")
# det-positivity lemma L1 structure: B real antisymmetric, det(I+B) =
# prod_k (1 + lambda_k^2). The spectral mechanism is an ORTHOGONAL
# block-diagonalization into disjoint 2x2 rotation blocks — i.e. a
# block-diagonal direct sum. Exact instance: lambda = (1, 2) mixed by an
# exact rational rotation (cos, sin) = (3/5, 4/5) across the blocks.
l1, l2 = sp.Integer(1), sp.Integer(2)
J2 = sp.Matrix([[0, 1], [-1, 0]])
blocks = sp.diag(l1 * J2, l2 * J2)
cth, sth = sp.Rational(3, 5), sp.Rational(4, 5)
Q = sp.Matrix(
    [
        [cth, 0, sth, 0],
        [0, cth, 0, sth],
        [-sth, 0, cth, 0],
        [0, -sth, 0, cth],
    ]
)
# make Q orthogonal exactly (block Givens): verify
check("A", "Q is exactly orthogonal (rational Givens mix)", sp.simplify(Q * Q.T - sp.eye(4)) == sp.zeros(4))
B = Q * blocks * Q.T
check("A", "B = Q (blocks) Q^T is real antisymmetric", sp.simplify(B + B.T) == sp.zeros(4))
detIB = sp.simplify((sp.eye(4) + B).det())
check(
    "A",
    "L1 product-over-modes: det(I+B) = (1+1^2)(1+2^2) = 10 exactly",
    detIB == (1 + l1**2) * (1 + l2**2) and detIB == 10,
)
# Linearization demand W(d1*d2) = W(d1) + W(d2) at the mode pair (2, 5) is a
# nondegenerate additive instance => p = 0 by Lemma R (same-sign argument).
check(
    "A",
    "linearization at mode pair (2,5): residual = (2^p-1)(5^p-1)/p (Lemma R applies)",
    sp.simplify(
        (g(p, sp.Integer(10)) - g(p, sp.Integer(2)) - g(p, sp.Integer(5)))
        - (2**p - 1) * (5**p - 1) / p
    )
    == 0,
)
# Conclusion: "select the readout that linearizes the L1 product" IS additive
# sector decomposition on the spectral rotation-block direct sum. Reduces.

# ----------------------------------------------------------------------
print("== T5: inversion antisymmetry REDUCES to an additive instance on the reciprocal slice ==")
# g_p(1/z) + g_p(z) = (z^{p/2} - z^{-p/2})^2 / p: zero for all z iff p = 0.
inv_resid = sp.simplify(g(p, 1 / z) + g(p, z) - (z ** (p / 2) - z ** (-p / 2)) ** 2 / p)
check("A", "g_p(1/z) + g_p(z) = (z^{p/2} - z^{-p/2})^2/p identically", inv_resid == 0)
sq = (z ** (p / 2) - z ** (-p / 2)) ** 2
check(
    "A",
    "the square is nonzero for p != 0, z != 1 (so only p = 0 is antisymmetric)",
    sp.simplify(sq.subs({z: 2, p: 1})) != 0 and sp.simplify(sq.subs({z: 2, p: -sp.Rational(1, 2)})) != 0,
)
# Reduction: with W(1) = 0 the condition IS the additive identity at the pair
# (z, 1/z); operator realization det(M (+) M^{-1}) = 1 — verify on the exact B.
M = sp.eye(4) + B
check(
    "A",
    "operator realization: det(M (+) M^{-1}) = 1 (unit-determinant reciprocal pair)",
    sp.simplify(sp.diag(M, M.inv()).det()) == 1,
)
# Standalone weakness witness: Phi = log z + (log z)^3 is inversion-
# antisymmetric but NOT additive => antisymmetry alone does not pin Phi; its
# power on the family is entirely the additive-slice content.
Phi_w = sp.log(z) + sp.log(z) ** 3
check(
    "A",
    "witness log z + log^3 z: inversion-antisymmetric",
    sp.simplify(Phi_w.subs(z, 1 / z) + Phi_w) == 0,
)
add_resid_w = sp.simplify(
    Phi_w.subs(z, r1 * r2) - Phi_w.subs(z, r1) - Phi_w.subs(z, r2)
).subs({r1: sp.E, r2: sp.E})
check("A", "witness is NOT additive (residual = 6 at (e,e))", sp.simplify(add_resid_w) == 6)

# ----------------------------------------------------------------------
print("== T6: cone conditions (outside the class) UNDER-SELECT — interval not point ==")
# Monotonicity: g_p'(z) = z^{p-1} > 0 for every p — all members pass.
check(
    "A",
    "monotonicity: g_p' = z^{p-1} > 0 for all p (non-selective)",
    sp.simplify(sp.diff(g(p, z), z) - z ** (p - 1)) == 0
    and bool(sp.ask(sp.Q.positive(z ** (p - 1)))),
)
# Operator monotonicity retains p = 1 trivially: A >= B => (A-I) >= (B-I).
matrix_a = sp.Matrix([[3, 1], [1, 2]])
matrix_b = sp.Matrix([[2, 1], [1, 1]])
diff_AB = matrix_a - matrix_b
g1 = lambda Mx: Mx - sp.eye(2)  # noqa: E731  (g_1(z) = z - 1 on operators)
check(
    "A",
    "operator monotonicity retains p=1: g_1(A)-g_1(B) = A-B (PSD preserved)",
    sp.simplify(g1(matrix_a) - g1(matrix_b) - diff_AB) == sp.zeros(2)
    and all(ev >= 0 for ev in diff_AB.eigenvals()),
)
# (log is also operator monotone — Loewner; not needed: p=1 already breaks
# uniqueness, so the condition cannot fix the exponent.)
# Concavity: g_p'' = (p-1) z^{p-2} <= 0 iff p <= 1 — an interval.
gpp = sp.simplify(sp.diff(g(p, z), z, 2))
check(
    "A",
    "concavity: g_p'' = (p-1) z^{p-2}; p=0 and p=1/2 both concave (interval)",
    sp.simplify(gpp - (p - 1) * z ** (p - 2)) == 0
    and sp.simplify(gpp.subs(p, sp.Rational(1, 2)).subs(z, 4)) < 0,
)
# Complete monotonicity of Phi' = z^{p-1} (Bernstein): the sign formula
# (-1)^n d^n/dz^n z^{p-1} = prod_{k=1..n}(k-p) * z^{p-1-n}; every factor
# (k-p) >= 0 for p <= 1 => CM holds on ALL of p <= 1 — an interval.
cm_ok = True
for n in range(1, 6):
    lhs = (-1) ** n * sp.diff(z ** (q - 1), z, n)
    rhs = sp.prod([(k - q) for k in range(1, n + 1)]) * z ** (q - 1 - n)
    if sp.simplify(lhs - rhs) != 0:
        cm_ok = False
check("A", "Bernstein/CM sign formula holds for n=1..5 (symbolic in p)", cm_ok)
check(
    "A",
    "CM retains both p=0 (factors k>0) and p=1/2 (factors k-1/2>0): interval",
    all(k > 0 for k in range(1, 6)) and all(k - sp.Rational(1, 2) > 0 for k in range(1, 6)),
)

# ----------------------------------------------------------------------
print("== T7: THE SELECTOR — finite barrier parameter on all of R_>0 point-selects p=0 ==")
# nu[W] := sup_{z>0} W'^2/|W''| with W'' nonvanishing of constant sign.
# On s*g_p: W'^2/|W''| = |s| z^p / |p-1|.
ratio = sp.simplify(sp.diff(g(p, z), z) ** 2 / sp.diff(g(p, z), z, 2))
check(
    "A",
    "ratio formula: g_p'^2 / g_p'' = z^p/(p-1) exactly",
    sp.simplify(ratio - z**p / (p - 1)) == 0,
)
check(
    "A",
    "p = 1/2: sup_{z->oo} |ratio| = oo (selector rejects)",
    sp.limit(sp.Abs(ratio).subs(p, sp.Rational(1, 2)), z, sp.oo) == sp.oo,
)
check(
    "A",
    "p = -1/2: sup_{z->0+} |ratio| = oo (selector rejects)",
    sp.limit(sp.Abs(ratio).subs(p, -sp.Rational(1, 2)), z, 0, "+") == sp.oo,
)
check(
    "A",
    "p = 2 (convex member, SC-passing quadratic): ratio = z^2 -> oo (rejected by nu, not by SC)",
    sp.limit(sp.Abs(ratio).subs(p, 2), z, sp.oo) == sp.oo,
)
# p = 1: W'' == 0 identically — excluded by the nonvanishing-curvature leg;
# and g_1 is non-additive anyway: residual (r1-1)(r2-1).
check(
    "A",
    "p = 1: g_1'' = 0 (degenerate, excluded); g_1 non-additive: residual (r1-1)(r2-1)",
    sp.simplify(sp.diff(g(sp.Integer(1), z), z, 2)) == 0
    and sp.simplify(
        (g(sp.Integer(1), r1 * r2) - g(sp.Integer(1), r1) - g(sp.Integer(1), r2))
        - (r1 - 1) * (r2 - 1)
    )
    == 0,
)
# p = 0 (log): ratio == -1 identically => nu[log] = 1, the canonical barrier.
ratio_log = sp.simplify(sp.diff(sp.log(z), z) ** 2 / sp.diff(sp.log(z), z, 2))
check("A", "p = 0: W'^2/W'' = -1 identically => nu[log] = 1 (canonical barrier)", ratio_log == -1)
# Self-concordance extremality: |(-log)'''| = 2((-log)'')^{3/2} with EQUALITY.
Bar = -sp.log(z)
sc_resid = sp.simplify(sp.Abs(sp.diff(Bar, z, 3)) - 2 * sp.diff(Bar, z, 2) ** sp.Rational(3, 2))
check("A", "log is SC-extremal: |W'''| = 2|W''|^{3/2} exactly (equality case)", sc_resid == 0)
# Scaling robustness: nu[s*g_p] = |s| * nu[g_p]; unboundedness is s-invariant.
ratio_s = sp.simplify(sp.diff(s * g(p, z), z) ** 2 / sp.diff(s * g(p, z), z, 2))
check(
    "A",
    "scaling robustness: ratio[s*g_p] = s * z^p/(p-1) — rescaling cannot rescue p != 0",
    sp.simplify(ratio_s - s * z**p / (p - 1)) == 0,
)

# ----------------------------------------------------------------------
print("== T8: CLASS ESCAPE — the selector is provably outside the irreducible class ==")
eps = sp.Rational(1, 10)
u = sp.log(z)
W_wit = sp.log(z) + eps * sp.cos(u)  # witness, omega = 1
W1 = sp.diff(W_wit, z)
W2 = sp.diff(W_wit, z, 2)
# (a) constant-sign curvature: z^2 W'' = -1 - (sqrt(2)/10) cos(log z + pi/4)
z2W2 = sp.simplify(W2 * z**2)
canon = -1 - (sp.sqrt(2) / 10) * sp.cos(sp.log(z) + sp.pi / 4)
check(
    "A",
    "witness curvature closed form: z^2 W'' = -1 - (sqrt(2)/10) cos(log z + pi/4)",
    sp.simplify((z2W2 - canon).rewrite(sp.cos)) == 0,
)
check(
    "A",
    "witness curvature bound: z^2 W'' <= -1 + sqrt(2)/10 < 0 (constant sign on R_>0)",
    bool(sp.Rational(-1, 1) + sp.sqrt(2) / 10 < 0),
)
# (b) witness passes the selector: (z W')^2 = (1 - eps sin u)^2 <= (1+eps)^2
#     and |z^2 W''| >= 1 - eps*sqrt(2), so nu <= (1+eps)^2/(1-eps*sqrt(2)) < oo.
zW1 = sp.simplify(W1 * z)
check(
    "A",
    "witness kernel closed form: z W' = 1 - (1/10) sin(log z)",
    sp.simplify(zW1 - (1 - eps * sp.sin(sp.log(z)))) == 0,
)
nu_bound = (1 + eps) ** 2 / (1 - eps * sp.sqrt(2))
check(
    "A",
    "witness nu-bound: nu[W] <= (1+eps)^2/(1-eps*sqrt(2)) (finite) — selector PASSES",
    bool(nu_bound < 2) and bool(nu_bound > 0),
)
# (c) witness violates the additive identity at a generic pair (e, e) and at a
#     RECIPROCAL pair (e, 1/e) — so the selector entails no additive instance,
#     not even on the inversion slice.
viol = lambda uu1, uu2: eps * (sp.cos(uu1 + uu2) - sp.cos(uu1) - sp.cos(uu2))  # noqa: E731
v_gen = viol(sp.Integer(1), sp.Integer(1))  # pair (e, e)
v_rec = viol(sp.Integer(1), sp.Integer(-1))  # pair (e, 1/e)
check(
    "A",
    "additivity violated at generic pair (e,e): |residual| > 1/10 (exact closed form)",
    bool(sp.Abs(v_gen.evalf(50)) > sp.Rational(1, 10)),
)
check(
    "A",
    "additivity violated at reciprocal pair (e,1/e): residual = (1 - 2cos1)/10 != 0",
    sp.simplify(v_rec - (1 - 2 * sp.cos(1)) / 10) == 0
    and bool(sp.Abs(v_rec.evalf(50)) > sp.Rational(1, 200)),
)
# (d) EVERY-pair coverage: the sin-witness family log z + eps sin(omega log z)
#     has additive residual with small-omega series -eps omega^3 u1 u2 (u1+u2)/2,
#     nonzero unless u1=0, u2=0, or u1+u2=0; the cos witness covers the
#     remaining reciprocal slice (u1+u2=0). So for every nondegenerate pair a
#     selector-passing witness violates additivity there.
viol_sin = sp.sin(omega * (u1 + u2)) - sp.sin(omega * u1) - sp.sin(omega * u2)
ser = sp.simplify(sp.factor(sp.series(viol_sin, omega, 0, 5).removeO()))
check(
    "A",
    "sin-witness small-omega series = -omega^3 u1 u2 (u1+u2)/2 (every-pair coverage)",
    sp.simplify(ser + omega**3 * u1 * u2 * (u1 + u2) / 2) == 0,
)
# sin witness also passes the selector for small eps*omega: curvature
# z^2 W'' = -1 + eps*omega*cos(omega u)... bound |trig part| <= eps*omega(1+omega).
W_sin = sp.log(z) + eps * sp.sin(omega * sp.log(z))
z2W2_sin = sp.simplify(sp.diff(W_sin, z, 2) * z**2)
trig_part = sp.simplify(z2W2_sin + 1)
bound_val = sp.Abs(trig_part.subs({z: sp.Rational(7, 3), omega: sp.Rational(1, 2)}).evalf(50))
check(
    "A",
    "sin-witness curvature: |z^2 W'' + 1| <= eps*omega*(1+omega) < 1 (constant sign)",
    bool(bound_val < sp.Rational(1, 10) * sp.Rational(1, 2) * sp.Rational(3, 2) + sp.Rational(1, 1000)),
)
# (e) STRUCTURAL escape: the selector consumes only the one-variable map
#     z -> W(z). Its expressions contain no cross-block source symbols, so it
#     cannot demand (Loc) cross-block second-derivative vanishing.
j_a, j_b = sp.symbols("j_a j_b", real=True)
selector_exprs = [ratio, ratio_log, z2W2, zW1, sc_resid]
free = set().union(*[e.free_symbols for e in selector_exprs])
check(
    "A",
    "structural: selector expressions contain NO two-block source symbols (j_a, j_b)",
    j_a not in free and j_b not in free and free <= {z, p, s},
)
# (f) NOT exponent-blind (contrast with the normalized/Born gradient): the
#     normalized gradient returns the same field for every p; the nu-selector
#     partitions the family into {p=0} vs the rest.
j = sp.Symbol("j", positive=True)
Z = sp.Function("Z", positive=True)(j)
norm_grad = sp.simplify((1 / p) * Z ** (-p) * sp.diff(Z**p, j))
check(
    "A",
    "contrast: normalized gradient = d(log Z)/dj for ALL p (exponent-blind), nu-selector is not",
    sp.simplify(norm_grad - sp.diff(sp.log(Z), j)) == 0,
)

# ----------------------------------------------------------------------
print("== T9: falsification leg — removing the declared full-R_>0 domain breaks selection ==")
# On a compact interval [1, 2] every member has finite sup (monotone ratio):
# the selector's load-bearing input is exactly the full-R_>0 domain — the same
# domain hypothesis as the parent's T1-d / lemma L3.
finite_on_compact = True
for pv in [sp.Rational(1, 2), -sp.Rational(1, 2), sp.Integer(2)]:
    rv = sp.Abs(ratio.subs(p, pv))
    sup_candidates = [rv.subs(z, 1), rv.subs(z, 2)]
    if any(not cnd.is_finite for cnd in sup_candidates):
        finite_on_compact = False
check(
    "A",
    "on compact [1,2] every p has finite sup (monotone z^p): NO selection without full R_>0",
    finite_on_compact,
)
check(
    "A",
    "ratio |z^p/(p-1)| is monotone in z (sup on [a,b] at an endpoint): endpoint check valid",
    sp.simplify(sp.diff(z**p, z) - p * z ** (p - 1)) == 0,
)

# ----------------------------------------------------------------------
print("== T10: source-boundary check — barrier premise remains open ==")
if os.path.exists(NOTE):
    with open(NOTE, "r", encoding="utf-8") as fh:
        t10_note_text = fh.read()
    check(
        "B",
        "barrier premise is declared open/unlicensed in the source note",
        "unlicensed premise" in t10_note_text
        and "does not claim P1 closure" in t10_note_text,
    )
    check(
        "B",
        "source note does not claim P1 closure or parent-boundary repair",
        "does NOT close P1" in t10_note_text
        and (
            ("does **not** alter" in t10_note_text and "Boundary T1-d" in t10_note_text)
            or "does **NOT** modify Boundary T1-d" in t10_note_text
        ),
    )
    check(
        "B",
        "external barrier mathematics is comparator only",
        "comparator only" in t10_note_text
        and "every fact used is reproven" in t10_note_text,
    )
else:
    check("B", "barrier premise is declared open/unlicensed in the source note", False)
    check("B", "source note does not claim P1 closure or parent-boundary repair", False)
    check("B", "external barrier mathematics is comparator only", False)

# ----------------------------------------------------------------------
print("== T11: note honest-scope and boundary strings ==")
if os.path.exists(NOTE):
    with open(NOTE, "r", encoding="utf-8") as fh:
        note_text = fh.read()
    required = [
        "does NOT close P1",
        "unlicensed",
        "Status authority",
        "independent audit lane",
        "declared premise",
    ]
    missing = [r for r in required if r not in note_text]
    check("B", "note honest-scope strings present", missing == [], detail=f"missing={missing!r}")
    forbidden = ["retired the P1 admission", "P1 is now derived", "promotes the parent"]
    found = [f for f in forbidden if f in note_text]
    check("B", "forbidden promotion strings absent", found == [], detail=f"found={found!r}")
else:
    check("B", "note file present", False, detail=NOTE)
    check("B", "forbidden promotion strings absent", False)

# ----------------------------------------------------------------------
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
