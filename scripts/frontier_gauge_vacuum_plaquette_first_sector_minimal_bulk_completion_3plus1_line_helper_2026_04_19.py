#!/usr/bin/env python3
"""
Shared helper layer for the retained `3d+1 -> 3d` complement-line reduction
on the least-positive-bulk selected Wilson branch.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from frontier_dm_leptogenesis_ne_projected_source_law_derivation import (
    hermitian_linear_responses,
)
from frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_packet_theorem_2026_04_19 import (
    selected_transfer_and_packet,
)
from frontier_gauge_vacuum_plaquette_spatial_environment_character_measure import (
    build_recurrence_matrix,
)
from frontier_perron_frobenius_step2_nilpotent_chain_source_response_calculus_2026_04_19 import (
    live_from_response_pack,
)


ROOT = Path(__file__).resolve().parent.parent
NOTE_FILENAME = "GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_HELPER_NOTE_2026-04-19.md"
NOTE_PATH = ROOT / "docs" / NOTE_FILENAME
SELF_PATH = Path(__file__).resolve()

PASS = 0
FAIL = 0

ALLOWED_CITATION_MARKERS = (
    "line-helper interface",
    "helper-interface",
    "line-helper utilities",
    "line-helper authority packet",
    "helper registration",
    "one-hop dependency",
    "one-hop authority",
    "not a derivation",
    "without deriving",
)

FORBIDDEN_CITATION_MARKERS = (
    "derives the complement-line frame",
    "derives the selected_line",
    "derives the boundary-first weights",
    "physically forces the selected_line",
    "closes any downstream gauge-vacuum-plaquette theorem",
    "moves the selector",
    "moves a selector",
    "authority for moving",
)

ORIGINAL_RETAINED_WEIGHTS = ((0, 0), (1, 0), (0, 1), (1, 1))
ORDERED_LINE_BASIS = (1, 0, 2, 3)
BOUNDARY_FIRST_WEIGHTS = tuple(ORIGINAL_RETAINED_WEIGHTS[i] for i in ORDERED_LINE_BASIS)
_RETAINED_BLOCK_ORIGINAL: np.ndarray | None = None


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def normalize_line(line: np.ndarray) -> np.ndarray:
    arr = np.asarray(line, dtype=float).reshape(4)
    norm = float(np.linalg.norm(arr))
    if norm <= 0.0:
        raise ValueError("complement line must be nonzero")
    return arr / norm


def line_from_positive_angles(theta: float, phi: float, psi: float) -> np.ndarray:
    """
    Unit complement line on the positive `(1,1)` hemisphere of the retained
    ambient `S^3/{±1}`.
    """

    cpsi = float(np.cos(psi))
    return normalize_line(
        np.array(
            [
                np.cos(theta) * np.cos(phi) * cpsi,
                np.sin(theta) * np.cos(phi) * cpsi,
                np.sin(phi) * cpsi,
                np.sin(psi),
            ],
            dtype=float,
        )
    )


def positive_angles_from_line(line: np.ndarray) -> np.ndarray:
    vec = normalize_line(line)
    if vec[3] < 0.0:
        vec = -vec
    xy = float(np.hypot(vec[0], vec[1]))
    theta = float(np.arctan2(vec[1], vec[0]))
    phi = float(np.arctan2(vec[2], xy))
    psi = float(np.arcsin(np.clip(vec[3], -1.0, 1.0)))
    return np.array([theta, phi, psi], dtype=float)


def selected_retained_block_original() -> np.ndarray:
    global _RETAINED_BLOCK_ORIGINAL
    if _RETAINED_BLOCK_ORIGINAL is not None:
        return np.array(_RETAINED_BLOCK_ORIGINAL, dtype=float)
    pkg = selected_transfer_and_packet()
    transfer = np.asarray(pkg["transfer"], dtype=float)
    _jmat, weights, index = build_recurrence_matrix(5)
    retained = [index[w] for w in ORIGINAL_RETAINED_WEIGHTS]
    _RETAINED_BLOCK_ORIGINAL = transfer[np.ix_(retained, retained)]
    return np.array(_RETAINED_BLOCK_ORIGINAL, dtype=float)


def selected_retained_block_boundary_first() -> np.ndarray:
    """
    Retained `4x4` block in the original retained basis
    `((0,0),(1,0),(0,1),(1,1))`.

    The boundary-first structure is carried by `ORDERED_LINE_BASIS` during the
    ordered projection/Gram-Schmidt reduction, not by a separate coordinate
    permutation of the retained block.
    """

    return selected_retained_block_original()


def induced_ordered_slice_from_line(line: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    In the original retained coordinates, fix the ambient order
    `(1,0) -> (0,0) -> (0,1) -> (1,1)` and let the chosen complement line be
    the only free datum. The induced `3d` slice is obtained by projecting those
    ordered ambient basis vectors off the line and Gram-Schmidt
    orthonormalizing in that fixed order.
    """

    c = normalize_line(line)
    cols: list[np.ndarray] = []
    basis = np.eye(4, dtype=float)
    for idx in ORDERED_LINE_BASIS:
        v = basis[:, idx].copy()
        v -= float(c @ v) * c
        for q in cols:
            v -= float(q @ v) * q
        norm = float(np.linalg.norm(v))
        if norm > 1.0e-14:
            cols.append(v / norm)
        if len(cols) == 3:
            break
    if len(cols) != 3:
        raise RuntimeError("ordered line reduction failed to recover a 3d slice")
    return np.column_stack(cols), c


