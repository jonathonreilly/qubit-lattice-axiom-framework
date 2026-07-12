#!/usr/bin/env python3
"""Exact formation-gate relocation checks (rhalf block 13).

This runner verifies one two-level compatibility model:

  1. the exact K-tied, two-slice records-only OS/Berezin measure of block 10;
  2. an independent state phi_w = (w, 1-w) on the registrable quotient C + C.

The block-10 Grassmann/Berezin engine is loaded from its source up to the start
of its report section, so the same exact Gaussian-rational implementation is
reused rather than replaced.  No floating-point helper or scan is invoked.
All new algebra is over Fraction or SymPy Rational.  Numbered PASS/FAIL lines;
exit 0 iff FAIL=0.  Nothing here derives or prefers w.
"""

from fractions import Fraction
from pathlib import Path
import re

import sympy as sp


PASS = 0
FAIL = 0


def check(num, description, condition, detail=""):
    """Print one numbered result and update the exact scorecard."""
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    line = f"[{tag}] ({num:02d}) {description}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def normalize_markdown(text):
    return re.sub(r"\s+", " ", text)


def cr_to_sympy(value):
    """Convert block 10's exact CR value to an exact SymPy expression."""
    re_part = sp.Rational(value.re.numerator, value.re.denominator)
    im_part = sp.Rational(value.im.numerator, value.im.denominator)
    return re_part + sp.I * im_part


ROOT = Path(__file__).resolve().parents[1]
BLOCK10_RUNNER = ROOT / "scripts/frontier_records_only_os_reconstruction_2026_07_11.py"
BLOCK9_NOTE = ROOT / "docs/KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md"
BLOCK10_NOTE = ROOT / "docs/RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md"
AXIOMS_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


# Reuse only the exact engine-definition prelude.  The marker is immediately
# before block 10's reporting/check section; its numerical scan helpers are
# defined later or remain uncalled, and no block-10 report is executed here.
ENGINE_MARKER = 'print("=" * 72)\nprint("Records-only OS reconstruction'
engine_source = BLOCK10_RUNNER.read_text(encoding="utf-8")
engine_namespace = {"__name__": "block10_exact_engine_reuse"}
engine_error = ""
try:
    marker_ok = engine_source.count(ENGINE_MARKER) == 1
    if not marker_ok:
        raise RuntimeError("block-10 engine/report marker is not unique")
    engine_prelude = engine_source.split(ENGINE_MARKER, 1)[0]
    exec(compile(engine_prelude, str(BLOCK10_RUNNER), "exec"), engine_namespace)
    required = {
        "F", "CR", "W_of", "dag", "matmul3", "cr_det", "reg_gram",
        "norm_gram", "is_hermitian", "leading_minors",
    }
    engine_ok = required.issubset(engine_namespace) and engine_namespace["F"] is Fraction
except Exception as exc:  # pragma: no cover - failure path is the certificate
    engine_ok = False
    engine_error = f"{type(exc).__name__}: {exc}"

check(
    1,
    "block 10's exact Gaussian-rational Berezin/OS engine is reused from the allowed runner prelude",
    engine_ok,
    engine_error or "Fraction/CR path; no float scan invoked",
)

if not engine_ok:
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("VERDICT: FAIL -- block-10 engine reuse did not initialize; no theorem certificate emitted.")
    raise SystemExit(1)


F = engine_namespace["F"]
CR = engine_namespace["CR"]
W_of = engine_namespace["W_of"]
dag = engine_namespace["dag"]
matmul3 = engine_namespace["matmul3"]
cr_det = engine_namespace["cr_det"]
reg_gram = engine_namespace["reg_gram"]
norm_gram = engine_namespace["norm_gram"]
is_hermitian = engine_namespace["is_hermitian"]
leading_minors = engine_namespace["leading_minors"]


# ---------------------------------------------------------------------------
# T1: one exact tied measure and its independent formation-state extension
# ---------------------------------------------------------------------------
a0 = CR(F(4, 5))
b0 = CR(F(3, 10), F(1, 5))
c0 = b0.conj()
W0 = W_of(a0, b0, c0)

check(
    2,
    "the witness is exactly K-tied: a is real, c=conj(b), and W^dag=W",
    a0.im == 0 and c0 == b0.conj() and dag(W0) == W0,
    "a=4/5, b=3/10+i/5, c=3/10-i/5",
)

G0, Z0 = reg_gram(W0, W0)
Gn0 = norm_gram(G0, Z0)
minors0 = leading_minors(Gn0)
W0_sq = matmul3(W0, W0)
quarter_identity = [
    [CR(F(1, 4)) if i == j else CR(0) for j in range(3)]
    for i in range(3)
]
W0_sq_plus_quarter = [
    [W0_sq[i][j] + quarter_identity[i][j] for j in range(3)]
    for i in range(3)
]
Z0_factor = cr_det(W0_sq_plus_quarter)

