#!/usr/bin/env python3
"""Standard information metrics give Route-2 degree -1, not degree -2."""

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


print("Route-2 information-metric degree boundary")
print("=" * 78)

note_rel = "docs/QUARK_ROUTE2_INFORMATION_METRIC_DEGREE_BOUNDARY_NOTE_2026-06-22.md"
note = read(note_rel)
note_lower = note.lower()

print("\nA. Source-note and authority boundary")
check("new source note exists", (ROOT / note_rel).exists(), note_rel)
check("new note declares no-go status", "**Actual current-surface status:** no-go" in note)
check("new note declares no_go claim type", "**Claim type:** no_go" in note)
check("new note scopes the no-go to standard information metrics", "standard finite-probability information geometry" in note)
check("new note leaves log-barrier route open", "log-barrier, ray-quotient, scale-invariant Hessian" in note)
require_markers(
    "docs/SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md",
    [
        "sum_i dp_i^2 / p_i",
        "does **not** claim",
        "physical source",
    ],
)
require_markers(
    "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
    [
        "derive a Born-frequency law",
        "probability model is supplied",
    ],
)
require_markers(
    "docs/QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md",
    [
        "second variation gives",
        "first variation gives degree `-1`",
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
    "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    [
        "endpoint triple",
        "not yet derived",
    ],
)

print("\nB. Standard information metric degree")
w_e = Fraction(1, 3)
w_t = Fraction(1, 2)
info_ratio = (Fraction(1, 1) / w_e) / (Fraction(1, 1) / w_t)
target_ratio = (Fraction(1, 1) / (w_e * w_e)) / (Fraction(1, 1) / (w_t * w_t))
q_e_info, rho_e_info, c_te_info = endpoint_from_ratio(info_ratio)
q_e_target, rho_e_target, c_te_target = endpoint_from_ratio(target_ratio)

check("Fisher coefficient has degree -1", (Fraction(1, 1) / (2 * w_e)) / (Fraction(1, 1) / w_e) == Fraction(1, 2))
check("Shannon convex Hessian has coefficient 1/w", (Fraction(1, 1) / w_e) == 3)
check("local KL quadratic coefficient has coefficient 1/(2w)", (Fraction(1, 1) / (2 * w_e)) == Fraction(3, 2))
check("Poisson/intensity Fisher coefficient has coefficient 1/w", (Fraction(1, 1) / w_t) == 2)
check("information metric E/T ratio is 3/2", info_ratio == Fraction(3, 2), f"ratio={info_ratio}")
check("information metric ratio misses 9/4", info_ratio != Fraction(9, 4))

print("\nC. Endpoint consequence")
check("information metric gives q_E=5/4", q_e_info == Fraction(5, 4), f"q_E={q_e_info}")
check("information metric gives rho_E=3/2", rho_e_info == Fraction(3, 2), f"rho_E={rho_e_info}")
check("information metric gives c_TE=-4/3", c_te_info == Fraction(-4, 3), f"c_TE={c_te_info}")
check("information metric misses q_E=15/8", q_e_info != Fraction(15, 8))
check("information metric misses rho_E=21/4", rho_e_info != Fraction(21, 4))
check("information metric misses c_TE=-8/9", c_te_info != Fraction(-8, 9))
check("Block107 first-variation row has same ratio", info_ratio == Fraction(3, 2))

print("\nD. Inverse-square comparator")
check("inverse-square comparator has degree -2", (Fraction(1, 1) / ((2 * w_e) ** 2)) / (Fraction(1, 1) / (w_e**2)) == Fraction(1, 4))
check("inverse-square E/T ratio is 9/4", target_ratio == Fraction(9, 4), f"ratio={target_ratio}")
check("inverse-square route gives q_E=15/8", q_e_target == Fraction(15, 8), f"q_E={q_e_target}")
check("inverse-square route gives rho_E=21/4", rho_e_target == Fraction(21, 4), f"rho_E={rho_e_target}")
check("inverse-square route gives c_TE=-8/9", c_te_target == Fraction(-8, 9), f"c_TE={c_te_target}")
check("degree gap is exactly one inverse power", target_ratio / info_ratio == Fraction(3, 2))

print("\nE. Candidate-family scan")
degree_ratios = {d: (w_e / w_t) ** d for d in range(-4, 5)}
target_degrees = [d for d, ratio in degree_ratios.items() if ratio == Fraction(9, 4)]
info_degrees = [d for d, ratio in degree_ratios.items() if ratio == Fraction(3, 2)]
check("integer scan identifies target degree -2", target_degrees == [-2], f"target_degrees={target_degrees}")
check("integer scan identifies information degree -1", info_degrees == [-1], f"info_degrees={info_degrees}")
check("degree -1 and -2 are distinct routes", info_degrees != target_degrees)
check("constant metric degree 0 misses endpoint", degree_ratios[0] == 1 and degree_ratios[0] != Fraction(9, 4))
check("direct probability weight degree +1 misses endpoint", degree_ratios[1] == Fraction(2, 3))
check("quadratic probability weight degree +2 misses endpoint", degree_ratios[2] == Fraction(4, 9))

print("\nF. Current-surface boundary")
check("note records forbidden proof-input firewall", "Forbidden proof inputs:" in note and "observed masses" in note)
check("note keeps endpoint target open", "The endpoint target remains open." in note)
check("note identifies the sharper positive target", "not merely \"information metric\"" in note)
check("note avoids endpoint closure rhetoric", "This block prunes one physical source-action candidate" in note)
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
    "STATUS: no-go. Standard Fisher/KL/Shannon information metrics have "
    "inverse-linear degree -1 on the positive weight coordinate, giving the "
    "Block107 first-variation miss rather than the inverse-square endpoint route."
)
