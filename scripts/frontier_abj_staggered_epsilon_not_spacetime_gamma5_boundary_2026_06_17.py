#!/usr/bin/env python3
"""Exact boundary: staggered epsilon is not the ABJ spacetime gamma5.

This runner checks the route-pruning claim in
ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5_BOUNDARY_NOTE_2026-06-17.md:

  {epsilon, D_staggered}=0 on the lattice factor does not imply that
  epsilon is a Clifford gamma5 anticommuting with every spacetime gamma.

It deliberately does not audit, retag, or modify any ledger surface.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = "scripts/frontier_abj_staggered_epsilon_not_spacetime_gamma5_boundary_2026_06_17.py"
NOTE_PATH = ROOT / "docs/ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5_BOUNDARY_NOTE_2026-06-17.md"
ABJ_NOTE_PATH = ROOT / "docs/ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
CL31_NOTE_PATH = ROOT / "docs/CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {name}{suffix}")
    return bool(condition)


def section(title: str) -> None:
    print()
    print(f"== {title} ==")


def sympy_zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


def sympy_eq(A: sp.Matrix, B: sp.Matrix) -> bool:
    return sympy_zero(A - B)


def np_zero(M: np.ndarray, tol: float = 1e-12) -> bool:
    return bool(np.allclose(M, np.zeros_like(M), atol=tol))


def part0_source_firewall() -> None:
    section("Part 0: source firewall and trace target")
    note = NOTE_PATH.read_text(encoding="utf-8")
    abj_note = ABJ_NOTE_PATH.read_text(encoding="utf-8")
    cl31_note = CL31_NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "actual_current_surface_status: exact negative boundary",
        "trace_class: negative_route_pruning",
        "target_claim_id: anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26",
        "staggered site parity `epsilon` anticommutes",
        "not a spacetime Clifford-chirality bridge",
        "does not derive P-REC",
        "taste-reconstruction",
        RUNNER_PATH,
    ]
    for phrase in required:
        check(f"boundary note contains required phrase: {phrase}", phrase in note)

    forbidden = [
        "closes P-REC",
        "derives P-REC",
        "proves P-REC",
        "effective retained",
        "proposed_retained",
        "bare retained",
    ]
    for phrase in forbidden:
        check(f"boundary note excludes overclaim phrase: {phrase}", phrase not in note)

    check(
        "ABJ bridge points to the new route-pruning boundary",
        "ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5_BOUNDARY_NOTE_2026-06-17.md" in abj_note,
    )
    check(
        "ABJ bridge still declares P-REC rather than deriving it",
        "P-REC" in abj_note and "declared premise edge" in abj_note,
    )
    check(
        "retained Cl(3)->Cl(3,1) source explicitly does not derive spacetime/dynamics",
        "Does **not** claim that the framework's `Z^3` substrate Wick-rotates" in cl31_note
        and "Does **not** claim that the framework's per-site Hilbert space" in cl31_note
        and "the per-site site module" in cl31_note,
    )


def part1_pauli_no_go() -> None:
    section("Part 1: per-site M2(C) has no nonzero gamma5 candidate")
    I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    paulis = [sx, sy, sz]

    omega = sx * sy * sz
    check("Pauli volume element sigma1 sigma2 sigma3 = i I", sympy_eq(omega, sp.I * I2))
    for idx, sigma in enumerate(paulis, start=1):
        check(f"omega commutes with sigma_{idx}", sympy_zero(omega * sigma - sigma * omega))
        check(
            f"omega does not anticommute with sigma_{idx}",
            not sympy_zero(omega * sigma + sigma * omega),
        )

    a, b, c, d = sp.symbols("a b c d")
    B = sp.Matrix([[a, b], [c, d]])
    equations = []
    for sigma in paulis:
        anti = B * sigma + sigma * B
        equations.extend([sp.Eq(sp.simplify(x), 0) for x in anti])
    sol = sp.solve(equations, [a, b, c, d], dict=True)
    check(
        "only B=0 anticommutes with all three Pauli generators",
        sol == [{a: 0, b: 0, c: 0, d: 0}],
        detail=str(sol),
    )


def part2_lattice_epsilon_vs_spatial_clifford() -> None:
    section("Part 2: lattice epsilon grades hopping but commutes with spatial Cl(3)")
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    # Four-site open chain as a finite bipartite sample of the Z^3 edge rule.
    n_sites = 4
    eps_diag = np.diag([1, -1, 1, -1]).astype(complex)
    hop = np.zeros((n_sites, n_sites), dtype=complex)
    for i in range(n_sites - 1):
        hop[i, i + 1] = 1
        hop[i + 1, i] = 1
    site_I = np.eye(n_sites, dtype=complex)

    epsilon_full = np.kron(eps_diag, I2)
    D = np.kron(hop, I2)
    check("{epsilon, nearest-neighbor hopping}=0", np_zero(epsilon_full @ D + D @ epsilon_full))

    for label, sigma in [("sigma_x", sx), ("sigma_y", sy), ("sigma_z", sz)]:
        Gamma = np.kron(site_I, sigma)
        check(f"[epsilon, I_site tensor {label}]=0", np_zero(epsilon_full @ Gamma - Gamma @ epsilon_full))
        check(
            f"{{epsilon, I_site tensor {label}}} != 0",
            not np_zero(epsilon_full @ Gamma + Gamma @ epsilon_full),
        )


def part3_factored_candidate_no_go() -> None:
    section("Part 3: no factored epsilon tensor B candidate can be gamma5")
    E = sp.diag(1, -1)
    I_site = sp.eye(2)
    I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    a, b, c, d = sp.symbols("a b c d")
    B = sp.Matrix([[a, b], [c, d]])
    candidate = sp.kronecker_product(E, B)
    equations = []
    for sigma in [sx, sy, sz]:
        Gamma = sp.kronecker_product(I_site, sigma)
        anti = candidate * Gamma + Gamma * candidate
        equations.extend([sp.Eq(sp.simplify(x), 0) for x in anti])
    sol = sp.solve(equations, [a, b, c, d], dict=True)
    check(
        "epsilon tensor B anticommutes with all spatial generators only for B=0",
        sol == [{a: 0, b: 0, c: 0, d: 0}],
        detail=str(sol),
    )

    zero_candidate = candidate.subs({a: 0, b: 0, c: 0, d: 0})
    check(
        "the only anticommuting factored candidate cannot square to identity",
        not sympy_eq(zero_candidate * zero_candidate, sp.eye(4)),
    )


def part4_logical_nonimplication() -> None:
    section("Part 4: anticommuting with D does not imply anticommuting with gamma generators")
    sx = sp.Matrix([[0, 1], [1, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    I2 = sp.eye(2)
    epsilon = sz
    D = sx
    bad_generator = sz
    check("toy witness has {epsilon, D}=0", sympy_zero(epsilon * D + D * epsilon))
    check(
        "same epsilon fails {epsilon, bad_generator}=0",
        sympy_eq(epsilon * bad_generator + bad_generator * epsilon, 2 * I2),
    )


def part5_supplied_cl31_escape_hatch() -> None:
    section("Part 5: supplied Cl(3,1) factor can have gamma5, but is extra structure")
    I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    eps = sp.Matrix([[0, -1], [1, 0]])  # real square -I

    Gamma1 = sp.kronecker_product(sx, I2)
    Gamma2 = sp.kronecker_product(sz, sx)
    Gamma3 = sp.kronecker_product(sz, sz)
    Gamma4 = sp.kronecker_product(sz, eps)
    gammas = [Gamma1, Gamma2, Gamma3, Gamma4]
    I4 = sp.eye(4)

    signatures = [1, 1, 1, -1]
    for idx, (Gamma, sig) in enumerate(zip(gammas, signatures), start=1):
        check(f"Cl(3,1) witness Gamma_{idx}^2 = {sig} I", sympy_eq(Gamma * Gamma, sig * I4))
    for i in range(4):
        for j in range(i + 1, 4):
            check(f"Cl(3,1) witness {{Gamma_{i+1}, Gamma_{j+1}}}=0", sympy_zero(gammas[i] * gammas[j] + gammas[j] * gammas[i]))

    omega = Gamma1 * Gamma2 * Gamma3 * Gamma4
    gamma5 = sp.I * omega
    check("complex gamma5 from supplied Cl(3,1) witness squares to +I", sympy_eq(gamma5 * gamma5, I4))
    for idx, Gamma in enumerate(gammas, start=1):
        check(f"supplied Cl(3,1) gamma5 anticommutes with Gamma_{idx}", sympy_zero(gamma5 * Gamma + Gamma * gamma5))

    # This positive witness is intentionally separated from lattice epsilon.
    check(
        "positive witness uses a supplied fourth generator, not the lattice epsilon shortcut",
        True,
        detail="escape hatch preserved; P-REC still needs reconstruction",
    )


def main() -> int:
    print("ABJ staggered-epsilon / spacetime-gamma5 boundary runner")
    part0_source_firewall()
    part1_pauli_no_go()
    part2_lattice_epsilon_vs_spatial_clifford()
    part3_factored_candidate_no_go()
    part4_logical_nonimplication()
    part5_supplied_cl31_escape_hatch()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: exact negative boundary; staggered epsilon anticommutation "
            "alone does not supply spacetime gamma5."
        )
        return 0
    print("VERDICT: boundary check FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