check(
    3,
    "the reused engine gives the exact two-slice identity Z=det(W^2+I/4), with Z real and positive",
    Z0 == Z0_factor and Z0.im == 0 and Z0.re > 0,
    f"Z={Z0}",
)
check(
    4,
    "the tied records-only Gram is exactly Hermitian positive definite (five positive rational Sylvester minors)",
    is_hermitian(G0, Z0)
    and all(m.im == 0 and m.re > 0 for m in minors0),
    "registrable basis {1,N,TCsym,e2,e3}",
)


# The P-even registrable quotient: functions are constant on the doublet.
P_s = sp.diag(1, 0, 0)
P_d = sp.diag(0, 1, 1)
P_swap = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
x_s, x_d, y_s, y_d = sp.symbols("x_s x_d y_s y_d")
X = x_s * P_s + x_d * P_d
Y = y_s * P_s + y_d * P_d
XY_expected = x_s * y_s * P_s + x_d * y_d * P_d

check(
    5,
    "P_s and P_d generate the registrable function algebra C+C, with every readout constant on the doublet",
    P_s * P_s == P_s
    and P_d * P_d == P_d
    and P_s * P_d == sp.zeros(3)
    and P_s + P_d == sp.eye(3)
    and P_s.rank() == 1
    and P_d.rank() == 2
    and sp.simplify(X * Y - XY_expected) == sp.zeros(3)
    and P_swap * X * P_swap == X
    and X == sp.diag(x_s, x_d, x_d),
    "minimal central cells have carrier ranks 1 and 2",
)

w = sp.symbols("w", real=True)
w_d = sp.symbols("w_d", real=True)
normalization_solution = sp.solve(sp.Eq(w + w_d, 1), w_d)[0]
positive_domain = sp.reduce_inequalities([w >= 0, 1 - w >= 0], w)
expected_domain = sp.And(w >= 0, w <= 1)

check(
    6,
    "a normalized positive state on the two-cell quotient is exactly the one-number family phi_w=(w,1-w)",
    normalization_solution == 1 - w
    and sp.simplify(w + (1 - w)) == 1
    and sp.simplify(sp.Equivalent(positive_domain, expected_domain)) == sp.true,
    "0<=w<=1; no second dial coordinate survives normalization",
)

# Exact factorization through projection onto the measure component.  The first
# component of (M_tied, phi_w) is the same certificate for all formation states.
measure_certificate = [cr_to_sympy(Z0)]
measure_certificate.extend(cr_to_sympy(entry) for row in Gn0 for entry in row)
measure_certificate.extend(cr_to_sympy(minor) for minor in minors0)
projection_at_cell_counting = tuple(expr.subs(w, sp.Rational(1, 2)) for expr in measure_certificate)
projection_at_carrier_trace = tuple(expr.subs(w, sp.Rational(1, 3)) for expr in measure_certificate)

check(
    7,
    "every tied-measure certificate factors through projection away from phi_w and is unchanged when w changes",
    all(w not in expr.free_symbols and sp.diff(expr, w) == 0 for expr in measure_certificate)
    and projection_at_cell_counting == projection_at_carrier_trace,
    "exact equality at w=1/2 and w=1/3, representative of all w",
)


# ---------------------------------------------------------------------------
# T2: exact formation-gate arithmetic
# ---------------------------------------------------------------------------
a_sq, b_abs_sq, E_tot = sp.symbols("a_sq b_abs_sq E_tot", positive=True)
energy_solution = sp.solve(
    [sp.Eq(3 * a_sq, w * E_tot), sp.Eq(6 * b_abs_sq, (1 - w) * E_tot)],
    (a_sq, b_abs_sq),
    dict=True,
)[0]
r_derived = sp.factor(energy_solution[b_abs_sq] / energy_solution[a_sq])

check(
    8,
    "solving E_s=3a^2=w E_tot and E_d=6|b|^2=(1-w)E_tot derives r=(1-w)/(2w)",
    sp.simplify(r_derived - (1 - w) / (2 * w)) == 0,
    f"derived r={r_derived}",
)

w_cell = sp.solve(sp.Eq(w * E_tot, (1 - w) * E_tot), w)[0]
r_cell = sp.simplify(r_derived.subs(w, w_cell))
check(
    9,
    "uniformity over the two outcome cells solves w=1/2 and then r=1/2",
    w_cell == sp.Rational(1, 2) and r_cell == sp.Rational(1, 2),
    "E_s=E_d",
)

w_mode = sp.solve(sp.Eq((1 - w) * E_tot, 2 * w * E_tot), w)[0]
r_mode = sp.simplify(r_derived.subs(w, w_mode))
check(
    10,
    "uniformity per real mode (one singlet mode, two doublet modes) solves w=1/3 and then r=1",
    w_mode == sp.Rational(1, 3) and r_mode == 1,
    "E_d=2E_s",
)

r_symbol = sp.symbols("r", positive=True)
w_inverse = sp.solve(sp.Eq(r_symbol, r_derived), w)[0]
check(
    11,
    "the continuous fork has exactly one coordinate: w=1/(1+2r) is the inverse of r=(1-w)/(2w)",
    sp.simplify(w_inverse - 1 / (1 + 2 * r_symbol)) == 0,
    f"derived inverse w={w_inverse}",
)


