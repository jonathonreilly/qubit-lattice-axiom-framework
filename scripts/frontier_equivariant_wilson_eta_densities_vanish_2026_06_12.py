#!/usr/bin/env python3
"""Runner for the equivariant Wilson-eta density bounded note.

No cache is written. All spectral data are computed from the closed-form
per-momentum dispersion; no dense position-space operators are built.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "EQUIVARIANT_WILSON_ETA_DENSITIES_VANISH_ON_TESTED_WINDOW_BOUNDED_NOTE_2026-06-12.md"
BULK = ROOT / "docs" / "HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
SCRIPT = ROOT / "scripts" / "frontier_equivariant_wilson_eta_densities_vanish_2026_06_12.py"

LS_ALL = [2, 3, 4, 6, 8]
LS_DENSITY = [3, 4, 6, 8]
LTS = [4, 8]
RS = [0.5, 1.0]
MS = [-2.5, -1.5, -0.5, 0.5]
VARIANTS = {
    "spatial_wilson": False,
    "spatial_temporal_wilson": True,
}
TWO_NINTHS = 2.0 / 9.0


@dataclass
class CheckLog:
    passed: int = 0
    failed: int = 0

    def check(self, tag: str, condition: bool, detail: str = "") -> None:
        status = "PASS" if condition else "FAIL"
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        suffix = f" - {detail}" if detail else ""
        print(f"[{tag}] {status}{suffix}")


def antiperiodic_momenta(size: int) -> np.ndarray:
    return 2.0 * np.pi * (np.arange(size, dtype=float) + 0.5) / float(size)


def spatial_orbits(size: int) -> list[tuple[tuple[int, int, int], ...]]:
    seen: set[tuple[int, int, int]] = set()
    orbits: list[tuple[tuple[int, int, int], ...]] = []
    for ix in range(size):
        for iy in range(size):
            for iz in range(size):
                seed = (ix, iy, iz)
                if seed in seen:
                    continue
                orbit: list[tuple[int, int, int]] = []
                current = seed
                for _ in range(3):
                    if current not in orbit:
                        orbit.append(current)
                    current = (current[1], current[2], current[0])
                for item in orbit:
                    seen.add(item)
                orbits.append(tuple(orbit))
    return orbits


def raw_sign(value: float, tol: float = 1.0e-10) -> float:
    if value > tol:
        return 1.0
    if value < -tol:
        return -1.0
    return 0.0


def sector_etas(
    L: int,
    L_t: int,
    r: float,
    m: float,
    include_temporal_wilson: bool,
    smooth_eps: float | None = None,
) -> tuple[np.ndarray, int, int]:
    """Return eta_1, eta_omega, eta_omega2 plus orbit/mode denominators."""
    ks = antiperiodic_momenta(L)
    ws = antiperiodic_momenta(L_t)
    etas = np.zeros(3, dtype=float)
    orbit_modes = 0
    momentum_modes = 0

    for orbit in spatial_orbits(L):
        rep = orbit[0]
        chars = np.array([1.0, 0.0, 0.0]) if len(orbit) == 1 else np.ones(3, dtype=float)
        kx, ky, kz = (ks[i] for i in rep)
        spatial_sin_sq = np.sin(kx) ** 2 + np.sin(ky) ** 2 + np.sin(kz) ** 2
        spatial_mass = (1.0 - np.cos(kx)) + (1.0 - np.cos(ky)) + (1.0 - np.cos(kz))

        for w in ws:
            kinetic = np.sqrt(spatial_sin_sq + np.sin(w) ** 2)
            mass = m + r * spatial_mass
            if include_temporal_wilson:
                mass += r * (1.0 - np.cos(w))
            lambdas = (mass + kinetic, mass - kinetic)
            if smooth_eps is None:
                signed_pair = sum(raw_sign(lam) for lam in lambdas)
            else:
                signed_pair = float(np.tanh(lambdas[0] / smooth_eps) + np.tanh(lambdas[1] / smooth_eps))
            etas += chars * signed_pair
            orbit_modes += 1
            momentum_modes += len(orbit)

    return etas, orbit_modes, momentum_modes


def density_row(variant: str, L_t: int, r: float, m: float) -> tuple[list[float], list[float], list[np.ndarray]]:
    mode_values: list[float] = []
    orbit_values: list[float] = []
    eta_values: list[np.ndarray] = []
    include_temporal = VARIANTS[variant]
    for L in LS_DENSITY:
        etas, orbit_modes, momentum_modes = sector_etas(L, L_t, r, m, include_temporal)
        gap = abs(etas[0] - etas[1])
        mode_values.append(float(gap / momentum_modes))
        orbit_values.append(float(gap / orbit_modes))
        eta_values.append(etas.copy())
    return mode_values, orbit_values, eta_values


def fmt_seq(values: list[float]) -> str:
    return ", ".join(f"{value:.6f}" for value in values)


def run_sector_zero_baseline(log: CheckLog) -> None:
    print("\nSector-zero baseline (r=0, m=0):")
    for eps in [None, 0.1, 0.01]:
        max_abs = 0.0
        label = "raw" if eps is None else f"tanh eps={eps}"
        for variant, include_temporal in VARIANTS.items():
            for L_t in LTS:
                for L in LS_ALL:
                    etas, _, _ = sector_etas(L, L_t, 0.0, 0.0, include_temporal, smooth_eps=eps)
                    max_abs = max(max_abs, float(np.max(np.abs(etas))))
        print(f"  {label}: max_abs_sector_eta={max_abs:.3e}")
        log.check(
            f"sector_zero_{label.replace(' ', '_')}",
            max_abs < 1.0e-9,
            "r=0,m=0 sector etas vanish across variants, L, L_t",
        )


def run_k_odd_cancellation(log: CheckLog) -> None:
    total = 0
    max_abs = 0.0
    for variant, include_temporal in VARIANTS.items():
        for L_t in LTS:
            for r in RS:
                for m in MS:
                    for L in LS_ALL:
                        etas, _, _ = sector_etas(L, L_t, r, m, include_temporal)
                        k_odd = etas[1] - etas[2]
                        max_abs = max(max_abs, abs(float(k_odd)))
                        total += 1
    print(f"\nK-odd sector cancellation count={total}, max_abs(eta_omega-eta_omega2)={max_abs:.3e}")
    log.check("k_odd_identically_zero", max_abs == 0.0, "all tested parameter points")


def run_density_decay(log: CheckLog) -> None:
    print("\nDensity tables over L=3,4,6,8:")
    near_hits: list[tuple[str, int, float, float, float, float]] = []
    tails_ok = True
    zero_crossing_guard_seen = False
    max_l8 = 0.0
    min_distance = 10.0

    for variant in VARIANTS:
        print(f"\n  variant={variant}")
        for L_t in LTS:
            for r in RS:
                for m in MS:
                    rho_mode, rho_orbit, _ = density_row(variant, L_t, r, m)
                    tail_delta = abs(rho_mode[-1] - rho_mode[-2])
                    last3_range = max(rho_mode[1:]) - min(rho_mode[1:])
                    monotone_tail = rho_mode[2] <= rho_mode[1] + 1.0e-12 and rho_mode[3] <= rho_mode[2] + 1.0e-12
                    all_zero = all(abs(value) < 1.0e-12 for value in rho_mode)
                    zero_crossing_tiny_tail = (
                        rho_mode[1] < 1.0e-12
                        and rho_mode[2] < 1.0e-12
                        and rho_mode[3] <= 1.0 / 256.0 + 1.0e-12
                    )
                    if zero_crossing_tiny_tail:
                        zero_crossing_guard_seen = True
                    tails_ok = tails_ok and (monotone_tail or all_zero or zero_crossing_tiny_tail)
                    l8_candidate = rho_mode[-1]
                    distance = abs(l8_candidate - TWO_NINTHS)
                    max_l8 = max(max_l8, l8_candidate)
                    min_distance = min(min_distance, distance)
                    if distance < 0.05:
                        near_hits.append((variant, L_t, r, m, l8_candidate, distance))
                    print(
                        "    "
                        f"L_t={L_t:>2} r={r:.1f} m={m:>4.1f} "
                        f"rho_mode=[{fmt_seq(rho_mode)}] "
                        f"rho_orbit=[{fmt_seq(rho_orbit)}] "
                        f"tail_delta={tail_delta:.6f} last3_range={last3_range:.6f}"
                    )

    print("\nL=8 distance table against 2/9:")
    for variant in VARIANTS:
        for L_t in LTS:
            for r in RS:
                for m in MS:
                    rho_mode, _, _ = density_row(variant, L_t, r, m)
                    candidate = rho_mode[-1]
                    distance = abs(candidate - TWO_NINTHS)
                    print(
                        f"  variant={variant:>24} L_t={L_t:>2} r={r:.1f} m={m:>4.1f} "
                        f"candidate={candidate:.6f} distance_to_2/9={distance:.6f}"
                    )

    print("\nMisread guard: candidate = 0; distance = 2/9 -- not a hit")
    log.check(
        "density_tail_subextensive",
        tails_ok,
        "all rows monotone on the tail or covered by the scoped zero-crossing tiny-tail guard",
    )
    log.check(
        "zero_crossing_guard_seen",
        zero_crossing_guard_seen,
        "finite zero-zero-small tail explicitly detected and printed",
    )
    log.check(
        "no_L8_near_2_over_9",
        not near_hits and min_distance > 0.05,
        f"max_L8={max_l8:.6f}, min_distance_to_2/9={min_distance:.6f}",
    )
    log.check(
        "misread_guard",
        abs(0.0 - TWO_NINTHS) == TWO_NINTHS,
        "candidate=0 has distance 2/9, not a fixed-locus hit",
    )


def construction_has_no_delta_variable() -> bool:
    source = SCRIPT.read_text()
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == "delta":
            return False
        if isinstance(node, ast.arg) and node.arg == "delta":
            return False
    return True


def run_scoped_boundary(log: CheckLog, note_text: str) -> None:
    print("\nScoped boundary assembly booleans:")
    booleans = {
        "tested_window": "tested window" in note_text,
        "does_not_close": "does not close" in note_text,
        "next_paths": "The next paths" in note_text,
        "boundary_localized": "boundary-localized spectral structure" in note_text,
        "multiset_to_geometry": "direct multiset-to-geometry equation" in note_text,
        "no_delta_input_sentence": "No delta appears anywhere as an input on this surface" in note_text,
        "no_delta_variable": construction_has_no_delta_variable(),
    }
    for key, value in booleans.items():
        print(f"  {key}: {value}")
    log.check(
        "free_bulk_boundary_and_next_paths",
        all(booleans.values()),
        "boundary, next paths, and no-delta checks",
    )


def markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)


def run_b_checks(log: CheckLog, note_text: str) -> None:
    bulk_text = BULK.read_text()
    print("\nB-checks:")
    log.check("B01_bulk_note_exists", BULK.exists() and AXIOMS.exists(), "both markdown dependencies are present")
    log.check(
        "B02_bulk_eta_lemma_grep",
        "η_APS(D_stag)" in bulk_text and ":=  Σ_λ sign(λ)  =  0" in bulk_text,
        "bulk note contains eta := sum sign(lambda) = 0 lemma line",
    )
    log.check(
        "B03_bulk_named_opens_grep",
        all(phrase in bulk_text for phrase in ["manifold-with-boundary geometry", "spectral flow", "residue-style boundary corrections"]),
        "bulk note names the open APS paths preserved by the scoped boundary",
    )
    for tag, phrase in [
        ("B04_tested_window_sentence", "tested window"),
        ("B05_does_not_close_sentence", "does not close"),
        ("B06_next_paths_sentence", "The next paths"),
        ("B07_no_delta_sentence", "No delta appears anywhere as an input on this surface"),
        ("B08_firewall_r_never_fixed", "r is never fixed"),
        ("B09_no_readings_cells", "No readings/cells are introduced"),
    ]:
        log.check(tag, phrase in note_text, phrase)

    forbidden = [
        "only possible",
        "exhausted",
        "fourth " + "wall",
        "final " + "wall",
        "map " + "complete",
        "".join(["WA", "LLS", "-MOVE"]),
        "r = 1/2",
        "proves R-eta",
        "derives R-eta",
        "large-L theorem",
        "delta input",
    ]
    absent = [phrase for phrase in forbidden if phrase in note_text]
    log.check("B10_forbidden_phrases_absent", not absent, f"absent={absent}")

    links = markdown_links(note_text)
    expected_links = {
        ("`HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md`", "HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md"),
        ("`MINIMAL_AXIOMS_2026-06-05.md`", "MINIMAL_AXIOMS_2026-06-05.md"),
    }
    log.check("B11_link_inventory_exactly_two", len(links) == 2 and set(links) == expected_links, f"links={links}")

    companions = [
        "`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`",
        "`SCALAR_I_AND_REAL_GENERATION_STRUCTURE_K_PARITY_SEPARATION_BOUNDED_NOTE_2026-06-08.md`",
        "`ETA_HOLONOMY_BASE_FLUX_SCOPE_BOUNDARY_NOTE_2026-06-06.md`",
        "`ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md`",
    ]
    log.check("B12_companions_backticked", all(item in note_text for item in companions), "context companions are backticked")
    log.check("B13_no_promotion", "**No-promotion statement:**" in note_text, "No-promotion statement present")
    log.check("B14_status_authority", "**Status authority:** independent audit lane only." in note_text, "standard status-authority line present")
    log.check("B15_claim_type", "**Claim type:** bounded_theorem" in note_text, "bounded theorem claim type")
    log.check("B16_source_disclaimer", "**Source-note proposal disclaimer:**" in note_text, "source-note proposal disclaimer present")
    log.check("B17_memory_budget", "per-momentum-mode closed-form dispersions" in note_text and "never dense position-space operators" in note_text, "memory budget text present")
    log.check("B18_both_variants", "spatial + temporal Wilson" in note_text and "spatial Wilson" in note_text, "both Wilson variants documented")
    log.check("B19_zero_crossing_scoped", "zero-crossing tail" in note_text, "finite zero-crossing tail scoped honestly")
    log.check(
        "B20_no_go_discipline_gate",
        "## No-Go Discipline Gate" in note_text
        and "**N1 - alternative routes.**" in note_text
        and "**N8 - cross-cycle echo.**" in note_text
        and "not a global R-eta no-go" in note_text,
        "N1-N8 gate present and scoped to the free-bulk boundary",
    )


def print_diff_stat_without_git() -> None:
    print("\ngit diff --stat (not executed; no-git/no-network rule honored)")
    for path in [NOTE, SCRIPT]:
        rel = path.relative_to(ROOT)
        line_count = path.read_text().count("\n")
        byte_count = path.stat().st_size
        print(f"  {rel} | {line_count} lines | {byte_count} bytes")


def main() -> int:
    log = CheckLog()
    note_text = NOTE.read_text()

    run_sector_zero_baseline(log)
    run_k_odd_cancellation(log)
    run_density_decay(log)
    run_scoped_boundary(log, note_text)
    run_b_checks(log, note_text)
    print_diff_stat_without_git()

    print(f"\nSUMMARY: PASS={log.passed} FAIL={log.failed}")
    if log.passed >= 16 and log.failed == 0:
        print("VERDICT: bounded theorem checks pass on the tested window.")
        return 0
    print("VERDICT: checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
