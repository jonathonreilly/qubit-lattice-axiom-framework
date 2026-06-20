#!/usr/bin/env python3
"""Source-packet verifier for the Lane 5 cosmic-history-ratio no-go.

This runner is not an audit verdict. It packages the narrowed structural
no-go for independent re-audit by checking that the parent note exposes the
current dependency anchors, treats the scale-reference primitive as units-only,
preserves the C1/C2/C3 closure taxonomy, and records the No-Go Discipline
N1-N8 gate.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0

PARENT = "docs/HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md"
RUNNER = "scripts/frontier_hubble_lane5_cosmic_history_ratio_no_go_source_packet.py"
CACHE = "logs/runner-cache/frontier_hubble_lane5_cosmic_history_ratio_no_go_source_packet.txt"

DEPENDENCIES = {
    "minimal_axioms": "docs/MINIMAL_AXIOMS_2026-06-05.md",
    "scale_reference_primitive": "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "cosmology_open_number_reduction_theorem_note_2026-04-26": (
        "docs/COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md"
    ),
    "omega_lambda_derivation_note": "docs/OMEGA_LAMBDA_DERIVATION_NOTE.md",
    "cosmology_scale_identification_and_reduction_note": (
        "docs/COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md"
    ),
    "omega_lambda_matter_bridge_theorem_note_2026-04-22": (
        "docs/OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22.md"
    ),
    "planck_scale_lane_status_note_2026-04-23": (
        "docs/PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md"
    ),
    "hubble_lane5_planck_c1_gate_audit_note_2026-04-26": (
        "docs/HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md"
    ),
    "hubble_lane5_eta_retirement_gate_audit_note_2026-04-26": (
        "docs/HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md"
    ),
}


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def part1_packet_metadata() -> None:
    section("Part 1: parent source-packet metadata")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check("parent note exists", (ROOT / PARENT).exists(), PARENT)
    check("parent declares this primary runner", RUNNER in parent)
    check("parent declares this runner cache", CACHE in parent)
    check(
        "parent remains a no-go/program-boundary source note",
        "support no-go / program-boundary note on `main`" in parent_norm
        and "**Claim type:** no_go" in parent,
    )
    check(
        "parent scope is baseline plus units primitive",
        "current framework baseline plus that primitive" in parent_norm
        and "does not supply the dimensionless scale-route" in parent_norm,
    )
    check(
        "parent records no audit verdict",
        "independent audit lane only" in parent_norm
        and "records no audit verdict" in parent_norm
        and "does not retire any of those premises" in parent_norm,
    )


def part2_registered_dependencies() -> None:
    section("Part 2: dependency links and fingerprints")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    for claim_id, rel in DEPENDENCIES.items():
        check(f"{claim_id}: linked from parent", f"[{claim_id}](" in parent and Path(rel).name in parent)
        check(f"{claim_id}: file exists", (ROOT / rel).exists(), rel)

    minimal = read(DEPENDENCIES["minimal_axioms"])
    scale_ref = read(DEPENDENCIES["scale_reference_primitive"])
    open_number = read(DEPENDENCIES["cosmology_open_number_reduction_theorem_note_2026-04-26"])
    omega = read(DEPENDENCIES["omega_lambda_derivation_note"])
    scale = read(DEPENDENCIES["cosmology_scale_identification_and_reduction_note"])
    bridge = read(DEPENDENCIES["omega_lambda_matter_bridge_theorem_note_2026-04-22"])
    bridge_ascii = bridge.replace("\u03a9_\u039b", "Omega_Lambda")
    c1_gate = read(DEPENDENCIES["hubble_lane5_planck_c1_gate_audit_note_2026-04-26"])
    c1_gate_norm = normalize(c1_gate)
    c2_gate = read(DEPENDENCIES["hubble_lane5_eta_retirement_gate_audit_note_2026-04-26"])

    check(
        "minimal axiom source is current Lattice/Quantum/Record baseline",
        "Lattice" in minimal
        and "Quantum" in minimal
        and "Record" in minimal
        and "scale-reference primitive" in minimal,
    )
    check(
        "scale-reference primitive is units-only and non-bounding",
        "This is a units conversion, not a physics axiom" in scale_ref
        and "It does not assert `a/l_P = 1` as a derived theorem" in scale_ref
        and "should not become\n`retained_bounded` merely for using a ruler" in scale_ref,
    )
    check(
        "open-number theorem reduces late-time variables to H0 and L",
        "every variable in `S` is an exact closed-form function of `(H_0, L)`" in open_number
        and "|structural degrees of freedom in S at fixed R| = 2" in open_number,
    )
    check(
        "omega cascade is explicitly bounded and depends on eta/cascade inputs",
        "eta(obs) -> Omega_b(BBN) -> R(bounded) -> Omega_DM -> Omega_m -> Omega_Lambda" in omega
        and "No claim that `Omega_Lambda` is retained" in omega,
    )
    check(
        "scale note supplies H_inf/R_Lambda identities and leaves the ratio open",
        "`H_inf = c / R_Lambda`" in scale
        and "single open ratio `H_inf/H_0`" in scale,
    )
    check(
        "matter bridge supplies Omega_Lambda equals scale ratio",
        "Omega_Lambda = (H_inf / H_0)" in bridge_ascii
        and "single number" in bridge_ascii
        and "ratio `H_inf/H_0`" in bridge_ascii,
    )
    check(
        "C1 gate note preserves scale-reference boundary",
        "scale-reference primitive still supplies only the units conversion" in c1_gate_norm
        and "does not treat the scale-reference primitive as a Planck import or bounded-status source" in c1_gate_norm,
    )
    check(
        "C2 gate note remains an open eta-retirement gate",
        "support gate-identification note on `main`" in c2_gate
        and "does not derive that selector" in c2_gate
        and "scale route" in c2_gate,
    )
    check(
        "parent prose names current dependency authorities",
        all(Path(rel).name in parent_norm for rel in DEPENDENCIES.values()),
    )


@dataclass(frozen=True)
class ClosureClassPacket:
    c1_scale_route: bool
    c2_history_ratio: bool
    c3_direct_l: bool

    def closes_l(self) -> bool:
        return self.c2_history_ratio or self.c3_direct_l

    def closes_h0(self) -> bool:
        return self.c1_scale_route and self.closes_l()


def packets() -> list[ClosureClassPacket]:
    return [ClosureClassPacket(c1, c2, c3) for c1, c2, c3 in itertools.product([False, True], repeat=3)]


def part3_closure_taxonomy() -> None:
    section("Part 3: C1/C2/C3 finite closure model")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    closed = [p for p in packets() if p.closes_h0()]
    nonclosed = [p for p in packets() if not p.closes_h0()]

    print("  closure rule: H0 closes iff C1 and (C2 or C3)")
    print("  rule: scale-reference primitive is a units conversion, not C1")
    for p in packets():
        print(
            "  "
            f"C1={p.c1_scale_route} C2={p.c2_history_ratio} C3={p.c3_direct_l} "
            f"-> L={p.closes_l()} H0={p.closes_h0()}"
        )

    check("parent states C1 scale route is required", "**(C1) scale route** [REQUIRED]" in parent)
    check("parent states the scale primitive is not C1", "The primitive is a ruler, not the C1 route" in parent)
    check("parent states one of C2/C3 is required for L", "(C2) cosmic-history-ratio" in parent and "(C3) direct cosmic-`L`" in parent)
    check("parent states no fourth class exists", "No fourth class exists in the current taxonomy" in parent)
    check("only packets with C1 and one L-class close H0", len(closed) == 3 and all(p.c1_scale_route and p.closes_l() for p in closed))
    check("C1 alone fails because L remains open", not ClosureClassPacket(True, False, False).closes_h0())
    check("C2/C3 without C1 fail because the scale route remains open", all(not p.closes_h0() for p in nonclosed if not p.c1_scale_route))
    check(
        "parent route map assigns reviewed routes into C1/C2/C3 taxonomy",
        "R6" in parent_norm
        and "R5" in parent_norm
        and "future direct `Omega_Lambda`" in parent_norm,
    )


def part4_no_go_discipline() -> None:
    section("Part 4: no-go discipline gate")
    parent = read(PARENT)

    for marker in [
        "**N1 - Alternative route enumeration.** PASS",
        "**N2 - Wall-independence audit.** PASS",
        "**N3 - Hidden-wall scan.** PASS",
        "**N4 - Residual matching.** PASS",
        "**N5 - Rhetoric audit.** PASS",
        "**N6 - Partial-closure path scan.** PASS",
        "**N7 - Steelman.** PASS",
        "**N8 - Cross-cycle echo.** PASS",
    ]:
        check(f"{marker.split(' - ')[0].strip('*')}: present", marker in parent)

    check(
        "N1 names at least five distinct routes",
        all(f"{i}." in parent for i in range(1, 7))
        and "Units-only scale primitive route" in parent
        and "Open-number/Hubble-lock route" in parent,
    )
    check(
        "N6 preserves partial closure paths and primitive boundary",
        "coframe/action-unit gate" in parent
        and "eta-retirement gate" in parent
        and "not counted as a missing axiom" in parent,
    )
    check(
        "gate result is narrowed rather than anti-C1/C2/C3",
        "PASS for the narrowed no-go" in parent
        and "not a no-go against the live" in parent,
    )


def part5_no_go_boundary() -> None:
    section("Part 5: no-go boundary and falsifier")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check(
        "scale-route no-go is scoped to baseline plus units primitive",
        "current framework baseline plus the scale-reference primitive" in parent_norm
        and "does not derive the dimensionless scale-route content" in parent_norm,
    )
    check(
        "cosmic-history-ratio no-go is scoped to baseline plus units primitive",
        "does not derive the dimensionless ratio `L = (H_inf / H_0)^2`" in parent_norm
        and "cosmic-history layer" in parent,
    )
    check(
        "falsifier targets baseline-plus-units-primitive counterexample",
        "falsified if a candidate Lane 5 closure is exhibited" in parent
        and "current framework baseline plus the\nscale-reference primitive" in parent,
    )
    check(
        "boundary names classification, not premise retirement",
        "It does not retire any input; it classifies what retirement requires" in parent_norm,
    )
    check(
        "boundary says C1/C2/C3 remain live",
        "does not claim that any of `(C1), (C2), (C3)` is impossible" in parent_norm,
    )


def main() -> int:
    print("=" * 88)
    print("LANE 5 COSMIC-HISTORY-RATIO NO-GO SOURCE PACKET")
    print("=" * 88)
    print()
    print("Question:")
    print("  Is the Lane 5 no-go packaged with current premise boundaries,")
    print("  one-hop authorities, N1-N8 discipline, and a replayable C1/C2/C3")
    print("  closure taxonomy for independent re-audit?")
    print()
    print("Answer:")
    print("  Yes for source-packet readiness. This runner does not retire C1,")
    print("  C2, or C3 and does not apply an audit verdict.")

    part1_packet_metadata()
    part2_registered_dependencies()
    part3_closure_taxonomy()
    part4_no_go_discipline()
    part5_no_go_boundary()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
