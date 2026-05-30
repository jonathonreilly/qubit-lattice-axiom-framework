#!/usr/bin/env python3
"""Raw Hermitian-pair to projector-packet interface.

This runner verifies only finite linear algebra:

  * U_pair = U_e^dagger U_nu is unitary;
  * |U_pair|^2 is doubly stochastic;
  * |U_pair|^2 is invariant under independent eigenvector rephasings.

It intentionally does not compute leptogenesis transport diagnostics or import
the DM transport helper module.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "dm_leptogenesis_pmns_projector_interface_note_2026-04-16"
RUNNER_PATH = "scripts/frontier_dm_leptogenesis_pmns_projector_interface.py"
NOTE_PATH = ROOT / "docs/DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md"

# Pure linear-algebra helpers used as the raw Hermitian-pair interface for
# every dm_leptogenesis_pmns_* downstream runner. These are reinstated by the
# 2026-05-27 runner repair for the dm_leptogenesis_pmns_transport candidate row:
# the prior raw-interface rewrite stripped these helpers and broke ImportError
# in 10+ downstream scripts (all importing `canonical_h` from this module).
# The helpers below match the pre-strip definitions verbatim and import no
# transport machinery, preserving the raw-interface narrowing intent.
CYCLE = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def canonical_y(x: np.ndarray, y: np.ndarray, delta: float) -> np.ndarray:
    """Canonical Y_lepton construction from (x, y, delta) coordinates."""
    phase_block = np.diag(
        np.array([y[0], y[1], y[2] * np.exp(1j * delta)], dtype=complex)
    )
    return np.diag(np.asarray(x, dtype=complex)) + phase_block @ CYCLE


def canonical_h(x: np.ndarray, y: np.ndarray, delta: float) -> np.ndarray:
    """Canonical Hermitian pair H = Y Y^dagger from (x, y, delta) coordinates."""
    ymat = canonical_y(x, y, delta)
    return ymat @ ymat.conj().T


def monomial_y(masses: np.ndarray) -> np.ndarray:
    """Monomial Y from a diagonal mass vector."""
    return np.diag(np.asarray(masses, dtype=complex)) @ CYCLE


def monomial_h(masses: np.ndarray) -> np.ndarray:
    """Monomial Hermitian H = Y Y^dagger from a diagonal mass vector."""
    ymat = monomial_y(masses)
    return ymat @ ymat.conj().T


def canonical_left_diagonalizer(h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    evals, u = np.linalg.eigh(h)
    order = np.argsort(np.real(evals))
    evals = np.real(evals[order])
    u = u[:, order]
    return evals, u


def projector_packet(h_nu: np.ndarray, h_e: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    _eval_nu, u_nu = canonical_left_diagonalizer(h_nu)
    _eval_e, u_e = canonical_left_diagonalizer(h_e)
    u_pair = u_e.conj().T @ u_nu
    return u_pair, np.abs(u_pair) ** 2


def pmns_projector_packet(h_nu: np.ndarray, h_e: np.ndarray) -> np.ndarray:
    """Column-normalized PMNS projector packet |U_PMNS|^2 from a Hermitian pair.

    Returns the doubly-stochastic |U|^2 matrix (after column-stochastic
    normalization). Distinct from `projector_packet` above, which returns the
    raw (u_pair, |u_pair|^2) tuple without normalization; the two helpers are
    kept side by side because downstream runners import either name.
    """
    _eval_nu, u_nu = canonical_left_diagonalizer(h_nu)
    _eval_e, u_e = canonical_left_diagonalizer(h_e)
    u_pmns = u_e.conj().T @ u_nu
    packet = np.abs(u_pmns) ** 2
    return packet / np.sum(packet, axis=0, keepdims=True)


def deterministic_pairs() -> list[tuple[str, np.ndarray, np.ndarray]]:
    rng = np.random.default_rng(seed=20260525)
    pairs: list[tuple[str, np.ndarray, np.ndarray]] = []

    h_nu = np.array(
        [
            [2.6, 0.2 + 0.1j, -0.3j],
            [0.2 - 0.1j, 1.7, 0.4 + 0.2j],
            [0.3j, 0.4 - 0.2j, 1.2],
        ],
        dtype=complex,
    )
    h_e = np.array(
        [
            [1.1, -0.1j, 0.15 + 0.04j],
            [0.1j, 2.4, -0.2 + 0.05j],
            [0.15 - 0.04j, -0.2 - 0.05j, 3.0],
        ],
        dtype=complex,
    )
    pairs.append(("canonical", h_nu + 2.0 * np.eye(3), h_e + 2.0 * np.eye(3)))

    for idx in range(8):
        a = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        b = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        h1 = a @ a.conj().T + 1e-3 * np.eye(3)
        h2 = b @ b.conj().T + 1e-3 * np.eye(3)
        pairs.append((f"random_{idx}", h1, h2))
    return pairs


def part0_source_firewall() -> None:
    print("\n" + "=" * 88)
    print("PART 0: SOURCE FIREWALL")
    print("=" * 88)

    note = NOTE_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    required_note_phrases = [
        "Raw Pair-to-Projector Interface",
        "raw-interface repair",
        "does not claim carrier authority",
        "does not claim physical N1 column selection",
        "does not compute or retain eta/eta_obs diagnostics",
        "does not import dm_leptogenesis_exact_common",
        "No new repo-wide axiom is introduced",
        # 2026-05-28 audit repair: intrinsic-projector claim restricted to
        # simple spectra; note must carry the degenerate-spectrum caveat.
        "simple (non-degenerate) spectra",
        RUNNER_PATH,
    ]
    for phrase in required_note_phrases:
        check(f"source note states boundary phrase: {phrase}", phrase in note)

    forbidden_source_phrases = [
        "from " + "dm_leptogenesis_exact_common import",
        "solve_multisource_" + "flavored_transport",
        "eta_ratio_single_source_" + "flavored",
    ]
    for phrase in forbidden_source_phrases:
        check(f"runner source excludes transport helper phrase: {phrase}", phrase not in source)


def part1_unitary_and_doubly_stochastic() -> list[tuple[str, np.ndarray]]:
    print("\n" + "=" * 88)
    print("PART 1: UNITARY PAIR MATRIX AND DOUBLY STOCHASTIC PACKET")
    print("=" * 88)

    packets: list[tuple[str, np.ndarray]] = []
    max_unitary_err = 0.0
    max_row_err = 0.0
    max_col_err = 0.0
    min_entry = 1.0
    for name, h_nu, h_e in deterministic_pairs():
        u_pair, packet = projector_packet(h_nu, h_e)
        packets.append((name, packet))
        max_unitary_err = max(max_unitary_err, float(np.linalg.norm(u_pair @ u_pair.conj().T - np.eye(3))))
        max_row_err = max(max_row_err, float(np.linalg.norm(np.sum(packet, axis=1) - np.ones(3))))
        max_col_err = max(max_col_err, float(np.linalg.norm(np.sum(packet, axis=0) - np.ones(3))))
        min_entry = min(min_entry, float(np.min(packet)))

    check("U_pair is unitary on every deterministic Hermitian pair", max_unitary_err < 1e-10, f"max err={max_unitary_err:.2e}")
    check("|U_pair|^2 has row sums equal to one", max_row_err < 1e-10, f"max row err={max_row_err:.2e}")
    check("|U_pair|^2 has column sums equal to one", max_col_err < 1e-10, f"max col err={max_col_err:.2e}")
    check("|U_pair|^2 entries are non-negative", min_entry >= -1e-14, f"min entry={min_entry:.2e}")

    print("  canonical packet:")
    print(np.round(packets[0][1], 6))
    return packets


def part2_rephasing_invariance() -> None:
    print("\n" + "=" * 88)
    print("PART 2: EIGENVECTOR REPHASING INVARIANCE")
    print("=" * 88)

    rng = np.random.default_rng(seed=20260526)
    max_rephase_err = 0.0
    samples = 0
    for _name, h_nu, h_e in deterministic_pairs():
        _eval_nu, u_nu = canonical_left_diagonalizer(h_nu)
        _eval_e, u_e = canonical_left_diagonalizer(h_e)
        base = np.abs(u_e.conj().T @ u_nu) ** 2
        for _ in range(8):
            phase_nu = np.diag(np.exp(1j * rng.uniform(-np.pi, np.pi, size=3)))
            phase_e = np.diag(np.exp(1j * rng.uniform(-np.pi, np.pi, size=3)))
            phased = np.abs((u_e @ phase_e).conj().T @ (u_nu @ phase_nu)) ** 2
            max_rephase_err = max(max_rephase_err, float(np.linalg.norm(base - phased)))
            samples += 1

    check(
        "|U_pair|^2 is invariant under independent eigenvector rephasings",
        max_rephase_err < 1e-10,
        f"max err={max_rephase_err:.2e}, samples={samples}",
    )


def part2b_degenerate_spectrum_noninvariance() -> None:
    """Demonstrate that for a DEGENERATE Hermitian pair the projector is
    NOT intrinsic: a non-diagonal unitary rotation within a degenerate
    eigenspace yields a different |U_pair|^2.

    This is the 2026-05-28 audit-repair exhibit. It bounds the scope of
    the 'intrinsic to the pair' reading to SIMPLE (non-degenerate)
    spectra, where the eigenbasis is unique up to column phases.
    """
    print("\n" + "=" * 88)
    print("PART 2b: DEGENERATE-SPECTRUM NON-INVARIANCE (scope boundary)")
    print("=" * 88)

    # H_nu degenerate: eigenvalues (2, 2, 5). The 2-fold eigenspace admits
    # a continuum of orthonormal bases related by U(2) rotations.
    # Build H_nu = Q diag(2,2,5) Q^dagger for a fixed unitary Q.
    rng = np.random.default_rng(seed=20260528)
    a = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    q, _ = np.linalg.qr(a)  # random unitary Q
    d_deg = np.diag([2.0, 2.0, 5.0])
    h_nu = q @ d_deg @ q.conj().T
    h_nu = 0.5 * (h_nu + h_nu.conj().T)  # symmetrize against roundoff

    # A non-degenerate H_e to pair with.
    b = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    h_e = b @ b.conj().T + 1e-3 * np.eye(3)

    # Eigenbasis 1: the canonical diagonalizer's choice for h_nu.
    _, u_nu_1 = canonical_left_diagonalizer(h_nu)
    _, u_e = canonical_left_diagonalizer(h_e)
    p1 = np.abs(u_e.conj().T @ u_nu_1) ** 2

    # Eigenbasis 2: rotate the degenerate 2D eigenspace (columns 0,1 of
    # u_nu_1, which share eigenvalue 2) by a non-diagonal U(2) rotation.
    theta = 0.7
    rot2 = np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta),  np.cos(theta)]], dtype=complex)
    u_nu_2 = u_nu_1.copy()
    u_nu_2[:, [0, 1]] = u_nu_1[:, [0, 1]] @ rot2
    # u_nu_2 still diagonalizes h_nu (rotation within the degenerate eigenspace).
    # Validity: u_nu_2 is unitary and still diagonalizes h_nu.
    still_unitary = float(np.linalg.norm(u_nu_2 @ u_nu_2.conj().T - np.eye(3)))
    off_diag = u_nu_2.conj().T @ h_nu @ u_nu_2
    off_diag_mag = float(np.linalg.norm(off_diag - np.diag(np.diag(off_diag))))

    p2 = np.abs(u_e.conj().T @ u_nu_2) ** 2
    projector_changed = float(np.linalg.norm(p1 - p2))

    check("rotated eigenbasis is still unitary", still_unitary < 1e-10,
          f"||UU^dag - I|| = {still_unitary:.2e}")
    check("rotated eigenbasis still diagonalizes the degenerate H_nu",
          off_diag_mag < 1e-9, f"off-diag = {off_diag_mag:.2e}")
    check(
        "DEGENERATE pair: |U_pair|^2 CHANGES under eigenspace rotation "
        "(projector is NOT intrinsic for degenerate spectra)",
        projector_changed > 1e-3,
        f"||P1 - P2|| = {projector_changed:.4f} (both are valid eigenbases of the same pair)",
    )
    print(f"  ||P1 - P2|| = {projector_changed:.6f} -- nonzero confirms the")
    print("  intrinsic-projector claim is restricted to SIMPLE spectra.")


def part3_result() -> None:
    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Raw algebraic interface:")
    print("    - supplied Hermitian pair -> U_pair = U_e^dagger U_nu")
    print("    - |U_pair|^2 is doubly stochastic")
    print("    - |U_pair|^2 is invariant under eigenvector rephasings")
    print()
    print("  Carrier authority, physical N1 column selection, and eta diagnostics remain outside this repaired row.")


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS PMNS PROJECTOR RAW INTERFACE")
    print("=" * 88)

    part0_source_firewall()
    part1_unitary_and_doubly_stochastic()
    part2_rephasing_invariance()
    part2b_degenerate_spectrum_noninvariance()
    part3_result()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
