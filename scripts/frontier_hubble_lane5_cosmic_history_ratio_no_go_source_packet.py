#!/usr/bin/env python3
"""Source-packet verifier for the Lane 5 cosmic-history-ratio no-go.

This runner is not an audit verdict.  It packages the structural no-go for
independent re-audit by checking that the parent note exposes the dependency
links named by the prior conditional audit and that the C1/C2/C3 closure
taxonomy is mechanically consistent with the cited cosmology source notes.
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
    "minimal_axioms_2026-04-11": "docs/MINIMAL_AXIOMS_2026-04-11.md",
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
    "planck_scale_lane_status_note_2026-04-23": "docs/PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md",
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
        "parent remains a support no-go/program-boundary note",
        "support no-go / program-boundary note" in parent_norm
        and "Bounds the closure space for Lane 5" in parent_norm,
    )
    check(
        "parent boundary does not retire C1/C2/C3 inputs",
        "does not claim that any of `(C1), (C2), (C3)` is impossible" in parent_norm
        and "It does not retire any input" in parent_norm,
    )


def part2_registered_dependencies() -> None:
    section("Part 2: dependency links and fingerprints")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    for claim_id, rel in DEPENDENCIES.items():
        check(f"{claim_id}: linked from parent", f"[{claim_id}](" in parent and Path(rel).name in parent)
        check(f"{claim_id}: file exists", (ROOT / rel).exists(), rel)

    minimal = read(DEPENDENCIES["minimal_axioms_2026-04-11"])
    open_number = read(DEPENDENCIES["cosmology_open_number_reduction_theorem_note_2026-04-26"])
    omega = read(DEPENDENCIES["omega_lambda_derivation_note"])
    scale = read(DEPENDENCIES["cosmology_scale_identification_and_reduction_note"])
    bridge = read(DEPENDENCIES["omega_lambda_matter_bridge_theorem_note_2026-04-22"])
    bridge_ascii = bridge.replace("\u03a9_\u039b", "Omega_Lambda")
    planck = read(DEPENDENCIES["planck_scale_lane_status_note_2026-04-23"])

    check(
        "minimal axiom stack is source-limited and does not auto-promote bounded lanes",
        "local algebra" in minimal
        and "spatial substrate" in minimal
        and "do not automatically promote a bounded lane to retained" in normalize(minimal),
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
        "Planck lane status keeps absolute scale as explicit package pin",
        "`a^(-1) = M_Pl`" in planck
        and "fallback package pin remains active" in planck,
    )
    check(
        "parent prose names all dependency authorities",
        all(Path(rel).name in parent_norm for rel in DEPENDENCIES.values()),
    )


@dataclass(frozen=True)
class ClosureClassPacket:
    c1_absolute_scale: bool
    c2_history_ratio: bool
    c3_direct_l: bool

    def closes_l(self) -> bool:
        return self.c2_history_ratio or self.c3_direct_l

    def closes_h0(self) -> bool:
        return self.c1_absolute_scale and self.closes_l()


def packets() -> list[ClosureClassPacket]:
    out: list[ClosureClassPacket] = []
    for c1, c2, c3 in itertools.product([False, True], repeat=3):
        out.append(ClosureClassPacket(c1, c2, c3))
    return out


def part3_closure_taxonomy() -> None:
    section("Part 3: C1/C2/C3 finite closure model")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    closed = [p for p in packets() if p.closes_h0()]
    nonclosed = [p for p in packets() if not p.closes_h0()]

    print("  closure rule: H0 closes iff C1 and (C2 or C3)")
    for p in packets():
        print(
            "  "
            f"C1={p.c1_absolute_scale} C2={p.c2_history_ratio} C3={p.c3_direct_l} "
            f"-> L={p.closes_l()} H0={p.closes_h0()}"
        )

    check("parent states C1 absolute-scale premise is required", "(C1) absolute-scale axiom" in parent)
    check("parent states one of C2/C3 is required for L", "(C2) cosmic-history-ratio" in parent and "(C3) direct cosmic-`L`" in parent)
    check("parent states no fourth class exists", "No fourth class exists" in parent)
    check("only packets with C1 and one L-class close H0", len(closed) == 3 and all(p.c1_absolute_scale and p.closes_l() for p in closed))
    check("C1 alone fails because L remains open", not ClosureClassPacket(True, False, False).closes_h0())
    check("C2/C3 without C1 fail because absolute time remains open", all(not p.closes_h0() for p in nonclosed if not p.c1_absolute_scale))
    check(
        "parent route map assigns reviewed routes into C1/C2/C3 taxonomy",
        "R6" in parent_norm
        and "R5" in parent_norm
        and "future direct `Omega_Lambda`" in parent_norm,
    )


def part4_no_go_boundary() -> None:
    section("Part 4: no-go boundary and falsifier")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check(
        "absolute-time no-go is scoped to A_min alone",
        "On `A_min` alone" in parent
        and "H_0`, the de Sitter Hubble scale `H_inf`, and the spectral-gap radius `R_Lambda` cannot be derived" in parent_norm,
    )
    check(
        "cosmic-history-ratio no-go is scoped to A_min alone",
        "dimensionless ratio `L = (H_inf / H_0)^2` cannot be derived" in parent_norm
        and "cosmic-history layer" in parent,
    )
    check(
        "falsifier is existential and correctly targets A_min-alone counterexample",
        "falsified if a candidate Lane 5 closure is exhibited" in parent
        and "from `A_min` alone" in parent,
    )
    check(
        "boundary names this as classification, not premise retirement",
        "It does not retire any input; it classifies what retirement requires" in parent_norm,
    )


def main() -> int:
    print("=" * 88)
    print("LANE 5 COSMIC-HISTORY-RATIO NO-GO SOURCE PACKET")
    print("=" * 88)
    print()
    print("Question:")
    print("  Is the Lane 5 no-go packaged with the one-hop authorities and a")
    print("  replayable C1/C2/C3 closure taxonomy for independent re-audit?")
    print()
    print("Answer:")
    print("  Yes for source-packet readiness. This runner does not retire C1,")
    print("  C2, or C3 and does not apply an audit verdict.")

    part1_packet_metadata()
    part2_registered_dependencies()
    part3_closure_taxonomy()
    part4_no_go_boundary()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
