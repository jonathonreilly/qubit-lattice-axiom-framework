#!/usr/bin/env python3
"""Verifier for the theta G1 4D carrier supply current-surface no-go note."""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path

import numpy as np
import sympy as sp

import theta_g1_exact_branch_constraint_no_go_2026_07_04 as exact4


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
ANOMALY_TIME = DOCS / "ANOMALY_FORCES_TIME_THEOREM.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
BLOCK36 = DOCS / "THETA_G1_CLOSED_NONEXACT_INTERFACE_EXACT_SUPPORT_NOTE_2026-07-04.md"
G1_CURRENT = DOCS / "THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
CLOSED_NONEXACT = DOCS / "THETA_CLOSED_NONEXACT_SECTOR_RECORD_READOUT_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"

SOURCE_ROWS = {
    "minimal": "minimal_axioms",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "block36": "theta_g1_closed_nonexact_interface_exact_support_note_2026-07-04",
    "g1_current": "theta_g1_defect_closure_current_surface_no_go_note_2026-07-04",
    "closed_nonexact": "theta_closed_nonexact_sector_record_readout_current_surface_no_go_note_2026-07-04",
}

PASS = 0
FAIL = 0
RNG = np.random.default_rng(37)


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 96)
    print(title)
    print("=" * 96)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ledger_row(claim_id: str) -> dict:
    row = json.loads(read(LEDGER))["rows"].get(claim_id)
    if row is None:
        raise AssertionError(f"missing ledger row {claim_id}")
    return row


