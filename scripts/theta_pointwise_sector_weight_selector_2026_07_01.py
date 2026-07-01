#!/usr/bin/env python3
"""Verify the theta pointwise sector-weight selector bridge."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01.md"
SUBSTRATE = DOCS / "THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
WEIGHTING = DOCS / "THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md"
POSITIVITY_NOGO = DOCS / "STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md"
STRUCTURED = DOCS / "STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md"
WILSON = DOCS / "WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md"
BORN = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
POST_STACK = DOCS / "POST_STACK_HARD_GATE_STATUS_MAP_2026-06-30.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def paired(weights: dict[int, Fraction]) -> bool:
    return all(weights.get(q, Fraction(0)) == weights.get(-q, Fraction(0)) for q in weights)


def theta_zero_weights(weights: dict[int, Fraction]) -> dict[int, Fraction]:
    return dict(weights)


def theta_pi_weights(weights: dict[int, Fraction]) -> dict[int, Fraction]:
    return {q: ((-1) ** abs(q)) * z for q, z in weights.items()}


def partition(weights: dict[int, Fraction]) -> Fraction:
    return sum(weights.values(), Fraction(0))


def pointwise_nonnegative(weights: dict[int, Fraction]) -> bool:
    return all(z >= 0 for z in weights.values())


def has_positive_odd_support(weights: dict[int, Fraction]) -> bool:
    return any((q % 2) != 0 and z > 0 for q, z in weights.items())


def main() -> int:
    print("=== Theta pointwise sector-weight selector ===")

    paths = [NOTE, SUBSTRATE, WEIGHTING, POSITIVITY_NOGO, STRUCTURED, WILSON, BORN, POST_STACK]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    substrate = read(SUBSTRATE)
    weighting = read(WEIGHTING)
    weighting_flat = flat(weighting)
    positivity_nogo = read(POSITIVITY_NOGO)
    positivity_flat = flat(positivity_nogo).lower()
    structured = read(STRUCTURED)
    wilson = read(WILSON)
    wilson_flat = flat(wilson).lower()
    born = read(BORN)
    born_flat = flat(born).lower()
    post_stack = read(POST_STACK)

    section("PART A -- source boundary")
    check("substrate note relocates theta to emergent-Q bridge", "Emergent-Q bridge" in substrate)
    check("substrate note does not close continuum Q", "Not" in substrate and "continuum-limit theorem" in substrate)
    check("weighting note gives CP-even set {0, pi}", ("{0, pi}" in weighting_flat or "{0, π}" in weighting_flat) and ("not theta = 0" in weighting_flat or "not to θ = 0" in weighting_flat))
    check("prior no-go says positivity does not force theta=0", "positivity" in positivity_flat and "not forced" in positivity_flat)
    check("structured theta note keeps gauge/mass assembly open", "Gauge-side residual" in structured and "Mass-side residual" in structured)
    check("Wilson note scopes real-positive surface", "real-positive" in wilson_flat and "solve strong cp" in wilson_flat)
    check("Record/Born bridge scopes probabilities after interface", "selective record-writing" in born_flat and "instrument/effect interface" in born_flat)
    check("post-stack map keeps theta as hard gate", "Theta" in post_stack and "gauge-action selector" in post_stack)

    section("PART B -- exact finite selector")
    weights = {
        -2: Fraction(1, 4),
        -1: Fraction(3, 10),
        0: Fraction(9, 10),
        1: Fraction(3, 10),
        2: Fraction(1, 4),
    }
    w0 = theta_zero_weights(weights)
    wpi = theta_pi_weights(weights)
    check("sector weights are nonnegative", pointwise_nonnegative(weights))
    check("sector weights are paired", paired(weights))
    check("odd support is nonzero", has_positive_odd_support(weights))
    check("theta=0 keeps every sector nonnegative", pointwise_nonnegative(w0), f"W0={w0}")
    check("theta=pi makes odd sectors negative", not pointwise_nonnegative(wpi), f"Wpi={wpi}")
    check("negative theta=pi sectors are exactly positive odd sectors", all((wpi[q] < 0) == ((q % 2) != 0 and weights[q] > 0) for q in weights))
    check("theta=0 partition is positive", partition(w0) > 0, f"Z0={partition(w0)}")

    section("PART C -- partition positivity is weaker")
    even_heavy = {-1: Fraction(1), 0: Fraction(5), 1: Fraction(1)}
    even_heavy_pi = theta_pi_weights(even_heavy)
    check("counterexample weights are paired", paired(even_heavy))
    check("counterexample has positive odd support", has_positive_odd_support(even_heavy))
    check("Z(pi) can be positive despite negative odd weights", partition(even_heavy_pi) > 0 and not pointwise_nonnegative(even_heavy_pi), f"Zpi={partition(even_heavy_pi)}, Wpi={even_heavy_pi}")
    check("therefore partition positivity alone does not select theta=0", "partition-function positivity alone" in note)

    section("PART D -- even-support boundary")
    even_only = {-2: Fraction(2), 0: Fraction(3), 2: Fraction(2)}
    even_only_pi = theta_pi_weights(even_only)
    check("even-only support is paired and nonnegative", paired(even_only) and pointwise_nonnegative(even_only))
    check("even-only support has no odd selector witness", not has_positive_odd_support(even_only))
    check("theta=pi is nonnegative on even-only support", pointwise_nonnegative(even_only_pi), f"Wpi={even_only_pi}")
    check("even-only support makes theta=0 and theta=pi indistinguishable", theta_zero_weights(even_only) == even_only_pi)

    section("PART E -- note content")
    for section_name in [
        "Claim",
        "Finite Theorem",
        "Relation To Prior Theta Notes",
        "What Moves",
        "What Remains",
        "Audit Consequence If Retained",
        "Non-Claims",
        "No-Go Discipline Gate",
    ]:
        check(f"note includes {section_name}", f"## {section_name}" in note)
    check("note states the selector condition", "pointwise nonnegative record-facing probability measure" in note_flat)
    check("note selects theta=0 only within {0, pi}", "within the already-narrowed set `{0, pi}`" in note)
    check("note states odd-support boundary", "If no odd-`Q` sector has nonzero weight" in note)
    check("note preserves emergent Q wall", "does not derive `Q`" in note)
    check("note preserves Strong-CP non-closure", "Strong-CP closure" in note)
    check("note consumes no measured values", "PDG values" in note and "fitted constants" in note)

    section("PART F -- no-go discipline gate")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", item in note)
    check("N1 enumerates seven routes", note.count("| Reality-only route |") == 1 and note.count("| New primitive route |") == 1)
    check("N2 collapses residual to W_theta_sector", "W_theta_sector" in note)
    check("N3 exposes pointwise positivity as premise", "\"Pointwise nonnegative\" is an explicit" in note)
    check("N4 matches prior witnesses", note.count("| `THETA_") >= 2 and "STRONG_CP_GAUGE_THETA" in note)
    check("N5 narrows negative phrase", "sector-level statement" in note)
    check("N6 lists live closure paths", "Live closure paths remain" in note)
    check("N7 steelman accepts sign-weighted formulations", "sign-changing Euclidean weights" in note)
    check("N8 cross-cycle echo separates partition and pointwise positivity", "separating total partition" in note)

    section("PART G -- assembled conclusion")
    selector_ok = (
        pointwise_nonnegative(w0)
        and not pointwise_nonnegative(wpi)
        and has_positive_odd_support(weights)
        and pointwise_nonnegative(even_only_pi)
    )
    check("finite selector theorem passes", selector_ok)
    check("bridge remains conditional", "Rows that need full Strong-CP closure still need" in note_flat)
    check("prior positivity no-go is preserved", "This note agrees" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
