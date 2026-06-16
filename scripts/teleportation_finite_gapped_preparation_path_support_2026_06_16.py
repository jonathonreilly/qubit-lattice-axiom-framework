#!/usr/bin/env python3
"""Finite preparation-path support for the Poisson teleportation resource.

This runner checks a narrow support claim for the audited finite surfaces:
the existing Poisson/CHSH Hamiltonian family H(G) is an exactly affine
finite-dimensional Hermitian path from the null Hamiltonian to the
G=1000 resource Hamiltonian, and the sampled path keeps a positive
ground-state gap on the audited 1D N=8 and 2D 4x4 surfaces.

It does not prove a continuum gap, a microscopic apparatus Hamiltonian,
native readout, durable record formation, or a deterministic physical
teleportation-resource theorem.
"""

from __future__ import annotations

import dataclasses
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import eigvalsh

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from frontier_bell_inequality import build_H1, build_H2_tensor, build_poisson  # noqa: E402
from frontier_teleportation_resource_from_poisson import (  # noqa: E402
    AuditCase,
    audit_case,
    lattice_for_case,
)

NOTE = ROOT / "docs" / "TELEPORTATION_FINITE_GAPPED_PREPARATION_PATH_SUPPORT_NOTE_2026-06-16.md"
PARENT_NOTE = ROOT / "docs" / "TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md"

G_SAMPLES = (
    0.0,
    1e-6,
    1e-3,
    1e-2,
    0.1,
    1.0,
    3.0,
    10.0,
    30.0,
    100.0,
    300.0,
    600.0,
    1000.0,
)

FAILURES: list[str] = []
PASSES = 0


@dataclasses.dataclass(frozen=True)
class PathCase:
    label: str
    dim: int
    side: int
    mass: float = 0.0
    target_g: float = 1000.0
    min_gap_threshold: float = 1e-3
    target_bell_threshold: float = 0.90
    target_teleportation_mean_threshold: float = 0.95


PATH_CASES = (
    PathCase("1d_N8_last_taste_path", dim=1, side=8),
    PathCase("2d_4x4_last_taste_path", dim=2, side=4),
)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASSES
    status = "PASS" if condition else "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{status}] {label}{suffix}")
    if not condition:
        FAILURES.append(f"{label}{suffix}")
    else:
        PASSES += 1


def path_components(case: PathCase) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int]:
    audit_case_zero = AuditCase(case.label, case.dim, case.side, case.mass, 0.0)
    n_sites, adj, parity, _coords = lattice_for_case(audit_case_zero)
    h1 = build_H1(n_sites, adj, parity, mass=case.mass)
    poisson = build_poisson(n_sites, adj)
    h0 = build_H2_tensor(h1, poisson, 0.0, n_sites)
    interaction_diag = np.array(
        [poisson[i, j] for i in range(n_sites) for j in range(n_sites)],
        dtype=complex,
    )
    interaction = np.diag(interaction_diag)
    return h0, interaction, h1, poisson, n_sites


def hamiltonian_at(h0: np.ndarray, interaction: np.ndarray, g_value: float) -> np.ndarray:
    return h0 + g_value * interaction


def sampled_gap_report(case: PathCase) -> dict[str, object]:
    h0, interaction, h1, poisson, n_sites = path_components(case)
    gaps: list[tuple[float, float, float]] = []

    check(
        f"{case.label}: null Hamiltonian Hermitian",
        np.allclose(h0, h0.conj().T, atol=1e-12),
    )
    check(
        f"{case.label}: interaction Hamiltonian Hermitian",
        np.allclose(interaction, interaction.conj().T, atol=1e-12),
    )

    for g_value in G_SAMPLES:
        built = build_H2_tensor(h1, poisson, g_value, n_sites)
        affine = hamiltonian_at(h0, interaction, g_value)
        check(
            f"{case.label}: H(G={g_value:g}) equals affine path",
            np.allclose(built, affine, atol=1e-10),
        )
        evals = eigvalsh(affine)
        gap = float(evals[1] - evals[0])
        gaps.append((g_value, float(evals[0]), gap))
        check(
            f"{case.label}: sampled ground gap at G={g_value:g} positive",
            gap > case.min_gap_threshold,
            f"gap={gap:.12g}",
        )

    min_g, _energy_at_min, min_gap = min(gaps, key=lambda row: row[2])
    check(
        f"{case.label}: minimum sampled gap clears finite-support floor",
        min_gap > case.min_gap_threshold,
        f"min_gap={min_gap:.12g} at G={min_g:g}",
    )
    return {
        "case": case,
        "n_sites": n_sites,
        "gaps": gaps,
        "min_g": min_g,
        "min_gap": min_gap,
        "interaction_norm": float(np.linalg.norm(interaction, ord=2)),
    }


