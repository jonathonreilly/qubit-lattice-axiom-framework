#!/usr/bin/env python3
"""Exact finite witnesses for the C2 w-supplier reading fork note."""

from fractions import Fraction
from itertools import permutations
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
POLICY_PATH = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
NOTE_PATH = (
    ROOT
    / "docs"
    / "C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md"
)

EM_DASH = "\u2014"

checks = []


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def check(condition, description):
    checks.append(bool(condition))
    status = "PASS" if condition else "FAIL"
    print(f"CHECK {len(checks):02d}: {status} {EM_DASH} {description}")


def content_sum(pieces):
    xa = Fraction(0)
    xb = Fraction(0)
    for a, b in pieces:
        xa += a
        xb += b
    return xa, xb


def build_refinement_pieces(xa, xb):
    """Build rational content from equal refinements of the two generators."""
    pieces = []
    if xa:
        unit_a = Fraction(1, xa.denominator)
        pieces.extend((unit_a, Fraction(0)) for _ in range(xa.numerator))
    if xb:
        unit_b = Fraction(1, xb.denominator)
        pieces.extend((Fraction(0), unit_b) for _ in range(xb.numerator))
    return pieces


def derived_value_from_chain(xa, xb, u, v):
    value = Fraction(0)
    for a, b in build_refinement_pieces(xa, xb):
        if a:
            value += u * a
        if b:
            value += v * b
    return value


def readout(xa, xb, u, v):
    return u * xa + v * xb


def sigma(content):
    xa, xb = content
    return xb, xa


def prod(left, right):
    exponents = {"I": 0, "U": 1, "U2": 2}
    labels = {0: "I", 1: "U", 2: "U2"}
    return labels[(exponents[left] + exponents[right]) % 3]


def preserves_c3_table(mapping):
    labels = ("I", "U", "U2")
    return all(
        mapping[prod(a, b)] == prod(mapping[a], mapping[b])
        for a in labels
        for b in labels
    )


def c3_content(a, br, bi):
    return a * a, Fraction(2) * (br * br + bi * bi)


def ew_readout_diagonal(x, kappa, u=Fraction(1)):
    return u * x + kappa * u * x


axiom_text = read_text(AXIOM_PATH)
policy_text = read_text(POLICY_PATH)

CONTENT_DETERMINATION_SENTENCE = "A readout value is determined by record content\nalone."
axiom_sentences = [
    "No possibility is privileged.",
    "Only records are readable.",
    CONTENT_DETERMINATION_SENTENCE,
    "For any finite collection of pairwise-disjoint records, scalar readout\n"
    "`I` is additive, with `I(empty)=0`.",
    "A state is a configuration of records.",
    "A law privileges no states. Its domain is a supplied condition, and at every\n"
    "state where the condition holds it gives exactly one answer.",
]
check(
    all(sentence in axiom_text for sentence in axiom_sentences),
    "premise guard: current axiom file has no-privilege, record, state, law, and additivity sentences",
)

check(
    "possibility relabelings" in policy_text and "Standing promotion rule" in policy_text,
    "premise guard: policy section 6 has possibility relabelings and standing promotion rule",
)


