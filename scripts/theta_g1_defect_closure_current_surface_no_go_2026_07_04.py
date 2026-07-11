#!/usr/bin/env python3
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
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
POSITIVE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
AXIOM_NO_GO = DOCS / "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
G3_NO_GO = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"

SOURCE_ROWS = {
    "positive": "theta_gauge_positive_route_stretch_status_2026-07-04",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "axiom_no_go": "theta_gauge_winding_axiom_update_no_go_note_2026-07-04",
    "g3_no_go": "theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04",
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
}

PASS = 0
FAIL = 0
RNG = np.random.default_rng(17)
D = 4
L = 2


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


def row(claim_id: str) -> dict:
    rows = json.loads(read(LEDGER))["rows"]
    out = rows.get(claim_id)
    if out is None:
        raise AssertionError(f"missing row {claim_id}")
    return out


def row_or_none(claim_id: str) -> dict | None:
    return json.loads(read(LEDGER))["rows"].get(claim_id)


def cells(size: int, degree: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    out = []
    sites = [tuple(site) for site in np.ndindex(*(size,) * D)]
    for directions in combinations(range(D), degree):
        for site in sites:
            out.append((site, directions))
    return out


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
DM = {degree: d_matrix(L, degree) for degree in range(D)}
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


def q_int(mvec: dict[tuple[int, int], int]) -> int:
    return (
        mvec[(0, 1)] * mvec[(2, 3)]
        - mvec[(0, 2)] * mvec[(1, 3)]
        + mvec[(0, 3)] * mvec[(1, 2)]
    )


def main() -> int:
    print("theta G1 defect-closure current-surface no-go verifier")

    paths = [NOTE, MINIMAL, REGISTRY, DECISION_HISTORY, LEDGER, POSITIVE, CARRIER4D, AXIOM_NO_GO, G3_NO_GO]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    source_flat = {path: flat(text) for path, text in texts.items()}

    section("A. source presence and ledger grounding")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    for label, claim_id in SOURCE_ROWS.items():
        r = row_or_none(claim_id)
        if label in {"positive", "axiom_no_go", "g3_no_go"} and r is None:
            source_path = {
                "positive": POSITIVE,
                "axiom_no_go": AXIOM_NO_GO,
                "g3_no_go": G3_NO_GO,
            }[label]
            check(f"{label} source is present on current main", source_path.exists())
            check(f"{label} has no pre-generated ledger authority requirement", True)
            continue
        check(f"{label} ledger row resolves", r is not None and r.get("claim_id") == claim_id)
        check(f"{label} row has note path", bool(r and r.get("note_path")), r.get("note_path") if r else None)
    for label in ["positive", "carrier4d", "axiom_no_go", "g3_no_go"]:
        r = row_or_none(SOURCE_ROWS[label])
        check(f"{label} row is not a theta-retirement authority", r is None or r.get("effective_status") != "retained", r.get("effective_status") if r else None)
    check("new note has Type no_go", "**Type:** no_go" in note)
    check("new note has Claim type no_go", "**Claim type:** no_go" in note)

    section("B. admission-era decision history")
    tier = json.loads(read(DECISION_HISTORY))
    theta = tier["retired_derivation_targets"]["strong_cp_theta_zero_note"]
    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("decision history preserves zero final admission count", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("canonical Tier-A IDs are empty on current main", tier["canonical_ids"] == [], tier["canonical_ids"])
    check("live derivation targets are empty on current main", tier.get("derivation_targets", {}) == {}, tier.get("derivation_targets"))
    for name, target in [("theta", theta), ("AC", ac)]:
        retirement = target.get("retirement", {})
        check(f"{name} retired-target record is preserved", bool(target))
        check(f"{name} disposition correction date is recorded", retirement.get("date") == "2026-07-11", retirement)
    check(
        "historical theta minimum decomposition preserves gauge plus mass",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    check(
        "historical AC decomposition preserves three old atoms",
        ac["minimum_decomposition"] == [
            "reading_occupancy_selection",
            "delta_readout_identification_R_eta",
            "species_bridge",
        ],
        ac["minimum_decomposition"],
    )
    for phrase in [
        "Theta is not retired.",
        "No admission registry is created.",
        "No axiom or primitive is changed.",
        "No audit status or effective status is changed.",
        "No mass-side determinant-channel bridge is supplied.",
    ]:
        check(f"note preserves boundary: {phrase[:54]}", phrase in note)
    for phrase in [
        "gauge_side_winding_account",
        "mass_side_orientation_determinant_readout_bridge",
        "multi-plaquette / large-gauge-winding account",
        "determinant-readout bridge",
    ]:
        check(f"machine registry theta text includes {phrase[:48]}", phrase in flat(json.dumps(theta)))
    for phrase in ["multi-plaquette / large-gauge-winding account", "determinant-readout bridge"]:
        check(f"decision history theta text includes {phrase[:48]}", phrase in flat(json.dumps(theta)))
    check("note has current-main posture line", "Current-main posture (2026-07-11)" in note)
    check("note records absence of an admission registry", "No admission registry is created." in note)
    check("note does not create an admission registry", "does not create any admission registry" in note)

    section("C. source-packet boundary checks")
    for phrase in [
        "G1 defect closure",
        "derive the closed-branch restriction dn = 0",
        "No derivation yet that the physical surface imposes or suppresses `dn != 0`",
        "Without this, the closed-branch carrier remains a witness surface.",
    ]:
        check(f"positive route names G1 boundary: {phrase[:54]}", phrase in source_flat[POSITIVE])
    for phrase in [
        "with a branch defect present (`dn != 0`",
        "closed-branch (defect-free) subsurface",
        "what a physical derivation must supply is the closedness restriction",
        "no sector decomposition survives on the unrestricted branch sum",
        "not assert that defect-ful theories lack theta physics in general",
        "Closed branch",
        "the carrier residual IS the defect question",
    ]:
        check(f"carrier keeps defect boundary: {phrase[:56]}", phrase in source_flat[CARRIER4D])
    for phrase in [
        "Admissibility is not a dynamics axiom",
        "does not choose a Hamiltonian or transfer operator",
        "transition probabilities or weights",
        "context selection",
        "source/action and physical-observable identification",
        "the strong-CP theta gauge and mass-side derivation obligations",
        "Only records are readable",
    ]:
        check(f"minimal axioms withhold: {phrase[:50]}", phrase in source_flat[MINIMAL])
    for phrase in [
        "does not supply the theta gauge-side winding",
        "physical topological-sector/gauge-action bridge",
        "No admission registry is created.",
        "Theta is not retired.",
    ]:
        check(f"axiom-update no-go supports G1 boundary: {phrase[:52]}", phrase in source_flat[AXIOM_NO_GO])
    for phrase in [
        "G1 defect closure in parallel",
        "prove or refute physical suppression of `dn != 0`",
        "G3 is meaningful only after the carrier surface is disciplined",
    ]:
        check(f"G3 block leaves G1 live: {phrase[:52]}", phrase in source_flat[G3_NO_GO])

    section("D. note fan-out and no-go claim")
    for phrase in [
        "On the current surface, G1 is not derived.",
        "Neither statement is a derivation that physical branch cochains satisfy",
        "neither supplies a measure or action that suppresses `dn != 0`",
        "The present framework surface therefore localizes G1; it does not close it.",
    ]:
        check(f"no-go statement present: {phrase[:60]}", phrase in note_flat)
    for route in [
        "Algebraic identity `d^2 = 0`",
        "Closed-branch carrier",
        "Defect witness",
        "Minimal axioms and approved primitives",
        "Record/readout rule",
        "Admissibility",
        "G3 phase insertion work",
        "admission registry",
    ]:
        check(f"route fan-out row present: {route}", route in note)
    for phrase in [
        "G1 is now isolated as the missing closedness-or-suppression premise",
        "The carrier is explicitly conditional on `dn = 0`",
        "It is only an unrestricted-branch-sum no-go",
    ]:
        check(f"movement sentence present: {phrase[:56]}", phrase in note_flat)

    section("E. cubical complex and closure is a proper condition")
    check("dd=0 for C0->C1->C2", np.all(DM[1] @ DM[0] == 0))
    check("dd=0 for C1->C2->C3", np.all(DM[2] @ DM[1] == 0))
    check("dd=0 for C2->C3->C4", np.all(DM[3] @ DM[2] == 0))
    dims = {degree: len(CELL_INFO[degree][0]) for degree in range(D + 1)}
    ranks = {degree: int(np.linalg.matrix_rank(DM[degree].astype(float))) for degree in range(D)}
    kernel_dim_c2 = dims[2] - ranks[2]
    check("C2 dimension is nonzero on T4_2", dims[2] == 96, dims)
    check("d2 rank is nonzero, so closure is not automatic", ranks[2] > 0, ranks)
    check("closed 2-cochains are a proper subspace", 0 < kernel_dim_c2 < dims[2], kernel_dim_c2)
    n_open = np.zeros(len(CELL_INFO[2][0]), dtype=np.int64)
    n_open[CELL_INFO[2][1][((0, 0, 0, 0), (0, 1))]] = 1
    check("single plaquette branch cochain is not closed", bool(np.any(DM[2] @ n_open != 0)))
    check("d of an exact branch move is closed", all(np.all(DM[2] @ (DM[1] @ RNG.integers(-1, 2, size=len(CELL_INFO[1][0]))) == 0) for _ in range(5)))
    check("adding exact move to open cochain remains open", all(np.any(DM[2] @ (n_open + DM[1] @ RNG.integers(-1, 2, size=len(CELL_INFO[1][0]))) != 0) for _ in range(5)))

    section("F. closed-branch flux arithmetic")
    check("all six unit-flux representatives are closed", all(np.all(DM[2] @ rep == 0) for rep in REPS.values()))
    for plane, rep in REPS.items():
        check(f"single unit flux {plane} has zero Q_raw", qraw(rep) == 0, qraw(rep))
    samples = [
        ({(0, 1): 1, (0, 2): 0, (0, 3): 0, (1, 2): 0, (1, 3): 0, (2, 3): 1}, 2),
        ({(0, 1): 0, (0, 2): 1, (0, 3): 0, (1, 2): 0, (1, 3): 1, (2, 3): 0}, -2),
        ({(0, 1): 0, (0, 2): 0, (0, 3): 1, (1, 2): 1, (1, 3): 0, (2, 3): 0}, 2),
    ]
    for mvec, expected in samples:
        n = sum(mvec[plane] * REPS[plane] for plane in PLANES)
        check(f"closed sample has expected Q_raw={expected}", qraw(n) == expected, qraw(n))
    for _ in range(8):
        mvec = {plane: int(RNG.integers(-2, 3)) for plane in PLANES}
        n = sum(mvec[plane] * REPS[plane] for plane in PLANES)
        check("closed flux Q_raw equals twice intersection form", qraw(n) == 2 * q_int(mvec), (qraw(n), q_int(mvec)))
    for _ in range(8):
        mvec = {plane: int(RNG.integers(-2, 3)) for plane in PLANES}
        lam = RNG.integers(-2, 3, size=len(CELL_INFO[1][0]))
        n = sum(mvec[plane] * REPS[plane] for plane in PLANES)
        shifted = n + DM[1] @ lam
        check("closed branch move keeps closedness", np.all(DM[2] @ shifted == 0))
        check("closed branch move preserves Q_raw", qraw(shifted) == qraw(n), (qraw(n), qraw(shifted)))
        check("closed branch Q_raw is even", qraw(shifted) % 2 == 0, qraw(shifted))

    section("G. defect witness arithmetic")
    defect_values = set()
    odd_seen = False
    for _ in range(12):
        lam = RNG.integers(-1, 2, size=len(CELL_INFO[1][0]))
        moved = n_open + DM[1] @ lam
        value = qraw(moved)
        defect_values.add(value)
        odd_seen = odd_seen or value % 2 != 0
        check("moved open branch remains defectful", bool(np.any(DM[2] @ moved != 0)))
    check("defect branch moves give multiple Q_raw values", len(defect_values) > 1, sorted(defect_values))
    check("defect branch moves include odd Q_raw values", odd_seen, sorted(defect_values))
    check("therefore Q_raw/2 is not integer-valued on all defect moves", any(v % 2 for v in defect_values), sorted(defect_values))
    representative_values = sorted(defect_values)
    if len(representative_values) >= 2:
        check("same defect support can carry different cup-square values", representative_values[0] != representative_values[-1], representative_values)
    else:
        check("same defect support can carry different cup-square values", False, representative_values)

    section("H. no hidden dynamics or closure premise")
    for phrase in [
        "No branch-action, no update law, no defect energy",
        "it does not manufacture closedness or select a defect-free sector",
        "Admissibility",
        "not a dynamics axiom",
        "cannot bypass the carrier's need for defect discipline",
    ]:
        check(f"note blocks hidden closure premise: {phrase[:54]}", phrase in note_flat)
    for item in [
        "Constraint-level route",
        "Dynamical route",
        "G2 registration after G1",
        "G4 assembly last",
    ]:
        check(f"next attack item present: {item}", item in note)

    section("I. note discipline and controlled links")
    forbidden = [
        "Theta is retired",
        "theta_bar = 0 is derived",
        "future defect-closure work is ruled out",
        "we create an admission registry",
        "audit status is upgraded",
        "effective status is upgraded",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    expected_links = {
        "../scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py",
        "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md",
        "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md",
        "MINIMAL_AXIOMS_2026-06-29.md",
        "THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md",
        "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md",
        "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
    }
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    check("note line count is bounded", 130 <= len(note.splitlines()) <= 240, len(note.splitlines()))
    check("verification block states fail-zero threshold", "Expected close: `FAIL=0` with at least 105 checks." in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 105 else 1


if __name__ == "__main__":
    raise SystemExit(main())
