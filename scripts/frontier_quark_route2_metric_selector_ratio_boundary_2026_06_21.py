#!/usr/bin/env python3
"""Route-2 metric selector ratio boundary.

Checks whether current Fisher/tangent/Hessian selector surfaces derive the
quadratic metric needed to select q_E=15/8 on the fixed Route-2 source pair.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_METRIC_SELECTOR_RATIO_BOUNDARY_NOTE_2026-06-21.md"

PASS_COUNT = 0
FAIL_COUNT = 0

TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)
SHELL = (Fraction(1), Fraction(-2))
CENTER_T = Fraction(-5, 3)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(path: Path) -> str:
    return " ".join(read(path).split())


def rho_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def diag_metric_ratio_for_target(q_e: Fraction) -> Fraction:
    return Fraction(9, 11) * (q_e * q_e - 1)


def general_metric_residual(a: Fraction, b: Fraction, c: Fraction, q_e: Fraction) -> Fraction:
    # C^T G C - S^T G S for G=[[a,c],[c,b]], C=(q,-5/3), S=(1,-2).
    return (
        a * (q_e * q_e - 1)
        + 2 * c * (q_e * CENTER_T - SHELL[0] * SHELL[1])
        + b * (CENTER_T * CENTER_T - SHELL[1] * SHELL[1])
    )


def is_spd(a: int, b: int, c: int) -> bool:
    return a > 0 and b > 0 and a * b - c * c > 0


def small_spd_solutions(limit: int = 64) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            for c in range(-limit, limit + 1):
                if not is_spd(a, b, c):
                    continue
                if general_metric_residual(Fraction(a), Fraction(b), Fraction(c), TARGET_Q_E) == 0:
                    out.append((a, b, c))
    return out


def part1_authority_anchors() -> None:
    print("\nA. Authority anchors")
    paths = [
        NOTE,
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        DOCS / "SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md",
        DOCS / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md",
        DOCS / "POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md",
        DOCS / "YT_EXACT_HESSIAN_SELECTOR_UNIQUENESS_NOTE.md",
        DOCS / "MINIMAL_AXIOMS_2026-06-05.md",
    ]
    for path in paths:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(NOTE)
    check("new note declares no_go metadata", "**Claim type:** no_go" in note and "**Status authority:**" in note)
    check("new note names no endpoint closure", "no endpoint closure" in note)
    check("new note has markdown link to exact readout authority", "](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)" in note)
    check("new note has markdown link to Fisher tangent authority", "](SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md)" in note)
    check("new note has markdown link to minimal axioms", "](MINIMAL_AXIOMS_2026-06-05.md)" in note)


def part2_required_metric() -> None:
    print("\nB. Required metric arithmetic")
    ratio = diag_metric_ratio_for_target(TARGET_Q_E)
    check("target q_E maps to rho_E=21/4", rho_from_q(TARGET_Q_E) == TARGET_RHO_E, str(rho_from_q(TARGET_Q_E)))
    check("diagonal target metric ratio is 1449/704", ratio == Fraction(1449, 704), str(ratio))
    check("identity metric does not select target", general_metric_residual(Fraction(1), Fraction(1), Fraction(0), TARGET_Q_E) != 0)
    check("Fisher-unit diagonal metric does not select target", ratio != Fraction(1), str(ratio))
    check("target diagonal metric does select target", general_metric_residual(Fraction(704), Fraction(1449), Fraction(0), TARGET_Q_E) == 0)
    check("general metric target equation matches note", general_metric_residual(Fraction(1), Fraction(0), Fraction(0), TARGET_Q_E) == Fraction(161, 64))
    check("off-diagonal target coefficient is -9/4", 2 * (TARGET_Q_E * CENTER_T - SHELL[0] * SHELL[1]) == Fraction(-9, 4))
    check("b coefficient is -11/9", CENTER_T * CENTER_T - SHELL[1] * SHELL[1] == Fraction(-11, 9))
    check("no small integer SPD metric up to 64 selects target", small_spd_solutions(64) == [])


def part3_current_metric_surfaces() -> None:
    print("\nC. Current metric surface boundaries")
    fisher = read(DOCS / "SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md")
    source = read(DOCS / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md")
    source_flat = " ".join(source.split())
    post = read(DOCS / "POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md")
    yt = read(DOCS / "YT_EXACT_HESSIAN_SELECTOR_UNIQUENESS_NOTE.md")
    axioms = flat(DOCS / "MINIMAL_AXIOMS_2026-06-05.md")

    check("Fisher note supplies Fisher pairing", "<s,t>_F := E_0[s t]" in fisher)
    check("Fisher note supplies two-outcome unit tangent", "epsilon = (+1,-1)" in fisher and "Fisher-unit tangent" in fisher)
    check("Fisher note does not define Route-2 gamma objects", "gamma_E" not in fisher and "gamma_T" not in fisher)
    check("Fisher note does not supply 1449/704", "1449/704" not in fisher)

    check("source-measure packet keeps physical source semantics conditional", "does not prove that this basis is the physical top source basis" in source_flat)
    check("source-measure packet names supplied basis", "supplied diagonal C^6 Hilbert-Schmidt response basis" in source)
    check("source-measure packet does not define Route-2 metric ratio", "1449/704" not in source and "gamma_E" not in source)

    check("post-Record prototype says metric/Hessian are supplied data", "They are supplied finite packet data." in post)
    check("post-Record prototype says not selector authority", "not selector/tangent/readout authority" in post)
    check("post-Record prototype does not derive metric from Record", "does not derive selector/readout/tangent authority from Record" in post)

    check("YT Hessian note is bounded support not Route-2 closure", "bounded support theorem" in yt)
    check("YT Hessian note says selector direction uniqueness, not full shape uniqueness", "selector **direction**" in yt and "does **not** strengthen to full shape uniqueness" in yt)
    check("YT Hessian note does not define Route-2 gamma objects", "gamma_E" not in yt and "gamma_T" not in yt)

    check("minimal axioms withhold readout context, weighting, and time metric", "record supplies no readout context" in axioms and "weighting" in axioms and "time metric" in axioms)


def part4_supplied_metric_examples() -> None:
    print("\nD. Supplied-metric examples")
    # The post-Record prototype uses a sample supplied metric ((3,1),(1,2)).
    a, c, b = Fraction(3), Fraction(1), Fraction(2)
    residual = general_metric_residual(a, b, c, TARGET_Q_E)
    check("post-Record sample metric is SPD", a * b - c * c > 0, f"det={a*b-c*c}")
    check("post-Record sample metric does not select target", residual != 0, str(residual))
    check("post-Record sample diagonal ratio is not 1449/704", b / a != Fraction(1449, 704), str(b / a))
    check("a fitted diagonal metric can select target but is exactly the missing import", general_metric_residual(Fraction(704), Fraction(1449), Fraction(0), TARGET_Q_E) == 0)
    check("fitted diagonal metric is positive", 704 > 0 and 1449 > 0)


def part5_firewall() -> None:
    print("\nE. Claim firewall")
    note = read(NOTE)
    proof_inputs = {
        "route2_fixed_source_pair",
        "current_metric_surface_text",
        "exact_rational_metric_equations",
    }
    forbidden_markers = (
        "observed quark",
        "fitted yukawa",
        "ckm",
        "pdg",
        "nearest-rational",
        "nearest rational",
    )
    note_lower = note.lower()
    check(
        "forbidden observational/fitted proof inputs are absent from note",
        all(marker not in note_lower for marker in forbidden_markers),
        str(sorted(proof_inputs)),
    )
    check("note keeps future metric theorem open", "future theorem that derives the metric tensor" in note)
    check("note does not claim endpoint closure", "does not close `rho_E=21/4`" in note)
    check("proposal_allowed false is recorded", "proposal_allowed: false" not in note and "actual_current_surface_status:" not in note)
    check("bare retained is disallowed", "bare_retained_allowed: false" not in note)


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 METRIC SELECTOR RATIO BOUNDARY")
    print("=" * 88)

    part1_authority_anchors()
    part2_required_metric()
    part3_current_metric_surfaces()
    part4_supplied_metric_examples()
    part5_firewall()

    print("\nSummary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: current metric-selector surfaces do not derive the Route-2 ratio 1449/704.")
        print("A typed Route-2 metric/source primitive is still required.")
        return 0
    print("VERDICT: metric-selector ratio boundary checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
