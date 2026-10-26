#!/usr/bin/env python3
"""Documentary eta-route inventory and finite stipulated Boolean model.

No eta retirement, physical selector or yield theorem is established.
The cited reduced-surface diagnostic reports two candidates against a
required three branches; that unresolved obligation is reported, not scored
as a successful scientific check. Historical failed captures remain valid.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md', 'docs/DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_REDUCED_SURFACE_SELECTOR_SUPPORT_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_REDUCTION_EXHAUSTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_MICROSCOPIC_D_LAST_MILE_NOTE_2026-04-16.md', 'docs/OMEGA_LAMBDA_DERIVATION_NOTE.md', 'docs/R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md', 'docs/HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md']

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
    check("parent declares documentary open-gate scope",
          "**Claim type:** open_gate" in parent and "documentary route inventory" in parent_norm)
    check("parent withdraws exact-support promotion inference",
          "withdraws its former reliance" in parent_norm
          and "former conclusion" in parent_norm and "is withdrawn" in parent_norm)
    check("parent leaves physical selector and yield open",
          "physical selector/yield/readout obligations remain open" in parent_norm
          and "apply an audit verdict" in parent_norm)


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
    print("  OPEN SCIENTIFIC OBLIGATION (documentary observation; no transport rerun):")
    diagnostic_failure_reported = ("two clustered candidates" in reduced
        and "required three branches" in reduced and "exits nonzero" in reduced)
    print(f"  Source reports two candidates versus required three and nonzero exit: {diagnostic_failure_reported}")
    print("  No exact-support, physical-selector or yield theorem is inherited from this diagnostic.")
    if not diagnostic_failure_reported:
        raise RuntimeError("reduced-surface diagnostic boundary changed; review required")
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
        "Lane 5 inventory names the reviewed C1/C2/C3 routes",
        "(C1) absolute-scale" in cosmic
        and "(C2) cosmic-history-ratio" in cosmic
        and "(C3) direct cosmic-`L`" in cosmic
        and "former necessity no-go is withdrawn" in cosmic,
    )


def part3_single_gate_inventory() -> None:
    section("Part 3: historical gate inventory and unresolved proof obligation")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check("parent identifies the historical candidate gate without sufficiency",
          "right-sensitive 2-real `Z_3`" in parent_norm
          and "doublet-block point-selection law" in parent_norm
          and "not a proof that a single gate is sufficient" in parent_norm)
    check("historical gate object and odd-slot readout remain explicit",
          "`dW_e^H = Schur_{E_e}(D_-)`" in parent and "`A13`" in parent
          and "sign(sin(delta))" in parent)
    check("parent preserves the failed diagnostic as an open obligation",
          "required-three-branch diagnostic remains a failed proof obligation" in parent_norm
          and "earlier source-packet FAIL is preserved" in parent_norm)
    check("historical shortcut references are inventoried without exhaustion",
          all(marker in parent for marker in CLOSED_ROUTE_MARKERS)
          and "a list is not an exhaustion theorem" in parent_norm)
    check("parent does not close DM-lane work", "does NOT close any of the DM lane work" in parent)


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

    print("  stipulated route model: eta retires if the supplied selector premise is true")
    print("  rule: C2 numeric closure also needs the separate alpha_GUT lane")
    print("  stipulated separated-input route: H0 flag also needs C1; joint routes are not excluded")

    check("all-false model assignment returns false eta flag", not current.eta_retired())
    check("selector-only model assignment sets eta flag but not C2 flag", gate_only.eta_retired() and not gate_only.c2_numerically_closed())
    check("all-true assignment satisfies the stipulated route rule", full_c2_plus_scale.h0_closed_through_c2())
    check(
        "parent records alpha_GUT as a separate remaining cascade dependency",
        "remaining cascade dependency is `alpha_GUT in [0.03, 0.05]`" in parent_norm,
    )
    check(
        "parent limits separate C1 requirement to this route",
        "Within that route, `(C1)` supplies the separately fixed scale" in parent_norm
        and "joint relations are not excluded" in parent_norm.lower(),
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
    print("Documentary and stipulated-rule checks only; physical selector/yield closure remains OPEN.")
    print("The earlier exact-support source check failed and has not become a scientific PASS.")

    part1_packet_metadata()
    part2_registered_dependencies()
    part3_single_gate_inventory()
    part4_non_promotion_model()

    print()
    print("=" * 88)
    print(f"DOCUMENTARY / STIPULATED-MODEL CHECKS: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("UNRESOLVED: reduced-surface required-three-branch diagnostic; physical selector/yield/readout.")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
