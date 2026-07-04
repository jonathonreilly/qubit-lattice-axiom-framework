#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from itertools import combinations
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G1_EXACT_BRANCH_CONSTRAINT_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
POSITIVE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
G1_CURRENT = DOCS / "THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
AXIOM_NO_GO = DOCS / "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
G3_NO_GO = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"

SOURCE_ROWS = {
    "positive": "theta_gauge_positive_route_stretch_status_2026-07-04",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "g1_current": "theta_g1_defect_closure_current_surface_no_go_note_2026-07-04",
    "axiom_no_go": "theta_gauge_winding_axiom_update_no_go_note_2026-07-04",
    "g3_no_go": "theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04",
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
}

PASS = 0
FAIL = 0
D = 4
L = 2
RNG = np.random.default_rng(29)


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
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def cells(size: int, degree: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    sites = [tuple(site) for site in np.ndindex(*(size,) * D)]
    return [(site, directions) for directions in combinations(range(D), degree) for site in sites]


def cell_index(size: int, degree: int):
    listed = cells(size, degree)
    return listed, {cell: idx for idx, cell in enumerate(listed)}


def shift(site: tuple[int, ...], axis: int, size: int) -> tuple[int, ...]:
    out = list(site)
    out[axis] = (out[axis] + 1) % size
    return tuple(out)


def d_matrix(size: int, degree: int) -> np.ndarray:
    _, source_index = cell_index(size, degree)
    target_cells, target_index = cell_index(size, degree + 1)
    mat = np.zeros((len(target_cells), len(source_index)), dtype=np.int64)
    for (site, directions), row_idx in target_index.items():
        for j, axis in enumerate(directions):
            rest = tuple(direction for direction in directions if direction != axis)
            sign = (-1) ** j
            mat[row_idx, source_index[(shift(site, axis, size), rest)]] += sign
            mat[row_idx, source_index[(site, rest)]] -= sign
    return mat


CELL_INFO = {degree: cell_index(L, degree) for degree in range(D + 1)}
D1 = d_matrix(L, 1)
D2 = d_matrix(L, 2)
PLANES = list(combinations(range(D), 2))


def cup(a: np.ndarray, da: int, b: np.ndarray, db: int) -> np.ndarray:
    _, out_index = CELL_INFO[da + db]
    _, a_index = CELL_INFO[da]
    _, b_index = CELL_INFO[db]
    out = np.zeros(len(out_index), dtype=np.result_type(a.dtype, b.dtype))
    for (site, directions), out_idx in out_index.items():
        total = 0
        for first in combinations(directions, da):
            second = tuple(direction for direction in directions if direction not in first)
            permutation = list(first) + list(second)
            inversions = sum(
                1
                for i in range(len(permutation))
                for j in range(i + 1, len(permutation))
                if permutation[i] > permutation[j]
            )
            shifted_site = site
            for axis in first:
                shifted_site = shift(shifted_site, axis, L)
            total += ((-1) ** inversions) * a[a_index[(site, first)]] * b[b_index[(shifted_site, second)]]
        out[out_idx] = total
    return out


def flux_rep(mu: int, nu: int) -> np.ndarray:
    representative = np.zeros(len(CELL_INFO[2][0]), dtype=np.int64)
    for (site, directions), idx in CELL_INFO[2][1].items():
        if directions == (mu, nu) and site[mu] == 0 and site[nu] == 0:
            representative[idx] = 1
    return representative


REPS = {plane: flux_rep(*plane) for plane in PLANES}


def qraw(n: np.ndarray) -> int:
    return int(np.sum(cup(n, 2, n, 2)))


def ledger_row(claim_id: str) -> dict:
    rows = json.loads(read(LEDGER))["rows"]
    row = rows.get(claim_id)
    if row is None:
        raise AssertionError(f"missing ledger row {claim_id}")
    return row


def main() -> int:
    print("theta G1 exact-branch constraint no-go verifier")

    paths = [NOTE, MINIMAL, REGISTRY, TIER_A, LEDGER, POSITIVE, CARRIER4D, G1_CURRENT, AXIOM_NO_GO, G3_NO_GO]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    flats = {path: flat(text) for path, text in texts.items()}

    section("A. source presence and claim firewall")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note has Type no_go", "**Type:** no_go" in note)
    check("note has Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares exact-branch shortcut scope", "globally exact, `n = dA`" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    for phrase in [
        "This note does not retire theta",
        "does not set `theta_bar = 0`",
        "does not edit any Tier-A registry",
        "does not claim that future closed-nonexact bundle",
    ]:
        check(f"scope boundary phrase present: {phrase[:52]}", phrase in note_flat)
    for banned in [
        "theta is retired",
        "theta_bar = 0 is derived",
        "registry is edited",
        "closed-nonexact routes are impossible",
        "G1 is closed",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. source rows and registry state")
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger_row(claim_id)
        check(f"{label} ledger row resolves", row.get("claim_id") == claim_id)
        check(f"{label} row has note path", bool(row.get("note_path")), row.get("note_path"))
    for label in ["positive", "carrier4d", "g1_current", "axiom_no_go", "g3_no_go"]:
        row = ledger_row(SOURCE_ROWS[label])
        check(f"{label} not effective retained closure", row.get("effective_status") != "retained", row.get("effective_status"))
    tier = json.loads(read(TIER_A))
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "theta minimum decomposition remains two atoms",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    for phrase in [
        "gauge_side_winding_account",
        "mass_side_orientation_determinant_readout_bridge",
        "multi-plaquette / large-gauge-winding account",
        "determinant-readout bridge",
    ]:
        if phrase in {"gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"}:
            check(f"theta machine registry text includes {phrase[:50]}", phrase in flat(json.dumps(theta)))
        else:
            check(f"theta registry text includes {phrase[:50]}", phrase in flat(json.dumps(theta)) and phrase in flats[REGISTRY])

    section("C. current theta-surface boundary checks")
    for phrase in [
        "search for a native branch law that forces `dn = 0`",
        "gate on the abelianized theta gauge carrier",
        "On the current surface, G1 is not derived.",
    ]:
        check(f"G1 current note names next shortcut: {phrase[:54]}", phrase in flats[G1_CURRENT])
    for phrase in [
        "G1 defect closure",
        "No derivation yet that the physical surface imposes or suppresses `dn != 0`",
        "Without this, the closed-branch carrier remains a witness surface.",
    ]:
        check(f"positive synthesis preserves G1 boundary: {phrase[:54]}", phrase in flats[POSITIVE])
    for phrase in [
        "H^2(T^4, Z) = Z^6",
        "Defect closure",
        "derive the closed-branch (dn = 0) restriction",
        "defect-free",
        "no sector decomposition survives on the unrestricted branch sum",
    ]:
        check(f"carrier source has boundary phrase: {phrase[:54]}", phrase in flats[CARRIER4D])
    for phrase in [
        "Admissibility is not a dynamics axiom",
        "source/action and physical-observable identification",
        "context selection",
        "transition probabilities or weights",
    ]:
        check(f"minimal axioms withhold {phrase[:48]}", phrase in flats[MINIMAL])
    for phrase in [
        "does not supply the theta gauge-side winding",
        "gauge-action",
        "topological-sector",
    ]:
        check(f"axiom no-go preserves gauge boundary: {phrase[:52]}", phrase in flats[AXIOM_NO_GO])

    section("D. exact cochain complex checks")
    check("D1 shape is C2 x C1", D1.shape == (96, 64), D1.shape)
    check("D2 shape is C3 x C2", D2.shape == (64, 96), D2.shape)
    check("d2*d1 = 0", np.max(np.abs(D2 @ D1)) == 0)
    rank_d1 = sp.Matrix(D1).rank()
    rank_d2 = sp.Matrix(D2).rank()
    ker_d2 = D2.shape[1] - rank_d2
    h2_dim = ker_d2 - rank_d1
    check("rank d1 = 45", rank_d1 == 45, rank_d1)
    check("rank d2 = 45", rank_d2 == 45, rank_d2)
    check("dim ker d2 = 51", ker_d2 == 51, ker_d2)
    check("dim H2 = 6", h2_dim == 6, h2_dim)
    check("note records rank facts", "rank d1 = 45" in note and "dim H^2 = 51 - 45 = 6" in note)

    section("E. closed non-exact flux sectors")
    for plane, rep in REPS.items():
        rank_aug = sp.Matrix(np.column_stack([D1, rep])).rank()
        check(f"unit flux {plane} is closed", np.max(np.abs(D2 @ rep)) == 0)
        check(f"unit flux {plane} is not exact", rank_aug > rank_d1, rank_aug)
    e01_e23 = REPS[(0, 1)] + REPS[(2, 3)]
    check("complementary flux sum is closed", np.max(np.abs(D2 @ e01_e23)) == 0)
    check("complementary flux sum is not exact", sp.Matrix(np.column_stack([D1, e01_e23])).rank() > rank_d1)
    check("complementary flux has Qraw=2", qraw(e01_e23) == 2, qraw(e01_e23))
    check("complementary flux has Q=1", qraw(e01_e23) // 2 == 1)

    section("F. exact branches close defects but erase Q")
    for idx in range(10):
        link = RNG.integers(-2, 3, size=D1.shape[1])
        n = D1 @ link
        check(f"exact sample {idx} is closed", np.max(np.abs(D2 @ n)) == 0)
        check(f"exact sample {idx} has Qraw=0", qraw(n) == 0, qraw(n))
    zero = np.zeros(D1.shape[1], dtype=np.int64)
    check("zero exact branch is closed", np.max(np.abs(D2 @ (D1 @ zero))) == 0)
    check("zero exact branch has Qraw=0", qraw(D1 @ zero) == 0)
    check("note states exactness closes by d2=0", "dn = d(dA) = 0" in note)
    check("note states exactness kills carrier", "The route closes the defect by deleting the carrier." in note)

    section("G. theorem and no-go discipline text")
    for heading in [
        "Frame 1: exact branches do close defects",
        "Frame 2: exact branches erase the cohomology carrier",
        "Frame 3: exact branches have zero theta charge",
        "Frame 4: exactness is not the physical bundle/sector bridge",
        "Frame 5: Record and Admissibility do not select exactness",
    ]:
        check(f"fan-out heading present: {heading}", heading in note)
    for phrase in [
        "is invalid",
        "Exactness is too strong.",
        "closed non-exact sector data",
        "global-link exactness shortcut",
        "Closed-nonexact sector theorem",
        "Dynamical defect suppression",
        "Owner governance",
    ]:
        check(f"note contains theorem/queue phrase: {phrase}", phrase in note_flat)
    for label in [f"N{i}" for i in range(1, 9)]:
        check(f"no-go gate has {label}", f"**{label}" in note)
    check("N3 forbids bundle primitive", "no bundle/sector primitive" in note)
    check("N5 says not universal no-go", "not a universal no-go against closed-nonexact bundle" in note_flat)
    check("N7 distinguishes Bianchi from sector structure", "distinguishes global exactness from" in note)
    check("expected total present", "TOTAL: PASS=138 FAIL=0" in note)

    section("H. final summary")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
