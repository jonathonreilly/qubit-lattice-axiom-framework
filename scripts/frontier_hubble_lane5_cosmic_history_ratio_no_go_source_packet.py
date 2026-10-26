#!/usr/bin/env python3
"""Documentary verifier and finite stipulated-rule table for Lane 5.

No physical route exhaustion or framework non-derivability is established.
The numerical Boolean model checks its definition, not physical necessity.
This runner records no audit verdict or N1-N8 approval.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md', 'docs/COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md', 'docs/OMEGA_LAMBDA_DERIVATION_NOTE.md', 'docs/COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md', 'docs/OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22.md', 'docs/PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md', 'docs/HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md', 'docs/HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md')

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
    "minimal_axioms": "docs/MINIMAL_AXIOMS_2026-06-29.md",
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
    check("parent is an open route inventory", "**Claim type:** open_gate" in parent
          and "former necessity no-go is withdrawn" in parent_norm)
    check("parent distinguishes conditional family from axiom independence",
          "independently free positive parameters" in parent_norm
          and "does not prove independence" in parent_norm)
    check("parent records no audit verdict or retired premises",
          "records no audit verdict" in parent_norm
          and "does not retire any of those premises" in parent_norm)


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
        "minimal axiom source is current Lattice/Qubit/Admissibility/Record baseline",
        "Lattice" in minimal
        and "Qubit" in minimal
        and "Admissibility" in minimal
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
        "C2 inventory leaves selector/yield open and withdraws exact-support inference",
        "documentary route inventory" in c2_gate
        and "withdraws its former reliance" in c2_gate
        and "failed proof obligation" in c2_gate,
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

    print("  closure rule (bookkeeping over the REVIEWED routes, NOT a proof of exhaustive coverage):")
    print("    stipulated closure flag = C1 and (C2 or C3)")
    print("  rule: scale-reference primitive is a units conversion, not C1")
    for p in packets():
        print(
            "  "
            f"C1={p.c1_scale_route} C2={p.c2_history_ratio} C3={p.c3_direct_l} "
            f"-> L={p.closes_l()} H0={p.closes_h0()}"
        )

    check("parent names separated-input route inventory",
          "(C1) absolute-scale route" in parent and "(C2) cosmic-history-ratio retirement" in parent
          and "(C3) direct cosmic-`L` derivation" in parent)
    check("parent keeps units separate from C1", "The primitive is a ruler, not the C1 route" in parent)
    check("parent marks rule as stipulated and non-exhaustive",
          "the stipulated rule" in parent and "not an exhaustive classification of physical routes" in parent_norm)
    check("three packets satisfy the stipulated C1-and-L rule", len(closed) == 3 and all(p.c1_scale_route and p.closes_l() for p in closed))
    check("C1 alone does not satisfy the stipulated rule", not ClosureClassPacket(True, False, False).closes_h0())
    check("packets without C1 do not satisfy the stipulated rule", all(not p.closes_h0() for p in nonclosed if not p.c1_scale_route))


def part4_scope_boundary() -> None:
    section("Part 4: documentary scope and open proof obligations")
    parent = normalize(read(PARENT))
    check("parent withdraws non-derivability inference",
          "That inference is withdrawn" in parent and "No framework-wide non-derivability theorem is established" in parent)
    check("parent keeps a joint-relation alternative open",
          "H_inf = k sqrt(L)" in parent and "H_0=k" in parent
          and "not a derivation of that physical relation" in parent)
    check("parent distinguishes partial C2 retirement from L closure",
          "not full `L` closure" in parent and "complete L-supplying cascade premise" in parent)
    check("parent names the missing independence proof",
          "independence/underdetermination proof" in parent and "provides no such proof" in parent)
    check("parent withdraws no-go certification",
          "No N1–N8 PASS certificate" in parent and "Literal source checks verify documentary consistency only" in parent)


def execution_scope() -> None:
    section("Execution scope")
    print(f"Enumerated {len(packets())} Boolean assignments; "
          f"{sum(p.closes_h0() for p in packets())} satisfy the stipulated rule.")
    print("Dependency existence and note text were checked; their physical conclusions were not re-proved.")
    print("No lattice/site/mode/continuum calculation or physical route exhaustion was executed.")
    print("No N1-N8 certification, input retirement, or audit verdict follows from these checks.")


def main() -> int:
    print("=" * 88)
    print("LANE 5 SEPARATED-INPUT INVENTORY AND STIPULATED BOOLEAN MODEL")
    print("Checks below concern the finite rule and source wording, not exhaustive physics.")

    part1_packet_metadata()
    part2_registered_dependencies()
    part3_closure_taxonomy()
    part4_scope_boundary()
    execution_scope()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
