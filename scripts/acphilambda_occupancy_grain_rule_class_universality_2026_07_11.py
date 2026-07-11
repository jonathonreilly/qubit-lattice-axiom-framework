#!/usr/bin/env python3
"""Exact checks for the bounded occupancy-grain rule-class theorem note."""

from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MINIMAL = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
CLASS_NOTE = (
    ROOT
    / "docs/RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md"
)
ADOPTION = ROOT / "docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md"
NO_GO = (
    ROOT
    / "docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md"
)

PASS_COUNT = 0
FAIL_COUNT = 0
BLOCK_COUNTS = {}


def flat(text):
    """Normalize markdown prose only for verbatim-with-wrapping checks."""
    return " ".join(text.split())


def check(block, label, condition):
    """Print one computed check result."""
    global PASS_COUNT, FAIL_COUNT
    BLOCK_COUNTS[block] = BLOCK_COUNTS.get(block, 0) + 1
    number = BLOCK_COUNTS[block]
    passed = bool(condition)
    if passed:
        PASS_COUNT += 1
        result = "PASS"
    else:
        FAIL_COUNT += 1
        result = "FAIL"
    print(f"{block}.{number} {result}: {label}")


minimal_text = MINIMAL.read_text(encoding="utf-8")
class_text = CLASS_NOTE.read_text(encoding="utf-8")
adoption_text = ADOPTION.read_text(encoding="utf-8")
no_go_text = NO_GO.read_text(encoding="utf-8")


print("[U1] Verbatim Record-clause memo checks")
permanence_clause = (
    "A site never carries more than one record; records are permanent."
)
readability_clause = (
    "Only records are readable. A readout value is determined by record content alone."
)
additivity_clause = (
    "For any finite collection of pairwise-disjoint records, scalar readout "
    "`I` is additive, with `I(empty)=0`."
)
check("U1", "permanence clause occurs verbatim", flat(permanence_clause) in flat(minimal_text))
check("U1", "readability clause occurs verbatim", flat(readability_clause) in flat(minimal_text))
check("U1", "additivity and I(empty)=0 occur verbatim", flat(additivity_clause) in flat(minimal_text))


print("[U2] Permanence-to-stationarity mechanical implication")
q, t = sp.symbols("q t", real=True)
I_s, I_d = sp.symbols("I_s I_d", real=True)
Delta_I = sp.symbols("Delta_I", nonzero=True, real=True)
readout_q = (1 - q) * I_s + q * I_d
readout_t = (1 - t) * I_s + t * I_d
readout_change = sp.factor(readout_t - readout_q)
expected_change = (t - q) * (I_d - I_s)
check(
    "U2",
    "a moved weight changes the affine content readout by (t-q)(I_d-I_s)",
    sp.simplify(readout_change - expected_change) == 0,
)
nondegenerate_change = readout_change.subs(I_d, I_s + Delta_I)
stationary_solution = sp.solve(sp.Eq(nondegenerate_change, 0), t)
check(
    "U2",
    "nondegenerate content readout equality forces t=q",
    stationary_solution == [q],
)
q_witness = sp.Rational(1, 3)
t_witness = q_witness**2 / (q_witness**2 + (1 - q_witness) ** 2)
witness_change = readout_change.subs(
    {q: q_witness, t: t_witness, I_s: sp.Integer(2), I_d: sp.Integer(7)}
)
check(
    "U2",
    "strict repeat-write witness is readout-visible between steps",
    sp.simplify(witness_change) != 0,
)