def cells(dim: int, degree: int, side: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    dirs = list(itertools.combinations(range(dim), degree))
    sites = list(itertools.product(range(side), repeat=dim))
    return [(site, direction) for site in sites for direction in dirs]


def coboundary(dim: int, degree: int, side: int) -> np.ndarray:
    domain = cells(dim, degree, side)
    codomain = cells(dim, degree + 1, side)
    domain_index = {cell: i for i, cell in enumerate(domain)}
    mat = np.zeros((len(codomain), len(domain)), dtype=np.int64)
    for row, (site, dirs) in enumerate(codomain):
        dirs_list = list(dirs)
        for pos, mu in enumerate(dirs_list):
            face_dirs = tuple(d for d in dirs_list if d != mu)
            sign = -1 if pos % 2 else 1
            shifted = list(site)
            shifted[mu] = (shifted[mu] + 1) % side
            shifted = tuple(shifted)
            mat[row, domain_index[(shifted, face_dirs)]] += sign
            mat[row, domain_index[(site, face_dirs)]] -= sign
    return mat


def rank(mat: np.ndarray) -> int:
    if mat.size == 0:
        return 0
    return int(sp.Matrix(mat).rank())


def betti(dim: int, degree: int, side: int) -> int:
    c_k = len(cells(dim, degree, side))
    rank_prev = rank(coboundary(dim, degree - 1, side)) if degree > 0 else 0
    rank_next = rank(coboundary(dim, degree, side)) if degree < dim else 0
    return c_k - rank_next - rank_prev


def constant_flux(dim: int, side: int, plane: tuple[int, int]) -> np.ndarray:
    c2 = cells(dim, 2, side)
    vec = np.zeros(len(c2), dtype=np.int64)
    for idx, (_site, dirs) in enumerate(c2):
        if dirs == plane:
            vec[idx] = 1
    return vec


def nonexact_rank_witness(dim: int, side: int, vec: np.ndarray) -> tuple[int, int]:
    d1 = coboundary(dim, 1, side)
    r1 = rank(d1)
    r_aug = rank(np.column_stack([d1, vec]))
    return r1, r_aug


def q4_flux(m: dict[tuple[int, int], int]) -> int:
    return (
        m.get((0, 1), 0) * m.get((2, 3), 0)
        - m.get((0, 2), 0) * m.get((1, 3), 0)
        + m.get((0, 3), 0) * m.get((1, 2), 0)
    )


def main() -> int:
    print("theta G1 4D carrier supply current-surface no-go verifier")

    paths = [
        NOTE,
        MINIMAL,
        KINETIC,
        ANOMALY_TIME,
        REGISTRY,
        TIER_A,
        LEDGER,
        CARRIER4D,
        BLOCK36,
        G1_CURRENT,
        CLOSED_NONEXACT,
    ]
    texts = {path: read(path) for path in paths}
    flats = {path: flat(text) for path, text in texts.items()}
    note = texts[NOTE]
    note_flat = flats[NOTE]

    section("A. source presence, metadata, and claim firewall")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note has Type no_go", "**Type:** no_go" in note)
    check("note has Claim type no_go", "**Claim type:** no_go" in note)
    check("runner path is wired", Path(__file__).name in note)
    check("note declares independent audit boundary", "independent audit lane only" in note_flat)
    for phrase in [
        "This note does not retire theta",
        "does not set `theta_bar = 0`",
        "does not edit any Tier-A registry",
        "does not claim that future 4D gauge-carrier",
    ]:
        check(f"scope boundary phrase present: {phrase[:60]}", phrase in note_flat)
    for banned in [
        "theta is retired",
        "theta_bar = 0 is derived",
        "the Tier-A registry is edited",
        "the physical 4D carrier is now derived",
        "kinetic isotropy supplies theta topology",
        "anomaly-forces-time supplies theta topology",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. source rows and Tier-A state")
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger_row(claim_id)
        check(f"{label} ledger row resolves", row.get("claim_id") == claim_id)
        check(f"{label} row has expected status shape", row.get("effective_status") in {"retained", "retained_bounded", "unaudited", "audited_conditional"} or label == "minimal", row.get("effective_status"))
    tier = json.loads(read(TIER_A))
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "theta minimum decomposition remains gauge plus mass atoms",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    check(
        "AC minimum decomposition remains two atoms",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    check("registry still names multi-plaquette winding", "multi-plaquette / large-gauge-winding account" in flats[REGISTRY])

    section("C. current-surface non-supply guards")
    for phrase in [
        "Physical sites are the points of the cubic lattice `Z^3`",
        "formation rule",
        "source/action and physical-observable identification",
        "time metric",
        "central-sector decomposition",
    ]:
        check(f"minimal axiom guard present: {phrase[:58]}", phrase in flats[MINIMAL])
    for phrase in [
        "not a re-axiomatization of time",
        "fixes only the one dimensionless graining ratio",
        "not a fourth spatial dimension",
        "does not supply any dimensionless dynamical quantity",
        "does not supply the absolute scale",
    ]:
        check(f"kinetic primitive boundary present: {phrase[:58]}", phrase in flats[KINETIC])
    for phrase in [
        "conditional 3+1 derivation",
        "B-AXIS",
        "declared boundary",
        "No step defines time via the anomaly",
        "does not derive B-AXIS",
    ]:
        check(f"anomaly-time boundary present: {phrase[:58]}", phrase in flats[ANOMALY_TIME])
    for phrase in [
        "This result is conditional support",
        "4D multi-plaquette carrier",
        "No actual current-surface G1 theorem is supplied",
    ]:
        check(f"Block36 remains conditional: {phrase[:58]}", phrase in flats[BLOCK36])
    for phrase in [
        "On the current surface, G1 is not derived.",
        "Record axiom's new formation sentence is also not a defect law",
    ]:
        check(f"G1 current no-go memory present: {phrase[:58]}", phrase in flats[G1_CURRENT])
    for phrase in [
        "physical sector-record/readout licensing",
        "closed non-exact sector labels are already licensed",
    ]:
        check(f"closed-nonexact no-go memory present: {phrase[:58]}", phrase in flats[CLOSED_NONEXACT])

    section("D. finite T3 versus T4 carrier arithmetic")
    side = 2
    d1_t3 = coboundary(3, 1, side)
    d2_t3 = coboundary(3, 2, side)
    d3_t3 = coboundary(3, 3, side)
    check("T3 C0 count", len(cells(3, 0, side)) == 8, len(cells(3, 0, side)))
    check("T3 C1 count", len(cells(3, 1, side)) == 24, len(cells(3, 1, side)))
    check("T3 C2 count", len(cells(3, 2, side)) == 24, len(cells(3, 2, side)))
    check("T3 C3 count", len(cells(3, 3, side)) == 8, len(cells(3, 3, side)))
    check("T3 C4 count is zero", len(cells(3, 4, side)) == 0, len(cells(3, 4, side)))
    check("T3 d2*d1 = 0", np.max(np.abs(d2_t3 @ d1_t3)) == 0)
    check("T3 d3 has zero rows", d3_t3.shape == (0, 8), d3_t3.shape)
    check("T3 rank d1 = 14", rank(d1_t3) == 14, rank(d1_t3))
    check("T3 rank d2 = 7", rank(d2_t3) == 7, rank(d2_t3))
    check("T3 H2 dim = 3", betti(3, 2, side) == 3, betti(3, 2, side))
    check("T3 H4 dim = 0", betti(3, 4, side) == 0, betti(3, 4, side))
    for plane in [(0, 1), (0, 2), (1, 2)]:
        rep = constant_flux(3, side, plane)
        r1, r_aug = nonexact_rank_witness(3, side, rep)
        check(f"T3 unit spatial flux {plane} is closed", np.max(np.abs(d2_t3 @ rep)) == 0)
        check(f"T3 unit spatial flux {plane} is non-exact", r_aug > r1, (r1, r_aug))
    plane_pairs = list(itertools.combinations([(0, 1), (0, 2), (1, 2)], 2))
    for a, b in plane_pairs:
        check(f"T3 planes {a},{b} cannot span four directions", len(set(a) | set(b)) < 4, (a, b))

    check("T4 C4 count is nonzero", len(cells(4, 4, side)) == 16, len(cells(4, 4, side)))
    check("T4 H2 dim is six in imported carrier module", len(exact4.REPS) == 6)
    t4_h2 = exact4.D2.shape[1] - rank(exact4.D2) - rank(exact4.D1)
    check("T4 H2 dim = 6", t4_h2 == 6, t4_h2)
    complementary = exact4.REPS[(0, 1)] + exact4.REPS[(2, 3)]
    check("T4 complementary e01+e23 is closed", np.max(np.abs(exact4.D2 @ complementary)) == 0)
    check("T4 complementary e01+e23 has Qraw=2", exact4.qraw(complementary) == 2, exact4.qraw(complementary))
    for _ in range(20):
        spatial = {
            (0, 1): int(RNG.integers(-3, 4)),
            (0, 2): int(RNG.integers(-3, 4)),
            (1, 2): int(RNG.integers(-3, 4)),
        }
        check("spatial-only flux embeds with zero 4D Q", q4_flux(spatial) == 0, spatial)
    for _ in range(20):
        m = {
            (0, 1): int(RNG.integers(-3, 4)),
            (0, 2): int(RNG.integers(-3, 4)),
            (0, 3): int(RNG.integers(-3, 4)),
            (1, 2): int(RNG.integers(-3, 4)),
            (1, 3): int(RNG.integers(-3, 4)),
            (2, 3): int(RNG.integers(-3, 4)),
        }
        direct = q4_flux(m)
        manual = m[(0, 1)] * m[(2, 3)] - m[(0, 2)] * m[(1, 3)] + m[(0, 3)] * m[(1, 2)]
        check("4D Q formula uses complementary planes", direct == manual, m)
    check("T4 odd support requires fourth direction example", q4_flux({(0, 1): 1, (2, 3): 1}) == 1)
    check("note records T3 H2 but C4/H4 obstruction", "H^2(T^3,Z) = Z^3" in note and "C^4(T^3) = 0" in note and "H^4(T^3,Z) = 0" in note)
    check("note records spatial-only zero embedding", "spatial-only carrier cannot be the Block36 carrier" in note)

    section("E. no-go statement and route preservation")
    for phrase in [
        "therefore the physical 4D closed-nonexact theta carrier is supplied",
        "is invalid",
        "does not supply the 4D cubical/gauge carrier",
        "Theta's gauge-side winding account therefore remains live",
    ]:
        check(f"no-go statement phrase present: {phrase[:58]}", phrase in note_flat)
    for phrase in [
        "Physical 4D carrier theorem",
        "Closed-nonexact interface theorem",
        "Dynamical defect suppression",
        "G2 sector/readout registration",
        "G3 phase source",
        "Owner governance",
    ]:
        check(f"remaining route present: {phrase}", phrase in note)
    for phrase in [
        "The kinetic-isotropy primitive is not rejected",
        "The anomaly-forces-time theorem is not rejected or narrowed",
        "Block36's supplied-interface support is not rejected",
    ]:
        check(f"preservation phrase present: {phrase[:58]}", phrase in note)
    for gate in ["N1 alternative route enumeration", "N2 wall independence", "N3 hidden-wall scan", "N4 residual matching", "N5 proven surface", "N6 partial closure", "N7 steelman", "N8 cross-cycle echo"]:
        check(f"no-go discipline gate present: {gate}", gate in note)

    total = PASS + FAIL
    print("\n" + "=" * 96)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL} CHECKS={total}")
    print("=" * 96)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
