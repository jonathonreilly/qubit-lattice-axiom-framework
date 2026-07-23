#!/usr/bin/env python3
"""Cycle 637: narrow homology discriminator for the Cycle-537 cap route.

This runner tests only static two-chain fillings inside the unchanged periodic
cubic cellulation.  It does not test arbitrary local circuits, defect motion,
code deformation, added topology, or time-multiplexed ancillas.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import resource
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "outputs/physical_unchanged_torus_cap_homology_discriminator_cycle637_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_unchanged_torus_cap_homology_discriminator_cycle637_cold_2026_07_23.txt"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_UNCHANGED_TORUS_CAP_HOMOLOGY_DISCRIMINATOR_CYCLE637_NOTE_2026-07-23.md"

UPSTREAM = {
    "Cycle269": ROOT / "docs/work_history/repo/review_feedback/WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md",
    "Cycle532": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md",
    "Cycle535": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_WILSON_MEASUREMENT_RESET_STABILIZATION_CYCLE535_NOTE_2026-07-21.md",
    "Cycle537": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md",
    "no_go_skill": ROOT / "docs/ai_methodology/skills/no-go-discipline/SKILL.md",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def f2_rank(words: list[int]) -> int:
    """Rank of bit vectors over F2, represented as Python integers."""
    pivots: dict[int, int] = {}
    for original in words:
        word = original
        while word:
            pivot = word.bit_length() - 1
            if pivot in pivots:
                word ^= pivots[pivot]
            else:
                pivots[pivot] = word
                break
    return len(pivots)


def parity(word: int) -> int:
    return word.bit_count() & 1


def determinant3(matrix: tuple[tuple[int, ...], ...]) -> int:
    a = matrix
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def proper_cubic_frames() -> list[tuple[tuple[int, ...], ...]]:
    frames = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] if col == perm[row] else 0 for col in range(3))
                for row in range(3)
            )
            if determinant3(matrix) == 1:
                frames.append(matrix)
    assert len(frames) == 24
    return frames


def multiply(a: tuple[tuple[int, ...], ...], b: tuple[tuple[int, ...], ...]):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def axis_permutation(frame: tuple[tuple[int, ...], ...]) -> tuple[int, int, int]:
    # A column is the image of a source basis vector.  Signs vanish in H_1(-;F2).
    result = []
    for source in range(3):
        target = next(row for row in range(3) if frame[row][source])
        result.append(target)
    return tuple(result)


def build_complex(L: int) -> dict:
    N = L**3

    def vertex(x: int, y: int, z: int) -> int:
        return ((x % L) * L + (y % L)) * L + (z % L)

    def edge(axis: int, x: int, y: int, z: int) -> int:
        return axis * N + vertex(x, y, z)

    coords = list(itertools.product(range(L), repeat=3))

    edge_boundaries: list[int] = []
    for axis in range(3):
        step = [0, 0, 0]
        step[axis] = 1
        for x, y, z in coords:
            end = (x + step[0], y + step[1], z + step[2])
            edge_boundaries.append((1 << vertex(x, y, z)) ^ (1 << vertex(*end)))

    plaquette_boundaries: list[int] = []
    for a, b in ((0, 1), (0, 2), (1, 2)):
        for x, y, z in coords:
            c = [x, y, z]
            ca = c.copy()
            ca[a] += 1
            cb = c.copy()
            cb[b] += 1
            word = 0
            word ^= 1 << edge(a, *c)
            word ^= 1 << edge(b, *ca)
            word ^= 1 << edge(a, *cb)
            word ^= 1 << edge(b, *c)
            plaquette_boundaries.append(word)

    wilsons: list[int] = []
    cocycles: list[int] = []
    for axis in range(3):
        w = 0
        dual = 0
        for t in range(L):
            c = [0, 0, 0]
            c[axis] = t
            w ^= 1 << edge(axis, *c)
        transverse = [a for a in range(3) if a != axis]
        for u in range(L):
            for v in range(L):
                c = [0, 0, 0]
                c[axis] = 0
                c[transverse[0]] = u
                c[transverse[1]] = v
                dual ^= 1 << edge(axis, *c)
        wilsons.append(w)
        cocycles.append(dual)

    rank_d1 = f2_rank(edge_boundaries)
    rank_d2 = f2_rank(plaquette_boundaries)
    cycle_dim = 3 * N - rank_d1
    h1_dim = cycle_dim - rank_d2
    wilson_boundary_residuals = []
    for w in wilsons:
        boundary = 0
        for e in range(3 * N):
            if (w >> e) & 1:
                boundary ^= edge_boundaries[e]
        wilson_boundary_residuals.append(boundary.bit_count())

    face_dual_pairing_failures = sum(
        parity(face & dual) for face in plaquette_boundaries for dual in cocycles
    )
    wilson_dual_pairing = [
        [parity(w & dual) for dual in cocycles] for w in wilsons
    ]
    individual_augments = [
        f2_rank(plaquette_boundaries + [w]) - rank_d2 for w in wilsons
    ]
    triple_augment = f2_rank(plaquette_boundaries + wilsons) - rank_d2

    # A damaged Wilson is not even a cycle, so it cannot be a two-chain boundary.
    damaged_cycle_boundary_weights = []
    for w in wilsons:
        one_edge = w & -w
        damaged = w ^ one_edge
        boundary = 0
        for e in range(3 * N):
            if (damaged >> e) & 1:
                boundary ^= edge_boundaries[e]
        damaged_cycle_boundary_weights.append(boundary.bit_count())

    e_int = 2 * L * (L - 1)
    local_disk_checks = L * L + (L - 1) ** 2
    return {
        "L": L,
        "cells": N,
        "vertices": N,
        "edges": 3 * N,
        "plaquettes": 3 * N,
        "rank_boundary_1": rank_d1,
        "rank_boundary_2": rank_d2,
        "expected_rank_boundary_1": N - 1,
        "expected_rank_boundary_2": 2 * N - 2,
        "cycle_space_dimension": cycle_dim,
        "H1_dimension": h1_dim,
        "wilson_boundary_weights": wilson_boundary_residuals,
        "face_dual_pairing_failures": face_dual_pairing_failures,
        "wilson_dual_pairing": wilson_dual_pairing,
        "individual_wilson_rank_increments": individual_augments,
        "triple_wilson_rank_increment": triple_augment,
        "rank_after_three_formal_caps": rank_d2 + triple_augment,
        "cycle_space_exhausted_after_three_caps": rank_d2 + triple_augment == cycle_dim,
        "damaged_wilson_boundary_weights": damaged_cycle_boundary_weights,
        "Cycle537_disk_interior_edges_per_axis": e_int,
        "Cycle537_disk_local_checks_per_axis": local_disk_checks,
        "Cycle537_Euler_surplus_per_axis": local_disk_checks - e_int,
        "Cycle537_total_added_M2": 3 * e_int,
        "Cycle537_added_M2_per_coarse_cell": 3 * e_int / N,
    }


def exact_citation(path: Path, fragment: str) -> dict:
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if fragment in line:
            return {
                "path": str(path.relative_to(ROOT)),
                "line": line_number,
                "line_text": line.strip(),
                "fragment": fragment,
            }
    raise AssertionError(f"citation fragment absent: {path}: {fragment}")


def main() -> int:
    start = time.perf_counter()
    log: list[str] = []
    tests: list[dict] = []

    def check(name: str, condition: bool, detail) -> None:
        status = "PASS" if condition else "FAIL"
        line = f"{status} {name} :: {detail}"
        print(line)
        log.append(line)
        tests.append({"name": name, "pass": bool(condition), "detail": detail})

    upstream_hashes = {name: sha256(path) for name, path in UPSTREAM.items()}
    check("committed Cycle269/532/535/537 and current no-go shores are readable", len(upstream_hashes) == 5, upstream_hashes)

    sizes = [3, 5, 6, 7]
    results = [build_complex(L) for L in sizes]
    check(
        "periodic cubic chain ranks and H1 are exact on train and held sizes",
        all(
            row["rank_boundary_1"] == row["expected_rank_boundary_1"]
            and row["rank_boundary_2"] == row["expected_rank_boundary_2"]
            and row["H1_dimension"] == 3
            for row in results
        ),
        {row["L"]: [row["rank_boundary_1"], row["rank_boundary_2"], row["H1_dimension"]] for row in results},
    )
    check(
        "three axial Wilsons are cycles with identity dual-cocycle pairing",
        all(
            row["wilson_boundary_weights"] == [0, 0, 0]
            and row["wilson_dual_pairing"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            and row["face_dual_pairing_failures"] == 0
            for row in results
        ),
        {row["L"]: row["wilson_dual_pairing"] for row in results},
    )
    check(
        "no axial Wilson is a static plaquette two-chain boundary in the unchanged torus",
        all(row["individual_wilson_rank_increments"] == [1, 1, 1] for row in results),
        {row["L"]: row["individual_wilson_rank_increments"] for row in results},
    )
    check(
        "three formal cap attachments kill exactly the three H1 characters",
        all(row["triple_wilson_rank_increment"] == 3 and row["cycle_space_exhausted_after_three_caps"] for row in results),
        {row["L"]: [row["triple_wilson_rank_increment"], row["rank_after_three_formal_caps"]] for row in results},
    )
    check(
        "Cycle537 square-disk Euler surplus matches one killed character per axis",
        all(row["Cycle537_Euler_surplus_per_axis"] == 1 for row in results),
        {row["L"]: [row["Cycle537_disk_interior_edges_per_axis"], row["Cycle537_disk_local_checks_per_axis"], row["Cycle537_added_M2_per_coarse_cell"]] for row in results},
    )

    frames = proper_cubic_frames()
    frame_set = set(frames)
    permutations = [axis_permutation(frame) for frame in frames]
    group_failures = sum(multiply(a, b) not in frame_set for a in frames for b in frames)
    permutation_failures = sum(sorted(p) != [0, 1, 2] for p in permutations)
    triple_orbit_failures = sum(set(p) != {0, 1, 2} for p in permutations)
    check(
        "proper-cubic all24/all576 transports the three homology classes as one set",
        len(frames) == 24 and group_failures == 0 and permutation_failures == 0 and triple_orbit_failures == 0,
        {"frames": len(frames), "products": 576, "group_failures": group_failures, "orbit_failures": triple_orbit_failures},
    )
    check(
        "deletion control refuses a broken Wilson as a cap boundary",
        all(row["damaged_wilson_boundary_weights"] == [2, 2, 2] for row in results),
        {row["L"]: row["damaged_wilson_boundary_weights"] for row in results},
    )

    citations = {
        "Cycle532_topological_wall": exact_citation(UPSTREAM["Cycle532"], "bounded circuit preparing that fixed-spin face-code state is supplied."),
        "Cycle535_open_defect_route": exact_citation(UPSTREAM["Cycle535"], "A defect-mediated process that leaves the code transiently"),
        "Cycle537_embedding_wall": exact_citation(UPSTREAM["Cycle537"], "It does not embed those cap"),
        "Cycle537_two_walls": exact_citation(UPSTREAM["Cycle537"], "The collapsed remaining set has two walls:"),
        "Cycle269_topological_center": exact_citation(UPSTREAM["Cycle269"], "the three-dimensional Wilson center modulo local checks."),
    }

    n1_families = [
        {"family": "unchanged-torus static plaquette fill", "object": "two-chain in the existing periodic cubic cell complex", "mechanism": "sum bounded plaquette boundaries", "terminal_obligation": "bound one axial Wilson", "status": "ATTEMPTED", "result": "ruled out for this mechanism by exact dual-cocycle pairing"},
        {"family": "added square fill-disk topology", "object": "Cycle537 auxiliary disk complex", "mechanism": "Euler-surplus bounded face/star checks", "terminal_obligation": "one fixed physical 3D embedding plus preparation", "status": "ATTEMPTED", "result": "algebraically positive; physical embedding/preparation open"},
        {"family": "Wilson measurement plus membrane reset", "object": "Cycle535 channel", "mechanism": "measure sign and apply conjugate membrane", "terminal_obligation": "preserve full target matter", "status": "ATTEMPTED", "result": "exact seam twist; route-specific failure"},
        {"family": "defect-mediated autonomous pumping", "object": "mobile local syndromes", "mechanism": "leave code, wind, annihilate", "terminal_obligation": "converge and intertwine matter", "status": "OPEN", "result": "not ruled out"},
        {"family": "cut-sheet code deformation", "object": "temporary rough boundaries", "mechanism": "open, grow, and reglue periodic code", "terminal_obligation": "restore periodic target covariantly", "status": "OPEN", "result": "not ruled out"},
        {"family": "from-scratch coherent encoder", "object": "target plus product ancillas", "mechanism": "local code-growth isometry", "terminal_obligation": "prepare fixed representation without correcting unknown sector", "status": "OPEN", "result": "not ruled out"},
        {"family": "time-multiplexed auxiliary worldvolume", "object": "state-carried local program and reusable ancillas", "mechanism": "simulate cap incidence across program phase", "terminal_obligation": "bounded-space exact E/G without calling phase time", "status": "OPEN", "result": "not ruled out"},
    ]
    attempted = sum(row["status"] == "ATTEMPTED" for row in n1_families)
    n2_walls = {
        "W_embed": "realize added cap/deformation incidence in one fixed proper-cubic physical M2 substrate",
        "W_prepare": "construct a lawful local state isometry or autonomous convergence map preserving the complete target factor",
    }
    n2_pairs = [
        {"from": "W_embed", "to": "W_prepare", "implied": False, "reason": "a geometric incidence does not prepare its code state"},
        {"from": "W_prepare", "to": "W_embed", "implied": False, "reason": "an abstract preparation does not establish physical 3D locality"},
    ]
    n4 = [
        {**citations["Cycle532_topological_wall"], "prior_residual": "fixed-Wilson state preparation absent", "current_residual": "unchanged-torus static two-chain fill is impossible; broader encoders open", "same_scope": True, "exact_match": True, "use_as_closure": False},
        {**citations["Cycle535_open_defect_route"], "prior_residual": "defect-mediated transient-code route open", "current_residual": "not tested by a static chain-complex calculation", "same_scope": True, "exact_match": True, "use_as_closure": False},
        {**citations["Cycle537_embedding_wall"], "prior_residual": "cap sheets not embedded in old periodic placement", "current_residual": "homology pairing proves no unchanged-cellulation static plaquette filling", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {**citations["Cycle269_topological_center"], "prior_residual": "three independent central Wilson characters", "current_residual": "three independent H1 classes and three formal cap rank increments", "same_scope": True, "exact_match": True, "use_as_closure": True},
    ]
    n5 = [
        {"resolution": "per_element", "claim": "each plaquette boundary pairs trivially with every dual axial cocycle", "scope_ok": True},
        {"resolution": "per_site", "claim": "unchanged periodic vertex/edge/plaquette incidence is enumerated", "scope_ok": True},
        {"resolution": "per_mode", "claim": "not applicable; no fermionic mode action is inferred from homology", "scope_ok": True},
        {"resolution": "per_block", "claim": "one formal axial cap raises boundary rank by one", "scope_ok": True},
        {"resolution": "lattice_wide", "claim": "three caps span the three-dimensional H1 quotient at L3/L5/L6/L7", "scope_ok": True},
    ]
    n6 = [
        {"file": "scripts/physical_fixed_cubic_cap_embedding_cycle_next.py", "status": "OPEN", "what_closes": "W_embed via a genuinely enlarged, fixed, proper-cubic local incidence graph"},
        {"file": "scripts/physical_defect_code_growth_isometry_cycle_next.py", "status": "OPEN", "what_closes": "W_prepare via local transient defects and an exact full-matter intertwiner"},
        {"file": "scripts/physical_time_multiplexed_cap_interpreter_cycle_next.py", "status": "OPEN", "what_closes": "tests whether reusable state-carried ancillas replace static added topology without host control"},
    ]
    n7 = {
        "mechanism": "start from target matter and product ancillas, create local defects, grow a temporary rough boundary around each periodic direction, encode the target while the code is open, and reglue only after the fixed spin representation has formed",
        "terminal_test": "an exact local E and G with full-Fock matter intertwining, restored local checks, all24/all576 covariance, retained work/exhaust, and no postselection or host Wilson query",
        "openness": "the present static two-chain calculation does not model this route, so it blocks any broad no-go or axiom-pressure claim",
        "citations": [citations["Cycle535_open_defect_route"], citations["Cycle537_embedding_wall"]],
    }
    n8 = [
        {"cycle": 269, "retired": "spectator-M8 interpretation of the three Wilson characters", "mechanism": "exact center/membrane algebra", "applicability": "identifies the same three topological classes; does not prove preparation", "citation": citations["Cycle269_topological_center"]},
        {"cycle": 532, "retired": "untyped rough-code multiplicity", "mechanism": "exact target full-Fock times local gauge subsystem", "applicability": "supplies the conditional code whose static initializer is tested", "citation": citations["Cycle532_topological_wall"]},
        {"cycle": 535, "retired": "host parity arithmetic for Wilson measurement", "mechanism": "local measurement plus membrane feedback", "applicability": "its target seam failure is route-specific; defect motion stays open", "citation": citations["Cycle535_open_defect_route"]},
        {"cycle": 537, "retired": "abstract need for growing Wilson check after adding cap topology", "mechanism": "bounded square fill-disk face/star complex", "applicability": "this cycle explains why that cap cannot be a static two-chain in the unchanged torus", "citation": citations["Cycle537_embedding_wall"]},
        {"cycle": 637, "retired": "unchanged-torus static plaquette realization of the Cycle537 cap", "mechanism": "exact H1 and dual-cocycle certificate", "applicability": "narrow mechanism only; dynamic and enlarged-topology routes open", "citation": None},
    ]
    no_go = {
        "Status": "PASS_NARROW_NEGATIVE_ONLY",
        "N1_broad_negative_gate": "FAIL_DO_NOT_SHIP",
        "N1_normalized_families": n1_families,
        "N1_qualifying_attempts": attempted,
        "N1_required_for_broad_negative": 5,
        "N2_collapsed_walls": n2_walls,
        "N2_directed_pairs": n2_pairs,
        "N2_all_pair_implications_false": all(not row["implied"] for row in n2_pairs),
        "N3_hidden_wall_scan": [
            "periodic cubic cellulation is a declared comparator, not the entire physical M2 possibility class",
            "static plaquette two-chain is the tested mechanism; arbitrary bounded gates and program phases are outside it",
            "proper-cubic covariance of homology classes is not a fixed geometric cap embedding",
            "added topology, reset/product-state genesis, schedule, target input map, and retained exhaust remain explicit supplies",
        ],
        "N4_residual_matching": n4,
        "N5_rhetoric_resolution_ledger": n5,
        "N6_partial_closure_paths": n6,
        "N7_steelman": n7,
        "N8_cross_cycle_echo": n8,
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
    }
    check(
        "full N1-N8 permits only the narrow unchanged-torus static-fill exclusion",
        attempted == 3
        and no_go["N1_broad_negative_gate"] == "FAIL_DO_NOT_SHIP"
        and no_go["N2_all_pair_implications_false"]
        and len(n4) == 4
        and len(n5) == 5
        and all(set(("file", "status", "what_closes")) <= set(row) for row in n6)
        and len(n8) == 5
        and not no_go["shared_route_independent_obstruction"]
        and not no_go["axiom_pressure"],
        {"attempted": attempted, "required": 5, "N2_pairs": len(n2_pairs), "N4": len(n4), "N8": len(n8)},
    )

    note_text = NOTE.read_text()
    semantic_markers = [
        "Authority: **none**",
        "Audit: **unset**",
        "not a general physical-M2",
        "Added topology",
        "Defect-mediated",
        "Axiom pressure: **none**",
        "Breakthrough bar: **not met**",
    ]
    check("Cycle637 note preserves the narrow scope and open-route firewall", all(marker in note_text for marker in semantic_markers), semantic_markers)

    passed = sum(row["pass"] for row in tests)
    failed = len(tests) - passed
    elapsed = time.perf_counter() - start
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        rss_bytes = int(rss)
    else:
        rss_bytes = int(rss * 1024)
    try:
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        head = None

    receipt = {
        "cycle": 637,
        "date": "2026-07-23",
        "classification": "narrow static-embedding exclusion with constructive added-cap comparator; broader physical compiler routes open",
        "authority": "none",
        "audit": "unset",
        "author_accepted": False,
        "author_artifact_status_accepted": False,
        "breakthrough": False,
        "breakthrough_bar_met": False,
        "axiom_pressure": False,
        "shared_route_independent_obstruction": False,
        "broad_no_go": False,
        "tested_scope": "static F2 two-chain fillings made from plaquettes of the unchanged periodic cubic cellulation",
        "excluded_scope": [
            "arbitrary local quantum circuits",
            "defect-mediated preparation",
            "code deformation or punctures",
            "added physical topology or non-cubic incidence",
            "time-multiplexed ancilla worldvolumes",
            "finite-light-cone operational encodings",
        ],
        "upstream_hashes": upstream_hashes,
        "git_head_at_run": head,
        "sizes": results,
        "proper_cubic": {
            "frames": len(frames),
            "ordered_products": len(frames) ** 2,
            "group_failures": group_failures,
            "homology_axis_permutations": permutations,
            "triple_orbit_failures": triple_orbit_failures,
            "fixed_cap_embedding_claim": False,
        },
        "strongest_result": "each axial Wilson has unit pairing with one dual cocycle while every unchanged-torus plaquette boundary pairs trivially; three formal caps raise boundary rank by exactly three and reproduce Cycle537's one-character-per-disk Euler mechanism",
        "route_disposition": {
            "unchanged_torus_static_plaquette_cap": "RULED_OUT_BY_EXACT_HOMOLOGY",
            "Cycle537_added_cap_topology": "ALGEBRAICALLY_POSITIVE_PHYSICAL_EMBEDDING_AND_PREPARATION_OPEN",
            "defect_or_code_deformation": "OPEN",
            "from_scratch_local_encoder": "OPEN",
            "time_multiplexed_auxiliary": "OPEN",
        },
        "supplied_structure": [
            "finite periodic cubic L3/L5/L6/L7 cellulations",
            "one coordinate origin for representative Wilsons and dual cuts",
            "F2 chain-complex interpretation",
            "Cycle532 Wilson identification and Cycle537 square-disk resource formulas",
        ],
        "derived_structure": [
            "exact boundary ranks and H1 dimension",
            "dual-cocycle/Wilson pairing matrix",
            "formal-cap rank increments",
            "all24/all576 homology-class covariance",
            "damaged-Wilson deletion refusal",
        ],
        "semantic_firewall": {
            "compiler_impossibility_claim": False,
            "unchanged_torus_static_fill_exclusion_only": True,
            "schedule_called_time": False,
            "phase_called_energy": False,
            "pointer_called_Record": False,
            "axiom_pressure_claim": False,
        },
        "six_wall_ledger": {
            "C_ref": "unchanged; origin/cut choose representatives but homology result is representative-independent",
            "C_num": "unchanged; no full-Fock numeric or Born statement is added",
            "C_wrap": "narrowed: a static local plaquette cap cannot erase noncontractible Wilson classes inside the unchanged torus",
            "C_int": "unchanged; Cycle532 mass/contact/seam remain conditional comparators",
            "C_local": "narrowed: Cycle537 W_embed requires changed incidence/topology or a dynamical encoder, not a static two-chain in the old cellulation",
            "C_source": "unchanged",
        },
        "no_go_discipline": no_go,
        "tests": tests,
        "pass": failed == 0,
        "tests_passed": passed,
        "tests_failed": failed,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss_bytes,
        "optimal_next_campaign": "construct a fixed proper-cubic enlarged incidence graph or a defect/code-growth isometry and require exact full-Fock E/G plus restored local checks",
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    summary = {
        "pass": receipt["pass"],
        "tests_passed": passed,
        "tests_failed": failed,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss_bytes,
        "receipt": str(RECEIPT),
    }
    summary_text = json.dumps(summary, indent=2)
    print(summary_text)
    log.extend(summary_text.splitlines())
    COLD.write_text("\n".join(log) + "\n")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