print("[U3] Symmetric record-influence family and repeat-write exemplar")
sector_weights = sp.Matrix([q, 1 - q])
repeat_weights = sector_weights.multiply_elementwise(sector_weights)
repeat_Z = sp.Add(*repeat_weights)
lueders_update = sp.cancel(repeat_weights[0] / repeat_Z)
check(
    "U3",
    "repeat write multiplies the two influence weights to q^2 and (1-q)^2",
    repeat_weights == sp.Matrix([q**2, (1 - q) ** 2]),
)
check(
    "U3",
    "normalization gives q -> q^2/(q^2+(1-q)^2) exactly",
    sp.simplify(lueders_update - q**2 / (q**2 + (1 - q) ** 2)) == 0,
)
f = sp.Function("f")
general_update = f(q) / (f(q) + f(1 - q))
exchanged_update = general_update.xreplace({q: 1 - q})
check(
    "U3",
    "the common-f family obeys T(1-q)=1-T(q)",
    sp.simplify(exchanged_update + general_update - 1) == 0,
)
k = sp.symbols("k", positive=True)
power_update = q**k / (q**k + (1 - q) ** k)
check(
    "U3",
    "the k=2 power-family member is the repeat-write exemplar",
    sp.simplify(power_update.subs(k, 2) - lueders_update) == 0,
)


print("[U4] Universal fixed points and equal-power-per-block arithmetic")
F_half, F_one = sp.symbols("F_half F_one", positive=True)


def normalized_pair(left, right):
    return sp.cancel(left / (left + right))


check(
    "U4",
    "f(0)=0 and f(1)>0 fix q=0",
    sp.simplify(normalized_pair(0, F_one)) == 0,
)
check(
    "U4",
    "exchange symmetry fixes q=1/2",
    sp.simplify(normalized_pair(F_half, F_half) - sp.Rational(1, 2)) == 0,
)
check(
    "U4",
    "f(0)=0 and f(1)>0 fix q=1",
    sp.simplify(normalized_pair(F_one, 0) - 1) == 0,
)
F_q, F_1q = sp.symbols("F_q F_1q", positive=True)
fixed_numerator = sp.together(F_q / (F_q + F_1q) - q).as_numer_denom()[0]
odds_numerator = sp.expand(F_q * (1 - q) - q * F_1q)
check(
    "U4",
    "an interior fixed point is exactly the input-odds equality",
    sp.simplify(fixed_numerator - odds_numerator) == 0,
)
for exponent in (sp.Integer(2), sp.Integer(3), sp.Rational(5, 2), sp.Integer(4)):
    fixed_equation = sp.Eq(
        q**exponent * (1 - q),
        q * (1 - q) ** exponent,
    )
    exact_solutions = sp.solve(fixed_equation, q)
    check(
        "U4",
        f"exact solve for k={exponent} has only 0, 1/2, 1",
        set(exact_solutions) == {sp.Integer(0), sp.Rational(1, 2), sp.Integer(1)},
    )

a2, b2, r = sp.symbols("a2 b2 r", positive=True)
p_s_raw = a2 / (a2 + 2 * b2)
p_d_raw = 2 * b2 / (a2 + 2 * b2)
p_d_from_r = sp.cancel(p_d_raw.subs(b2, r * a2))
p_s_from_r = sp.cancel(p_s_raw.subs(b2, r * a2))
check(
    "U4",
    "a^2 and two |b|^2 contributions give p_d=2r/(1+2r)",
    sp.simplify(p_d_from_r - 2 * r / (1 + 2 * r)) == 0,
)
check(
    "U4",
    "the derived two-sector occupancies normalize exactly",
    sp.simplify(p_s_from_r + p_d_from_r - 1) == 0,
)
r_half_solution = sp.solve(sp.Eq(p_d_from_r, sp.Rational(1, 2)), r)
check(
    "U4",
    "p_d=1/2 is equivalent to r=1/2",
    r_half_solution == [sp.Rational(1, 2)],
)


