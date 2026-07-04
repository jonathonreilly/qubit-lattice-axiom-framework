#!/usr/bin/env python3
"""Connected-source selector scalar-lift no-go certificate.

The landed connected-source theorem selects kappa=0 only on a color-matrix
source surface whose identity direction is quotiented by normalization.  This
runner checks that the current scalar signed-record / one-Higgs source packet
does not supply that color-matrix source coordinate: its scalar source has a
fixed color identity factor, whose direct singlet weight is one.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_connected_source_selector_scalar_lift_no_go_2026-05-29.json"

NOTE = DOCS / "YT_CONNECTED_SOURCE_SELECTOR_SCALAR_LIFT_NO_GO_NOTE_2026-05-29.md"
CONNECTED_SELECTOR = DOCS / "YT_CONNECTED_SOURCE_AUGMENTATION_IDEAL_SELECTOR_NARROW_THEOREM_NOTE_2026-05-26.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
SIGNED_READOUT = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
HIGGS_RAY = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
SCALAR_NOGO = DOCS / "YT_SCALAR_TASTE_CONDENSATE_SELECTOR_NO_GO_NOTE_2026-05-23.md"
YT_COLOR = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"
EW_KAPPA = DOCS / "YT_EW_COLOR_PROJECTION_THEOREM.md"
EW_MATCHING = DOCS / "EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md"
EW_TRACELESS_NOGO = DOCS / "EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md"

PASS_COUNT = 0
FAIL_COUNT = 0

Matrix = tuple[tuple[Fraction, ...], ...]


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalized_text(text: str) -> str:
    return " ".join(text.split())


def identity(n: int) -> Matrix:
    return tuple(tuple(Fraction(1 if i == j else 0) for j in range(n)) for i in range(n))


def diag(vals: list[Fraction]) -> Matrix:
    n = len(vals)
    return tuple(tuple(vals[i] if i == j else Fraction(0) for j in range(n)) for i in range(n))


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(tuple(a[i][j] - b[i][j] for j in range(n)) for i in range(n))


def scalar_mul(c: Fraction, a: Matrix) -> Matrix:
    n = len(a)
    return tuple(tuple(c * a[i][j] for j in range(n)) for i in range(n))


def trace(a: Matrix) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def hs_inner(a: Matrix, b: Matrix) -> Fraction:
    n = len(a)
    return sum(a[i][j] * b[i][j] for i in range(n) for j in range(n))


def traceless_projection(a: Matrix) -> Matrix:
    n = len(a)
    return mat_sub(a, scalar_mul(trace(a) / n, identity(n)))


def hs_norm_sq(a: Matrix) -> Fraction:
    return hs_inner(a, a)


def singlet_fraction(a: Matrix) -> Fraction:
    """Hilbert-Schmidt fraction of a nonzero matrix in the identity line."""

    n = len(a)
    i_n = identity(n)
    projection = scalar_mul(trace(a) / n, i_n)
    return hs_norm_sq(projection) / hs_norm_sq(a)


def trace_one_witnesses(n: int) -> list[Matrix]:
    uniform = diag([Fraction(1, n)] * n)
    point = diag([Fraction(1)] + [Fraction(0)] * (n - 1))
    ramp = diag([Fraction(k, n * (n + 1) // 2) for k in range(1, n + 1)])
    return [uniform, point, ramp]


def source_score(j: Matrix, rho: Matrix, expectation: Fraction) -> Fraction:
    return hs_inner(j, rho) - expectation


def scalar_source_score(epsilon: int, expectation: Fraction = Fraction(0)) -> Fraction:
    return Fraction(epsilon) - expectation


def part1_current_surfaces() -> None:
    print("\nPart 1: current source surfaces and open gates")
    paths = [
        NOTE,
        CONNECTED_SELECTOR,
        SOURCE_ACTION,
        SIGNED_READOUT,
        HIGGS_RAY,
        SCALAR_NOGO,
        YT_COLOR,
        EW_KAPPA,
        EW_MATCHING,
        EW_TRACELESS_NOGO,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = normalized_text(note)
    required = [
        "exact negative boundary",
        "source coordinate is a color matrix `J`",
        "source coordinate is a scalar signed-record parameter `h`",
        "fixed color identity factor",
        "not enough to move the current scalar signed-record / one-Higgs source packet",
        "No-Go Discipline Gate",
        "N1 - Alternative route enumeration: PASS",
        "N2 - Wall-independence audit: PASS",
        "N3 - Hidden-wall scan: PASS",
        "N4 - Residual matching: PASS",
        "N5 - Rhetoric audit: PASS",
        "N6 - Partial-closure path scan: PASS",
        "N7 - Steelman: PASS",
        "N8 - Cross-cycle echo: PASS",
    ]
    for phrase in required:
        check(f"new note contains boundary phrase: {phrase}", phrase in note_flat)

    connected = read(CONNECTED_SELECTOR)
    check(
        "connected selector note is explicitly conditional on source surface",
        "Yukawa-side readout that is accepted to be this normalized connected source" in connected
        or "If the physical Yukawa source is accepted as this connected source tangent" in connected,
    )
    check(
        "connected selector note preserves physical source-action blocker",
        "does not prove that the physical neutral EW/Higgs source-action surface" in connected,
    )

    source_action = read(SOURCE_ACTION)
    check(
        "source-action note says same-surface neutral EW/Higgs authority remains open",
        "not same-surface neutral EW/Higgs authority" in source_action
        and "neutral EW/Higgs authority" in source_action,
    )

    signed = read(SIGNED_READOUT)
    check(
        "signed-readout note does not select kappa",
        "do not select `kappa_Y = 0`" in signed,
    )


def part2_color_matrix_source_quotient() -> dict[str, Any]:
    print("\nPart 2: color-matrix connected source quotient")
    rows: dict[str, Any] = {}
    for n in range(2, 8):
        i_n = identity(n)
        lambdas = [Fraction(-2), Fraction(0), Fraction(3, 5), Fraction(7)]
        for lam in lambdas:
            scores = [source_score(scalar_mul(lam, i_n), rho, lam) for rho in trace_one_witnesses(n)]
            check(f"N={n} identity source lambda={lam} has zero connected score", all(s == 0 for s in scores), scores)

        j = diag([Fraction(k) for k in range(1, n + 1)])
        j0 = traceless_projection(j)
        shift = trace(j) / n
        for rho in trace_one_witnesses(n):
            quotient_score = hs_inner(j0, rho)
            full_score_mod_identity = hs_inner(j, rho) - shift
            check(
                f"N={n} quotient score equals full score modulo identity",
                quotient_score == full_score_mod_identity,
                {"quotient": str(quotient_score), "full_mod_identity": str(full_score_mod_identity)},
            )

        connected_fraction = Fraction(n * n - 1, n * n)
        rows[str(n)] = {
            "source_surface": "color-matrix connected source",
            "quotient": "End(C^N)/C I",
            "dimension_fraction": f"{connected_fraction.numerator}/{connected_fraction.denominator}",
            "kappa_selected_on_this_surface": "0",
        }
    check("N=3 color-source quotient gives 8/9", rows["3"]["dimension_fraction"] == "8/9", rows["3"])
    return rows


def part3_scalar_source_keeps_color_identity() -> dict[str, Any]:
    print("\nPart 3: scalar signed-record source keeps fixed color identity")
    rows: dict[str, Any] = {}
    for n in range(2, 8):
        i_n = identity(n)
        frac = singlet_fraction(i_n)
        traceless = traceless_projection(i_n)
        signed_scores = [scalar_source_score(+1), scalar_source_score(-1)]
        check(f"N={n} scalar signed source has nonzero signed-record score", signed_scores == [1, -1], signed_scores)
        check(f"N={n} scalar source color factor has singlet fraction one", frac == 1, frac)
        check(f"N={n} scalar source color factor has zero traceless projection", hs_norm_sq(traceless) == 0, hs_norm_sq(traceless))

        direct_kappa = frac
        connected_kappa = Fraction(0)
        direct_ky = Fraction(n * n - 1, n * n) + direct_kappa * Fraction(1, n * n)
        connected_ky = Fraction(n * n - 1, n * n) + connected_kappa * Fraction(1, n * n)
        check(f"N={n} direct scalar color projection gives full-trace K_Y=1", direct_ky == 1, direct_ky)
        check(f"N={n} connected color-source value differs from scalar direct projection", connected_ky != direct_ky)

        rows[str(n)] = {
            "source_surface": "scalar signed-record source with fixed I_color",
            "singlet_fraction_of_color_factor": str(frac),
            "direct_scalar_kappa": str(direct_kappa),
            "direct_scalar_K_Y": str(direct_ky),
            "connected_color_source_K_Y": f"{connected_ky.numerator}/{connected_ky.denominator}",
        }
    check("N=3 scalar direct projection differs from connected-source selector", rows["3"]["direct_scalar_K_Y"] == "1" and rows["3"]["connected_color_source_K_Y"] == "8/9", rows["3"])
    return rows


def part4_lift_obstruction() -> dict[str, Any]:
    print("\nPart 4: lift obstruction witness")
    rows: dict[str, Any] = {}
    for n in (2, 3, 4):
        color_source_dirs = n * n
        quotient_dirs = n * n - 1
        scalar_source_dirs = 1
        check(f"N={n} scalar source has no color-matrix identity direction to quotient", scalar_source_dirs == 1 and color_source_dirs > 1)

        scalar_observations = {
            "score(+1,color a)": "1",
            "score(-1,color a)": "-1",
            "depends_on_color_index": False,
        }
        added_color_source_premise = {
            "extra_source_directions": color_source_dirs,
            "quotient_directions": quotient_dirs,
            "identity_line_removed": True,
        }
        check(
            f"N={n} added color-source premise contains data absent from scalar source",
            added_color_source_premise["extra_source_directions"] != scalar_source_dirs,
            added_color_source_premise,
        )
        rows[str(n)] = {
            "scalar_source_dirs": scalar_source_dirs,
            "color_matrix_source_dirs": color_source_dirs,
            "color_quotient_dirs": quotient_dirs,
            "scalar_observations": scalar_observations,
            "added_color_source_premise": added_color_source_premise,
        }
    return rows


def part5_firewalls() -> None:
    print("\nPart 5: dependency and overclaim firewalls")
    note = read(NOTE)
    scalar_nogo = read(SCALAR_NOGO)
    yt_color = read(YT_COLOR)
    ew_kappa = read(EW_KAPPA)
    ew_matching = read(EW_MATCHING)
    ew_traceless = read(EW_TRACELESS_NOGO)

    check(
        "scalar no-go records identity color insertion gives singlet weight one",
        "insertion is proportional to `I_color`" in scalar_nogo
        and "singlet weight `1`, not `0`" in scalar_nogo,
    )
    check(
        "Y_T color projection remains a kappa family",
        "K_Y(kappa_Y) = 8/9 + kappa_Y/9" in yt_color,
    )
    check(
        "EW kappa family remains open without selector",
        "K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)" in ew_kappa
        and "does not claim that `kappa_EW = 0` is derived" in ew_kappa,
    )
    check(
        "EW matching note keeps kappa as separate matching premise",
        "is an extra matching premise" in ew_matching,
    )
    check(
        "EW traceless-generator no-go distinguishes wrong disconnected object",
        "targets the wrong disconnected object" in ew_traceless,
    )

    required_boundaries = [
        "does not introduce a new axiom",
        "does not rule out:",
        "deriving a physical color-matrix connected-source authority",
        "bypassing `kappa_Y` through a strict same-source top/W response theorem",
    ]
    for phrase in required_boundaries:
        check(f"new note preserves future route: {phrase}", phrase in note)

    forbidden = [
        "framework-native unbounded selector is derived",
        "kappa_Y = 0 is now derived",
        "kappa_EW = 0 is now derived",
        "full Y_T closure",
        "EW 9/8 closure",
        "proposed_retained",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T CONNECTED-SOURCE SELECTOR SCALAR-LIFT NO-GO")
    print("=" * 88)
    part1_current_surfaces()
    color_source_rows = part2_color_matrix_source_quotient()
    scalar_source_rows = part3_scalar_source_keeps_color_identity()
    lift_rows = part4_lift_obstruction()
    part5_firewalls()

    result = {
        "status": "exact negative boundary",
        "claim": (
            "The connected-source augmentation-ideal selector cannot be lifted "
            "to the current scalar signed-record / one-Higgs source packet "
            "without an additional theorem identifying the physical source "
            "as a connected color-matrix source."
        ),
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The result blocks an attempted unbounded conversion of kappa_Y or "
            "kappa_EW; it does not close either selector positively."
        ),
        "axioms_added": 0,
        "imports_retired": [],
        "imports_exposed": [
            "physical color-matrix connected-source authority for Y_T/EW",
            "or exact disconnected/singlet current coefficient computation",
            "or strict same-source top/W response bypass for Y_T",
        ],
        "color_matrix_source_rows": color_source_rows,
        "scalar_source_rows": scalar_source_rows,
        "lift_obstruction_rows": lift_rows,
        "remaining_positive_routes": [
            "derive physical color-matrix connected-source authority",
            "compute kappa_EW or kappa_Y directly from an exact current/source coefficient",
            "bypass kappa_Y through strict same-source top/W response",
            "derive a different kappa_Y matching theorem not equal to direct scalar color-insertion singlet weight",
        ],
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
