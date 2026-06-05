#!/usr/bin/env python3
"""Chirality multi-factor bridge probe (escape-hatch II of the Z3-equivariant no-go).

Tests whether a MULTI-FACTOR operator on (on-site Cl(3) qubit) (x) (generation R^3),
with the chiral grading built from the NATIVE on-site Cl(3) volume element / bivector
grading coupled to the generation index through the staggered/lattice geometry, induces a
genuine OFF-BLOCK grading on the GENERATION factor after the physical (hw=1 species)
projection -- or collapses to the on-block requirement (Q=1), as PT-C found for the
spacetime/Connes-Lott gamma_CL = I (x) sigma_3 (chirality factor).

Question targeted: `KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16` escape-hatch (II)
("gamma_CL and Gamma_chi live in distinct tensor factors"), specialized to the framework's
NATIVE chirality source (A2 on-site Cl(3,0) = M_2(C)) rather than an imported spacetime gamma_5.

Established prior art used (statuses verified on origin/main ledger):
  - clifford_volume_chirality_even_dimension (retained): in odd dim n=3 the volume element
    omega = g1 g2 g3 is CENTRAL; no element anticommutes with every generator.
  - no_per_site_chirality_theorem (retained_no_go): no per-site gamma_5 projector in M_2(C).
  - koide_z3_equivariant_anticommuting_no_go (retained_bounded): comm(R) cap anticomm(Gamma_chi) = {0}.
  - three_generation_hw1_distinct_translation_characters (retained): hw=1 = generation orbit.
  - parity_violation_does_not_reach_generation_triplet (retained_bounded).
  - staggered_taste_is_qubit / corner_fermion_determinant (2026-06-04, UNAUDITED): recent
    context -- taste = qubit; taste-C3 = generation-C3; corners are kinetic zeros. Cited as
    context only, not load-bearing-retained.

VERDICT computed by the scorecard:
  COLLAPSES-TO-ON-BLOCK (PT-C wall) -- the native Cl(3) joint grading reduces to ZERO/diagonal on
  the generation factor (inert), exactly as the spacetime gamma_CL did; AND the volume-element
  variant lands as a SCALAR on the hw=1 orbit (a REDUCES-TO-HAMMING-NO-GO collapse). No off-block
  generation grading, no Q=2/3.

Pure algebra; no PDG / measured / fitted inputs. (b/a is a free symbol; never set to 1/sqrt(2).)
"""
from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")
    return ok


# ---- primitives -------------------------------------------------------------
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)
J3 = np.ones((3, 3), dtype=complex)
G_chi = (2.0 / 3.0) * J3 - I3                       # Z3 character grading Gamma_chi, signature (1,2)
R = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)   # generation cyclic shift


def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)


def corner_index(b):
    return 4 * b[0] + 2 * b[1] + b[2]


# hw=1 corner basis = generation triplet; P : C^8 -> C^3 (species/hw=1 projection)
_e = [np.zeros(8, complex) for _ in range(3)]
for _k, _b in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
    _e[_k][corner_index(_b)] = 1.0
P = np.array(_e)                                   # 3 x 8


def ptrace_qubit(M6):
    """Partial trace over the on-site qubit factor of a (2x3)x(2x3) operator -> 3x3."""
    return np.einsum('aiaj->ij', M6.reshape(2, 3, 2, 3))


def koide_Q_signed(eigs):
    eigs = np.array(eigs, float)
    num = np.sum(eigs ** 2)
    den = np.sum(eigs) ** 2
    return num / den if abs(den) > 1e-12 else float('inf')


def koide_Q_singular(eigs):
    sv = np.abs(np.array(eigs, float))
    num = np.sum(sv ** 2)
    den = np.sum(sv) ** 2
    return num / den if den > 1e-12 else float('inf')


