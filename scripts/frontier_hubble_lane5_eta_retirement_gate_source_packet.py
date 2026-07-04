#!/usr/bin/env python3
"""Source-packet verifier for the Hubble Lane 5 eta-retirement gate.

This runner is not an audit verdict. It packages the source-side evidence for
the Cycle 4 gate note by checking that the parent note exposes its dependency
anchors, names the single residual DM/PMNS selector gate, and preserves the
non-promotion boundary: no eta retirement, no C2 closure, and no H0 closure are
claimed on the actual current surface.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0

PARENT = "docs/HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md"
RUNNER = "scripts/frontier_hubble_lane5_eta_retirement_gate_source_packet.py"
CACHE = "logs/runner-cache/frontier_hubble_lane5_eta_retirement_gate_source_packet.txt"

DEPENDENCIES = {
    "dm_leptogenesis_transport_status_note_2026-04-16": (
        "docs/DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-04-16.md"
    ),
    "dm_leptogenesis_pmns_reduced_surface_selector_support_note_2026-04-16": (
        "docs/DM_LEPTOGENESIS_PMNS_REDUCED_SURFACE_SELECTOR_SUPPORT_NOTE_2026-04-16.md"
    ),
    "dm_leptogenesis_pmns_reduction_exhaustion_theorem_note_2026-04-16": (
        "docs/DM_LEPTOGENESIS_PMNS_REDUCTION_EXHAUSTION_THEOREM_NOTE_2026-04-16.md"
    ),
    "dm_leptogenesis_pmns_microscopic_d_last_mile_note_2026-04-16": (
        "docs/DM_LEPTOGENESIS_PMNS_MICROSCOPIC_D_LAST_MILE_NOTE_2026-04-16.md"
    ),
    "omega_lambda_derivation_note": "docs/OMEGA_LAMBDA_DERIVATION_NOTE.md",
    "r_base_group_theory_derivation_theorem_note_2026-04-24": (
        "docs/R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md"
    ),
    "hubble_lane5_cosmic_history_ratio_necessity_no_go_note_2026-04-26": (
        "docs/HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md"
    ),
}

CLOSED_ROUTE_MARKERS = [
    "DM_LEPTOGENESIS_UNIVERSAL_YUKAWA_NO_GO_NOTE_2026-04-15.md",
    "DM_NEUTRINO_CANONICAL_TWO_HIGGS_SLOT_NO_GO_NOTE_2026-04-15.md",
    "DM_NEUTRINO_POLAR_ALIGNED_CORE_NO_GO_NOTE_2026-04-15.md",
    "DM_NEUTRINO_TWO_HIGGS_23_SYMMETRIC_SLOT_NO_GO_NOTE_2026-04-15.md",
    "DM_NEUTRINO_Z3_CIRCULANT_MASS_BASIS_NO_GO_NOTE_2026-04-15.md",
    "DM_PMNS_",
    "DM_WILSON_",
    "DM_STRONG_CP_GAMMA_TRANSFER_NO_GO_NOTE_2026-04-15.md",
]


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
        "parent remains an open-gate support source packet",
        "support gate-identification note on `main`" in parent_norm
        and "**Claim type:** open_gate" in parent
        and "identifies the precise residual microscopic selector law" in parent_norm,
    )
    check(
        "source-packet boundary says it is not a theorem",
        "This is an audit / gate-identification artifact, not a theorem" in parent_norm,
    )
    check(
        "source-packet boundary forbids promotion claims",
        "does not derive the missing right-sensitive selector law" in parent_norm
        and "retire `eta`" in parent_norm
        and "apply an audit verdict" in parent_norm,
    )


def part2_registered_dependencies() -> None:
    section("Part 2: dependency links and source fingerprints")
    parent = read(PARENT)

    for claim_id, rel in DEPENDENCIES.items():
        check(f"{claim_id}: linked from parent", f"[{claim_id}](" in parent and Path(rel).name in parent)
        check(f"{claim_id}: file exists", (ROOT / rel).exists(), rel)

    transport = read(DEPENDENCIES["dm_leptogenesis_transport_status_note_2026-04-16"])
    reduced = read(DEPENDENCIES["dm_leptogenesis_pmns_reduced_surface_selector_support_note_2026-04-16"])
    exhaustion = read(DEPENDENCIES["dm_leptogenesis_pmns_reduction_exhaustion_theorem_note_2026-04-16"])
    last_mile = read(DEPENDENCIES["dm_leptogenesis_pmns_microscopic_d_last_mile_note_2026-04-16"])
    omega = read(DEPENDENCIES["omega_lambda_derivation_note"])
    r_base = read(DEPENDENCIES["r_base_group_theory_derivation_theorem_note_2026-04-24"])
    cosmic = read(DEPENDENCIES["hubble_lane5_cosmic_history_ratio_necessity_no_go_note_2026-04-26"])

    check(
        "transport status names undershoot and exact support branch",
        "`eta / eta_obs = 0.188785929502`" in transport and "`eta / eta_obs = 1`" in transport,
    )
    check(
        "transport status isolates the right-sensitive doublet-block law",
        "right-sensitive microscopic selector law" in transport
        and "doublet-block point-selection law" in transport,
    )
    check(
        "transport status records the local selected slice as subcritical",
        "transport-subcritical" in transport,
    )
    check(
        "reduced-surface note supplies exact eta-support witness only",
        "`eta / eta_obs = 1`" in reduced and "support" in normalize(reduced).lower(),
    )
    check(
        "reduction exhaustion note is part of the PMNS route boundary",
        "exhaustion" in normalize(exhaustion).lower()
        and ("PMNS" in exhaustion or "pmns" in exhaustion),
    )
    check(
        "D-last-mile note remains quantitative support, not eta retirement",
        "`eta / eta_obs =" in last_mile and "last-mile" in normalize(last_mile).lower(),
    )
    check(
        "Omega cascade remains bounded and does not retain Omega_Lambda",
        "eta(obs) -> Omega_b(BBN) -> R(bounded) -> Omega_DM -> Omega_m -> Omega_Lambda" in omega
        and "No claim that `Omega_Lambda` is retained" in omega,
    )
    check(
        "R_base theorem supplies an observation-free 31/9 identity",
        "R_base = 31/9" in r_base and "No observed cosmological value enters" in r_base,
    )
    check(
        "Lane 5 no-go supplies the C1/C2/C3 closure taxonomy",
        "(C1) scale route" in cosmic
        and "(C2) cosmic-history-ratio" in cosmic
        and "(C3) direct cosmic-`L`" in cosmic,
    )


def part3_single_gate_inventory() -> None:
    section("Part 3: single residual eta-retirement gate")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check(
        "parent identifies a single residual microscopic selector law",
        "single residual microscopic selector law" in parent_norm,
    )
    check(
        "gate object is the right-sensitive Z3 doublet-block law",
        "right-sensitive 2-real `Z_3` doublet-block point-selection law" in parent_norm
        and "`dW_e^H = Schur_{E_e}(D_-)`" in parent,
    )
    check(
        "odd-slot readout is explicitly named",
        "odd slot `A13`" in parent and "sign(sin(delta))" in parent,
    )
    check(
        "local diagonal route is recorded as transport-subcritical",
        "transport-subcritical" in parent_norm,
    )
    check(
        "closed shortcut routes are inventoried",
        all(marker in parent for marker in CLOSED_ROUTE_MARKERS),
    )
    check(
        "parent explicitly says it does not close DM-lane work",
        "does NOT close any of the DM lane work" in parent,
    )


@dataclass(frozen=True)
class EtaGatePacket:
    right_sensitive_selector_retained: bool
    alpha_gut_retired: bool
    absolute_scale_retained: bool

    def eta_retired(self) -> bool:
        return self.right_sensitive_selector_retained

    def c2_numerically_closed(self) -> bool:
        return self.eta_retired() and self.alpha_gut_retired

    def h0_closed_through_c2(self) -> bool:
        return self.absolute_scale_retained and self.c2_numerically_closed()


def part4_non_promotion_model() -> None:
    section("Part 4: finite non-promotion model")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    current = EtaGatePacket(
        right_sensitive_selector_retained=False,
        alpha_gut_retired=False,
        absolute_scale_retained=False,
    )
    gate_only = EtaGatePacket(
        right_sensitive_selector_retained=True,
        alpha_gut_retired=False,
        absolute_scale_retained=False,
    )
    full_c2_plus_scale = EtaGatePacket(
        right_sensitive_selector_retained=True,
        alpha_gut_retired=True,
        absolute_scale_retained=True,
    )

    print("  rule: eta retires only if the right-sensitive selector is retained")
    print("  rule: C2 numeric closure also needs the separate alpha_GUT lane")
    print("  rule: H0 closure still needs the C1 scale route")

    check("actual current packet does not retire eta", not current.eta_retired())
    check("selector gate alone retires eta but not full C2 numerics", gate_only.eta_retired() and not gate_only.c2_numerically_closed())
    check("full C2-plus-scale packet would close the modeled route", full_c2_plus_scale.h0_closed_through_c2())
    check(
        "parent records alpha_GUT as a separate remaining cascade dependency",
        "remaining cascade dependency is `alpha_GUT in [0.03, 0.05]`" in parent_norm,
    )
    check(
        "parent records C1 as separately required for H0",
        "The `(C1)` half (scale route) remains separately required for `H_0` itself" in parent_norm,
    )
    check(
        "runner boundary forbids audit-result mutation",
        "does not derive" in parent_norm and "apply an audit verdict" in parent_norm,
    )


def main() -> int:
    print("=" * 88)
    print("HUBBLE LANE 5 ETA-RETIREMENT GATE SOURCE PACKET")
    print("=" * 88)
    print()
    print("Question:")
    print("  Is the Cycle 4 eta-retirement gate packaged with source anchors,")
    print("  a replayable single-gate inventory, and a non-promotion boundary?")
    print()
    print("Answer:")
    print("  Yes for source-packet readiness. This runner does not retire eta,")
    print("  close C2, close H0, or apply an audit verdict.")

    part1_packet_metadata()
    part2_registered_dependencies()
    part3_single_gate_inventory()
    part4_non_promotion_model()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
