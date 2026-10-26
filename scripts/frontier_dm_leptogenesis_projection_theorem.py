#!/usr/bin/env python3
r"""Conditional positive-matrix projection identity.
Supply H>0, Y_+=sqrt(H), and U_M. Then Y_mass^dag Y_mass=U_M^dag H U_M.
Physical Yukawa/readout matching and K00=2tau normalization are additional
premises. Documentary older kernels record chosen conventions, not closure.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DM_LEPTOGENESIS_PROJECTION_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/work_history/dm/DM_LEPTOGENESIS_FULL_AXIOM_CLOSURE_NOTE_2026-04-16.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/frontier_dm_leptogenesis.py', 'scripts/frontier_dm_leptogenesis_exact_kernel_closure.py', 'scripts/frontier_dm_leptogenesis_transport_status.py']

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0

PI = np.pi
OMEGA = np.exp(2j * PI / 3.0)
UZ3 = (1.0 / np.sqrt(3.0)) * np.array(
    [
        [1.0, 1.0, 1.0],
        [1.0, OMEGA, OMEGA * OMEGA],
        [1.0, OMEGA * OMEGA, OMEGA],
    ],
    dtype=complex,
)
R = np.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0 / np.sqrt(2.0), 1.0 / np.sqrt(2.0)],
        [0.0, -1.0 / np.sqrt(2.0), 1.0 / np.sqrt(2.0)],
    ],
    dtype=complex,
)
U_HEAVY = UZ3 @ R


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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def positive_sqrt(h: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(h)
    if np.min(vals) <= 0.0:
        raise ValueError("positive_sqrt expects a positive-definite Hermitian matrix")
    return vecs @ np.diag(np.sqrt(vals)) @ vecs.conj().T


def make_positive(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    return x.conj().T @ x + 0.7 * np.eye(3)


def part1_positive_polar_section_is_the_intrinsic_right_orbit_representative() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE POSITIVE POLAR REPRESENTATIVE SATISFIES Y^DAG Y = H")
    print("=" * 88)

    max_err = 0.0
    min_eval = 1e9
    for seed in (3, 11, 19, 27):
        h = make_positive(seed)
        y = positive_sqrt(h)
        err = np.linalg.norm(y.conj().T @ y - h)
        max_err = max(max_err, err)
        min_eval = min(min_eval, float(np.min(np.linalg.eigvalsh(h))))

    check(
        "The sampled Hermitian blocks are strictly positive on the generic full-rank patch",
        min_eval > 0.0,
        f"min eigenvalue={min_eval:.6f}",
    )
    check(
        "The positive polar representative satisfies Y_+^dag Y_+ = H exactly",
        max_err < 1e-12,
        f"max reconstruction error={max_err:.2e}",
    )


def part2_the_heavy_basis_denominator_is_exactly_k00() -> None:
    print("\n" + "=" * 88)
    print("PART 2: THE HEAVY-BASIS DENOMINATOR IS EXACTLY K00")
    print("=" * 88)

    max_err = 0.0
    max_entry_err = 0.0
    for seed in (5, 13, 21, 29):
        h = make_positive(seed)
        y = positive_sqrt(h)
        y_mass = y @ U_HEAVY
        k_mass = U_HEAVY.conj().T @ h @ U_HEAVY
        err = np.linalg.norm(y_mass.conj().T @ y_mass - k_mass)
        entry_err = abs((y_mass.conj().T @ y_mass)[0, 0] - k_mass[0, 0])
        max_err = max(max_err, err)
        max_entry_err = max(max_entry_err, entry_err)

    check(
        "Right-basis rotation gives Y_mass^dag Y_mass = U_M^dag H U_M = K_mass",
        max_err < 1e-12,
        f"max matrix error={max_err:.2e}",
    )
    check(
        "The supplied matrix entry equals (K_mass)00",
        max_entry_err < 1e-12,
        f"max entry error={max_entry_err:.2e}",
    )


def part3_the_projection_identity_matches_the_existing_k00_theorem() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE PROJECTION IDENTITY MATCHES THE EXISTING K00 THEOREM")
    print("=" * 88)

    k00_note = read("docs/DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md")
    polar_note = read("docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md")

    check(
        "The K00 parent explicitly keeps physical coefficient identification as an extra premise",
        "additional physical coefficient-identification premise" in k00_note,
    )
    check(
        "The post-canonical polar theorem already records the intrinsic positive representative Y_+(H) = H^(1/2)",
        "Y_+(H)=H^(1/2)" in polar_note.replace(" ", ""),
    )
    check(
        "The supplied matrix identity does not fix physical normalization",
        "It does not identify the independent target functional" in k00_note,
        "physical readout and K00=2tau matching remain supplied assumptions",
    )


def part4_the_runner_surface_now_has_an_exact_denominator_divide() -> None:
    print("\n" + "=" * 88)
    print("PART 4: THE OLD REDUCED RUNNER AND THE REFRESHED EXACT RUNNER NOW DIFFER SHARPLY")
    print("=" * 88)

    reduced = read("scripts/frontier_dm_leptogenesis.py")
    exact_kernel = read("scripts/frontier_dm_leptogenesis_exact_kernel_closure.py")
    full_axiom = read("scripts/frontier_dm_leptogenesis_transport_status.py")
    # Stale-path: `read("docs/DM_LEPTOGENESIS_FULL_AXIOM_CLOSURE_NOTE_2026-04-16.md")`
    # — the note was relocated to
    # `docs/work_history/dm/DM_LEPTOGENESIS_FULL_AXIOM_CLOSURE_NOTE_2026-04-16.md`
    # by commit d2e754fdc / d328018df ("Restore main and add ..." / "Trim DM
    # package to science-only surface", 2026-04-16/17). Redirected the read()
    # to the new location so the K00 projection-law check still verifies the
    # historical authority surface.
    full_axiom_note = read(
        "docs/work_history/dm/DM_LEPTOGENESIS_FULL_AXIOM_CLOSURE_NOTE_2026-04-16.md"
    )

    check(
        "The old reduced runner still states (Y^dag Y)11 = y0^2 on the reduced Z3 texture benchmark",
        "(Y^dag Y)_{11} = y_0^2" in reduced,
    )
    check(
        "The refreshed exact-kernel runner now inserts the explicit /K00 denominator",
        "/ k00" in exact_kernel and "K00   = 2" in exact_kernel,
    )
    check(
        "Historical transport source records a chosen K00=2 convention, not its derivation",
        "physical denominator as K00 = 2" in full_axiom and "exact projection law `K00 = 2`" in full_axiom_note,
    )


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS PROJECTION THEOREM")
    print("=" * 88)

    part1_positive_polar_section_is_the_intrinsic_right_orbit_representative()
    part2_the_heavy_basis_denominator_is_exactly_k00()
    part3_the_projection_identity_matches_the_existing_k00_theorem()
    part4_the_runner_surface_now_has_an_exact_denominator_divide()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
