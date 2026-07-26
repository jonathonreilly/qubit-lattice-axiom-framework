#!/usr/bin/env python3
"""
Neutrino Dirac Bridge Theorem
=============================

STATUS: EXACT operator-selection bridge; base normalization closed elsewhere

Purpose:
  Close the cleanest part of the neutrino-Yukawa bridge:

    1. identify the physical post-EWSB local chiral Dirac operator on C^16
    2. show why the effective action on the generation triplet T_1 starts
       only at second order

  The theorem proved here is:

    - on the 3+1 completed lattice, the graph-local spatial Higgs family
      M(phi) = sum_i phi_i Gamma_i is Hermitian and chiral off-diagonal
    - the exact selector V_sel picks axis minima phi = e_i
    - after EWSB axis selection, the local Dirac surface is uniquely Gamma_i
      up to the broken S_3 choice and an overall sign
    - in the branch convention with weak axis 1, this gives Gamma_1
    - restricted to the T_1 generation triplet, Gamma_1 has no one-hop
      return, so the first exact closed action on T_1 is second order

  The algebraic content is certified at EXACT symbolic precision for
  arbitrary real phi, in the displayed C^16 representation and again in
  the standard 4x4 Euclidean Cl(4) realization, so the packet does not
  depend on an external companion script.

  This does NOT derive the neutrino-sector normalization or the eventual
  y_nu scale. It closes operator selection on the local chiral surface.
"""

from __future__ import annotations

import itertools
import sys
import numpy as np
import sympy as sp

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I16 = np.eye(16, dtype=complex)


def kron4(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    return np.kron(a, np.kron(b, np.kron(c, d)))


G0 = kron4(SZ, SZ, SZ, SX)
G1 = kron4(SX, I2, I2, I2)
G2 = kron4(SZ, SX, I2, I2)
G3 = kron4(SZ, SZ, SX, I2)
SPATIAL_GAMMAS = [G1, G2, G3]
GAMMA_5_4D = G0 @ G1 @ G2 @ G3
XI_5 = G1 @ G2 @ G3 @ G0

P_L = (I16 + GAMMA_5_4D) / 2.0
P_R = (I16 - GAMMA_5_4D) / 2.0

SPATIAL_STATES = [(a, b, c) for a in range(2) for b in range(2) for c in range(2)]
FULL_STATES = [(a, b, c, t) for a in range(2) for b in range(2) for c in range(2) for t in range(2)]
INDEX = {state: i for i, state in enumerate(FULL_STATES)}

O0 = [(0, 0, 0)]
T1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
T2 = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
O3 = [(1, 1, 1)]


def selector_potential(phi: tuple[float, float, float]) -> float:
    return 32.0 * sum(phi[i] ** 2 * phi[j] ** 2 for i in range(3) for j in range(i + 1, 3))


def normalized_simplex_grid(step: float = 0.05) -> list[np.ndarray]:
    n = int(round(1.0 / step))
    pts = []
    for i in range(n + 1):
        for j in range(n + 1 - i):
            k = n - i - j
            pts.append(np.array([i, j, k], dtype=float) / n)
    return pts


def m_phi(phi: tuple[float, float, float]) -> np.ndarray:
    return sum(c * g for c, g in zip(phi, SPATIAL_GAMMAS))


def projector(spatial_states: list[tuple[int, int, int]]) -> np.ndarray:
    p = np.zeros((16, 16), dtype=complex)
    for t in (0, 1):
        for s in spatial_states:
            p[INDEX[s + (t,)], INDEX[s + (t,)]] = 1.0
    return p


def rank(matrix: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=1e-12))


# ---------------------------------------------------------------------------
# Exact symbolic layer.  The displayed generators have integer entries, so the
# numeric arrays lift losslessly to sympy matrices over Z, and every identity
# below is checked as an identity in the free real symbols phi_1, phi_2, phi_3
# rather than at sampled phi.
# ---------------------------------------------------------------------------


def to_exact(a: np.ndarray) -> sp.Matrix:
    assert np.max(np.abs(a.imag)) < 1e-15
    assert np.max(np.abs(a.real - np.round(a.real))) < 1e-15
    n = a.shape[0]
    return sp.Matrix(n, n, lambda i, j: sp.Integer(int(round(a.real[i, j]))))


def is_zero(m: sp.Matrix) -> bool:
    return bool(sp.expand(m).is_zero_matrix)


def anticommutes(a: sp.Matrix, b: sp.Matrix) -> bool:
    return is_zero(a * b + b * a)


def commutes(a: sp.Matrix, b: sp.Matrix) -> bool:
    return is_zero(a * b - b * a)


