#!/usr/bin/env python3
"""Finite trace-relative Gibbs/Radon-Nikodym certificate.

This runner checks the load-bearing finite-dimensional theorem in
docs/RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20.md:
for a finite matrix algebra M_d(C), a self-adjoint H defines
D_H = exp(-H) / tau(exp(-H)); D_H is positive, tau(D_H)=1, and
omega_H(O)=tau(D_H O) is positive for positive O.

It deliberately does not prove any rho_ref identification or Wilson/RP carrier
representation bridge.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE = REPO_ROOT / "docs/RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20.md"
TOL = 1e-10


def check(name: str, condition: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if condition else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(condition)


def expm_hermitian(h: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(h)
    return (vecs * np.exp(-vals)) @ vecs.conj().T


def tau(a: np.ndarray) -> complex:
    return np.trace(a) / a.shape[0]


def positive_from_seed(seed: int, d: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return a.conj().T @ a


def hermitian_from_seed(seed: int, d: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return (a + a.conj().T) / 2


def main() -> int:
    passed: list[bool] = []
    note = NOTE.read_text(encoding="utf-8")

    passed.append(check(
        "note states normalized-trace theorem as load-bearing scope",
        "No `rho_ref` or Wilson configuration-space measure is a" in note
        and "load-bearing premise of this theorem" in note,
    ))
    passed.append(check(
        "pre-record reference note is not a markdown load-bearing dependency",
        "[`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`]" not in note,
    ))

    for d in (2, 4, 8):
        h = hermitian_from_seed(100 + d, d)
        e_minus_h = expm_hermitian(h)
        z_h = tau(e_minus_h)
        d_h = e_minus_h / z_h
        eig_d = np.linalg.eigvalsh(d_h)
        passed.append(check(
            f"d={d}: exp(-H) positive and Z_H=tau(exp(-H)) positive",
            np.min(np.linalg.eigvalsh(e_minus_h)) > 0 and np.real(z_h) > 0 and abs(np.imag(z_h)) < TOL,
            f"min_eig(exp(-H))={np.min(np.linalg.eigvalsh(e_minus_h)):.3e}, Z_H={z_h:.12g}",
        ))
        passed.append(check(
            f"d={d}: D_H positive with tau(D_H)=1",
            np.min(eig_d) > -TOL and abs(tau(d_h) - 1) < TOL,
            f"min_eig(D_H)={np.min(eig_d):.3e}, tau(D_H)={tau(d_h):.12g}",
        ))

        positives = [positive_from_seed(1000 + 10 * d + j, d) for j in range(3)]
        omega_values = [tau(d_h @ o) for o in positives]
        density_values = [np.trace(e_minus_h @ o) / np.trace(e_minus_h) for o in positives]
        passed.append(check(
            f"d={d}: omega_H(O)=tau(D_H O) is positive on sampled O>=0",
            all(np.real(v) >= -TOL and abs(np.imag(v)) < TOL for v in omega_values),
            "; ".join(f"{np.real(v):.6e}" for v in omega_values),
        ))
        passed.append(check(
            f"d={d}: normalized-trace formula equals density-matrix formula",
            all(abs(a - b) < TOL for a, b in zip(omega_values, density_values)),
            f"max_diff={max(abs(a-b) for a, b in zip(omega_values, density_values)):.3e}",
        ))

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print("FINDING: finite Gibbs Radon-Nikodym density closes relative to tau_Lambda.")
    print("rho_ref and Wilson/RP carrier bridges are explicitly out of scope.")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
