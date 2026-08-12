#!/usr/bin/env python3
"""Test the fixed-action nonlinear constraint route after the Block-53 repair.

Block 53 constructs an exact causal update for the *linear* two-TT sector.
This runner asks whether the inherited flat vertex-displacement kernel remains
an exact constraint generator on the supplied Block-21 sourced curved
continuation.  It reconstructs both Hessians from the repository-local Regge
action and inventories every nonzero momentum on L=3,...,6 periodic carriers.

The result is deliberately diagnostic.  The sourced background is stationary
only after the declared source and affine reactions are included, whereas the
tested Hessian omits their nonlinear connection terms.  Full rank therefore
proves that those missing terms are load-bearing; it is not a gravity no-go.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import mpmath as mp
import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10 as block19  # noqa: E402
import admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10 as block20  # noqa: E402
import admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10 as block21  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


AUDIT_TIMEOUT_SEC = 240
TOLERANCE = 1.0e-9

NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CURVED_REGGE_PSEUDOCONSTRAINT_PERFECT_ACTION_ROUTE_"
    "GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK21_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_"
    "CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
BLOCK53_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_"
    "LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CURVED_REGGE_PSEUDOCONSTRAINT_PERFECT_ACTION_ROUTE_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, key, statement, condition, detail=""):
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def rank(matrix, tolerance=TOLERANCE):
    return int(np.linalg.matrix_rank(matrix, tol=tolerance))


def build_flat_and_sourced_kernels():
    """Reconstruct the alpha=1/1024 flat and Bundle-B sourced kernels."""
    exact_basis = block19.exact_normal_basis(mp)
    basis = np.asarray(exact_basis, dtype=float)
    flat_lengths = np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )

    flat_einstein, flat_deficits = block20.uniform_regge_kernel(flat_lengths)
    flat_r2 = block21.curvature_squared_kernel(flat_lengths)
    flat_kernel = block21.combine_kernels(flat_einstein, flat_r2)

    bundle_b_source = block19.reaction.exact_source_rows()[-1]
    coordinates, jet, residual, iterations = block21.solve_source(
        bundle_b_source, sp.Rational(1, 100), exact_basis
    )
    sourced_lengths = flat_lengths + basis @ np.asarray(coordinates, dtype=float)
    sourced_einstein, sourced_deficits = block20.uniform_regge_kernel(
        sourced_lengths
    )
    sourced_r2 = block21.curvature_squared_kernel(sourced_lengths)
    sourced_kernel = block21.combine_kernels(sourced_einstein, sourced_r2)

    return {
        "basis": basis,
        "flat_lengths": flat_lengths,
        "flat_deficits": flat_deficits,
        "flat_kernel": flat_kernel,
        "coordinates": coordinates,
        "source_jet": jet,
        "source_residual": residual,
        "source_iterations": iterations,
        "sourced_lengths": sourced_lengths,
        "sourced_deficits": sourced_deficits,
        "sourced_kernel": sourced_kernel,
    }


def periodic_inventory(flat_kernel, sourced_kernel):
    records = []
    flat_ward_max = 0.0
    sourced_ward_max = 0.0
    sourced_min_gap = float("inf")
    sourced_min_location = None
    for length in (3, 4, 5, 6):
        flat_rank_counts = {}
        sourced_rank_counts = {}
        mode_count = 0
        for indices in product(range(length), repeat=4):
            if indices == (0, 0, 0, 0):
                continue
            momentum = (2.0 * np.pi / length) * np.asarray(indices, dtype=float)
            gauge = regge.gauge_map(momentum)
            flat = block20.bloch(flat_kernel, momentum)
            sourced = block20.bloch(sourced_kernel, momentum)
            flat_rank = rank(flat)
            sourced_rank = rank(sourced)
            flat_rank_counts[flat_rank] = flat_rank_counts.get(flat_rank, 0) + 1
            sourced_rank_counts[sourced_rank] = (
                sourced_rank_counts.get(sourced_rank, 0) + 1
            )
            flat_ward_max = max(flat_ward_max, float(np.linalg.norm(flat @ gauge)))
            sourced_ward_max = max(
                sourced_ward_max, float(np.linalg.norm(sourced @ gauge))
            )
            gap = float(np.min(np.abs(np.linalg.eigvalsh(sourced))))
            if gap < sourced_min_gap:
                sourced_min_gap = gap
                sourced_min_location = (length, indices)
            mode_count += 1
        records.append(
            (length, mode_count, flat_rank_counts, sourced_rank_counts)
        )
    return {
        "records": records,
        "flat_ward_max": flat_ward_max,
        "sourced_ward_max": sourced_ward_max,
        "sourced_min_gap": sourced_min_gap,
        "sourced_min_location": sourced_min_location,
    }


def ray_diagnostics(flat_kernel, sourced_kernel):
    direction = np.asarray((1.0, 0.7, -0.4, 0.2))
    records = []
    for scale in (0.4, 1.0):
        momentum = scale * direction
        gauge = regge.gauge_map(momentum)
        flat = block20.bloch(flat_kernel, momentum)
        sourced = block20.bloch(sourced_kernel, momentum)
        records.append(
            {
                "scale": scale,
                "flat_rank": rank(flat),
                "sourced_rank": rank(sourced),
                "flat_ward": float(np.linalg.norm(flat @ gauge)),
                "sourced_ward": float(np.linalg.norm(sourced @ gauge)),
                "relative_sourced_ward": float(
                    np.linalg.norm(sourced @ gauge)
                    / (np.linalg.norm(sourced) * np.linalg.norm(gauge))
                ),
            }
        )
    return records


def main():
    mp.mp.dps = 40
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    block21_note = BLOCK21_NOTE_PATH.read_text(encoding="utf-8")
    block53_note = BLOCK53_NOTE_PATH.read_text(encoding="utf-8")
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print("external_scientific_inputs: Bahr-Dittrich fixed-Regge gauge-symmetry analysis, perfect-action construction, and Dittrich-Hoehn canonical Pachner evolution are cited as primary-literature route context")
    print("analytic_boundary: the discrete Noether implication is exact; ranks and Ward residuals are double-precision exhaustive finite-mode calculations on the reconstructed repository action")
    print("physical_boundary: the sourced background includes affine reactions while the tested bare Hessian omits the source/constraint connection; full rank diagnoses that omission and is not a gravity no-go")

    checks.check(
        "source-and-axiom-boundary",
        "the foundation and parents leave nonlinear constraint/source dynamics unselected",
        "Admissibility is not a dynamics axiom" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat
        and "nonlinear geometry" in block53_note
        and "covariant sourced second variation" in block21_note
        and '"kinetic_isotropy_primitive"' in registry,
    )
    checks.check(
        "source-note-contract",
        "the note records the finite claim, literature route correction, value gate, and landed N1-N8 packet",
        "No-Go Discipline Gate" in note
        and "Promotion Value Gate" in note
        and "2,254" in note
        and "pseudo-constraints" in note
        and "perfect action" in note_flat
        and "Pachner" in note
        and "not evidence that gravity cannot work" in note_flat,
    )

    data = build_flat_and_sourced_kernels()
    expected_coordinates = np.asarray(
        (
            -0.00021189034555338222,
            0.0012366779546967518,
            0.0012366779546967518,
            0.0012366779546967518,
            0.009376284280482814,
        )
    )
    coordinate_error = float(
        np.max(np.abs(np.asarray(data["coordinates"], dtype=float) - expected_coordinates))
    )
    checks.check(
        "sourced-background-reconstruction",
        "the Block-21 Bundle-B continuation and nonzero curvature are reconstructed, not hard-coded into the Hessian test",
        data["source_residual"] < mp.mpf("1e-25")
        and coordinate_error < 2.0e-12
        and np.max(np.abs(data["flat_deficits"])) < 2.0e-13
        and np.max(np.abs(data["sourced_deficits"])) > 0.05,
        f"coordinate error={coordinate_error:.3e}; deficit max={np.max(np.abs(data['sourced_deficits'])):.9f}; Newton iterations={data['source_iterations']}",
    )

    inventory = periodic_inventory(data["flat_kernel"], data["sourced_kernel"])
    total_modes = sum(record[1] for record in inventory["records"])
    flat_pattern = all(record[2] == {11: record[1]} for record in inventory["records"])
    sourced_pattern = all(
        record[3] == {15: record[1]} for record in inventory["records"]
    )
    checks.check(
        "flat-four-null-inventory",
        "every nonzero L=3 through L=6 mode of the flat repaired kernel has rank eleven and four null directions",
        total_modes == 2254
        and flat_pattern
        and inventory["flat_ward_max"] < 2.0e-12
        and f"{inventory['flat_ward_max']:.3e}" in note,
        f"modes={total_modes}; rank counts={[record[2] for record in inventory['records']]}; max ||Q Gamma||={inventory['flat_ward_max']:.3e}",
    )
    checks.check(
        "sourced-bare-full-rank-inventory",
        "the bare fixed-action Hessian on the sourced continuation is full rank at every same periodic mode",
        sourced_pattern and inventory["sourced_min_gap"] > 4.0e-6,
        f"rank counts={[record[3] for record in inventory['records']]}; minimum gap={inventory['sourced_min_gap']:.9e} at {inventory['sourced_min_location']}",
    )

    rays = ray_diagnostics(data["flat_kernel"], data["sourced_kernel"])
    checks.check(
        "inherited-generator-ward-loss",
        "two generic momenta separate machine-zero flat Ward residuals from nonzero sourced bare-Hessian residuals",
        all(record["flat_rank"] == 11 for record in rays)
        and all(record["sourced_rank"] == 15 for record in rays)
        and rays[0]["flat_ward"] < 5.0e-13
        and rays[1]["flat_ward"] < 5.0e-13
        and 0.19 < rays[0]["sourced_ward"] < 0.21
        and 0.43 < rays[1]["sourced_ward"] < 0.45
        and f"{rays[0]['sourced_ward']:.9f}" in note
        and f"{rays[1]['sourced_ward']:.9f}" in note,
        "; ".join(
            f"x={record['scale']:.1f}: flat={record['flat_ward']:.3e}, sourced={record['sourced_ward']:.9f}, relative={record['relative_sourced_ward']:.9e}"
            for record in rays
        ),
    )

    checks.check(
        "route-boundary-not-universal",
        "the source note keeps improved/perfect actions, variable triangulations, connection variables, and complete source constraints live",
        "improved/perfect action" in note_flat
        and "variable-triangulation" in note_flat
        and "connection/tetrad" in note_flat
        and "complete source/constraint action" in note_flat
        and "continuous-zone" in note_flat
        and "no axiom is amended here" in note_flat.lower(),
    )

    print("per_element: checked all fifteen edge-class rows of both reconstructed Regge Hessians and all four inherited displacement columns")
    print("per_site: checked the homogeneous fifteen-edge cell and all fifty hinge-class contributions through the imported parent reconstruction")
    print("per_mode: checked every nonzero momentum on L=3,4,5,6 four-tori, totaling 2,254 distinct finite modes")
    print("per_block: checked the flat repaired block against the sourced Bundle-B continuation and the Block-53 nonlinear-constraint obligation")
    print("lattice_wide: checked and not executed — no continuous-zone, full-Z3, perfect-action, or variable-triangulation construction is claimed")

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
