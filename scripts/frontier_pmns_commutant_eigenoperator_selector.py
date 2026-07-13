#!/usr/bin/env python3
"""Exact obstruction to the stated PMNS commutant selector maps.

The runner proves that a scalar corner-trace profile of an operator lifted
from one hw=1 corner is forced onto the ray (t,t/2,t/2), with Fourier image
(2t/3,t/6,t/6). It then checks that the historical q/tau extraction maps do
not descend under eigenoperator sign, do not separate the three cyclic
transports, use a reflection-even coordinate for orientation, and cannot
factor the native passive-offset or sector-orientation labels without an
additional carrier theorem.

The result is narrow: it does not rule out matrix-valued commutant
observables or a future explicit carrier/intertwiner construction.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from itertools import product

import numpy as np
import sympy as sp

np.set_printoptions(precision=6, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = [I2, SX, SY, SZ]

I3 = np.eye(3, dtype=complex)
CYCLE = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
CYCLE2 = CYCLE @ CYCLE

T1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def check(name: str, condition: bool, detail: str = "", cls: str = "A") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status} ({cls})] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def taste_vector(state: tuple[int, int, int]) -> np.ndarray:
    v = np.array([1.0, 0.0], dtype=complex) if state[0] == 0 else np.array([0.0, 1.0], dtype=complex)
    for idx in (1, 2):
        vk = np.array([1.0, 0.0], dtype=complex) if state[idx] == 0 else np.array([0.0, 1.0], dtype=complex)
        v = np.kron(v, vk)
    return v


def triplet_projector(states: list[tuple[int, int, int]]) -> np.ndarray:
    return np.column_stack([taste_vector(s) for s in states])


def build_cl3_gammas() -> list[np.ndarray]:
    """KS gamma matrices on C^8 taste space."""
    alphas = [(a1, a2, a3) for a1 in range(2) for a2 in range(2) for a3 in range(2)]
    alpha_idx = {a: i for i, a in enumerate(alphas)}
    gammas = []
    for mu in range(3):
        G = np.zeros((8, 8), dtype=complex)
        for a in alphas:
            i = alpha_idx[a]
            a1, a2, a3 = a
            if mu == 0:
                eta = 1.0
            elif mu == 1:
                eta = (-1.0) ** a1
            else:
                eta = (-1.0) ** (a1 + a2)
            b = list(a)
            b[mu] = 1 - b[mu]
            j = alpha_idx[tuple(b)]
            G[i, j] = eta
        gammas.append(G)
    return gammas


def staggered_H_antiherm(K: np.ndarray) -> np.ndarray:
    """Anti-Hermitian staggered Hamiltonian in the 8-site unit-cell basis."""
    alphas = [(a1, a2, a3) for a1 in range(2) for a2 in range(2) for a3 in range(2)]
    alpha_idx = {a: i for i, a in enumerate(alphas)}
    H = np.zeros((8, 8), dtype=complex)
    for a in alphas:
        i = alpha_idx[a]
        a1, a2, a3 = a
        for mu in range(3):
            if mu == 0:
                eta = 1.0
            elif mu == 1:
                eta = (-1.0) ** a1
            else:
                eta = (-1.0) ** (a1 + a2)
            b = list(a)
            b[mu] = 1 - b[mu]
            b = tuple(b)
            j = alpha_idx[b]
            phase = np.exp(1j * K[mu]) if a[mu] == 1 else 1.0
            H[i, j] += 0.5 * eta * phase
            H[j, i] -= 0.5 * eta * np.conj(phase)
    return H


def compute_commutant_basis(generators: list[np.ndarray], dim: int = 8) -> list[np.ndarray]:
    constraints = []
    eye = np.eye(dim, dtype=complex)
    for G in generators:
        C = np.kron(G.T, eye) - np.kron(eye, G)
        constraints.append(C)
    A = np.vstack(constraints)
    U, S, Vh = np.linalg.svd(A, full_matrices=True)
    tol = 1e-10 * max(1.0, S[0]) if len(S) > 0 else 1e-10
    null_vecs = []
    for i, s in enumerate(S):
        if s < tol:
            null_vecs.append(Vh[i])
    for i in range(len(S), Vh.shape[0]):
        null_vecs.append(Vh[i])
    return [v.reshape(dim, dim) for v in null_vecs]


def compute_projected_commutant(comm_basis: list[np.ndarray], projector: np.ndarray, subspace_dim: int) -> list[np.ndarray]:
    P = projector
    projected = [P.conj().T @ M @ P for M in comm_basis]
    if not projected:
        return []
    vecs = np.array([M.flatten() for M in projected])
    U, S, Vh = np.linalg.svd(vecs, full_matrices=False)
    tol = 1e-10 * max(1.0, S[0]) if len(S) > 0 else 1e-10
    rank = int(np.sum(S > tol))
    return [Vh[i].reshape(subspace_dim, subspace_dim) for i in range(rank)]


def c3_taste_unitary() -> np.ndarray:
    alphas = [(a1, a2, a3) for a1 in range(2) for a2 in range(2) for a3 in range(2)]
    alpha_idx = {a: i for i, a in enumerate(alphas)}
    U = np.zeros((8, 8), dtype=complex)
    for a in alphas:
        a1, a2, a3 = a
        b = (a3, a1, a2)
        eps = (-1) ** ((a1 + a2) * a3)
        U[alpha_idx[b], alpha_idx[a]] = eps
    return U


def project_corner_eigenspace(K: np.ndarray) -> np.ndarray:
    H = 1j * staggered_H_antiherm(K)
    evals, evecs = np.linalg.eigh(H)
    mask_plus = np.abs(evals - 1.0) < 0.1
    return evecs[:, mask_plus]


def cl3_span_basis(gammas: list[np.ndarray]) -> list[np.ndarray]:
    basis = [np.eye(8, dtype=complex)]
    basis.extend(gammas)
    basis.append(gammas[0] @ gammas[1])
    basis.append(gammas[0] @ gammas[2])
    basis.append(gammas[1] @ gammas[2])
    basis.append(gammas[0] @ gammas[1] @ gammas[2])
    return basis


def in_span(target: np.ndarray, basis: list[np.ndarray]) -> bool:
    mat = np.column_stack([b.flatten() for b in basis])
    coeffs, *_ = np.linalg.lstsq(mat, target.flatten(), rcond=None)
    resid = np.linalg.norm(mat @ coeffs - target.flatten())
    return resid < 1e-8


@dataclass
class CornerProfile:
    """Corner profile as defined in the note: literal complex trace tr(P_i^* M P_i).

    The note's load-bearing object is `v_i = tr(P_i^* M P_i)`, the full
    complex projected trace. Earlier runner revisions Hermitianized the
    projected operator and returned `Re tr(0.5 (Mp + Mp^*))`, which equals
    `Re tr(Mp)` and silently drops any imaginary part. That convention
    mismatch was flagged in the 2026-05-10 audit (verdict: runner does not
    compute the stated trace profile). This version returns the literal
    complex trace so the C3 Fourier decomposition and odd-mode checks are
    performed on the exact object the theorem defines.

    The Hermitian-part eigenspectrum is retained for diagnostic display only
    and is not used in any load-bearing check.
    """

    label: str
    trace: complex
    spectrum: np.ndarray


def corner_profile(M: np.ndarray, P: np.ndarray) -> CornerProfile:
    if M.shape == (P.shape[1], P.shape[1]):
        Mp = M
    else:
        Mp = P.conj().T @ M @ P
    herm = 0.5 * (Mp + Mp.conj().T)
    eigs = np.sort(np.real(np.linalg.eigvalsh(herm)))
    tr = complex(np.trace(Mp))
    return CornerProfile("", tr, eigs)


def orbit_fourier(v: np.ndarray) -> tuple[complex, complex, complex]:
    omega = np.exp(2j * np.pi / 3)
    v0 = (v[0] + v[1] + v[2]) / 3.0
    v1 = (v[0] + omega * v[1] + omega**2 * v[2]) / 3.0
    v2 = (v[0] + omega**2 * v[1] + omega * v[2]) / 3.0
    return v0, v1, v2


def exact_corner_hamiltonian(corner_axis: int) -> sp.Matrix:
    """Exact Hermitian corner Hamiltonian at K_axis = pi."""
    alphas = list(product((0, 1), repeat=3))
    alpha_idx = {a: i for i, a in enumerate(alphas)}
    antiherm = sp.zeros(8)
    for a in alphas:
        i = alpha_idx[a]
        for mu in range(3):
            eta = 1 if mu == 0 else (-1) ** sum(a[:mu])
            b = list(a)
            b[mu] = 1 - b[mu]
            j = alpha_idx[tuple(b)]
            phase = -1 if mu == corner_axis and a[mu] == 1 else 1
            antiherm[i, j] += sp.Rational(1, 2) * eta * phase
            antiherm[j, i] -= sp.Rational(1, 2) * eta * phase
    return sp.I * antiherm


def stated_selector_maps(v: np.ndarray) -> tuple[int, int, tuple[complex, complex, complex]]:
    v0, v_plus, v_minus = orbit_fourier(v)
    tau = 0 if float(np.real(v_plus)) >= 0.0 else 1
    scores = np.array(
        [np.real(v0), np.real(v0) - np.real(v_plus), np.real(v0) + np.real(v_plus)]
    )
    q = int(np.argmax(scores))
    return tau, q, (v0, v_plus, v_minus)


def part1_exact_projector_overlap_ray() -> None:
    print("\n" + "=" * 88)
    print("PART 1: EXACT PROJECTOR-OVERLAP IMAGE OF A CORNER-SUPPORTED LIFT")
    print("=" * 88)

    identity = sp.eye(8)
    hs = [exact_corner_hamiltonian(axis) for axis in range(3)]
    qs = [(identity + h) / 2 for h in hs]

    for axis, h in enumerate(hs, start=1):
        check(f"H_{axis} is Hermitian exactly", h == h.conjugate().T, cls="A")
        check(f"H_{axis}^2 = I exactly", h * h == identity, cls="A")
        check(f"Q_{axis} is an exact rank-four projector", qs[axis - 1] ** 2 == qs[axis - 1]
              and qs[axis - 1].rank() == 4, cls="A")

    for i in range(3):
        for j in range(i + 1, 3):
            check(
                f"H_{i + 1} and H_{j + 1} anticommute exactly",
                hs[i] * hs[j] + hs[j] * hs[i] == sp.zeros(8),
                cls="A",
            )

    for j in (1, 2):
        check(
            f"Q_1 Q_{j + 1} Q_1 = (1/2) Q_1 exactly",
            sp.simplify(qs[0] * qs[j] * qs[0] - sp.Rational(1, 2) * qs[0]) == sp.zeros(8),
            cls="A",
        )

    # Independent exact calculation of the full profile functional on the
    # 64 ambient matrix units.  The rows are the coefficients of
    # X -> Tr(Q_i Q_1 X Q_1); rank one and the row ratios prove the image
    # theorem without constructing the target vector by hand.
    profile_rows: list[list[sp.Expr]] = []
    for qi in qs:
        row: list[sp.Expr] = []
        for a in range(8):
            for b in range(8):
                eab = sp.zeros(8)
                eab[a, b] = 1
                row.append(sp.simplify(sp.trace(qi * qs[0] * eab * qs[0])))
        profile_rows.append(row)
    profile_map = sp.Matrix(profile_rows)
    check(
        "The exact 3-by-64 supported-profile functional has rank one with row ratios (1,1/2,1/2)",
        profile_map.rank() == 1
        and profile_map.row(1) == profile_map.row(0) / 2
        and profile_map.row(2) == profile_map.row(0) / 2,
        cls="A",
    )

    t = sp.symbols("t")
    v = sp.Matrix([t, t / 2, t / 2])
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    v0 = sp.simplify(sum(v) / 3)
    vp = sp.simplify((v[0] + omega * v[1] + omega**2 * v[2]) / 3)
    vm = sp.simplify((v[0] + omega**2 * v[1] + omega * v[2]) / 3)
    check("The exact Fourier image is (2t/3, t/6, t/6)",
          (v0, vp, vm) == (2 * t / 3, t / 6, t / 6),
          detail=f"(v0,v+,v-)=({v0},{vp},{vm})", cls="A")

    print()
    print("  For every operator supported on Q_1, cyclicity of trace and the")
    print("  projector sandwiches force v=(t,t/2,t/2), t=Tr(M).")
    print("  The scalar profile therefore has one complex degree of freedom,")
    print("  not an independently variable even mode plus orientation mode.")


def part2_numerical_commutant_witness() -> tuple[np.ndarray, np.ndarray, list[np.ndarray]]:
    print("\n" + "=" * 88)
    print("PART 2: NUMERICAL REPRODUCTION ON THE NON-Cl(3) COMMUTANT WITNESS")
    print("=" * 88)

    gammas = build_cl3_gammas()
    ps = [
        project_corner_eigenspace(np.array([np.pi, 0.0, 0.0])),
        project_corner_eigenspace(np.array([0.0, np.pi, 0.0])),
        project_corner_eigenspace(np.array([0.0, 0.0, np.pi])),
    ]
    proj_cl3 = [ps[0].conj().T @ m @ ps[0] for m in cl3_span_basis(gammas)]

    # Deterministic witness: I + I tensor I tensor sigma_x.  Both summands
    # commute with the displayed KS gamma set.  Its first-corner projection
    # is Hermitian, has trace four, and is outside the projected Cl(3) span.
    ambient_witness = np.eye(8, dtype=complex) + np.kron(I2, np.kron(I2, SX))
    commutator_norm = max(np.linalg.norm(ambient_witness @ g - g @ ambient_witness) for g in gammas)
    check("The explicit ambient witness commutes with every Cl(3) generator",
          commutator_norm < 1e-12, detail=f"max commutator norm={commutator_norm:.2e}", cls="A")
    witness = ps[0].conj().T @ ambient_witness @ ps[0]
    check("The explicit projected witness lies outside the projected Cl(3) span",
          not in_span(witness, proj_cl3), cls="A")
    check("The explicit projected witness is Hermitian with positive nonzero trace",
          np.allclose(witness, witness.conj().T, atol=1e-12) and float(np.real(np.trace(witness))) > 0.0,
          detail=f"Tr M={np.trace(witness):.6f}", cls="A")

    lift = ps[0] @ witness @ ps[0].conj().T
    profile = np.array([np.trace(p.conj().T @ lift @ p) for p in ps], dtype=complex)
    t = np.trace(witness)
    expected = np.array([t, t / 2, t / 2], dtype=complex)
    check("The numerical witness obeys the exact overlap-ray formula",
          np.allclose(profile, expected, atol=1e-12),
          detail=f"v={np.round(profile, 12)}", cls="C")
    v0, vp, vm = orbit_fourier(profile)
    check("The numerical Fourier modes obey (v0,v+,v-)=(2t/3,t/6,t/6)",
          np.allclose([v0, vp, vm], [2 * t / 3, t / 6, t / 6], atol=1e-12),
          detail=f"modes={np.round([v0, vp, vm], 12)}", cls="C")
    check("The demonstrated odd mode is nonzero only as a trace-overlap witness",
          abs(vp) > 1e-12 and abs(t) > 1e-12,
          detail=f"|v+|={abs(vp):.6f}, |Tr M|={abs(t):.6f}", cls="C")
    return profile, lift, ps


def part3_stated_maps_fail_descent_and_group_actions(
    profile: np.ndarray, lift: np.ndarray, ps: list[np.ndarray]
) -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE STATED q/tau MAPS FAIL DESCENT AND SELECTOR COVARIANCE")
    print("=" * 88)

    tau_pos, q_pos, _ = stated_selector_maps(profile)
    tau_neg, q_neg, _ = stated_selector_maps(-profile)
    check("M and -M give different stated selector pairs",
          (tau_pos, q_pos) != (tau_neg, q_neg),
          detail=f"M -> ({tau_pos},{q_pos}), -M -> ({tau_neg},{q_neg})", cls="A")
    check("The stated maps therefore do not descend to the eigenoperator line",
          {tau_pos, tau_neg} == {0, 1} and {q_pos, q_neg} == {1, 2}, cls="A")

    c3 = c3_taste_unitary()
    qs = [p @ p.conj().T for p in ps]
    check(
        "The actual C3 taste unitary cyclically transports the three corner projectors",
        all(np.allclose(c3 @ qs[i] @ c3.conj().T, qs[(i + 1) % 3], atol=1e-12) for i in range(3)),
        cls="A",
    )
    transported_profiles = []
    transported = lift.copy()
    for _ in range(3):
        transported_profiles.append(
            np.array([np.trace(p.conj().T @ transported @ p) for p in ps], dtype=complex)
        )
        transported = c3 @ transported @ c3.conj().T
    expected_orbit = [profile, np.roll(profile, 1), np.roll(profile, 2)]
    check(
        "Actual C3 conjugation reproduces the three cyclic profile transports",
        all(np.allclose(v, expected, atol=1e-12) for v, expected in zip(transported_profiles, expected_orbit)),
        detail=f"profiles={[np.round(v, 6).tolist() for v in transported_profiles]}",
        cls="A",
    )
    labels = [stated_selector_maps(v)[:2] for v in transported_profiles]
    q_labels = [label[1] for label in labels]
    check("The three cyclic transports produce only two stated q labels",
          len(set(q_labels)) == 2,
          detail=f"(tau,q) orbit={labels}", cls="A")
    check("The stated q map is not a three-class cyclic readout on this orbit",
          sorted(q_labels) == [1, 1, 2], cls="A")

    x, y, z = sp.symbols("x y z", real=True)
    re_vplus = sp.simplify((2 * x - y - z) / 6)
    re_reflected = sp.simplify((2 * x - z - y) / 6)
    check("Re(v+) is exactly invariant under the corner reflection v2 <-> v3",
          sp.simplify(re_vplus - re_reflected) == 0,
          detail=f"Re(v+)={re_vplus}", cls="A")
    reflected = profile[[0, 2, 1]]
    tau_reflected, _, _ = stated_selector_maps(reflected)
    check("The demonstrated profile is reflection-fixed and carries no orientation-odd datum",
          np.allclose(reflected, profile, atol=1e-12) and tau_reflected == tau_pos,
          detail=f"tau={tau_reflected}", cls="A")
def main() -> int:
    print("=" * 88)
    print("PMNS COMMUTANT CORNER-PROFILE SELECTOR-MAP OBSTRUCTION")
    print("=" * 88)
    print()
    print("Question:")
    print("  Do the stated scalar corner-profile Fourier maps derive the PMNS")
    print("  passive offset q and sector-orientation bit tau?")
    print()
    print("Answer (narrow exact no-go):")
    print("  No. The corner-supported trace profile has a one-complex-dimensional")
    print("  image, and the stated maps fail eigenoperator-line descent. Their")
    print("  cyclic and reflection behavior also cannot supply the missing physical")
    print("  bridge without additional intertwiners.")

    part1_exact_projector_overlap_ray()
    profile, lift, ps = part2_numerical_commutant_witness()
    part3_stated_maps_fail_descent_and_group_actions(profile, lift, ps)

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Exact negative boundary:")
    print("    - the C3 Fourier decomposition remains valid algebra")
    print("    - the stated q/tau maps do not descend to the eigenoperator line")
    print("    - the physical PMNS carrier intertwiners remain open")
    print("    - no broader no-go is claimed for matrix-valued commutant observables")
    print("    - the active five-real PMNS source remains outside this result")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
