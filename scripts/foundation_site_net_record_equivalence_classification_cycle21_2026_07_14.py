#!/usr/bin/env python3
"""Exact controls for the Cycle-21 site-net record-equivalence theorem.

Authority-free: this runner neither selects a law nor edits the foundation.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def normalized(path: Path) -> str:
    return " ".join(
        path.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .replace(">", "")
        .split()
    )


def gf2_mat(bits: tuple[int, ...]) -> np.ndarray:
    return np.array(bits, dtype=np.uint8).reshape(4, 4)


def rank_gf2(matrix: np.ndarray) -> int:
    work = matrix.copy() % 2
    rows, cols = work.shape
    rank = 0
    for col in range(cols):
        pivot = next((row for row in range(rank, rows) if work[row, col]), None)
        if pivot is None:
            continue
        work[[rank, pivot]] = work[[pivot, rank]]
        for row in range(rows):
            if row != rank and work[row, col]:
                work[row] ^= work[rank]
        rank += 1
    return rank


# Coordinates are (x1,z1,x2,z2); each site's symplectic block is [[0,1],[1,0]].
J = np.array(
    [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
    dtype=np.uint8,
)
V1 = {tuple(v) for v in ((0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0))}
V2 = {tuple(v) for v in ((0, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 1, 1))}


def image_subspace(matrix: np.ndarray, space: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    return {tuple((matrix @ np.array(v, dtype=np.uint8)) % 2) for v in space}


def pauli_label(vector: tuple[int, ...]) -> str:
    letters = []
    for site in range(2):
        x, z = vector[2 * site : 2 * site + 2]
        letters.append({(0, 0): "I", (1, 0): "X", (0, 1): "Z", (1, 1): "Y"}[(x, z)])
    return "".join(letters)


def weight(vector: tuple[int, ...]) -> int:
    return sum(vector[2 * site] or vector[2 * site + 1] for site in range(2))


# Symplectic Pauli actions, columns are images of X1,Z1,X2,Z2.
CZ = np.array(
    [[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1]],
    dtype=np.uint8,
)
SWAP = np.array(
    [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]],
    dtype=np.uint8,
)


def source_contract() -> None:
    section("A - Authority and source contract")
    note = normalized(NOTE)
    axioms = AXIOMS.read_text(encoding="utf-8").lower()
    check("A note exists", NOTE.is_file())
    check("A note is authority-free", "authority: none" in note)
    check("A note does not amend an axiom", "does not amend an axiom" in note)
    check("A note does not select a law", "select a microscopic law" in note)
    check("A named site M2 is present in foundation", "at each site" in axioms and "m_2" in axioms)
    check("A max one record per site is present", "site never carries more than one record" in axioms)
    check("A qubit basis neutrality is present", "no possibility is privileged" in axioms)


def symplectic_census() -> None:
    section("B - Exhaustive two-qubit symplectic census")
    symplectic: list[np.ndarray] = []
    preserving: list[np.ndarray] = []
    for bits in product((0, 1), repeat=16):
        matrix = gf2_mat(bits)
        if rank_gf2(matrix) != 4:
            continue
        if not np.array_equal((matrix.T @ J @ matrix) % 2, J):
            continue
        symplectic.append(matrix)
        images = {frozenset(image_subspace(matrix, V1)), frozenset(image_subspace(matrix, V2))}
        targets = {frozenset(V1), frozenset(V2)}
        if images == targets:
            preserving.append(matrix)
    check("B Sp(4,2) has 720 elements", len(symplectic) == 720)
    check("B site-plane normalizer has 72 elements", len(preserving) == 72)
    check("B 648 symplectic maps are entangling factor maps", len(symplectic) - len(preserving) == 648)
    check("B full Clifford quotient has 11520 elements", 16 * len(symplectic) == 11520)
    check("B site-net Clifford quotient has 1152 elements", 16 * len(preserving) == 1152)


def cz_and_swap_controls() -> None:
    section("C - Exact CZ and site-swap controls")
    check("C CZ is symplectic", np.array_equal((CZ.T @ J @ CZ) % 2, J))
    check("C swap is symplectic", np.array_equal((SWAP.T @ J @ SWAP) % 2, J))
    x1 = (1, 0, 0, 0)
    z1 = (0, 1, 0, 0)
    x2 = (0, 0, 1, 0)
    z2 = (0, 0, 0, 1)
    images_cz = [tuple((CZ @ np.array(v, dtype=np.uint8)) % 2) for v in (x1, z1, x2, z2)]
    check("C CZ sends X1 to X1Z2", pauli_label(images_cz[0]) == "XZ")
    check("C CZ fixes Z1", pauli_label(images_cz[1]) == "ZI")
    check("C CZ sends X2 to Z1X2", pauli_label(images_cz[2]) == "ZX")
    check("C CZ fixes Z2", pauli_label(images_cz[3]) == "IZ")
    check("C CZ does not permute named site factors", {frozenset(image_subspace(CZ, V1)), frozenset(image_subspace(CZ, V2))} != {frozenset(V1), frozenset(V2)})
    check("C CZ preserves local Z support weight", weight(images_cz[1]) == weight(z1) == 1)
    check("C CZ enlarges X1 support weight", weight(images_cz[0]) == 2 and weight(x1) == 1)
    check("C swap permutes named site factors", {frozenset(image_subspace(SWAP, V1)), frozenset(image_subspace(SWAP, V2))} == {frozenset(V1), frozenset(V2)})
    swap_x1 = tuple((SWAP @ np.array(x1, dtype=np.uint8)) % 2)
    check("C swap preserves record support weight", pauli_label(swap_x1) == "IX" and weight(swap_x1) == 1)


def documentation_contract() -> None:
    section("D - Theorem, scope, and no-go contract")
    note = normalized(NOTE)
    required = (
        "any star automorphism",
        "site permutation followed by onsite unitary recodings",
        "foundation-maximal site-record category",
        "law-selected record category",
        "full one-site m_2 record net",
        "scalar-additive record readout",
        "not automatically gauge",
        "no axiom sentence follows",
        "record-net closure",
        "common complex-linear pu(2) recoding",
    )
    for phrase in required:
        check(f"D required phrase is present: {phrase}", phrase in note)
    for index in range(1, 9):
        check(f"D N{index} section is present", f"n{index} —" in note)
    check(
        "D N7 keeps transported-net route live",
        "strongest surviving steelman" in note
        and "fixed-versus-transported reading remains live" in note,
    )
    check("D conclusion retains exact-law referent", "stable exact law identity" in note and "record-faithful equivalence class" in note)


def main() -> int:
    source_contract()
    symplectic_census()
    cz_and_swap_controls()
    documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print("BOUNDARY: maximal named-site record equivalence is factor permutation plus onsite recoding; larger quotients are law-relative")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
