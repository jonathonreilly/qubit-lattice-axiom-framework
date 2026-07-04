#!/usr/bin/env python3
"""Verifier for the theta G1 supplied defect-penalty support note."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import numpy as np
import sympy as sp

import theta_g1_exact_branch_constraint_no_go_2026_07_04 as exact


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G1_DEFECT_SUPPRESSION_SUPPLIED_PENALTY_EXACT_SUPPORT_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
BLOCK36 = DOCS / "THETA_G1_CLOSED_NONEXACT_INTERFACE_EXACT_SUPPORT_NOTE_2026-07-04.md"
BLOCK37 = DOCS / "THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
G1_CURRENT = DOCS / "THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
EXACT_BRANCH = DOCS / "THETA_G1_EXACT_BRANCH_CONSTRAINT_NO_GO_NOTE_2026-07-04.md"

SOURCE_ROWS = {
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "block36": "theta_g1_closed_nonexact_interface_exact_support_note_2026-07-04",
    "block37": "theta_g1_4d_carrier_supply_current_surface_no_go_note_2026-07-04",
    "g1_current": "theta_g1_defect_closure_current_surface_no_go_note_2026-07-04",
    "exact_branch": "theta_g1_exact_branch_constraint_no_go_note_2026-07-04",
}

PASS = 0
FAIL = 0
RNG = np.random.default_rng(38)


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


def defect_current(branch: np.ndarray) -> np.ndarray:
    return exact.D2 @ branch


def defect_norm(branch: np.ndarray) -> int:
    current = defect_current(branch)
    return int(current @ current)


def is_exact(branch: np.ndarray) -> bool:
    rank_d1 = sp.Matrix(exact.D1).rank()
    rank_aug = sp.Matrix(np.column_stack([exact.D1, branch])).rank()
    return rank_aug == rank_d1


def single_plaquette_defect() -> np.ndarray:
    branch = np.zeros(exact.D2.shape[1], dtype=np.int64)
    branch[exact.CELL_INFO[2][1][((0, 0, 0, 0), (0, 1))]] = 1
    return branch


def exact_move(scale: int = 1) -> np.ndarray:
    coeffs = RNG.integers(-scale, scale + 1, size=exact.D1.shape[1], dtype=np.int64)
    return exact.D1 @ coeffs


def random_defect_branch() -> np.ndarray:
    while True:
        branch = RNG.integers(-1, 2, size=exact.D2.shape[1], dtype=np.int64)
        if defect_norm(branch) > 0:
            return branch


def main() -> int:
    print("theta G1 supplied defect-penalty exact-support verifier")

    paths = [
        NOTE,
        MINIMAL,
        REGISTRY,
        TIER_A,
        LEDGER,
        CARRIER4D,
        BLOCK36,
        BLOCK37,
        G1_CURRENT,
        EXACT_BRANCH,
    ]
    texts = {path: read(path) for path in paths}
    flats = {path: flat(text) for path, text in texts.items()}
    note = texts[NOTE]
    note_flat = flats[NOTE]

    section("A. source presence, metadata, and claim firewall")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note has Type bounded_theorem", "**Type:** bounded_theorem" in note)
    check("note has Claim type bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note declares conditional support", "conditional exact-support source-side split" in note_flat)
    check("runner path is wired", Path(__file__).name in note)
    for phrase in [
        "This note does not retire theta",
        "does not set `theta_bar = 0`",
        "does not edit any Tier-A registry",
        "does not claim that the current framework derives a defect-penalty action",
    ]:
        check(f"scope boundary present: {phrase[:60]}", phrase in note_flat)
    for banned in [
        "theta is retired",
        "theta_bar = 0 is derived",
        "therefore the current framework derives a defect-penalty action",
        "finite-kappa physical suppression strength is derived",
        "the Tier-A registry is edited",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. source rows and Tier-A state")
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger_row(claim_id)
        check(f"{label} ledger row resolves", row.get("claim_id") == claim_id)
        check(f"{label} row has note path or premise", bool(row.get("note_path")) or label == "minimal", row.get("note_path"))
    tier = json.loads(read(TIER_A))
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "theta minimum decomposition unchanged",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    check("registry still names multi-plaquette winding", "multi-plaquette / large-gauge-winding account" in flats[REGISTRY])

    section("C. source-boundary memory")
    for phrase in [
        "source/action and physical-observable identification",
        "transition probabilities or weights",
        "Admissibility is not a dynamics axiom",
    ]:
        check(f"minimal axiom withholds {phrase[:42]}", phrase in flats[MINIMAL])
    for phrase in [
        "Dynamical suppression",
        "action/measure/energy theorem",
        "I1. The physical branch variable n",
    ]:
        check(f"Block36 suppression/interface memory: {phrase[:58]}", phrase in flats[BLOCK36])
    for phrase in [
        "physical 4D gauge-carrier theorem",
        "Theta's gauge-side winding account therefore remains live",
    ]:
        check(f"Block37 carrier non-supply memory: {phrase[:58]}", phrase in flats[BLOCK37])
    for phrase in [
        "On the current surface, G1 is not derived.",
        "do not supply the physical premise",
    ]:
        check(f"G1 current no-go memory: {phrase[:58]}", phrase in flats[G1_CURRENT])
    for phrase in [
        "The route closes the defect by deleting the carrier.",
        "Exactness is too strong",
    ]:
        check(f"exactness no-go memory: {phrase[:58]}", phrase in flats[EXACT_BRANCH])

    section("D. exact penalty algebra on T4_2")
    check("D2*D1 = 0", np.max(np.abs(exact.D2 @ exact.D1)) == 0)
    rank_d1 = sp.Matrix(exact.D1).rank()
    rank_d2 = sp.Matrix(exact.D2).rank()
    h2_dim = exact.D2.shape[1] - rank_d2 - rank_d1
    check("T4 H2 dim remains six", h2_dim == 6, h2_dim)

    complementary = exact.REPS[(0, 1)] + exact.REPS[(2, 3)]
    check("closed non-exact complementary branch has zero defect norm", defect_norm(complementary) == 0, defect_norm(complementary))
    check("closed non-exact complementary branch is not exact", not is_exact(complementary))
    check("closed non-exact complementary branch has Qraw=2", exact.qraw(complementary) == 2, exact.qraw(complementary))
    for plane, rep in exact.REPS.items():
        check(f"unit flux {plane} has zero defect norm", defect_norm(rep) == 0, defect_norm(rep))
        check(f"unit flux {plane} is not exact", not is_exact(rep))

    for idx in range(12):
        branch = exact_move(scale=2)
        check(f"exact branch sample {idx} has zero defect norm", defect_norm(branch) == 0, defect_norm(branch))
        check(f"exact branch sample {idx} has Qraw=0", exact.qraw(branch) == 0, exact.qraw(branch))

    defect = single_plaquette_defect()
    base_current = defect_current(defect)
    base_norm = defect_norm(defect)
    check("single plaquette branch is defectful", base_norm > 0, base_norm)
    check("single plaquette branch has unstable Qraw seed", exact.qraw(defect) != exact.qraw(complementary), exact.qraw(defect))
    for coeff in (-2, -1, 1, 2):
        moved = defect + coeff * exact_move(scale=1)
        check("exact local move preserves defect current", np.array_equal(defect_current(moved), base_current))
        check("exact local move preserves defect penalty", defect_norm(moved) == base_norm, defect_norm(moved))

    closed_family: list[np.ndarray] = [exact.REPS[(0, 1)], exact.REPS[(2, 3)], complementary]
    for _ in range(12):
        closed_family.append(complementary + exact_move(scale=1))
        closed_family.append(exact_move(scale=1))
    defect_family: list[np.ndarray] = [defect + exact_move(scale=1) for _ in range(12)]
    defect_family.extend(random_defect_branch() for _ in range(20))
    closed_norms = [defect_norm(branch) for branch in closed_family]
    defect_norms = [defect_norm(branch) for branch in defect_family]
    check("all closed-family branches have zero penalty", all(n == 0 for n in closed_norms), closed_norms[:8])
    check("all defect-family branches have positive penalty", all(n > 0 for n in defect_norms), defect_norms[:8])
    c_min = min(defect_norms)
    check("finite defect family has positive c_min", c_min > 0, c_min)

    ratios = []
    for kappa in [0.0, 0.5, 1.0, 2.0, 4.0]:
        w_closed = float(len(closed_family))
        w_def = sum(math.exp(-kappa * n) for n in defect_norms)
        ratios.append(w_def / (w_closed + w_def))
    check("defect fraction starts positive at kappa=0", ratios[0] > 0.0, ratios)
    check("defect fraction decreases with kappa", all(a >= b for a, b in zip(ratios, ratios[1:])), ratios)
    check("defect fraction is strongly suppressed by kappa=4", ratios[-1] < 1e-4, ratios[-1])
    for kappa in [0.5, 1.0, 2.0, 4.0]:
        w_def = sum(math.exp(-kappa * n) for n in defect_norms)
        bound = len(defect_family) * math.exp(-kappa * c_min)
        check(f"finite-family exponential defect bound at kappa={kappa}", w_def <= bound + 1e-12, (w_def, bound, c_min))

    section("E. note theorem and route boundaries")
    for phrase in [
        "The penalty is exact-move invariant",
        "Closed non-exact sectors survive",
        "Global exactness is not imposed",
        "Defectful branches are projected away",
        "W_def(kappa) <= N_def exp(-kappa c_min)",
    ]:
        check(f"theorem phrase present: {phrase[:58]}", phrase in note)
    for phrase in [
        "No physical 4D carrier is supplied",
        "No current-surface defect penalty",
        "No finite-`kappa` physical suppression strength is claimed",
        "No G2 physical sector/readout theorem is supplied",
    ]:
        check(f"non-claim present: {phrase[:58]}", phrase in note)
    for phrase in [
        "Physical 4D carrier theorem",
        "Defect-penalty action theorem",
        "Closed-nonexact interface theorem",
        "G2 sector/readout registration",
        "G3 phase source",
        "Mass-side determinant channel",
    ]:
        check(f"remaining route present: {phrase}", phrase in note)

    total = PASS + FAIL
    print("\n" + "=" * 96)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL} CHECKS={total}")
    print("=" * 96)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