def endpoint_resource_report(case: PathCase) -> dict[str, object]:
    null = audit_case(
        AuditCase(f"{case.label}_null", case.dim, case.side, case.mass, 0.0),
        trials=32,
        seed=20260616,
        high_fidelity_threshold=case.target_bell_threshold,
        probability_floor=1e-12,
    )
    target = audit_case(
        AuditCase(f"{case.label}_target", case.dim, case.side, case.mass, case.target_g),
        trials=32,
        seed=20260616,
        high_fidelity_threshold=case.target_bell_threshold,
        probability_floor=1e-12,
    )

    check(
        f"{case.label}: null endpoint is not a high-fidelity traced Bell resource",
        not bool(null["deterministic_high_fidelity_resource"]),
        f"Bell={null['logical_bell_fidelity']:.12g}",
    )
    check(
        f"{case.label}: target endpoint is a high-fidelity traced Bell resource",
        bool(target["deterministic_high_fidelity_resource"]),
        f"Bell={target['logical_bell_fidelity']:.12g}",
    )
    check(
        f"{case.label}: target endpoint has positive logical negativity",
        float(target["negativity"]) > 0.45,
        f"negativity={target['negativity']:.12g}",
    )
    check(
        f"{case.label}: target endpoint has high ideal teleportation mean fidelity",
        float(target["teleportation"]["mean"]) > case.target_teleportation_mean_threshold,
        f"mean={target['teleportation']['mean']:.12g}",
    )
    return {"null": null, "target": target}


def note_firewall_checks() -> None:
    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    required = (
        "actual_current_surface_status: bounded-support",
        "not a deterministic physical resource theorem",
        "audit_required_before_effective_retained: true",
        "No new axiom, primitive, approved premise, or apparatus theorem is introduced",
        "sampled finite-surface support",
    )
    for snippet in required:
        check(f"new support note contains firewall snippet: {snippet}", snippet in note_text)
    banned_status_lines = ("Status: retained", "**Status:** retained", "Status: promoted")
    for banned in banned_status_lines:
        check(f"new support note avoids bare status line `{banned}`", banned not in note_text)
    check(
        "parent note records 2026-06-16 finite preparation-path support",
        "2026-06-16 Finite Preparation-Path Support" in parent_text,
    )
    check(
        "parent note keeps apparatus/readout blocker open",
        "does not close physical detector/readout" in parent_text,
    )


def main() -> int:
    print("Teleportation finite preparation-path bounded-support runner")
    print("Status: sampled finite-surface support only; independent audit grades.")
    print()

    reports = []
    endpoint_reports = []
    for case in PATH_CASES:
        print(f"=== {case.label} ===")
        reports.append(sampled_gap_report(case))
        endpoint_reports.append(endpoint_resource_report(case))
        print()

    note_firewall_checks()

    print()
    print("Sampled path summary")
    for report, endpoint in zip(reports, endpoint_reports):
        case = report["case"]
        target = endpoint["target"]
        assert isinstance(case, PathCase)
        print(
            f"  {case.label}: n_sites={report['n_sites']}, "
            f"min_sampled_gap={report['min_gap']:.12g} at G={report['min_g']:g}, "
            f"||W||_2={report['interaction_norm']:.12g}, "
            f"target_Bell={target['logical_bell_fidelity']:.12g}, "
            f"target_Ftel_mean={target['teleportation']['mean']:.12g}"
        )

    print()
    print(f"TOTAL: PASS={PASSES:d} FAIL={len(FAILURES)}")
    if FAILURES:
        print("Failures:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print("VERDICT: bounded finite preparation-path support passes; physical apparatus/readout remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
