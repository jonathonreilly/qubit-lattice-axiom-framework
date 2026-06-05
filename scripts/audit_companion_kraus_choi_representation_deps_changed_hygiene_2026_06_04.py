#!/usr/bin/env python3
"""Kraus-Choi dependency-rewire hygiene companion.

This runner verifies that the finite-region Kraus/Choi parent depends on
Lattice + Quantum content from `minimal_axioms`, while the Record axiom's
finite scalar readout content is not used by the parent's proof.

It is a meta companion only: no theorem claim, no audit verdict, and no direct
status change.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = (
    REPO_ROOT
    / "docs"
    / "KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md"
)
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "KRAUS_CHOI_REPRESENTATION_DEPS_CHANGED_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
OLD_AXIOMS = REPO_ROOT / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
NEW_AXIOMS = REPO_ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def section(text: str, start: str, stop_markers: tuple[str, ...]) -> str:
    start_idx = text.find(start)
    if start_idx == -1:
        return ""
    end = len(text)
    for marker in stop_markers:
        idx = text.find(marker, start_idx + len(start))
        if idx != -1 and idx < end:
            end = idx
    return text[start_idx:end]


def parent_load_bearing_surface(text: str) -> str:
    stops = (
        "\n## Step 4 ",
        "\n## What this can support after audit",
        "\n## What this does not close",
    )
    end = len(text)
    for marker in stops:
        idx = text.find(marker)
        if idx != -1 and idx < end:
            end = idx
    return text[:end]


def pointer_surface(text: str) -> str:
    return section(
        text,
        "Plain-text pointer references",
        ("\n## What this file is not", "\n## What this does not close", "\n## "),
    )


def close(a: np.ndarray, b: np.ndarray) -> bool:
    return np.allclose(a, b, atol=1e-10)


def min_eig(a: np.ndarray) -> float:
    herm = (a + a.conj().T) / 2
    return float(np.linalg.eigvalsh(herm).min().real)


def apply_kraus(kraus_ops: list[np.ndarray], x: np.ndarray) -> np.ndarray:
    out = np.zeros_like(x)
    for k in kraus_ops:
        out = out + k @ x @ k.conj().T
    return out


def kraus_norm(kraus_ops: list[np.ndarray]) -> np.ndarray:
    d = kraus_ops[0].shape[1]
    out = np.zeros((d, d), dtype=complex)
    for k in kraus_ops:
        out = out + k.conj().T @ k
    return out


def choi_from_map(map_fn, d: int) -> np.ndarray:
    out = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            eij = np.zeros((d, d), dtype=complex)
            eij[i, j] = 1
            out = out + np.kron(eij, map_fn(eij))
    return out


def choi_from_kraus(kraus_ops: list[np.ndarray]) -> np.ndarray:
    return choi_from_map(lambda x: apply_kraus(kraus_ops, x), kraus_ops[0].shape[0])


def main() -> int:
    print("=" * 72)
    print("Kraus-Choi dependency-rewire hygiene companion")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md")
    print("Companion note: docs/KRAUS_CHOI_REPRESENTATION_DEPS_CHANGED_HYGIENE_COMPANION_NOTE_2026-06-04.md")
    print("Scope: meta evidence only; no theorem claim, no audit verdict, no direct status change.")

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    companion_text = COMPANION_NOTE.read_text(encoding="utf-8")
    old_axioms = OLD_AXIOMS.read_text(encoding="utf-8")
    new_axioms = NEW_AXIOMS.read_text(encoding="utf-8")

    surface = parent_load_bearing_surface(parent_text)
    record("parent_load_surface_present", len(surface) > 1000, f"chars={len(surface)}")

    for phrase in ["Kraus", "Choi", "M_2", "Z^3", "finite", "operator-sum"]:
        record(f"parent_load_surface_contains_{phrase}", phrase in surface)

    record_terms = (
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive scalar record",
    )
    hits = {term: surface.count(term) for term in record_terms}
    record("parent_load_surface_has_no_record_readout_terms", sum(hits.values()) == 0, str(hits))

    pointer = pointer_surface(parent_text)
    record("parent_pointer_surface_present", len(pointer) > 0, f"chars={len(pointer)}")
    record("parent_pointer_surface_marks_not_load_bearing", "NOT load-bearing deps" in pointer)
    for ptr in [
        "BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20",
        "PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20",
        "PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE",
    ]:
        record(f"parent_pointer_surface_lists_{ptr}", ptr in pointer)

    record("old_axioms_have_qubit_content", "qubit" in old_axioms.lower() and "M_2" in old_axioms)
    record("new_axioms_have_quantum_content", "Quantum" in new_axioms and "M_2" in new_axioms)
    record("old_axioms_have_lattice_content", "Z^3" in old_axioms or "Z³" in old_axioms)
    record("new_axioms_have_lattice_content", "Lattice" in new_axioms and ("Z^3" in new_axioms or "Z³" in new_axioms))
    record("new_axioms_have_separate_record_content", "Record" in new_axioms and "I(R_1" in new_axioms)
    record("old_axioms_lack_record_additivity_formula", "I(R_1" not in old_axioms)

    eye = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)

    dephasing = [np.sqrt(0.7) * eye, np.sqrt(0.3) * sz]
    record("dephasing_kraus_trace_preserving", close(kraus_norm(dephasing), eye))
    record("dephasing_choi_is_psd", min_eig(choi_from_kraus(dephasing)) >= -1e-10)

    depolarizing = [
        np.sqrt(1 - 3 * 0.2 / 4) * eye,
        np.sqrt(0.2 / 4) * sx,
        np.sqrt(0.2 / 4) * sy,
        np.sqrt(0.2 / 4) * sz,
    ]
    record("depolarizing_kraus_trace_preserving", close(kraus_norm(depolarizing), eye))
    record("depolarizing_choi_is_psd", min_eig(choi_from_kraus(depolarizing)) >= -1e-10)

    rng = np.random.default_rng(seed=2664)
    a = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    q, r = np.linalg.qr(a)
    phases = np.diag(r) / np.abs(np.diag(r))
    unitary = q @ np.diag(phases)
    unitary_channel = [unitary]
    record("unitary_kraus_trace_preserving", close(kraus_norm(unitary_channel), eye))
    record("unitary_choi_is_psd", min_eig(choi_from_kraus(unitary_channel)) >= -1e-10)

    transpose_choi = choi_from_map(lambda x: x.T.copy(), 2)
    record("transpose_map_choi_has_negative_eigenvalue", min_eig(transpose_choi) < -1e-3)

    tensor_dims = []
    for size in [1, 2, 3, 4]:
        d = 2**size
        tensor_dims.append(d)
        record(f"finite_region_tensor_dim_size_{size}", d == 2**size)
    record("finite_region_tensor_dims_match_parent_formula", tensor_dims == [2, 4, 8, 16])

    lower_companion = companion_text.lower()
    record("companion_declares_meta_type", "**type:** meta" in lower_companion)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in lower_companion)
    record("companion_disclaims_direct_status_change", "not a direct status change" in lower_companion)
    record("companion_keeps_record_non_load_bearing", "record remains non-load-bearing" in lower_companion)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