print("[U5] Load-bearing negative controls")
asymmetric_update = q**3 / (q**3 + (1 - q) ** 2)
asymmetric_fixed = sp.solveset(
    sp.Eq(asymmetric_update, q),
    q,
    domain=sp.Interval.open(0, 1),
)
shifted_root = (sp.sqrt(5) - 1) / 2
check(
    "U5",
    "N1 asymmetric f_d(x)=x^3, f_s(x)=x^2 has one exact interior fixed point",
    asymmetric_fixed == sp.FiniteSet(shifted_root),
)
check(
    "U5",
    "N1 asymmetric interior fixed point is not 1/2",
    sp.simplify(shifted_root - sp.Rational(1, 2)) != 0,
)
check(
    "U5",
    "N1 q=1/2 is moved by the asymmetric update",
    sp.simplify(asymmetric_update.subs(q, sp.Rational(1, 2)) - sp.Rational(1, 2))
    != 0,
)
identity_update = sp.cancel(q / (q + (1 - q)))
check(
    "U5",
    "N2 f(q)=q makes every q a fixed point",
    sp.simplify(identity_update - q) == 0,
)

p1, p2 = sp.symbols("p1 p2", real=True)
p3 = 1 - p1 - p2
three_Z = p1**2 + p2**2 + p3**2
three_update = [sp.cancel(component**2 / three_Z) for component in (p1, p2, p3)]
uniform_subs = {p1: sp.Rational(1, 3), p2: sp.Rational(1, 3)}
check(
    "U5",
    "N3 the three-sector symmetric square sharpening fixes (1/3,1/3,1/3)",
    all(
        sp.simplify(component.subs(uniform_subs) - sp.Rational(1, 3)) == 0
        for component in three_update
    ),
)
three_equations = [
    sp.together(three_update[0] - p1).as_numer_denom()[0],
    sp.together(three_update[1] - p2).as_numer_denom()[0],
]
three_solutions = sp.solve(three_equations, (p1, p2), dict=True)
interior_three_solutions = []
for solution in three_solutions:
    values = (solution[p1], solution[p2], sp.simplify(p3.subs(solution)))
    if all(bool(value > 0) for value in values):
        interior_three_solutions.append(values)
check(
    "U5",
    "N3 exact solve has the uniform point as its only simplex-interior fixed point",
    interior_three_solutions
    == [(sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3))],
)
per_sector_r_solution = sp.solve(
    sp.Eq(r / (1 + 2 * r), sp.Rational(1, 3)),
    r,
)
check(
    "U5",
    "N3 per-sector uniform occupancy reads r=1",
    per_sector_r_solution == [sp.Integer(1)],
)


print("[U6] Consumed-scope text checks")
class_statement = (
    "Thus every admissible blank-input one-step write under these declared readings "
    "is, up to a register basis unitary and register phase choice, in the "
    "controlled-copy isometry class."
)
single_orbit_statement = (
    "The class is therefore one register-unitary orbit, with column phases included "
    "in `U_R`."
)
candidate_one = """For the AC_phi_lambda charged-lepton matter-action surface, the physical
statistical grain is the K/CPT orbit or holomorphic-pair occupancy grain:
the doublet contributes once per K/CPT orbit rather than once per sector or
channel. This premise supplies only the matter-action occupancy grain needed
to discharge the surviving AC(i) measure-side realization binary."""
adoption_boundary = (
    "It supplies no value of `r`, `delta`, charged-lepton mass, mixing angle, "
    "probability rule, above-C3 taste/Dirac/chirality content, CKM/PMNS alignment, "
    "or sector-weight law."
)
no_go_boundary = (
    "The surviving no-go is only: the current minimal axioms do **not** force the "
    "formation rule/process/state/site/weight/rate."
)
check(
    "U6",
    "sibling controlled-copy class statement is consumed verbatim",
    flat(class_statement) in flat(class_text),
)
check(
    "U6",
    "sibling R5 single-register-orbit statement is consumed verbatim",
    flat(single_orbit_statement) in flat(class_text),
)
check(
    "U6",
    "adoption Candidate 1 is consumed verbatim",
    flat(candidate_one) in flat(adoption_text),
)
check(
    "U6",
    "adoption value and sector-weight boundary is consumed verbatim",
    flat(adoption_boundary) in flat(adoption_text),
)
check(
    "U6",
    "narrowed formation no-go boundary is consumed verbatim",
    flat(no_go_boundary) in flat(no_go_text),
)


print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
sys.exit(1 if FAIL_COUNT else 0)
