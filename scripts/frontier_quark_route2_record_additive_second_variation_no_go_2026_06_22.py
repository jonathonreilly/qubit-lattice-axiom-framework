#!/usr/bin/env python3
"""Record-additive scalar readout does not supply the Route-2 second variation."""

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


def monomial(w, degree):
    if degree >= 0:
        return w**degree
    return Fraction(1, 1) / (w ** (-degree))


def endpoint_from_ratio(ratio):
    q_t = Fraction(5, 6)
    s_te = Fraction(-2, 1)
    q_e = q_t * ratio
    rho_e = 6 * (q_e - 1)
    c_te = s_te * q_t / q_e
    return q_e, rho_e, c_te


print("Route-2 Record-additive second-variation no-go")
print("=" * 78)

note_rel = "docs/QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md"
note = read(note_rel)
note_lower = note.lower()

print("\nA. Source-note and authority boundary")
check("new source note exists", (ROOT / note_rel).exists(), note_rel)
check("new note declares no-go status", "**Actual current-surface status:** no-go" in note)
check("new note declares no_go claim type", "**Claim type:** no_go" in note)
check(
    "new note is not a blanket no-go against source action",
    "not a no-go against a future physical source-action theorem" in note,
)
check(
    "new note identifies the remaining second-variation import",
    "source-action, metric, log-barrier, Hessian" in note,
)
require_markers(
    "docs/MINIMAL_AXIOMS_2026-06-05.md",
    [
        "scalar readout `I` is finitely additive",
        "supplies no readout context",
        "weighting, normalization",
    ],
)
require_markers(
    "docs/QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md",
    [
        "scale-shift-invariant second variation",
        "does not derive that the Route-2 source row is such a second variation",
    ],
)
require_markers(
    "docs/QUARK_ROUTE2_SOURCE_ROW_DEGREE_SELECTOR_NO_GO_NOTE_2026-06-22.md",
    [
        "generic homogeneous source-row constraints do not select `d=-2`",
        "degree selector is the missing import",
    ],
)
require_markers(
    "docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
    [
        "fix the readout **norm**",
        "readout's **direction**",
    ],
)
require_markers(
    "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    [
        "endpoint triple",
        "not yet derived",
    ],
)

print("\nB. Finite-additive scalar response")
w_e = Fraction(1, 3)
w_t = Fraction(1, 2)
x = w_e
y = w_t
target_ratio = Fraction(9, 4)

def f_linear(w):
    return Fraction(7, 1) * w

h = Fraction(1, 6)
w0 = Fraction(1, 2)
linear_second_difference = f_linear(w0 + h) - 2 * f_linear(w0) + f_linear(w0 - h)
direct_additive_ratio = w_e / w_t
q_e_add, rho_e_add, c_te_add = endpoint_from_ratio(direct_additive_ratio)

check("linear finite-additive readout is additive", f_linear(x + y) == f_linear(x) + f_linear(y))
check("linear finite-additive readout has zero second difference", linear_second_difference == 0)
check("direct additive E/T ratio is 2/3", direct_additive_ratio == Fraction(2, 3))
check("direct additive ratio misses 9/4", direct_additive_ratio != target_ratio)
check("direct additive route gives q_E=5/9", q_e_add == Fraction(5, 9), f"q_E={q_e_add}")
check("direct additive route gives rho_E=-8/3", rho_e_add == Fraction(-8, 3), f"rho_E={rho_e_add}")
check("direct additive route gives c_TE=-3", c_te_add == Fraction(-3, 1), f"c_TE={c_te_add}")

print("\nC. Inverse-square and log-barrier obstruction")
additive_degrees = [
    n for n in range(-4, 5) if monomial(x + y, n) == monomial(x, n) + monomial(y, n)
]
inverse_square_left = monomial(x + y, -2)
inverse_square_right = monomial(x, -2) + monomial(y, -2)
q_e_hess, rho_e_hess, c_te_hess = endpoint_from_ratio(target_ratio)

check("monomial additivity scan selects only degree +1", additive_degrees == [1], f"degrees={additive_degrees}")
check(
    "inverse-square row is not finite-additive",
    inverse_square_left != inverse_square_right,
    f"(x+y)^-2={inverse_square_left}, x^-2+y^-2={inverse_square_right}",
)
check("inverse-square Hessian ratio is 9/4", target_ratio == Fraction(9, 4))
check("inverse-square route gives q_E=15/8", q_e_hess == Fraction(15, 8), f"q_E={q_e_hess}")
check("inverse-square route gives rho_E=21/4", rho_e_hess == Fraction(21, 4), f"rho_E={rho_e_hess}")
check("inverse-square route gives c_TE=-8/9", c_te_hess == Fraction(-8, 9), f"c_TE={c_te_hess}")
check("log-additivity witness fails at Route-2 weights", x + y != x * y, f"x+y={x+y}, xy={x*y}")
check("affine readout contributes no second variation", linear_second_difference == 0)

print("\nD. Normalization quotient does not rescue additivity")
def p_e(scale):
    return (scale * w_e) / (scale * (w_e + w_t))

p_second_radial = p_e(Fraction(3, 1)) - 2 * p_e(Fraction(2, 1)) + p_e(Fraction(1, 1))
normalized_diag_ratio = w_t / w_e
q_e_norm, rho_e_norm, c_te_norm = endpoint_from_ratio(normalized_diag_ratio)

check("normalized additive fraction is common-scale invariant", p_e(1) == p_e(2) == p_e(3), f"p_E={p_e(1)}")
check("normalized additive fraction has zero radial second difference", p_second_radial == 0)
check("normalized diagonal Hessian ratio is 3/2", normalized_diag_ratio == Fraction(3, 2))
check("normalized diagonal route gives q_E=5/4", q_e_norm == Fraction(5, 4), f"q_E={q_e_norm}")
check("normalized diagonal route gives rho_E=3/2", rho_e_norm == Fraction(3, 2), f"rho_E={rho_e_norm}")
check("normalized diagonal route gives c_TE=-4/3", c_te_norm == Fraction(-4, 3), f"c_TE={c_te_norm}")
check("normalized diagonal route misses 9/4", normalized_diag_ratio != target_ratio)

print("\nE. Current-surface boundary")
check("note records forbidden proof-input firewall", "Forbidden proof inputs:" in note and "observed masses" in note)
check("note keeps endpoint target open", "The endpoint target remains open." in note)
check(
    "note states the source-action/metric bridge remains needed",
    "derive a physical source-action/metric bridge" in note,
)
check(
    "note avoids endpoint closure rhetoric",
    "This note only prunes the Record-additive shortcut" in note,
)
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
    "STATUS: no-go. Minimal Record finite scalar additivity does not supply "
    "the nonzero second-variation Hessian needed by the Route-2 endpoint route; "
    "a source-action, metric, Hessian, ray-quotient, or equivalent physical bridge "
    "remains the live theorem target."
)
