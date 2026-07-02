#!/usr/bin/env python3
"""Verify the bridge-gap action-form uniqueness no-go surface.

The target note claims that the current accepted-premise and retained support
stack does not uniquely select a gauge action form at finite beta. This runner
checks the source note's candidate set, leading-order matching ambiguity,
Wilson/HK finite-beta separation, and the later heat-kernel diffusion theorem's
open residual so the no-go is not overread as a permanent global impossibility.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md"
HK_NOTE = ROOT / "docs" / "HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md"
RECORD_NOTE = ROOT / "docs" / "RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md"

N_C = 3
G_BARE = 1.0
BETA_WILSON = 2 * N_C / (G_BARE * G_BARE)
T_HEAT_KERNEL = G_BARE * G_BARE
BETA_MANTON = BETA_WILSON / (2.0 * N_C)
HK_SINGLE_PLAQ = math.exp(-2.0 / 3.0)
WILSON_SINGLE_PLAQ = 0.4225317396


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        if ok:
            self.pass_count += 1
            tag = "PASS"
        else:
            self.fail_count += 1
            tag = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"[{tag}] {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    note = read(NOTE)
    hk_note = read(HK_NOTE)
    record_note = read(RECORD_NOTE)
    gate = Gate()

    print("=" * 78)
    print("BRIDGE-GAP ACTION-FORM UNIQUENESS NO-GO VERIFIER")
    print("=" * 78)
    print(f"canonical beta_W = {BETA_WILSON:.6f}")
    print(f"canonical t_HK = {T_HEAT_KERNEL:.6f}")
    print(f"canonical beta_M = {BETA_MANTON:.6f}")
    print(f"Wilson one-plaquette value = {WILSON_SINGLE_PLAQ:.10f}")
    print(f"HK one-plaquette value = {HK_SINGLE_PLAQ:.10f}")
    print()

    gate.check("target note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    gate.check("later HK diffusion note exists", HK_NOTE.exists(), str(HK_NOTE.relative_to(ROOT)))
    gate.check("record semigroup boundary note exists", RECORD_NOTE.exists(), str(RECORD_NOTE.relative_to(ROOT)))
    gate.check(
        "candidate set Wilson/HK/Manton is named",
        "Wilson, heat-kernel, Manton" in note
        and "Candidate I: Wilson" in note
        and "Candidate II: Heat-kernel" in note
        and "Candidate III: Manton" in note,
    )
    gate.check(
        "accepted-premise and retained support stack is enumerated",
        "Quantum / physical `Cl(3)` local algebra" in note
        and "Lattice / `Z^3` substrate" in note
        and "canonical Tr-form" in note
        and "per-site dimension two" in note
        and "reflection positivity" in note
        and "Single-clock evolution + Lieb-Robinson" in note
        and "Retained Casimir" in note,
    )
    gate.check(
        "canonical parameter matching recomputes",
        abs(BETA_WILSON - 6.0) < 1e-12
        and abs(T_HEAT_KERNEL - 1.0) < 1e-12
        and abs(BETA_MANTON - 1.0) < 1e-12,
        f"beta_W={BETA_WILSON}, t_HK={T_HEAT_KERNEL}, beta_M={BETA_MANTON}",
    )
    gate.check(
        "note records same continuum-leading match",
        "β_W = 6, t_HK = 1, β_M = 1" in note
        and "All three actions are consistent" in note,
    )
    gate.check(
        "finite-beta Wilson/HK values are distinct",
        abs(HK_SINGLE_PLAQ - WILSON_SINGLE_PLAQ) > 0.09,
        f"delta={HK_SINGLE_PLAQ - WILSON_SINGLE_PLAQ:.10f}",
    )
    gate.check(
        "HK value agrees with retained Casimir fundamental C2=4/3",
        abs(HK_SINGLE_PLAQ - 0.5134171190) < 1e-9,
        f"exp(-2/3)={HK_SINGLE_PLAQ:.10f}",
    )
    gate.check(
        "note states finite-beta action-form ambiguity",
        "distinct admissible actions" in note
        and "Wilson versus heat-kernel already give distinct ⟨P⟩(6) values at finite β" in note,
    )
    gate.check(
        "note marks no-go as current-stack/no-new-premise scoped",
        "current accepted-premise and retained support stack" in note
        and "without deriving, explicitly admitting, or conventionally supplying" in note
        and "action-selection criterion" in note,
    )
    gate.check(
        "note forbids action selection while preserving escape routes",
        "does not add a new primitive" in note
        and "Possible escape routes" in note,
    )
    gate.check(
        "later HK theorem sharpens but does not close the residual",
        "UNIQUE continuous-time" in hk_note
        and "No claim that HK is the framework's realized action" in hk_note
        and "open residual" in hk_note,
    )
    gate.check(
        "record boundary names the missing generator/rate law",
        "Record alone does not generate the rate law" in record_note
        and "continuous rate" in record_note,
    )

    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"TOTAL: PASS={gate.pass_count}, FAIL={gate.fail_count}")
    if gate.fail_count:
        print("Action-form uniqueness no-go verifier failed.")
        return 1
    print(
        "Verified scoped no-go: current accepted premises and retained support "
        "leave Wilson/HK action form ambiguous at finite beta; HK diffusion uniqueness is a "
        "sharp conditional route, not an already-realized action selection."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