def compressed_local_block_from_line(line: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    block = selected_retained_block_original()
    qmat, c = induced_ordered_slice_from_line(line)
    h = qmat.T @ block @ qmat
    responses = np.array(hermitian_linear_responses(h.astype(complex)), dtype=float)
    live = np.array(live_from_response_pack(responses.tolist()), dtype=float)
    return h, responses, live, qmat


def slice_projector_from_line(line: np.ndarray) -> np.ndarray:
    qmat, _c = induced_ordered_slice_from_line(line)
    return qmat @ qmat.T


def reference_slice_projector(slot: str) -> np.ndarray:
    basis = np.eye(4, dtype=float)
    if slot == "rho1":
        cols = (1, 0, 3)
    elif slot == "rho2":
        cols = (0, 2, 3)
    else:
        raise ValueError("slot must be 'rho1' or 'rho2'")
    qmat = basis[:, cols]
    return qmat @ qmat.T


def projection_frobenius_distance(line: np.ndarray, slot: str) -> float:
    return float(
        np.linalg.norm(slice_projector_from_line(line) - reference_slice_projector(slot))
    )


def boundary_anchor_krylov_complement_line() -> np.ndarray:
    """
    Orthogonal complement of the boundary-anchored Krylov plane
    `span{e_(1,0), T e_(1,0), T^2 e_(1,0)}` on the boundary-first retained
    block. This is a natural cheap candidate selector used in later boundary
    theorems.
    """

    block = selected_retained_block_original()
    anchor = np.zeros(4, dtype=float)
    anchor[ORDERED_LINE_BASIS[0]] = 1.0
    krylov = np.column_stack([anchor, block @ anchor, block @ (block @ anchor)])
    qmat, _r = np.linalg.qr(krylov)
    u, _s, _vt = np.linalg.svd(qmat, full_matrices=True)
    line = u[:, 3]
    return normalize_line(line if line[0] >= 0.0 else -line)


def source_files_for_citation_firewall() -> list[Path]:
    files: list[Path] = []
    for root in (ROOT / "docs", ROOT / "scripts"):
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            if path.resolve() in {SELF_PATH, NOTE_PATH.resolve()}:
                continue
            if rel.startswith("docs/audit/") or rel.startswith("docs/publication/"):
                continue
            if path.suffix.lower() not in {".md", ".py", ".json", ".yaml", ".yml", ".txt"}:
                continue
            files.append(path)
    return files


def direct_citation_contexts(path: Path, window: int = 500) -> list[str]:
    text = path.read_text(errors="ignore")
    contexts: list[str] = []
    start = 0
    while True:
        idx = text.find(NOTE_FILENAME, start)
        if idx == -1:
            return contexts
        contexts.append(text[max(0, idx - window) : min(len(text), idx + len(NOTE_FILENAME) + window)])
        start = idx + len(NOTE_FILENAME)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    text_lower = " ".join(text.lower().split())
    required = [
        "Citation/use firewall (2026-06-18)",
        "helper-interface registration function",
        "may not be used as:",
        "one-hop dependency uses",
        "independent audit remains responsible for any effective-status movement",
    ]
    for needle in required:
        check(
            f"note contains citation firewall marker: {needle!r}",
            needle.lower() in text_lower,
        )
    forbidden = [
        "This helper derives the complement-line frame",
        "This helper derives the selected_line selector",
        "This helper closes downstream gauge-vacuum-plaquette theorems",
    ]
    for needle in forbidden:
        check(f"note avoids promotion phrase: {needle!r}", needle not in text)


def check_direct_citation_firewall() -> None:
    section("Direct citation firewall")
    contexts = []
    unqualified = []
    forbidden = []
    for path in source_files_for_citation_firewall():
        rel = path.relative_to(ROOT).as_posix()
        for context in direct_citation_contexts(path):
            lowered = " ".join(context.lower().split())
            contexts.append((rel, lowered))
            if not any(marker in lowered for marker in ALLOWED_CITATION_MARKERS):
                unqualified.append(rel)
            for marker in FORBIDDEN_CITATION_MARKERS:
                if marker in lowered:
                    forbidden.append(f"{rel}: {marker}")

    detail = ", ".join(sorted({rel for rel, _ in contexts})) or "no external direct citations"
    check(
        "all direct source citations qualify the helper note as helper-interface / one-hop authority",
        not unqualified,
        detail if not unqualified else "unqualified citations: " + ", ".join(sorted(set(unqualified))),
    )
    check(
        "direct source citations avoid complement-line-frame and selector-derivation language",
        not forbidden,
        detail if not forbidden else "forbidden contexts: " + "; ".join(sorted(set(forbidden))),
    )


def check_static_helper_contract() -> None:
    section("Static helper contract")
    check("original retained weights are the four retained corners", ORIGINAL_RETAINED_WEIGHTS == ((0, 0), (1, 0), (0, 1), (1, 1)))
    check("ordered line basis is boundary-first", ORDERED_LINE_BASIS == (1, 0, 2, 3))
    check("boundary-first weights are the ordered retained weights", BOUNDARY_FIRST_WEIGHTS == ((1, 0), (0, 0), (0, 1), (1, 1)))


def check_line_geometry_contract() -> None:
    section("Line geometry contract")
    raw = np.array([1.0, 2.0, 3.0, 4.0])
    line = normalize_line(raw)
    check("normalize_line returns a unit vector", abs(float(np.linalg.norm(line)) - 1.0) < 1.0e-14)
    try:
        normalize_line(np.zeros(4))
        zero_rejected = False
    except ValueError:
        zero_rejected = True
    check("normalize_line rejects the zero vector", zero_rejected)

    angle_line = line_from_positive_angles(0.31, 0.22, 0.17)
    angles = positive_angles_from_line(angle_line)
    rebuilt = line_from_positive_angles(*angles)
    check("positive angle chart round-trips a sample line", np.linalg.norm(angle_line - rebuilt) < 1.0e-12)

    qmat, c = induced_ordered_slice_from_line(angle_line)
    check("ordered slice has shape 4x3", qmat.shape == (4, 3))
    check("ordered slice columns are orthonormal", np.linalg.norm(qmat.T @ qmat - np.eye(3)) < 1.0e-12)
    check("ordered slice is orthogonal to the complement line", np.linalg.norm(qmat.T @ c) < 1.0e-12)


def check_live_helper_contract() -> None:
    section("Live helper contract")
    line = line_from_positive_angles(0.31, 0.22, 0.17)
    block = selected_retained_block_original()
    check("selected retained block has shape 4x4", block.shape == (4, 4))
    check("selected retained block is finite", bool(np.all(np.isfinite(block))))
    hmat, responses, live, qmat = compressed_local_block_from_line(line)
    check("compressed local block has shape 3x3", hmat.shape == (3, 3))
    check("compressed local block is finite", bool(np.all(np.isfinite(hmat))))
    check("response vector is finite", bool(np.all(np.isfinite(responses))))
    check("live response vector is finite", bool(np.all(np.isfinite(live))))
    check("compression basis is orthonormal", np.linalg.norm(qmat.T @ qmat - np.eye(3)) < 1.0e-12)
    d_rho1 = projection_frobenius_distance(line, "rho1")
    d_rho2 = projection_frobenius_distance(line, "rho2")
    check("rho1/rho2 projection distances are finite nonnegative", np.isfinite(d_rho1) and np.isfinite(d_rho2) and d_rho1 >= 0.0 and d_rho2 >= 0.0)
    try:
        reference_slice_projector("rho3")
        invalid_rejected = False
    except ValueError:
        invalid_rejected = True
    check("invalid reference slice labels are rejected", invalid_rejected)
    anchor_line = boundary_anchor_krylov_complement_line()
    check("boundary-anchor Krylov complement line is unit", abs(float(np.linalg.norm(anchor_line)) - 1.0) < 1.0e-12)


def main() -> None:
    print("Gauge-vacuum first-sector 3+1 line-helper source firewall")
    check_static_helper_contract()
    check_line_geometry_contract()
    check_live_helper_contract()
    check_note_boundary()
    check_direct_citation_firewall()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
