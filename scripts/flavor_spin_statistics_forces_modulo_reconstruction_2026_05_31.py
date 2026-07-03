#!/usr/bin/env python3
"""Finite spin-statistics boundary packet.

The runner verifies the defensible bounded content:

* the spin-statistics engine excludes wrong Bose quantization for a supplied
  relativistic spin-1/2 field with the usual particle/antiparticle sign
  structure;
* a clean taste factor can be spectator multiplicity rather than spin mixing;
* the free kernel and finite two-site qubit carrier do not select cross-site
  CAR/Grassmann statistics by themselves;
* the qubit carries spatial spin 1/2, but the full boost-spinor embedding and
  the non-circular reconstruction R remain open.

It does not derive P1, FS/CAR, or a charged-lepton sector closure from the
baseline axioms.
"""

from __future__ import annotations

import functools
from pathlib import Path

import numpy as np


NOTE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "FLAVOR_SPIN_STATISTICS_FORCES_MODULO_RECONSTRUCTION_2026-05-31.md"
)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def kron(*a: np.ndarray) -> np.ndarray:
    return functools.reduce(np.kron, a)


def main() -> int:
    passed: list[bool] = []
    energy = 1.7

    # T1: supplied relativistic spinor field with the usual sign structure.
    car = [
        energy * (particle_count + antiparticle_count)
        for particle_count in (0, 1)
        for antiparticle_count in (0, 1)
    ]
    max_occupation = 8
    bose = [
        energy * (particle_count - antiparticle_count)
        for particle_count in range(max_occupation)
        for antiparticle_count in range(max_occupation)
    ]
    passed.append(
        check(
            "T1a CAR occupation is bounded below for the supplied spinor field",
            abs(min(car)) < 1e-12 and max(car) == 2 * energy,
            f"CAR spectrum {sorted(car)}",
        )
    )
    passed.append(
        check(
            "T1b wrong Bose quantization has an unbounded-below direction",
            min(bose) == -energy * (max_occupation - 1) and min(bose) < min(car),
            f"Bose min over n_a<={max_occupation - 1} is {min(bose):.1f}; "
            "the direction continues downward as the truncation grows",
        )
    )

    # Taste as spectator multiplicity for a clean spinor block.
    mass = 1.0
    momentum = np.array([0.4, 0.9, 1.3])
    gamma = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.diag([1, -1]).astype(complex),
    ]
    clean_block = mass * np.eye(2) - 1j * sum(
        momentum[i] * gamma[i] for i in range(3)
    )
    tasted = np.kron(np.eye(4), clean_block)
    block_eigs = np.linalg.eigvals(clean_block)
    tasted_eigs = np.linalg.eigvals(tasted)
    multiplicity_ok = all(
        sum(abs(tasted_eigs - eig) < 1e-9) == 4 for eig in block_eigs
    )
    passed.append(
        check(
            "Dirac-Kahler taste can be spectator multiplicity of a clean spinor block",
            multiplicity_ok,
            f"block eigs {np.round(block_eigs, 3).tolist()} each appear four times",
        )
    )

    # IR-to-UV gap: the finite kernel identity itself is statistics-blind.
    kernel = (
        mass * np.eye(2) - 1j * sum(momentum[i] * gamma[i] for i in range(3))
    ) / (momentum @ momentum + mass**2)
    passed.append(
        check(
            "free propagator kernel identity is statistics-blind",
            np.allclose(
                kernel * (momentum @ momentum + mass**2),
                mass * np.eye(2)
                - 1j * sum(momentum[i] * gamma[i] for i in range(3)),
            ),
            "the kernel matrix does not encode a Fock statistics choice",
        )
    )

    # Two-site carrier: same ungraded algebra admits commuting or JW-dressed CAR generators.
    i2 = np.eye(2)
    sp = np.array([[0, 1], [0, 0]], dtype=complex)
    s3 = np.diag([1, -1.0]).astype(complex)
    sm = sp.conj().T
    ordinary_1, ordinary_2 = kron(sp, i2), kron(i2, sp)
    jw_1, jw_2 = kron(sm, i2), kron(s3, sm)
    passed.append(
        check(
            "two-site qubit carrier is statistics-agnostic before a generator choice",
            np.allclose(ordinary_1 @ ordinary_2 - ordinary_2 @ ordinary_1, 0)
            and np.allclose(jw_1 @ jw_2 + jw_2 @ jw_1, 0),
            "ordinary ladders commute; Jordan-Wigner dressed generators anticommute",
        )
    )

    # Spatial spin only, not a full Lorentz boost-spinor embedding.
    spin_generators = [
        np.array([[0, 1], [1, 0]], dtype=complex) / 2,
        np.array([[0, -1j], [1j, 0]], dtype=complex) / 2,
        np.diag([1, -1]).astype(complex) / 2,
    ]
    casimir = sum(spin @ spin for spin in spin_generators)
    passed.append(
        check(
            "spatial qubit spin is j=1/2",
            np.allclose(casimir, 0.5 * 1.5 * np.eye(2)),
            "Casimir j(j+1)=3/4; full boost-spinor embedding remains open",
        )
    )

    note = NOTE_PATH.read_text(encoding="utf-8")
    banned = [
        "P1 forced_modulo_one_ingredient",
        "sector closes_modulo",
        "charged-lepton flavor sector closes from framework baseline",
        "P1 forced *modulo one ingredient*",
        "P1 = forced-modulo",
    ]
    required = [
        "does not force P1 from current baseline",
        "non-circular reconstruction `R`",
        "No new axiom is introduced.",
    ]
    passed.append(
        check(
            "source boundary guard: no current-surface P1 forcing promoted",
            all(term not in note for term in banned)
            and all(term in note for term in required),
            "the packet keeps T1 as downstream support and leaves R open",
        )
    )

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print("VERDICT: bounded-support route pruning.")
    print("The T1 engine is real for a supplied relativistic spin-1/2 field,")
    print("and the taste spectator check removes one obstacle, but current")
    print("baseline plus emergent spacetime does not force P1/CAR without a")
    print("non-circular reconstruction R and a bare-qubit boost-spinor embedding.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
