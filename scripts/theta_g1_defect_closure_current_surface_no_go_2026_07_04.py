#!/usr/bin/env python3
"""Verifier for the theta G1 defect-closure current-surface no-go."""

from __future__ import annotations

import json
import re
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
POLICY = DOCS / "audit" / "AXIOM_MINIMALITY_POLICY.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
AXIOM_NODES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
POSITIVE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
AXIOM_NO_GO = DOCS / "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
G3_NO_GO = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
G3_SUPPORT = DOCS / "THETA_G3_CENTRAL_SECTOR_PHASE_CHARACTER_EXACT_SUPPORT_NOTE_2026-07-04.md"

PASS = 0
FAIL = 0
RNG = np.random.default_rng(17)


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


D = 4
L = 2


def cells(k: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    out: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    sites = [tuple(s) for s in np.ndindex(*(L,) * D)]
    for directions in combinations(range(D), k):
        for site in sites:
            out.append((site, directions))
    return out


def cell_index(k: int) -> tuple[list[tuple[tuple[int, ...], tuple[int, ...]]], dict[tuple[tuple[int, ...], tuple[int, ...]], int]]:
    cs = cells(k)
    return cs, {cell: index for index, cell in enumerate(cs)}


def shift(site: tuple[int, ...], mu: int) -> tuple[int, ...]:
    shifted = list(site)
    shifted[mu] = (shifted[mu] + 1) % L
    return tuple(shifted)


def d_matrix(k: int) -> np.ndarray:
    _, source_index = cell_index(k)
    target_cells, target_index = cell_index(k + 1)
    matrix = np.zeros((len(target_cells), len(source_index)), dtype=np.int64)
    for (site, directions), row in target_index.items():
        for pos, mu in enumerate(directions):
            remainder = tuple(direction for direction in directions if direction != mu)
            sign = (-1) ** pos
            matrix[row, source_index[(shift(site, mu), remainder)]] += sign
            matrix[row, source_index[(site, remainder)]] -= sign
    return matrix


CI = {k: cell_index(k) for k in range(D + 1)}
DM = {k: d_matrix(k) for k in range(D)}


def cup(left: np.ndarray, left_degree: int, right: np.ndarray, right_degree: int) -> np.ndarray:
    _, target_index = CI[left_degree + right_degree]
    _, left_index = CI[left_degree]
    _, right_index = CI[right_degree]
    out = np.zeros(len(target_index), dtype=np.result_type(left.dtype, right.dtype))
    for (site, directions), row in target_index.items():
        total = 0
        for left_dirs in combinations(directions, left_degree):
            right_dirs = tuple(direction for direction in directions if direction not in left_dirs)
            perm = list(left_dirs) + list(right_dirs)
            inversions = sum(
                1
                for i in range(len(perm))
                for j in range(i + 1, len(perm))
                if perm[i] > perm[j]
            )
            shifted_site = site
            for mu in left_dirs:
                shifted_site = shift(shifted_site, mu)
            total += (
                ((-1) ** inversions)
                * left[left_index[(site, left_dirs)]]
                * right[right_index[(shifted_site, right_dirs)]]
            )
        out[row] = total
    return out


PLANES = list(combinations(range(D), 2))


def flux_rep(mu: int, nu: int) -> np.ndarray:
    vector = np.zeros(len(CI[2][0]), dtype=np.int64)
    for (site, directions), index in CI[2][1].items():
        if directions == (mu, nu) and site[mu] == 0 and site[nu] == 0:
            vector[index] = 1
    return vector


REPS = {plane: flux_rep(*plane) for plane in PLANES}


def q_raw(branch: np.ndarray) -> int:
    return int(np.sum(cup(branch, 2, branch, 2)))


def q_int(fluxes: dict[tuple[int, int], int]) -> int:
    return (
        fluxes[(0, 1)] * fluxes[(2, 3)]
        - fluxes[(0, 2)] * fluxes[(1, 3)]
        + fluxes[(0, 3)] * fluxes[(1, 2)]
    )


def local_link_move(link: tuple[tuple[int, ...], tuple[int, ...]], coefficient: int = 1) -> np.ndarray:
    one_cochain = np.zeros(len(CI[1][0]), dtype=np.int64)
    one_cochain[CI[1][1][link]] = coefficient
    return DM[1] @ one_cochain


SOURCE_ROWS = {
    "positive_route": "theta_gauge_positive_route_stretch_status_2026-07-04",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "axiom_no_go": "theta_gauge_winding_axiom_update_no_go_note_2026-07-04",
    "g3_no_go": "theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04",
    "g3_support": "theta_g3_central_sector_phase_character_exact_support_note_2026-07-04",
    "minimal_axioms": "minimal_axioms",
}


def main() -> int:
    print("Theta G1 defect-closure current-surface no-go")
    print("=" * 88)

    paths = [
        NOTE,
        MINIMAL,
        POLICY,
        TIER_A,
        LEDGER,
        AXIOM_NODES,
        REGISTRY,
        POSITIVE,
        CARRIER4D,
        AXIOM_NO_GO,
        G3_NO_GO,
        G3_SUPPORT,
    ]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    minimal_flat = flat(texts[MINIMAL])
    policy_flat = flat(texts[POLICY])
    registry_flat = flat(texts[REGISTRY])
    positive_flat = flat(texts[POSITIVE])
    carrier_flat = flat(texts[CARRIER4D])
    axiom_no_go_flat = flat(texts[AXIOM_NO_GO])
    g3_no_go_flat = flat(texts[G3_NO_GO])
    g3_support_flat = flat(texts[G3_SUPPORT])
    tier = json.loads(texts[TIER_A])
    ledger = json.loads(texts[LEDGER])
    axiom_nodes = json.loads(texts[AXIOM_NODES])

    section("A - source presence, metadata, and registry state")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("new note declares no_go type", "**Type:** no_go" in note)
    check("new note declares no_go claim type", "**Claim type:** no_go" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "Tier-A canonical ids remain AC and theta",
        tier["canonical_ids"]
        == [
            "staggered_dirac_realization_gate_note_2026-05-03",
            "strong_cp_theta_zero_note",
        ],
        tier["canonical_ids"],
    )
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check(
        "theta decomposition remains gauge-side winding plus mass-side determinant bridge",
        theta["minimum_decomposition"]
        == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    check("minimal axioms remain the only axiom node plus approved primitives", axiom_nodes["canonical_ids"][0] == "minimal_axioms")
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger["rows"].get(claim_id)
        check(f"ledger row resolves for {label}", row is not None)
        if row:
            check(f"{label} is not effective retained authority for theta retirement", row.get("effective_status") != "retained", row.get("effective_status"))

    section("B - current source surface does not supply G1")
    for phrase in [
        "Admissibility is not a dynamics axiom",
        "does not choose a Hamiltonian or transfer operator",
        "transition probabilities or weights",
        "record-production process or physical persistence dynamics",
        "source/action and physical-observable identification",
        "central-sector decomposition",
        "Records form.",
        "which admissible possibility a new record locks, at which site, with what weight, or at what rate",
    ]:
        check(f"minimal axiom boundary contains: {phrase[:60]}", phrase in minimal_flat)
    for phrase in [
        "Record does not supply readout-context selection",
        "source/action",
        "formation rule",
        "choose a Hamiltonian or transfer operator",
        "physical observables",
    ]:
        check(f"minimality policy anti-laundering contains: {phrase[:60]}", phrase in policy_flat)
    for phrase in [
        "multi-plaquette / large-gauge-winding account",
        "gauge_side_winding_account",
        "determinant-readout bridge",
    ]:
        check(f"theta registry keeps residual: {phrase[:60]}", phrase in registry_flat or phrase in texts[TIER_A])
    for phrase in [
        "G1 defect closure",
        "derive the closed-branch restriction dn = 0",
        "No derivation yet that the physical surface imposes or suppresses `dn != 0`",
        "G1 in parallel later",
    ]:
        check(f"positive route keeps G1 live: {phrase[:60]}", phrase in positive_flat)
    for phrase in [
        "The exact 4D carrier therefore lives on the **closed-branch",
        "what a physical derivation must supply is the closedness restriction or its dynamical suppression",
        "`dn != 0` destroys class invariance",
        "derive (i-a) defect closure",
    ]:
        check(f"carrier note names defect wall: {phrase[:60]}", phrase in carrier_flat)
    for phrase in [
        "does not supply the theta gauge-side winding",
        "physical topological-sector/gauge-action bridge",
        "The Tier-A registry is not edited.",
        "Theta is not retired.",
    ]:
        check(f"axiom-update no-go keeps shortcut blocked: {phrase[:60]}", phrase in axiom_no_go_flat)
    check("G3 no-go leaves phase insertion open", "oriented functional, phase coefficient, and physical registration" in g3_no_go_flat)
    check("G3 support names G1 precondition", "Discipline `dn != 0`" in g3_support_flat)

    section("C - finite T4 cochain contrast")
    dims = {degree: len(CI[degree][0]) for degree in range(D + 1)}
    ranks = {degree: int(np.linalg.matrix_rank(DM[degree].astype(float))) for degree in range(D)}
    kernel_dim_c2 = dims[2] - ranks[2]
    check("C2 dimension is 96 on T4_2", dims[2] == 96, dims)
    check("d2 rank is nonzero, so closure is not automatic", ranks[2] > 0, ranks)
    check("closed 2-cochains are a proper subspace", 0 < kernel_dim_c2 < dims[2], kernel_dim_c2)
    check("cochain complex has d2*d1 = 0", np.all(DM[2] @ DM[1] == 0))
    check("cochain complex has d3*d2 = 0", np.all(DM[3] @ DM[2] == 0))
    closed_branch = REPS[(0, 1)] + REPS[(2, 3)]
    check("complementary-flux witness is closed", np.count_nonzero(DM[2] @ closed_branch) == 0)
    check("closed witness has Q_raw = 2", q_raw(closed_branch) == 2, q_raw(closed_branch))
    check("all six unit-flux representatives are closed", all(np.count_nonzero(DM[2] @ rep) == 0 for rep in REPS.values()))
    for plane, rep in REPS.items():
        check(f"single unit flux {plane} has zero Q_raw", q_raw(rep) == 0, q_raw(rep))
    samples = [
        ({(0, 1): 1, (0, 2): 0, (0, 3): 0, (1, 2): 0, (1, 3): 0, (2, 3): 1}, 2),
        ({(0, 1): 0, (0, 2): 1, (0, 3): 0, (1, 2): 0, (1, 3): 1, (2, 3): 0}, -2),
        ({(0, 1): 0, (0, 2): 0, (0, 3): 1, (1, 2): 1, (1, 3): 0, (2, 3): 0}, 2),
    ]
    for fluxes, expected in samples:
        branch = sum(fluxes[plane] * REPS[plane] for plane in PLANES)
        check(f"closed sample has expected Q_raw={expected}", q_raw(branch) == expected, q_raw(branch))
    for _ in range(8):
        fluxes = {plane: int(RNG.integers(-2, 3)) for plane in PLANES}
        branch = sum(fluxes[plane] * REPS[plane] for plane in PLANES)
        check("closed flux Q_raw equals twice intersection form", q_raw(branch) == 2 * q_int(fluxes), (q_raw(branch), q_int(fluxes)))
    for _ in range(8):
        fluxes = {plane: int(RNG.integers(-2, 3)) for plane in PLANES}
        branch = sum(fluxes[plane] * REPS[plane] for plane in PLANES)
        move = DM[1] @ RNG.integers(-2, 3, size=len(CI[1][0]))
        shifted = branch + move
        check("random closed branch move keeps closedness", np.count_nonzero(DM[2] @ shifted) == 0)
        check("random closed branch move preserves Q_raw", q_raw(shifted) == q_raw(branch), (q_raw(branch), q_raw(shifted)))
        check("random closed branch Q_raw remains even", q_raw(shifted) % 2 == 0, q_raw(shifted))
    closed_values = []
    for link in CI[1][1]:
        move = local_link_move(link)
        for coeff in (-2, -1, 1, 2):
            moved = closed_branch + coeff * move
            if np.count_nonzero(DM[2] @ moved) == 0:
                closed_values.append(q_raw(moved))
    check("closed branch local moves preserve Q_raw", set(closed_values) == {2}, sorted(set(closed_values)))

    defect_branch = np.zeros(len(CI[2][0]), dtype=np.int64)
    defect_branch[CI[2][1][((0, 0, 0, 0), (0, 1))]] = 1
    check("single plaquette witness has a nonzero defect dn", np.count_nonzero(DM[2] @ defect_branch) > 0)
    check("single plaquette witness starts with Q_raw = 0", q_raw(defect_branch) == 0, q_raw(defect_branch))
    check(
        "adding exact branch moves to the single-plaquette witness keeps the same defect current",
        all(
            np.array_equal(DM[2] @ (defect_branch + DM[1] @ RNG.integers(-1, 2, size=len(CI[1][0]))), DM[2] @ defect_branch)
            for _ in range(5)
        ),
    )
    defect_values = []
    for link in CI[1][1]:
        move = local_link_move(link)
        for coeff in (-2, -1, 1, 2):
            moved = defect_branch + coeff * move
            defect_values.append(q_raw(moved))
    defect_value_set = set(defect_values)
    check("defectful branch local moves change Q_raw", len(defect_value_set) > 1, sorted(defect_value_set))
    check("defectful branch local moves produce odd Q_raw values", any(value % 2 for value in defect_value_set), sorted(defect_value_set))
    check("defectful branch witness reproduces the no-sector values in the note", defect_value_set == {-2, -1, 0, 1, 2}, sorted(defect_value_set))

    section("D - note conclusion and overclaim guards")
    for phrase in [
        "On the current surface, G1 is not derived.",
        "is invalid on the current surface.",
        "This is not a universal no-go against defect closure.",
        "A future retained dynamics theorem",
        "Record axiom's new formation sentence is also not a defect law",
    ]:
        check(f"note states narrow no-go: {phrase[:60]}", phrase in note_flat)
    for phrase in [
        "Theta is not retired.",
        "The Tier-A registry is not edited.",
        "No G1 defect-closure theorem is supplied.",
        "No defect-suppression dynamics is supplied.",
        "No G3 phase source, coefficient, action entry, or physical weighting law is supplied.",
        "No primitive, axiom, audit status, or effective status is changed.",
    ]:
        check(f"note preserves boundary: {phrase[:60]}", phrase in note_flat)
    banned = [
        "Theta is retired.",
        "theta_bar = 0 is derived",
        "G1 is closed",
        "defects are suppressed",
        "dn = 0 follows from Record",
        "dn = 0 follows from Admissibility",
        "the carrier is physical",
        "Tier-A registry is edited",
        "The effective status is changed",
    ]
    for phrase in banned:
        check(f"banned overclaim absent: {phrase}", phrase not in note_flat)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