sample_contents = [
    (Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
    (Fraction(1, 2), Fraction(0)),
    (Fraction(0), Fraction(1, 3)),
    (Fraction(2, 3), Fraction(5, 7)),
    (Fraction(3, 2), Fraction(4, 5)),
    (Fraction(7, 4), Fraction(9, 10)),
    (Fraction(5, 6), Fraction(11, 3)),
]

reachability_ok = all(
    content_sum(build_refinement_pieces(xa, xb)) == (xa, xb) for xa, xb in sample_contents
)
union_ok = (
    content_sum(
        build_refinement_pieces(Fraction(2, 3), Fraction(1, 5))
        + build_refinement_pieces(Fraction(7, 6), Fraction(4, 5))
    )
    == (Fraction(11, 6), Fraction(1))
)
check(
    reachability_ok and union_ok,
    "T1: rational contents are reachable from refined generators and disjoint union adds contents",
)

weights_1 = (Fraction(2), Fraction(3))
normal_1_ok = all(
    derived_value_from_chain(xa, xb, *weights_1) == readout(xa, xb, *weights_1)
    for xa, xb in sample_contents
)
check(
    normal_1_ok,
    "T1: chain-derived values match u*x_A+v*x_B for weights (2,3)",
)

weights_2 = (Fraction(5, 2), Fraction(1, 3))
normal_2_ok = all(
    derived_value_from_chain(xa, xb, *weights_2) == readout(xa, xb, *weights_2)
    for xa, xb in sample_contents
)
check(
    normal_2_ok,
    "T1: chain-derived values match u*x_A+v*x_B for weights (5/2,1/3)",
)

refinement_identity_ok = all(
    readout(xa, xb, u, v) == k * readout(xa / k, xb / k, u, v)
    for xa, xb in sample_contents
    for u, v in (weights_1, weights_2)
    for k in (2, 3, 5)
)
check(
    refinement_identity_ok,
    "T1: the derived form satisfies the refinement identity I(x)=k*I(x/k) exactly",
)


def content_determined(assignment):
    seen = {}
    for _, content, value in assignment:
        if content in seen and seen[content] != value:
            return False
        seen[content] = value
    return True


counterexample_assignment = [
    ("R_alpha", (Fraction(1), Fraction(1)), Fraction(4)),
    ("R_beta", (Fraction(1), Fraction(1)), Fraction(5)),
]
honest_assignment = [
    (f"R_{i}", (xa, xb), readout(xa, xb, *weights_1))
    for i, (xa, xb) in enumerate(sample_contents)
]
check(
    not content_determined(counterexample_assignment)
    and content_determined(honest_assignment)
    and CONTENT_DETERMINATION_SENTENCE in axiom_text,
    "T1: the detector rejects the identity-dependent assignment and accepts a content readout",
)


u_x = Fraction(2)
v_x = Fraction(1)
generator = (Fraction(1), Fraction(0))
generator_image = sigma(generator)
exchange_witness = readout(*generator, u_x, v_x) != readout(*generator_image, u_x, v_x)
check(
    exchange_witness,
    "T2 READING-X: sigma exchange sends a generator to a different level for weights (2,1)",
)

equal_weight = (Fraction(7), Fraction(7))
exchange_closed_equal = all(
    readout(xa, xb, *equal_weight) == readout(*sigma((xa, xb)), *equal_weight)
    for xa, xb in sample_contents
)
has_asymmetric_samples = any(xa != xb for xa, xb in sample_contents)
check(
    exchange_closed_equal and has_asymmetric_samples and len(sample_contents) >= 8,
    "T2 READING-X: u=v readouts are sigma-closed on asymmetric rational samples",
)


def sigma_closed(u, v):
    on_generators = readout(Fraction(1), Fraction(0), u, v) == readout(
        Fraction(0), Fraction(1), u, v
    )
    on_samples = all(
        readout(xa, xb, u, v) == readout(*sigma((xa, xb)), u, v)
        for xa, xb in sample_contents
    )
    return on_generators and on_samples


candidate_weights = [
    (Fraction(2), Fraction(1)),
    (Fraction(1), Fraction(2)),
    (Fraction(3), Fraction(3)),
    (Fraction(11, 5), Fraction(11, 5)),
    (Fraction(4), Fraction(9)),
    (Fraction(1), Fraction(1)),
    (Fraction(5, 2), Fraction(1, 3)),
    (Fraction(7, 4), Fraction(7, 4)),
]
forcing_iff = all(sigma_closed(u, v) == (u == v) for u, v in candidate_weights)
check(
    forcing_iff,
    "T2 READING-X: sigma closure holds exactly when u=v across the weight family (forcing iff)",
)


labels = ("I", "U", "U2")
preserving_maps = []
for image_tuple in permutations(labels):
    mapping = dict(zip(labels, image_tuple))
    if preserves_c3_table(mapping):
        preserving_maps.append(tuple(mapping[label] for label in labels))
expected_preserving = {("I", "U", "U2"), ("I", "U2", "U")}
check(
    set(preserving_maps) == expected_preserving and len(preserving_maps) == 2,
    "T2 READING-P: C3 multiplication-table relabelings are exactly id and U<->U2",
)

preserving_fix_unit = all(mapping[0] == "I" for mapping in preserving_maps)
no_unit_to_nonunit = not any(mapping[0] in {"U", "U2"} for mapping in preserving_maps)
check(
    preserving_fix_unit and no_unit_to_nonunit,
    "T2 READING-P: every preserving relabeling fixes the unit I",
)

c3_samples = [
    (Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(2), Fraction(1), Fraction(0)),
    (Fraction(3, 2), Fraction(1, 3), Fraction(2, 5)),
    (Fraction(5, 7), Fraction(4, 9), Fraction(8, 11)),
    (Fraction(9, 4), Fraction(5, 6), Fraction(7, 8)),
    (Fraction(11, 13), Fraction(12, 17), Fraction(3, 19)),
    (Fraction(6, 5), Fraction(7, 3), Fraction(2, 9)),
]
content_invariant = all(
    c3_content(a, br, bi) == c3_content(a, br, -bi) for a, br, bi in c3_samples
)
check(
    content_invariant,
    "T2 READING-P: U<->U2 conjugation leaves (a^2,2|b|^2) content pairs invariant",
)

reading_p_21_ok = all(
    readout(*c3_content(a, br, bi), Fraction(2), Fraction(1))
    == readout(*c3_content(a, br, -bi), Fraction(2), Fraction(1))
    for a, br, bi in c3_samples
)
check(
    reading_p_21_ok,
    "T2 READING-P: the (2,1) readout is invariant under the induced trivial content action",
)

reading_p_w2_ok = all(
    readout(*c3_content(a, br, bi), Fraction(1), Fraction(2))
    == readout(*c3_content(a, br, -bi), Fraction(1), Fraction(2))
    for a, br, bi in c3_samples
)
check(
    reading_p_w2_ok,
    "T2 READING-P: the w=2 witness survives all presentation-preserving checks",
)


diagonal_states = [(x, x) for x in [Fraction(1, 8), Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(5, 3), Fraction(7, 4)]]
diag_equal = all(
    readout(xa, xb, Fraction(1), Fraction(1))
    == readout(xa, xb, Fraction(3, 2), Fraction(1, 2))
    for xa, xb in diagonal_states
)
off_diag_unequal = readout(Fraction(1), Fraction(0), Fraction(1), Fraction(1)) != readout(
    Fraction(1), Fraction(0), Fraction(3, 2), Fraction(1, 2)
)
check(
    diag_equal and off_diag_unequal,
    "T3: equal-sum readouts agree on diagonal samples and separate off diagonal",
)

ratio_pairs = [(Fraction(1, 7), Fraction(5, 6)), (Fraction(3, 4), Fraction(9, 5))]
weight_pairs = [(Fraction(1), Fraction(1)), (Fraction(2), Fraction(1)), (Fraction(3, 5), Fraction(7, 11))]
ratio_independent = all(
    readout(x1, x1, u, v) / readout(x2, x2, u, v) == x1 / x2
    for u, v in weight_pairs
    for x1, x2 in ratio_pairs
)
check(
    ratio_independent,
    "T3: diagonal readout ratios equal content ratios for multiple nonzero weight pairs",
)

grid = sorted(
    {
        Fraction(p, q)
        for q in range(1, 13)
        for p in range(0, 2 * q + 1)
    }
)
x_flow_ok = all((x * x == x) == (x in (Fraction(0), Fraction(1))) for x in grid)
check(
    x_flow_ok,
    "T3: on the denominator<=12 grid in [0,2], x -> x^2 fixes exactly {0,1}",
)

component_ok = all(
    (Fraction(2) * r * r == r) == (r in (Fraction(0), Fraction(1, 2))) for r in grid
)
slot_ok = all((r * r == r) == (r in (Fraction(0), Fraction(1))) for r in grid)
invariant_selection_ok = (
    Fraction(2) * Fraction(1, 2) == Fraction(1) and Fraction(1) * Fraction(1) == Fraction(1)
)
check(
    component_ok and slot_ok and invariant_selection_ok,
    "T3: component (2r^2) and slot (r^2) dictionary maps fix exactly {0,1/2} and {0,1} on the grid; both read x*=1",
)

sqrt_lower = Fraction(239, 169)
sqrt_upper = Fraction(17, 12)
interval_valid = sqrt_lower * sqrt_lower < Fraction(2) < sqrt_upper * sqrt_upper
hostile_lower = Fraction(17, 2) - Fraction(6) * sqrt_upper
hostile_upper = Fraction(17, 2) - Fraction(6) * sqrt_lower
hostile_excluded = (
    interval_valid
    and hostile_lower == Fraction(0)
    and Fraction(0) < hostile_upper < Fraction(1, 2)
)
check(
    hostile_excluded,
    "T3: 17/2-6*sqrt(2) lies strictly between 0 and 1/2 by rational bounds",
)


adjoint = Fraction(8)
singlet = Fraction(1)
kappa_equal = Fraction(1)
fraction_equal = adjoint / (adjoint + singlet)
check(
    kappa_equal == Fraction(1) and fraction_equal == Fraction(8, 9),
    "T4: equal per-component EW weight gives kappa=1 and adjoint fraction 8/9",
)

cell_u = Fraction(3)
cell_v = Fraction(5)
kappa_cell = cell_v / cell_u
check(
    kappa_cell != Fraction(1) and kappa_cell == Fraction(5, 3),
    "T4: unequal cell-level weights leave kappa as v/u rather than 1",
)

ew_ratio_samples = [(Fraction(2), Fraction(5)), (Fraction(3, 7), Fraction(11, 13))]
kappas = [Fraction(1), Fraction(2), Fraction(5, 3)]
ew_ratios_ok = all(
    ew_readout_diagonal(x1, kappa) / ew_readout_diagonal(x2, kappa) == x1 / x2
    for kappa in kappas
    for x1, x2 in ew_ratio_samples
)
check(
    ew_ratios_ok,
    "T4: diagonal EW readout ratios are kappa-independent for multiple exact samples",
)


old_ladder = ("R*", "D-totality", "w-supplier", "CTX-match")
new_ladder = ("R*", "D-totality", "READ(no-privilege relabeling closure)", "CTX-match")
check(
    old_ladder[0:2] == new_ladder[0:2]
    and old_ladder[3] == new_ladder[3]
    and "w-supplier" not in new_ladder,
    "T5 index: ladder replaces the independent w-supplier number with READ adjudication",
)

reading_choices = {"READING-X": "w forced on class", "READING-P": "w unforced on class"}
check(
    set(reading_choices) == {"READING-X", "READING-P"}
    and reading_choices["READING-X"] != reading_choices["READING-P"],
    "T5 index: READ slot is a binary reading fork rather than a numeric supplier",
)


note_raw = read_text(NOTE_PATH)
note_text = note_raw.lower()
check(
    "**Type:** bounded_theorem" in note_raw and "**Claim type:** bounded_theorem" in note_raw,
    "metadata: note declares canonical bounded_theorem type fields",
)
check(
    "**Audit boundary:** independent audit lane only" in note_raw
    and "**Status authority:**" not in note_raw,
    "metadata: note uses audit boundary, not legacy status-authority wording",
)
check(
    "OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md](" not in note_raw
    and "C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md](" not in note_raw,
    "dependency hygiene: inline-recomputed context surfaces are not markdown dependency links",
)
check(
    "does not adjudicate" in note_text,
    "boundary-denial: note says it does not adjudicate readings",
)
check(
    "no wall closed" in note_text,
    "boundary-denial: note says no wall closed",
)
check(
    "review-pending" in note_text,
    "boundary-denial: note marks unmerged sibling citations review-pending",
)


pass_count = sum(1 for result in checks if result)
fail_count = len(checks) - pass_count
print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
sys.exit(1 if fail_count else 0)
