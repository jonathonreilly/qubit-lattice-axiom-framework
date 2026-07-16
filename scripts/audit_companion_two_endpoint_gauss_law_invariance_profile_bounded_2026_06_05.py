#!/usr/bin/env python3
"""Finite checks for the two-endpoint Gauss-law invariance bounded note.

This runner verifies only the stated four-qubit endpoint model. It does not
derive gauge invariance of observables from the Record axiom, identify all
invariant operators with physical observables, derive endpoint Gauss
generators, or touch gauge dynamics, coupling values, electroweak breaking, or
color SU(3).
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    REPO_ROOT
    / "docs"
    / "TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md"
)

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


def op(x: np.ndarray, pos: int, n: int = 4) -> np.ndarray:
    mats = [I2] * n
    mats[pos] = x
    out = mats[0]
    for mat in mats[1:]:
        out = np.kron(out, mat)
    return out


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def close(a: np.ndarray, b: np.ndarray) -> bool:
    return np.allclose(a, b, atol=1e-10)


def nonzero(a: np.ndarray) -> bool:
    return np.linalg.norm(a) > 1e-9


def endpoint_profile(generators: tuple[np.ndarray, np.ndarray], obs: np.ndarray) -> list[bool]:
    return [not nonzero(comm(gen, obs)) for gen in generators]


I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SP = np.array([[0, 1], [0, 0]], dtype=complex)
SM = np.array([[0, 0], [1, 0]], dtype=complex)


def main() -> int:
    print("=" * 72)
    print("Two-endpoint Gauss-law invariance profile bounded checks")
    print("=" * 72)

    a_site, a_link, b_link, b_site = 0, 1, 2, 3
    zero = np.zeros((16, 16), dtype=complex)

    ga = op(SZ, a_site) + op(SZ, a_link)
    gb = op(SZ, b_link) + op(SZ, b_site)
    u1_generators = (ga, gb)

    bare = op(SP, a_link) @ op(SM, b_link)
    half = op(SM, a_site) @ op(SP, a_link) @ op(SM, b_link)
    full = op(SM, a_site) @ op(SP, a_link) @ op(SM, b_link) @ op(SP, b_site)

    bare_profile = endpoint_profile(u1_generators, bare)
    half_profile = endpoint_profile(u1_generators, half)
    full_profile = endpoint_profile(u1_generators, full)

    record("U1 bare link-end transport is variant at both endpoints", bare_profile == [False, False])
    record("U1 half-dressed transport is invariant only at endpoint A", half_profile == [True, False])
    record("U1 fully dressed Wilson-type line is invariant at both endpoints", full_profile == [True, True])
    record(
        "U1 endpoint-invariance count is monotone 0 to 1 to 2",
        [sum(bare_profile), sum(half_profile), sum(full_profile)] == [0, 1, 2],
    )
    record("U1 bare operator is not zero", nonzero(bare))
    record("U1 half-dressed operator is not zero", nonzero(half))
    record("U1 fully dressed operator is not zero", nonzero(full))

    paulis = [I2, SX, SY, SZ]
    basis = []
    for choice in product(range(4), repeat=4):
        mat = paulis[choice[0]]
        for idx in choice[1:]:
            mat = np.kron(mat, paulis[idx])
        basis.append(mat)

    def adjoint_matrix(generator: np.ndarray) -> np.ndarray:
        return np.array(
            [
                [np.trace(left.conj().T @ comm(generator, right)) / 16 for right in basis]
                for left in basis
            ],
            dtype=complex,
        )

    rank = np.linalg.matrix_rank(np.vstack([adjoint_matrix(ga), adjoint_matrix(gb)]), tol=1e-8)
    invariant_dim = 256 - int(rank)
    record("U1 invariant algebra is the commutant of the endpoint generators", invariant_dim > 0)
    record("U1 invariant algebra dimension is 36", invariant_dim == 36, f"dim={invariant_dim}")
    record("U1 invariant algebra is a proper subalgebra of the full four-qubit algebra", invariant_dim < 256)

    sa = tuple((op(s, a_site) + op(s, a_link)) / 2 for s in (SX, SY, SZ))
    sb = tuple((op(s, b_link) + op(s, b_site)) / 2 for s in (SX, SY, SZ))

    def su2_profile(obs: np.ndarray) -> list[bool]:
        return [
            all(close(comm(gen, obs), zero) for gen in sa),
            all(close(comm(gen, obs), zero) for gen in sb),
        ]

    singlet = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    singlet_projector = np.outer(singlet, singlet.conj())
    double_singlet = np.kron(singlet_projector, singlet_projector)

    record("SU2 bare link-end transport is variant at both endpoints", su2_profile(bare) == [False, False])
    record("SU2 double-singlet Wilson-type observable is invariant at both endpoints", su2_profile(double_singlet) == [True, True])
    record("SU2 double-singlet observable is nonzero", nonzero(double_singlet))

    text = NOTE.read_text(encoding="utf-8")
    # Normalize whitespace so multi-line firewall sentences match, and require
    # the COMPLETE four-axiom sentence (a bare "Lattice + Qubit +" prefix would
    # pass even if Admissibility or Record were absent, reordered, or replaced).
    text_norm = " ".join(text.split())
    for phrase in [
        "does not derive gauge invariance of observables from the Record axiom",
        "does not identify all gauge-invariant algebra elements with physical observables",
        "does not derive the endpoint Gauss generators from Lattice + Qubit + Admissibility + Record",
        "does not derive gauge dynamics",
        "does not require or establish a repo-wide quantum-link ontology",
    ]:
        record(f"source-note firewall present: {phrase}", phrase in text_norm)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
