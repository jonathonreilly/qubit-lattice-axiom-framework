#!/usr/bin/env python3
"""Log-action cocycle plus Hessian readout gives the Route-2 inverse-square row."""

from fractions import Fraction
from pathlib import Path


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {name}" + (f" -- {detail}" if detail else ""))


def read(rel):
    return (ROOT / rel).read_text()


def require_markers(rel, markers):
    content = read(rel)
    ok = True
    for marker in markers:
        if marker not in content:
            ok = False
            print(f"FAIL: {rel} missing marker: {marker}")
    check(f"{rel} contains required markers", ok, ", ".join(markers))


def endpoint_from_ratio(ratio):
    q_t = Fraction(5, 6)
    s_te = Fraction(-2, 1)
    q_e = q_t * ratio
    rho_e = 6 * (q_e - 1)
    c_te = s_te * q_t / q_e
    return q_e, rho_e, c_te


print("Route-2 log-action cocycle Hessian boundary")
print("=" * 78)

note_rel = "docs/QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md"
note = read(note_rel)
note_lower = note.lower()

print("\nA. Source-note and authority boundary")
check("new source note exists", (ROOT / note_rel).exists(), note_rel)
check("new note declares exact-support/open status", "**Actual current-surface status:** exact-support" in note)
check("new note declares open_gate claim type", "**Claim type:** open_gate" in note)
check("new note states the cocycle premise", "multiplicative-to-additive cocycle" in note)
check("new note leaves physical premise open", "does not assert that premise as current framework content" in note)
require_markers(
    "docs/QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md",
    [
        "scale-shift-invariant second variation",
        "Phi''(w) = C/w^2",
    ],
)
require_markers(
    "docs/QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md",
    [
        "does not derive the Block107 premise",
        "source-action, metric, log-barrier, Hessian",
    ],
)
require_markers(
    "docs/QUARK_ROUTE2_INFORMATION_METRIC_DEGREE_BOUNDARY_NOTE_2026-06-22.md",
    [
        "standard finite-probability information geometry",
        "degree `-1`, not degree `-2`",
    ],
)
require_markers(
    "docs/SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md",
    [
        "Product composition selects the logarithmic",
        "does not by itself select the physical logarithmic",
    ],
)
require_markers(
    "docs/REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md",
    [
        "multiplicative-to-additive Cauchy equation",
        "continuity on the positive real",
    ],
)
require_markers(
    "docs/FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM_2026-06-04.md",
    [
        "Record axiom alone supplies log-det readout",
        "requires the additive",
    ],
)
require_markers(
    "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    [
        "endpoint triple",
        "not yet derived",
    ],
)

print("\nB. Multiplicative cocycle finite witness")
# Work in an exact exponent coordinate: w = base^n. A differentiable additive
# character over multiplication is linear in n, i.e. log-like.
base = Fraction(3, 2)
scale = Fraction(7, 1)

def log_cocycle_on_power(n):
    return scale * n

check("cocycle identity holds in exponent coordinate", log_cocycle_on_power(2 + -3) == log_cocycle_on_power(2) + log_cocycle_on_power(-3))
check("identity element has zero action", log_cocycle_on_power(0) == 0)
check("inverse powers change sign", log_cocycle_on_power(-2) == -log_cocycle_on_power(2))

def raw_weight_on_power(n):
    return base**n

raw_cocycle_residual = raw_weight_on_power(1 + 2) - raw_weight_on_power(1) - raw_weight_on_power(2)
check("raw multiplicative weight is not additive under multiplication", raw_cocycle_residual != 0, f"residual={raw_cocycle_residual}")

print("\nC. Hessian row consequence")
w_e = Fraction(1, 3)
w_t = Fraction(1, 2)
log_hessian_ratio = (Fraction(1, 1) / (w_e * w_e)) / (Fraction(1, 1) / (w_t * w_t))
log_first_ratio = (Fraction(1, 1) / w_e) / (Fraction(1, 1) / w_t)
direct_weight_ratio = w_e / w_t
q_e, rho_e, c_te = endpoint_from_ratio(log_hessian_ratio)
q_e_first, rho_e_first, c_te_first = endpoint_from_ratio(log_first_ratio)
q_e_weight, rho_e_weight, c_te_weight = endpoint_from_ratio(direct_weight_ratio)