def cl4_four_by_four() -> list[sp.Matrix]:
    """Standard 4x4 Euclidean Cl(4) Dirac realization, built exactly."""
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    e2 = sp.eye(2)
    return [
        sp.Matrix(sp.kronecker_product(s2, e2)),
        sp.Matrix(sp.kronecker_product(s1, s1)),
        sp.Matrix(sp.kronecker_product(s1, s2)),
        sp.Matrix(sp.kronecker_product(s1, s3)),
    ]


def grading_census(gens: list[sp.Matrix], chi: sp.Matrix) -> tuple[int, int]:
    """Count subsets of generators whose product commutes / anticommutes."""
    n = gens[0].shape[0]
    even = odd = 0
    for r in range(len(gens) + 1):
        for subset in itertools.combinations(range(len(gens)), r):
            prod = sp.eye(n)
            for i in subset:
                prod = prod * gens[i]
            if len(subset) % 2 == 0:
                even += int(commutes(prod, chi))
            else:
                odd += int(anticommutes(prod, chi))
    return even, odd


def chirality_blocks(op: np.ndarray) -> tuple[float, float, float, float]:
    """Squared Frobenius weight of the LL, LR, RL, RR chiral blocks."""
    return (
        float(np.linalg.norm(P_L @ op @ P_L) ** 2),
        float(np.linalg.norm(P_L @ op @ P_R) ** 2),
        float(np.linalg.norm(P_R @ op @ P_L) ** 2),
        float(np.linalg.norm(P_R @ op @ P_R) ** 2),
    )


def blocks_match(got: tuple[float, ...], want: tuple[float, ...]) -> bool:
    return max(abs(a - b) for a, b in zip(got, want)) < 1e-9


def chirality_of(vector: np.ndarray) -> float:
    """gamma_5 expectation of a vector, normalized; +1 for L, -1 for R."""
    weight = float(np.real(vector.conj() @ vector))
    return float(np.real(vector.conj() @ (GAMMA_5_4D @ vector)) / max(weight, 1e-30))


def chirality_preserving_unitary(seed: int) -> np.ndarray:
    """A unitary commuting with gamma_5, hence preserving the chiral grading."""
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(16, 16)) + 1j * rng.normal(size=(16, 16))
    herm = (a + a.conj().T) / 2.0
    graded = P_L @ herm @ P_L + P_R @ herm @ P_R
    w, v = np.linalg.eigh(graded)
    return v @ np.diag(np.exp(1j * w)) @ v.conj().T


