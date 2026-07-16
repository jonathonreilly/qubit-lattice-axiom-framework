#!/usr/bin/env python3
"""Open-gate verifier for the emergent conformal-class causal consumer.

The runner certifies honest parking, not causal closure. It separates negative
record/time boundaries from positive causal inputs, keeps sampled one-particle
group speed distinct from Lieb-Robinson velocity, verifies the surviving
class/scale algebra, and exits nonzero on any failed check.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_"
    "NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md"
)

NEGATIVE_BOUNDARIES = {
    "record_history_order_time_rate_firewall_2026-06-05",
}
POSITIVE_CAUSAL_ACCEPTED_EFFECTIVE_STATUSES = frozenset({"retained", "retained_bounded"})
OPEN_BRIDGES = (
    "record_atom_to_formation_event_map",
    "formation_event_dependency_order",
    "formation_event_to_lr_observable_event_set_identification",
    "quasilocal_lieb_robinson_composition_with_declared_weight",
    "lr_envelope_to_exact_causal_relation",
    "causal_event_set_to_lorentzian_manifold_interface",
)
SOURCE_FILES = (
    "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md",
    "scripts/frontier_record_history_time_rate_firewall_2026_06_05.py",
    "logs/runner-cache/frontier_record_history_time_rate_firewall_2026_06_05.txt",
    "docs/RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
    "scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py",
    "logs/runner-cache/reconstructed_h_quasilocal_microcausality_bridge_runner.txt",
)
NON_LOAD_BEARING_LR_CONTEXT = (
    "docs/FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"  | {detail}" if detail else ""
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{suffix}")
    return ok


def cache_reports_clean_execution(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    return (
        "exit_code: 0" in text
        and ("FAIL=0" in text or "FAIL: 0" in text)
        and "Traceback" not in text
    )


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def sampled_one_particle_group_speed(mass: float = 0.3, count: int = 65) -> float:
    """Sample max |grad E_d| in lattice momentum units; not an LR velocity."""
    grid = np.linspace(-np.pi, np.pi, count, endpoint=False)
    p1, p2, p3 = np.meshgrid(grid, grid, grid, indexing="ij", sparse=True)
    s1, s2, s3 = np.sin(p1), np.sin(p2), np.sin(p3)
    c1, c2, c3 = np.cos(p1), np.cos(p2), np.cos(p3)
    radicand = mass * mass + s1 * s1 + s2 * s2 + s3 * s3
    denominator = np.sqrt(radicand) * np.sqrt(1.0 + radicand)
    speed_sq = (
        (s1 * c1 / denominator) ** 2
        + (s2 * c2 / denominator) ** 2
        + (s3 * c3 / denominator) ** 2
    )
    return float(np.sqrt(speed_sq).max())


def main() -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0

    print("=" * 78)
    print("Emergent conformal-class consumer: open causal-source bridge ledger")
    print("=" * 78)

    note_exists = NOTE.exists()
    note_text = NOTE.read_text(encoding="utf-8") if note_exists else ""
    check("source note exists", note_exists, display_path(NOTE))
    required_markers = [
        "**Claim type:** open_gate",
        "actual_current_surface_status: open",
        "No Lorentzian conformal class is assembled from the current packet.",
        "A `retained_no_go` row must never satisfy a positive",
        "sampled_one_particle_group_speed",
    ]
    check(
        "source note is an explicit open gate rather than a conditional assembly",
        all(marker in note_text for marker in required_markers),
        f"{sum(marker in note_text for marker in required_markers)}/{len(required_markers)} markers",
    )
    for bridge in OPEN_BRIDGES:
        check(f"named open bridge is explicit: {bridge}", bridge in note_text)

    check(
        "positive causal status acceptance excludes retained_no_go",
        "retained_no_go" not in POSITIVE_CAUSAL_ACCEPTED_EFFECTIVE_STATUSES,
        ", ".join(sorted(POSITIVE_CAUSAL_ACCEPTED_EFFECTIVE_STATUSES)),
    )
    check(
        "negative record/time row is kept in the negative-boundary class",
        "record_history_order_time_rate_firewall_2026-06-05" in NEGATIVE_BOUNDARIES,
    )

    for rel_path in SOURCE_FILES:
        path = ROOT / rel_path
        check(f"source packet path exists: {rel_path}", path.exists())
        if rel_path.startswith("logs/runner-cache/") and path.exists():
            check(
                f"owned cache reports clean execution: {rel_path}",
                cache_reports_clean_execution(path),
            )

    lr_context_name = Path(NON_LOAD_BEARING_LR_CONTEXT).name
    check(
        "free-bilinear LR candidate remains non-load-bearing context",
        NON_LOAD_BEARING_LR_CONTEXT not in SOURCE_FILES
        and f"`{lr_context_name}`" in note_text
        and f"]({lr_context_name})" not in note_text,
        "not a required source-packet file or citation-graph dependency",
    )

    print()
    print("Diagnostic only: one-particle group speed")
    group_speed = sampled_one_particle_group_speed()
    print(f"  sampled_one_particle_group_speed = {group_speed:.6f} (lattice units)")
    check(
        "sampled one-particle group speed is finite",
        np.isfinite(group_speed) and group_speed > 0,
        "not used as an LR velocity or causal-assembly gate",
    )

    print()
    print("Exact support: null relation fixes class, not scale")
    eta = np.diag([-1.0, 1.0, 1.0, 1.0])
    conformal_metric = 3.7 * eta
    null_vector = np.array([1.0, 1.0, 0.0, 0.0])
    altered_speed_metric = np.diag([-0.6**2, 1.0, 1.0, 1.0])
    same_null = (
        abs(null_vector @ eta @ null_vector) < 1e-12
        and abs(null_vector @ conformal_metric @ null_vector) < 1e-12
    )
    altered_null = abs(null_vector @ altered_speed_metric @ null_vector) > 1e-6
    check(
        "g and Omega^2 g share the null vector while an altered-speed metric does not",
        same_null and altered_null and not np.allclose(eta, conformal_metric),
    )

    print()
    print("Negative support: abstract index order does not fix clock rate")
    indices = np.arange(6)
    tau_a = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    tau_b = np.array([0.0, 0.5, 2.0, 2.1, 4.8, 5.0])
    order_preserved = np.all(np.diff(tau_a) > 0) and np.all(np.diff(tau_b) > 0)
    rates_differ = not np.allclose(np.diff(tau_a), np.diff(tau_b))
    check(
        "the same abstract index order admits different clock intervals",
        np.array_equal(indices, indices.copy()) and order_preserved and rates_differ,
        "this is not a formation-event or causal-order construction",
    )

    parked = all(bridge in note_text for bridge in OPEN_BRIDGES) and "**Claim type:** open_gate" in note_text
    check(
        "final conformal consumer remains parked behind the named bridges",
        parked,
        "runner certifies open-gate honesty, not causal closure",
    )

    print()
    print("CLAIM DISPOSITION: OPEN")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