# ---------------------------------------------------------------------------
# T3: the two canonical states are different restrictions
# ---------------------------------------------------------------------------
rho_carrier = sp.eye(3) / 3
carrier_w_s = sp.trace(rho_carrier * P_s)
carrier_w_d = sp.trace(rho_carrier * P_d)
carrier_r = sp.simplify(carrier_w_d / (2 * carrier_w_s))
carrier_functional = sp.simplify(sp.trace(rho_carrier * X))

check(
    12,
    "normalized trace on the supplied three-dimensional carrier restricts to weights (1/3,2/3), hence r=1",
    carrier_w_s == sp.Rational(1, 3)
    and carrier_w_d == sp.Rational(2, 3)
    and carrier_r == 1
    and carrier_functional == x_s / 3 + 2 * x_d / 3,
    "rho=I/3; dimension weighting",
)

rho_counting = sp.diag(sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4))
counting_w_s = sp.trace(rho_counting * P_s)
counting_w_d = sp.trace(rho_counting * P_d)
counting_r = sp.simplify(counting_w_d / (2 * counting_w_s))
counting_functional = sp.simplify(sp.trace(rho_counting * X))

check(
    13,
    "counting the two minimal central projections of C+C restricts to weights (1/2,1/2), hence r=1/2",
    counting_w_s == sp.Rational(1, 2)
    and counting_w_d == sp.Rational(1, 2)
    and counting_r == sp.Rational(1, 2)
    and counting_functional == (x_s + x_d) / 2,
    "rho=diag(1/2,1/4,1/4) on the carrier representation",
)


# ---------------------------------------------------------------------------
# T4/scope guards: the relocation occupies an explicitly disclaimed open gate
# ---------------------------------------------------------------------------
block9_text = normalize_markdown(BLOCK9_NOTE.read_text(encoding="utf-8"))
block10_text = normalize_markdown(BLOCK10_NOTE.read_text(encoding="utf-8"))
axioms_text = normalize_markdown(AXIOMS_NOTE.read_text(encoding="utf-8"))

block9_quote = (
    "no occupancy, weighting, or reading-section rule is adopted or derived. "
    "Both cells are lawful."
)
check(
    14,
    "block 9's exact does-not-claim sentence leaves occupancy/weighting/reading-section choice open",
    block9_quote in block9_text,
    "verbatim source guard",
)

block10_residual = (
    "no occupancy, weighting, or reading-section rule is adopted or derived. "
    "The per-cell equipartition/dial residual survives on the whole weight-reality set."
)
check(
    15,
    "block 10's exact does-not-claim/residual sentence leaves the formation dial untouched after weight-stage K-reality",
    block10_residual in block10_text,
    "verbatim source guard",
)

formation_gate_quote = (
    "formation rules (which admissible possibility a new record locks, at "
    "which site, with what weight, or at what rate);"
)
check(
    16,
    "the minimal axioms explicitly place formation rules, including with-what-weight, outside axiom content",
    formation_gate_quote in axioms_text,
    "verbatim source guard",
)


print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(
    "VERDICT: EXACT COMPATIBILITY AND FORMATION-GATE RELOCATION "
    "(BOUNDED_THEOREM); the tied measure coexists with phi_w, and w is not derived."
)
print(
    "T1: Block 10's tied Hermitian-PD two-slice measure extends to every state "
    "phi_w on C+C without changing any measure certificate."
)
print(
    "T2: Exact energy matching gives r=(1-w)/(2w), with cell counting "
    "w=1/2 -> r=1/2 and real-mode weighting w=1/3 -> r=1."
)
print(
    "T3: The named endpoints are restriction of normalized carrier trace and "
    "counting on the quotient's minimal central projections, respectively."
)
print(
    "T4: The sole relocated residue is the formation weight w; possible payers "
    "are formation dynamics, law-expressible-weight classification (in preparation), "
    "endpoint registration asymmetry (in preparation), or explicit owner admission."
)
print(
    "BINDING SURFACE: A landed theorem could have imposed phi_w=F(measure section) "
    "in block 9's does-not-claim surface, block 10's dial residual, or the axioms' "
    "open-gates list; none does so at the witnessed grade."
)
print(f"CHECKS: {PASS}/{PASS + FAIL} PASS; FAIL={FAIL}.")
print(
    "PROPOSED CLAIM_SCOPE: exact two-level compatibility on the time-homogeneous "
    "two-slice C_3 tied corner measure, formation fork r=(1-w)/(2w), and canonical "
    "endpoint identifications on A_reg=C+C; no selection of w."
)
print(
    "UNCERTAINTIES A HOSTILE AUDITOR COULD CONTEST: the supplied P-even orbit-clause "
    "grade, the energy-to-formation-state bridge, or a formation/measure binding "
    "theorem outside the witnessed block 9/10 and axiom surfaces."
)

raise SystemExit(0 if FAIL == 0 else 1)