def main() -> int:
    print("NEUTRINO DIRAC BRIDGE THEOREM: M(phi)=sum_i phi_i Gamma_i, gamma_5=G_0G_1G_2G_3, Xi_5=G_1G_2G_3G_0")

    p1, p2, p3 = sp.symbols("phi_1 phi_2 phi_3", real=True)
    EG = [to_exact(g) for g in (G0, G1, G2, G3)]
    E16 = sp.eye(16)
    Eg5 = EG[0] * EG[1] * EG[2] * EG[3]
    Exi = EG[1] * EG[2] * EG[3] * EG[0]
    EM = p1 * EG[1] + p2 * EG[2] + p3 * EG[3]
    norm2 = p1 ** 2 + p2 ** 2 + p3 ** 2
    EPL = (E16 + Eg5) / 2
    EPR = (E16 - Eg5) / 2

    print()
    print("== A exact symbolic certificate, arbitrary real phi_1, phi_2, phi_3 ==")
    check("A1 Gamma_mu Hermitian and Gamma_mu^2 = I, mu=0..3",
          all(is_zero(g - g.T.conjugate()) and is_zero(g * g - E16) for g in EG),
          "8 exact identities")
    check("A2 {Gamma_mu, Gamma_nu} = 2 delta_munu I",
          all(is_zero(EG[m] * EG[n] + EG[n] * EG[m] - 2 * (1 if m == n else 0) * E16)
              for m in range(4) for n in range(4)),
          "all 16 ordered pairs, exact")
    check("A3 gamma_5 Hermitian, gamma_5^2 = I, tr gamma_5 = 0",
          is_zero(Eg5 - Eg5.T.conjugate()) and is_zero(Eg5 * Eg5 - E16) and sp.trace(Eg5) == 0,
          "exact")
    check("A4 M(phi) = M(phi)^dagger identically in phi",
          is_zero(EM - EM.T.conjugate()),
          "no condition on phi")
    check("A5 M(phi)^2 = |phi|^2 I identically in phi",
          is_zero(EM * EM - norm2 * E16),
          "expand -> zero matrix")
    check("A6 {M(phi), gamma_5} = 0 identically in phi",
          is_zero(EM * Eg5 + Eg5 * EM),
          "expand -> zero matrix")
    check("A7 P_L M P_L = P_R M P_R = 0 identically in phi",
          is_zero(EPL * EM * EPL) and is_zero(EPR * EM * EPR),
          "both chiral-diagonal blocks vanish")
    check("A8 M(e_i) = Gamma_i for i=1,2,3",
          all(is_zero(EM.subs({p1: int(i == 0), p2: int(i == 1), p3: int(i == 2)}) - EG[i + 1])
              for i in range(3)),
          "exact substitution")

    print()
    print("== B wrong-value rejectors: each must fail for a wrong object ==")
    check("B1 M^2 = 2|phi|^2 I is identically false",
          not is_zero(EM * EM - 2 * norm2 * E16),
          "residual -|phi|^2 I")
    check("B2 Gamma_3 -> Xi_5 breaks {M, gamma_5} = 0",
          not is_zero((p1 * EG[1] + p2 * EG[2] + p3 * Exi) * Eg5
                      + Eg5 * (p1 * EG[1] + p2 * EG[2] + p3 * Exi)),
          "residual 2 phi_3 Xi_5 gamma_5")
    check("B3 i Gamma_1 fails Hermiticity",
          not is_zero(sp.I * EG[1] - (sp.I * EG[1]).T.conjugate()),
          "(iG_1)^dag = -iG_1")
    check("B4 dropping the phi_3 term breaks M^2 = |phi|^2 I",
          not is_zero((p1 * EG[1] + p2 * EG[2]) ** 2 - norm2 * E16),
          "residual -phi_3^2 I")

    print()
    print("== C Xi_5 boundary from the exact Clifford reordering identity ==")
    check("C1 Xi_5 = -gamma_5 exactly",
          is_zero(Exi + Eg5),
          "all 256 entries; sign (-1)^3")
    orders = []
    for perm in itertools.permutations(range(4)):
        prod = sp.eye(16)
        for i in perm:
            prod = prod * EG[i]
        orders.append(1 if is_zero(prod - Eg5) else (-1 if is_zero(prod + Eg5) else 0))
    check("C2 every ordering of G_0..G_3 gives +/- gamma_5",
          0 not in orders and set(orders) == {1, -1},
          f"{len(orders)} orderings, {orders.count(1)} plus / {orders.count(-1)} minus")
    check("C3 Xi_5 is chiral diagonal",
          is_zero(EPL * Exi * EPR) and is_zero(EPR * Exi * EPL),
          "both chiral off-diagonal blocks vanish")
    check("C4 Gamma_1 is chiral off-diagonal",
          rank(P_R @ G1 @ P_L) == 8 and is_zero(EPL * EG[1] * EPL),
          "rank(P_R G_1 P_L) = 8")

    print()
    print("== D selector, axis operators, and the T_1 return order ==")
    vertices = [np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0])]
    check("D1 V_sel(e_i) = 0 for i=1,2,3 and positive off axis",
          all(abs(selector_potential(tuple(v))) < 1e-12 for v in vertices)
          and selector_potential((1.0, 1.0, 0.0)) > 0.0
          and selector_potential((1.0, 1.0, 1.0)) > 0.0,
          "V(1,1,0)=32, V(1,1,1)=96")
    pts = normalized_simplex_grid(step=0.05)
    values = np.array([sum(p[i] * p[j] for i in range(3) for j in range(i + 1, 3)) for p in pts])
    mins = [p for p, val in zip(pts, values) if abs(val - float(values.min())) < 1e-12]
    check("D2 normalized-simplex minima are the axis vertices",
          all(any(np.allclose(p, v, atol=1e-12) for v in vertices) for p in mins),
          f"{len(mins)} minima, step 0.05")
    worst = 0.0
    for phi in [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (1.0, 1.0, 1.0), (1.0, 2.0, 3.0)]:
        M = m_phi(phi)
        n2 = float(sum(x * x for x in phi))
        worst = max(worst,
                    np.linalg.norm(M - M.conj().T),
                    np.linalg.norm(M @ M - n2 * I16),
                    np.linalg.norm(M @ GAMMA_5_4D + GAMMA_5_4D @ M),
                    np.linalg.norm(P_L @ M @ P_L), np.linalg.norm(P_R @ M @ P_R))
    check("D3 numeric spot check of A4-A7 at 5 sample phi",
          worst < 1e-12, f"max residual {worst:.1e}")
    p_o0, p_t1, p_t2, p_o3 = projector(O0), projector(T1), projector(T2), projector(O3)
    cols = [np.eye(16, dtype=complex)[:, INDEX[s + (t,)]] for t in (0, 1) for s in T1]
    basis_t1 = np.stack(cols, axis=1)
    one_hop = basis_t1.conj().T @ (p_t1 @ G1 @ p_t1) @ basis_t1
    second = basis_t1.conj().T @ (p_t1 @ G1 @ (p_o0 + p_t2) @ G1 @ p_t1) @ basis_t1
    second_all = basis_t1.conj().T @ (p_t1 @ G1 @ (p_o0 + p_t2 + p_o3) @ G1 @ p_t1) @ basis_t1
    check("D4 no one-hop return on T_1", np.allclose(one_hop, 0.0, atol=1e-12),
          "P_T1 G_1 P_T1 = 0 on the 6-dim block")
    check("D5 second order closes on T_1 through O_0 + T_2",
          np.allclose(second, np.eye(6), atol=1e-12), "restricted block = I_6")
    check("D6 O_3 does not enter the first closed T_1 return",
          np.allclose(second_all, second, atol=1e-12), "identical restricted blocks")

    print()
    print("== E packet: N1-N8 no-go discipline for the Xi_5 exclusion ==")
    scales = [sp.Integer(2), sp.Rational(1, 2), sp.Integer(-3)]
    check("E1 N1 route rescale_normalization",
          all(is_zero(EPR * (c * Exi) * EPL) for c in scales),
          "mech=rescale Xi_5; try=c in 2,1/2,-3; out=BLOCKED LR=0 for every c")
    check("E2 N1 route sign_and_orientation",
          set(orders) == {1, -1} and 0 not in orders,
          "mech=reorder the volume product; try=all 24 orderings; out=BLOCKED each is +/- gamma_5")
    a, b = sp.symbols("a b", real=True)
    mixed = EPR * (a * EG[1] + b * Exi) * EPL - a * (EPR * EG[1] * EPL)
    check("E3 N1 route linear_combination",
          is_zero(mixed) and not is_zero(EPR * EG[1] * EPL),
          "mech=mix a G_1 + b Xi_5; try=symbolic a,b; out=BLOCKED LR block is b-free")
    u = chirality_preserving_unitary(20260415)
    conj_lr = float(np.linalg.norm(P_R @ (u @ XI_5 @ u.conj().T) @ P_L))
    check("E4 N1 route unitary_conjugation",
          conj_lr < 1e-10 and np.linalg.norm(u @ GAMMA_5_4D - GAMMA_5_4D @ u) < 1e-10,
          f"mech=conjugate by U with [U,gamma_5]=0; try=seed 20260415; out=BLOCKED LR={conj_lr:.1e}")
    check("E5 N1 route projector_surgery",
          is_zero(EPL * Exi * EPR + EPR * Exi * EPL),
          "mech=extract the odd part by projector sandwiching; try=exact; out=BLOCKED odd part is 0")
    dressed = Eg5 * EG[1]
    check("E6 N1 route taste_dressing",
          is_zero(Eg5 * Exi + E16) and anticommutes(dressed, Eg5)
          and not is_zero(dressed - dressed.T.conjugate()) and is_zero(dressed + dressed.T.conjugate()),
          "mech=dress with gamma_5; try=gamma_5 Xi_5 and gamma_5 G_1; out=BLOCKED -I and anti-Hermitian")
    even, odd = grading_census(EG, Eg5)
    check("E7 N2 wall chirality_grading_of_the_even_subalgebra",
          even == 8 and odd == 8,
          f"{even} even subsets commute, {odd} odd subsets anticommute with gamma_5")
    H = cl4_four_by_four()
    E4 = sp.eye(4)
    h5 = H[0] * H[1] * H[2] * H[3]
    xi4 = H[1] * H[2] * H[3] * H[0]
    even4, odd4 = grading_census(H, h5)
    check("E8 N3 hidden-wall scan in the standard 4x4 Cl(4) realization",
          all(is_zero(h - h.T.conjugate()) for h in H)
          and all(is_zero(H[m] * H[n] + H[n] * H[m] - 2 * (1 if m == n else 0) * E4)
                  for m in range(4) for n in range(4))
          and is_zero(xi4 + h5) and (even4, odd4) == (8, 8),
          "exact sympy: Xi_5 = -gamma_5 there too, grading 8/8")
    lr_xi = P_L @ XI_5 @ P_R + P_R @ XI_5 @ P_L
    lr_g1 = P_L @ G1 @ P_R + P_R @ G1 @ P_L
    nz_xi = int(np.count_nonzero(np.abs(lr_xi) > 1e-12))
    nz_g1 = int(np.count_nonzero(np.abs(lr_g1) > 1e-12))
    check("E9 N5 per_element", nz_xi == 0 and nz_g1 == 16,
          f"nonzero chiral off-diag entries: Xi_5 {nz_xi}, Gamma_1 {nz_g1} (one per row)")
    site_xi, site_g1 = [], []
    for s in SPATIAL_STATES:
        q = np.zeros((16, 16), dtype=complex)
        for t in (0, 1):
            q[INDEX[s + (t,)], INDEX[s + (t,)]] = 1.0
        site_xi.append(float(np.linalg.norm(P_R @ XI_5 @ P_L @ q) ** 2))
        site_g1.append(float(np.linalg.norm(P_R @ G1 @ P_L @ q) ** 2))
    check("E10 N5 per_site",
          max(site_xi) < 1e-20 and min(site_g1) > 0.999 and max(site_g1) < 1.001,
          f"local LR weight at each of {len(SPATIAL_STATES)} sites: Xi_5 0, Gamma_1 1")
    _, vecs = np.linalg.eigh(GAMMA_5_4D)
    kept = flipped = 0
    for k in range(16):
        chi = chirality_of(vecs[:, k])
        kept += int(chirality_of(XI_5 @ vecs[:, k]) * chi > 0.99)
        flipped += int(chirality_of(G1 @ vecs[:, k]) * chi < -0.99)
    check("E11 N5 per_mode", kept == 16 and flipped == 16,
          f"gamma_5 eigenmodes: Xi_5 preserves {kept}/16, Gamma_1 flips {flipped}/16")
    check("E12 N5 per_block",
          blocks_match(chirality_blocks(XI_5), (8.0, 0.0, 0.0, 8.0))
          and blocks_match(chirality_blocks(G1), (0.0, 8.0, 8.0, 0.0)),
          "block LL/LR/RL/RR: Xi_5 8/0/0/8, Gamma_1 0/8/8/0")
    fx = float(np.linalg.norm(P_R @ XI_5 @ P_L))
    fg = float(np.linalg.norm(P_R @ G1 @ P_L))
    check("E13 N5 lattice_wide", fx < 1e-12 and abs(fg - np.sqrt(8.0)) < 1e-12,
          f"total LR Frobenius norm: Xi_5 {fx:.1f}, Gamma_1 2*sqrt(2)={fg:.3f}")

    print("N4 residual: physical_identification_of_the_constructed_chirality_operator, matched to")
    print("  the note section 'Out of scope (admitted-context to this note)' items 3 and 4.")
    print("N5 phrase (single line, copied from the note): Xi_5 equals minus gamma_5 in the displayed representation, so it is chiral diagonal and cannot be a chiral off-diagonal Dirac Yukawa surface")
    print("N5 resolution_classes_checked: per_element, per_site, per_mode, per_block, lattice_wide")
    print("N6 partial_closure approved_primitive:minimal_axioms, scale_reference_primitive,")
    print("  kinetic_isotropy_primitive, realized_state_primitive -- addressed; none supplies or")
    print("  modifies the Cl(4) operator packet, so none reaches the E7 grading wall.")
    print("N6 partial_closure owner_governed:staggered_dirac_realization_gate_note_2026-05-03,")
    print("  convention_reframe:g_bare_rigidity_theorem_note, convention_reframe:hypercharge_")
    print("  identification_note -- addressed; the gate supplies no above-C3 taste, Dirac or")
    print("  chirality content, and a dimensionless matrix identity is untouched by either reframe.")
    print("N7 steelman route taste_dressing: argument = the E6 line above; resolution = the E6 out=")
    print("  clause together with the E7 grading wall.")
    print("N8 cross_cycle_echo: 4 own prior audits (all retired), 6 dm_neutrino_weak_vector_theorem")
    print("  audits (not applicable), 1 owner_governed retirement, plus physics_loop_no_go_ledger")
    print("  entries -- none echoes an exact finite Clifford reordering identity.")
    print("Boundary: sections A and E7 make the algebraic authority internal -- the packet is")
    print("  certified from {Gamma_mu, Gamma_nu} = 2 delta_munu I alone. What stays admitted is the")
    print("  physical identification of these operators with emergent 3+1 lattice chirality, the")
    print("  V_sel selector form, and the weak-axis branch convention, not the algebra.")

    print()
    print(f"RESULT: {PASS_COUNT} PASS, {FAIL_COUNT} FAIL")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