check("log Hessian coefficient has degree -2", (Fraction(1, 1) / ((2 * w_e) ** 2)) / (Fraction(1, 1) / (w_e**2)) == Fraction(1, 4))
check("log first derivative has degree -1", (Fraction(1, 1) / (2 * w_e)) / (Fraction(1, 1) / w_e) == Fraction(1, 2))
check("log Hessian E/T ratio is 9/4", log_hessian_ratio == Fraction(9, 4), f"ratio={log_hessian_ratio}")
check("log first-derivative E/T ratio is 3/2", log_first_ratio == Fraction(3, 2), f"ratio={log_first_ratio}")
check("direct weight E/T ratio is 2/3", direct_weight_ratio == Fraction(2, 3), f"ratio={direct_weight_ratio}")
check("only Hessian ratio hits endpoint target", log_hessian_ratio == Fraction(9, 4) and log_first_ratio != Fraction(9, 4) and direct_weight_ratio != Fraction(9, 4))

print("\nD. Endpoint consequence")
check("log-action Hessian route gives q_E=15/8", q_e == Fraction(15, 8), f"q_E={q_e}")
check("log-action Hessian route gives rho_E=21/4", rho_e == Fraction(21, 4), f"rho_E={rho_e}")
check("log-action Hessian route gives c_TE=-8/9", c_te == Fraction(-8, 9), f"c_TE={c_te}")
check("first derivative falsifier gives q_E=5/4", q_e_first == Fraction(5, 4), f"q_E={q_e_first}")
check("first derivative falsifier gives rho_E=3/2", rho_e_first == Fraction(3, 2), f"rho_E={rho_e_first}")
check("first derivative falsifier gives c_TE=-4/3", c_te_first == Fraction(-4, 3), f"c_TE={c_te_first}")
check("direct weight falsifier gives q_E=5/9", q_e_weight == Fraction(5, 9), f"q_E={q_e_weight}")
check("direct weight falsifier gives rho_E=-8/3", rho_e_weight == Fraction(-8, 3), f"rho_E={rho_e_weight}")
check("direct weight falsifier gives c_TE=-3", c_te_weight == Fraction(-3, 1), f"c_TE={c_te_weight}")

print("\nE. Degree-family separation")
degree_ratios = {d: (w_e / w_t) ** d for d in range(-4, 5)}
target_degrees = [d for d, ratio in degree_ratios.items() if ratio == Fraction(9, 4)]
first_degrees = [d for d, ratio in degree_ratios.items() if ratio == Fraction(3, 2)]
weight_degrees = [d for d, ratio in degree_ratios.items() if ratio == Fraction(2, 3)]
check("integer scan identifies target degree -2", target_degrees == [-2], f"target_degrees={target_degrees}")
check("integer scan identifies first-derivative degree -1", first_degrees == [-1], f"first_degrees={first_degrees}")
check("integer scan identifies direct-weight degree +1", weight_degrees == [1], f"weight_degrees={weight_degrees}")
check("generic degree family remains nonselective", len(degree_ratios) == 9 and target_degrees != first_degrees)

print("\nF. Current-surface boundary")
check("note records forbidden proof-input firewall", "Forbidden proof inputs:" in note and "observed masses" in note)
check("note identifies remaining physical theorem", "derive that the Route-2 E/T source/readout primitive" in note)
check("note preserves parent open status", "The actual current surface remains open." in note)
check("note avoids endpoint-closure rhetoric", "future theorem premise" in note and "not asserted as" in note)
check(
    "new note has no retained proposal wording",
    "proposed_retained" not in note_lower
    and "would become retained" not in note_lower
    and "retained branch-local" not in note_lower,
)

print()
print("=" * 78)
print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
print(
    "STATUS: exact-support/open boundary. A multiplicative log-action cocycle "
    "plus Hessian row readout in w supplies the inverse-square Route-2 row and "
    "endpoint arithmetic, but the current surface does not derive that physical "
    "source/readout premise."
)