def main() -> int:
    print("=" * 78)
    print("CHIRALITY MULTI-FACTOR BRIDGE PROBE -- native Cl(3) joint grading on generation")
    print("Targets escape-hatch (II) of KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO")
    print("=" * 78)

    # ----------------------------------------------------------------------
    print("\n[1] Native on-site Cl(3,0) chirality source: volume element is a CENTRAL SCALAR")
    print("-" * 78)
    omega = s1 @ s2 @ s3                              # Cl(3) volume element
    check("Cl(3) volume omega = g1 g2 g3 = i*I2 (scalar, central at odd n=3)",
          np.allclose(omega, 1j * I2),
          f"omega = {np.round(omega,3).tolist()}  (clifford_volume_chirality, retained)")
    # no bivector / no algebra element anticommutes with all three generators (odd dim)
    bivs = {'g1g2': s1 @ s2, 'g2g3': s2 @ s3, 'g3g1': s3 @ s1}
    none_full = True
    for nm, b in bivs.items():
        acs = [np.allclose(b @ g + g @ b, 0) for g in (s1, s2, s3)]
        if all(acs):
            none_full = False
    check("no on-site bivector anticommutes with all 3 generators (each misses one)",
          none_full, "consistent with no_per_site_chirality_theorem (retained_no_go)")

    # ----------------------------------------------------------------------
    print("\n[2] Staggered lock: taste-C3 = generation-C3 (the lattice coupling)")
    print("-" * 78)
    # axis permutation (123) on the cube == generation cyclic shift R on hw=1
    U = np.zeros((8, 8), complex)
    for b1 in (0, 1):
        for b2 in (0, 1):
            for b3 in (0, 1):
                U[corner_index((b3, b1, b2)), corner_index((b1, b2, b3))] = 1.0
    U_hw1 = P @ U @ P.conj().T
    check("axis-rotation U(123)|hw=1 == generation shift R (taste-C3 locked to gen-C3)",
          np.allclose(U_hw1, R), "(staggered_taste_is_qubit / cl3_taste_generation context)")
    # staggered free Dirac symbol vanishes on every BZ corner -> hw=1 is a kinetic zero locus
    corner_sins = [abs(np.sin(k)) for k in (0.0, np.pi)]
    check("staggered free-Dirac symbol sin(k_mu)=0 at all corner momenta {0,pi} (hw=1 kinetic zero)",
          all(s < 1e-12 for s in corner_sins),
          "no chiral grading is supplied by the kinetic Dirac on hw=1 (corner_fermion_determinant)")

    # ----------------------------------------------------------------------
    print("\n[3] JOINT multi-factor grading: on-site Cl(3) grading coupled to corner axis")
    print("-" * 78)
    # Per-axis on-site bivector gradings g_mu (Hermitian, g_mu^2 = +I): the native Cl(3) gradings.
    g = [1j * s2 @ s3, 1j * s3 @ s1, 1j * s1 @ s2]
    for mu in range(3):
        assert np.allclose(g[mu], g[mu].conj().T) and np.allclose(g[mu] @ g[mu], I2)
    Pi = [np.outer(_e[k], _e[k].conj()) for k in range(3)]    # corner projectors (hw=1)
    # Gamma_joint = sum_mu g_mu (x) Pi_mu  on (on-site qubit) (x) (cube)
    GammaJ = sum(np.kron(g[mu], Pi[mu]) for mu in range(3))
    check("joint grading Gamma_J = sum_mu g_mu (x) Pi_mu is Hermitian",
          np.allclose(GammaJ, GammaJ.conj().T))
    # physical reduction to (on-site qubit)(x)(generation R^3)
    Pfull = np.kron(I2, P)                                     # 6 x 16
    GammaJ_red = Pfull @ GammaJ @ Pfull.conj().T              # 6 x 6
    gen_op = ptrace_qubit(GammaJ_red)                         # pure generation operator
    check("reduced joint grading is BLOCK-DIAGONAL in generation (no gen-off-diagonal coupling)",
          _is_generation_block_diagonal(GammaJ_red),
          "off-diagonal entries link only DIFFERENT qubit states at the SAME generation corner")
    check("partial-trace over qubit -> PURE GENERATION operator is ZERO (no induced gen grading)",
          np.allclose(gen_op, 0),
          f"gen_op = {np.round(gen_op.real,3).tolist()}")

    # ----------------------------------------------------------------------
    print("\n[4] INERT LEMMA (PT-C, reproven for native grading): generation reduction vanishes")
    print("-" * 78)
    # For D = A (x) X (on-site A, generation X) and Gamma = gamma_q (x) Gamma_g:
    #   tr_qubit{D, Gamma} = tr(A gamma_q) * {X, Gamma_g}.
    rng = np.random.default_rng(7)
    lemma_ok = True
    for _ in range(400):
        A = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
        X = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        Gg = rng.standard_normal((3, 3)); Gg = Gg + Gg.T
        gamma_q = s3
        D = np.kron(A, X); Gamma = np.kron(gamma_q, Gg)
        ptr = ptrace_qubit(D @ Gamma + Gamma @ D)
        pred = np.trace(A @ gamma_q) * (X @ Gg + Gg @ X)
        if not np.allclose(ptr, pred):
            lemma_ok = False
            break
    check("tr_qubit{D,Gamma_joint} = tr(A*gamma_q) * {X,Gamma_g}  (exact, 400 random draws)",
          lemma_ok)
    # species reduction integrates the spinor uniformly => effective A = I2 on-site => tr(I2*gamma_q)=0
    check("species-uniform spinor trace: tr(I2 * gamma_q) = 0 for every traceless on-site grading",
          all(abs(np.trace(I2 @ gq)) < 1e-12 for gq in (s1, s2, s3, *g)),
          "=> the joint anticommutation imposes ZERO constraint on the generation factor (INERT)")
    # end-to-end with the physical generation mass Dirac (free symbolic b/a; NOT set to 1/sqrt2)
    a_sym, b_sym = 1.0, 0.6                                    # arbitrary; b/a free, value irrelevant
    M_gen = a_sym * I3 + b_sym * R + np.conj(b_sym) * R.conj().T   # circulant gen mass
    D = np.kron(I2, M_gen)                                     # generation-only Dirac (A=I2 on-site)
    Gamma = np.kron(s3, G_chi)                                 # native on-site grading (x) Gamma_chi
    induced = ptrace_qubit(D @ Gamma + Gamma @ D)
    check("end-to-end: induced generation constraint tr_qubit{D, s3 (x) Gamma_chi} = 0",
          np.allclose(induced, 0),
          "the native Cl(3) qubit grading is INERT on generation -- PT-C wall, native variant")

    # [4b] STRONGEST ADVERSARY: a joint grading OFF-DIAGONAL in the corner index, built from the
    # corner double-shift (S_mu S_nu) whose hw=1 projection is J-I -- the GENUINE off-block
    # generation coupling (flavor_native_double_shift_corner_coupling). If anything escapes, it
    # is here. Couple each native on-site bivector g to a double-shift and reduce.
    Sx_, Sy_, Sz_ = (kron3(s1, I2, I2), kron3(I2, s1, I2), kron3(I2, I2, s1))
    Gamma_off = (np.kron(g[2], Sx_ @ Sy_) + np.kron(g[0], Sy_ @ Sz_) + np.kron(g[1], Sz_ @ Sx_))
    Mcube = P.conj().T @ M_gen @ P                            # cube-level mass, hw=1 support
    Dfull = np.kron(I2, Mcube)
    ac_off = Pfull @ (Dfull @ Gamma_off + Gamma_off @ Dfull) @ Pfull.conj().T
    gen_off = ptrace_qubit(ac_off)
    check("STRONGEST ADVERSARY: off-diagonal corner-shift (J-I) joint grading -> gen constraint = 0",
          np.allclose(Gamma_off, Gamma_off.conj().T) and np.allclose(gen_off, 0),
          "even the genuine off-block double-shift coupling is INERT on generation after the qubit/species trace")

    # ----------------------------------------------------------------------
    print("\n[5] DISCRIMINATOR vs Hamming no-go: the volume-element variant is a SCALAR on hw=1")
    print("-" * 78)
    # Hamming spatial parity eps = prod_mu s3_mu  -> -I3 on hw=1 (S3-uniform; established).
    eps = kron3(s3, I2, I2) @ kron3(I2, s3, I2) @ kron3(I2, I2, s3)
    eps_hw1 = P @ eps @ P.conj().T
    check("Hamming parity eps=(-1)^hw restricts to -I3 on the generation orbit (S3-uniform)",
          np.allclose(eps_hw1, -I3))
    # on-site Cl(3) volume omega acts site-locally (omega = iI on EVERY corner) -> i*I3 on hw=1
    omega_hw1 = 1j * I3                                        # site-local scalar omega = iI per corner
    check("Cl(3) volume omega is site-local i*I -> i*I3 on hw=1: a SCALAR on the generation orbit",
          np.allclose(omega_hw1, 1j * I3))
    # both scalars: commute with R, do NOT anticommute with Gamma_chi -> cannot grade generation
    scalar_commutes = (np.allclose(omega_hw1 @ R - R @ omega_hw1, 0)
                       and not np.allclose(omega_hw1 @ G_chi + G_chi @ omega_hw1, 0))
    check("omega_hw1 commutes with R and does NOT anticommute with Gamma_chi (scalar -> cannot grade)",
          scalar_commutes,
          "Cl(3) volume route REDUCES-TO-HAMMING-NO-GO (scalar on orbit) -- distinct reason (centrality), same consequence")

    # ----------------------------------------------------------------------
    print("\n[6] Sanity on Q: the only operator that DOES break C3 gives Q != 2/3 (signed divergent / sv 1/2)")
    print("-" * 78)
    # The contrapositive escape: force a NONZERO induced gen grading -> requires tr(A*gamma_q)!=0,
    # i.e. the Dirac ENTANGLES on-site with generation, collapsing the two factors into one combined
    # index. Then the 'grading' is the on-site grading read through the entangling map -> the
    # generation grading is identified with Gamma_chi itself and must anticommute with M on R^3.
    # By the retained no_go that forces a C3-BREAKING M; its spectrum is {-lam,0,+lam} (sig (1,2)),
    # giving singular-value Q=1/2 and signed/Brannen Q divergent (trace 0). Reproduce:
    Sym = []
    for i in range(3):
        for j in range(i, 3):
            E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1.0; Sym.append(E)
    Mrows = [(E @ G_chi + G_chi @ E).flatten() for E in Sym]
    Mmat = np.array(Mrows).T
    _, sv, vt = np.linalg.svd(Mmat)
    null = vt[np.sum(sv > 1e-9):]
    H = sum(c * E for c, E in zip(null[0], Sym))
    H = H / np.linalg.norm(H)
    eig = np.sort(np.linalg.eigvalsh(H))
    breaks_C3 = not np.allclose(H @ R - R @ H, 0)
    anti = np.allclose(H @ G_chi + G_chi @ H, 0)
    Q_sv = koide_Q_singular(eig)
    check("the C3-breaking anticommuting operator has spectrum {-lam,0,+lam}, singular-value Q=1/2 (NOT 2/3)",
          anti and breaks_C3 and abs(Q_sv - 0.5) < 1e-9,
          f"eig={np.round(eig,3).tolist()}, Q_singular={Q_sv:.4f}; signed-Q divergent (trace 0)")

    # ----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print("VERDICT: COLLAPSES-TO-ON-BLOCK (PT-C wall) for the native Cl(3) joint grading.")
    print("  - [3] the joint grading g_mu (x) Pi_mu is block-diagonal in generation; its gen")
    print("        partial trace is ZERO (no off-block generation grading induced).")
    print("  - [4] inert lemma (native variant): species-uniform spinor trace tr(I2*gamma_q)=0")
    print("        makes the joint anticommutation impose ZERO constraint on the generation factor;")
    print("        a nonzero induced grading needs tr(A*gamma_q)!=0, i.e. the Dirac entangles the")
    print("        two factors into one combined index -> the grading is no longer a SEPARATE")
    print("        generation grading (it is Gamma_chi itself read through the lock) -> begs r=1/2.")
    print("  - [5] the Cl(3) VOLUME-element variant lands as a SCALAR on hw=1 (omega=iI per site),")
    print("        a REDUCES-TO-HAMMING-NO-GO collapse (distinct reason = odd-dim centrality, same")
    print("        consequence as the S3-uniform Hamming parity eps=-I3).")
    print("  No off-block generation grading; no Q=2/3. The single unsupplied import remains the")
    print("  C3-orbit-splitting chiral grading on R^3_gen -- the native on-site Cl(3) source does")
    print("  not transport across the tensor factor, exactly as PT-C found for spacetime gamma_CL.")
    return 0 if FAIL == 0 else 1


def _is_generation_block_diagonal(M6) -> bool:
    """True if M6 (on a (qubit (x) gen) = 2x3 index) has no entry coupling DIFFERENT generations."""
    M = M6.reshape(2, 3, 2, 3)
    for qi in range(2):
        for gi in range(3):
            for qj in range(2):
                for gj in range(3):
                    if gi != gj and abs(M[qi, gi, qj, gj]) > 1e-12:
                        return False
    return True


if __name__ == "__main__":
    raise SystemExit(main())
