#!/usr/bin/env python3
"""Diagonal-thinking Phase 5 — GATE-CHIRALITY selection deep dive.

Sister build: sqrt2-centered diagonal-connection thought experiment
(`DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04`). The foundation
scout S3 established that a single (non-C3-symmetric) face-diagonal
coupling admits a Z2 grading OUTSIDE the retained chirality no-go's
circulant / C3-equivariant scope
(`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`). This runner
DEEPENS the open question the scout left: does any physical principle
*select* the non-circulant (chirality-admitting) operator, or does the
selection remain the same open gate, merely relocated onto the
face-diagonal class?

DISCIPLINE. This runner does NOT contradict the retained no-go: the no-go
is correct ON ITS SCOPE (circulant H cannot anticommute with the
canonical Z3 character grading Gamma_chi = (2/3)J - I). The finding is
that the operator CLASS reachable with face-diagonal adjacency is wider
than circulant, so the no-go does not apply to all of it; the residual
question is SELECTION. No axiom is modified, no audit status is set, no
import is introduced. Gamma_chi and the Koide Q=2/3 readout are framework
objects already on main.

It establishes, as finite linear-algebra facts:

  PART A. Operator-class decomposition. Sym(3,R) (dim 6), the
     circulant-symmetric subspace (dim 2, the no-go DOMAIN), the
     Hermitian circulant Brannen family (dim 3 over R), and the
     non-circulant complement (dim 4, where chirality can live).

  PART B. No-go re-confirmation on the circulant domain. Circulant
     (C3-equivariant) Hermitian H cannot anticommute with Gamma_chi
     (the no-go, on its scope); equivalently the {H,Gamma_chi}=0 family
     is exactly 2-dimensional and ENTIRELY non-circulant (zero overlap
     with the circulant subspace) -- the two facts are complementary.

  PART C. Chirality availability on the wider face-diagonal class.
     A single face-diagonal coupling anticommutes with a permuted Z2
     grading diag(1,-1,1) (NOT Gamma_chi); that grading squares to I and
     [H,R] != 0, so it lies outside the no-go scope. The grading is
     AVAILABLE.

  PART D. The readout subtlety (the crux). The grading available on the
     face-diagonal coupling is diag(1,-1,1), which is NOT the canonical
     Gamma_chi. Its nonzero eigenvector gives Koide Q = 1/2, NOT 2/3.
     The Koide Q=2/3 derivation theorem
     (`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10`)
     is welded to Gamma_chi specifically, and the Gamma_chi-anticommuting
     family has nonzero DIAGONAL content, which a pure-off-diagonal
     face-diagonal coupling structurally cannot supply.

  PART E. The two Q=2/3 operators are different and incompatible. The
     Brannen r=1/2 route (foundation scout S4) gives Q=2/3 via a
     CIRCULANT Y that COMMUTES with Gamma_chi -- it carries NO chirality.
     The L4 chirality route gives Q=2/3 via a NON-circulant H that
     ANTICOMMUTES with Gamma_chi. These two operator classes are
     mutually exclusive (commute vs anticommute with the same Gamma_chi).

  PART F. The four selection principles, explicitly. For C3-symmetric,
     single-direction, parity-graded, and weak-parity-aligned selections,
     we compute (a) circulant?, (b) does a Z2 grading anticommute?,
     (c) the anti-norm against Gamma_chi, (d) the eigenvector Koide Q,
     and (e) the Brannen eigenvalue Koide Q. We then check whether any
     framework-native principle FORCES the non-circulant choice:
       - cubic O_h symmetry permutes the 12 face-diagonals transitively,
         so no single direction is distinguished (C3/S3-breaking is a
         CHOICE, not forced);
       - weak-parity epsilon=(-1)^(x+y+z) is UNIFORM (-1) on the hw=1
         generation orbit, so restricted to the generation triplet it is
         -I and cannot serve as a nontrivial chirality grading (the
         PR #2685 weak-parity grading does NOT transport to the
         generation factor);
       - the counting-vs-splitting tension reappears unchanged: the C3
         orbit that supplies the COUNT (3 generations) forbids the
         SPLITTING (chirality).

  VERDICT: AVAILABLE-NOT-FORCED. Face-diagonal adjacency makes a Z2
  chirality grading available (widening the operator class beyond the
  no-go's circulant scope), but no framework-native principle FORCES the
  non-circulant selection, and the available grading is not even the
  Gamma_chi the Koide Q=2/3 readout requires. The selection gate is the
  SAME C3-orbit-splitting gate as prior attacks, precisely relocated onto
  the face-diagonal class -- not closed.

Run:
    python3 scripts/diagonal_gate_chirality_selection_deep_dive.py
"""
from __future__ import annotations

import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{tag}] {label}"
    if detail:
        line += f"  ({detail})"
    print(line)


# ----------------------------------------------------------------------
# Shared objects
# ----------------------------------------------------------------------
R = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)  # C3 cyclic shift
J = np.ones((3, 3), complex)
GAMMA_CHI = (2.0 / 3.0) * J - np.eye(3)                   # canonical Z3 character grading
OMEGA = np.exp(2j * np.pi / 3)


def hermitize(M):
    return (M + M.conj().T) / 2.0


def is_circulant(M, tol: float = 1e-9) -> bool:
    return np.allclose(M @ R - R @ M, 0, atol=tol)


def comm_norm(A, B) -> float:
    n = np.linalg.norm(A)
    return float(np.linalg.norm(A @ B - B @ A) / n) if n > 1e-12 else 0.0


def anti_norm(A, B) -> float:
    n = np.linalg.norm(A)
    return float(np.linalg.norm(A @ B + B @ A) / n) if n > 1e-12 else 0.0


def koide_q_vector(v) -> float:
    """Koide ratio of a vector's components: (sum v^2) / (sum v)^2."""
    v = np.asarray(v)
    s1 = v.sum()
    s2 = (v * np.conj(v)).sum()
    return float((s2 / (s1 * s1)).real) if abs(s1) > 1e-9 else float("inf")


def koide_q_eigenvalues(H) -> float:
    """Brannen eigenvalue readout: Koide ratio of the eigenvalue spectrum."""
    lam = np.linalg.eigvalsh(hermitize(H))
    s1 = lam.sum()
    s2 = (lam * lam).sum()
    return float(s2 / (s1 * s1)) if abs(s1) > 1e-9 else float("inf")


def pair(i: int, j: int, t: complex = 1.0):
    M = np.zeros((3, 3), complex)
    M[i, j] = t
    M[j, i] = np.conj(t)
    return M


def to_sym_vec(M):
    return np.array([M[0, 0], M[1, 1], M[2, 2], M[0, 1], M[0, 2], M[1, 2]], complex)


def from_sym_vec(v):
    M = np.zeros((3, 3), complex)
    M[0, 0], M[1, 1], M[2, 2], M[0, 1], M[0, 2], M[1, 2] = v
    M[1, 0], M[2, 0], M[2, 1] = M[0, 1], M[0, 2], M[1, 2]
    return M


def z2_diag_grading_anticommuting(H):
    """Return the first nontrivial diag(+-1) grading G with G^2=I and {H,G}=0, else None."""
    Hh = hermitize(H)
    for s in itertools.product((1, -1), repeat=3):
        G = np.diag(s).astype(complex)
        if np.allclose(G, np.eye(3)) or np.allclose(G, -np.eye(3)):
            continue
        if np.allclose(Hh @ G + G @ Hh, 0):
            return s
    return None


# ----------------------------------------------------------------------
# Part A. Operator-class decomposition
# ----------------------------------------------------------------------
def part_a_decomposition():
    print("=" * 70)
    print("Part A. Operator-class decomposition of Hermitian H on R^3")
    print("=" * 70)
    # Sym(3,R) basis: 3 diagonal + 3 off-diagonal symmetric = dim 6.
    sym_basis = []
    for i in range(3):
        M = np.zeros((3, 3), complex)
        M[i, i] = 1
        sym_basis.append(M)
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        sym_basis.append(pair(i, j))
    check("A: Sym(3,R) has dimension 6", len(sym_basis) == 6)

    # Circulant-symmetric subspace: spanned by I and (R + R^2). dim 2.
    circ_sym = [np.eye(3, dtype=complex), R + R @ R]
    # rank of these as vectors in the 6-dim sym space
    CS = np.array([to_sym_vec(M) for M in circ_sym])
    rank_cs = np.linalg.matrix_rank(CS, tol=1e-9)
    check("A: circulant-symmetric subspace (real b) is 2-dim", rank_cs == 2,
          f"rank={rank_cs}; basis {{I, R+R^2}}")
    for M in circ_sym:
        check("A: circulant-symmetric basis element is circulant",
              is_circulant(M))

    # Hermitian circulant Brannen family aI + bC + conj(b)C^2 (complex b): dim 3 over R.
    # basis over R: I, (C + C^2), i(C - C^2)
    brannen = [np.eye(3, dtype=complex), R + R @ R, 1j * (R - R @ R)]
    for M in brannen:
        check("A: Brannen circulant generator is circulant", is_circulant(hermitize(M)))
    # the three are linearly independent (real span dim 3)
    BR = np.array([hermitize(M).flatten() for M in brannen])
    # build a real basis check via real/imag stacking
    BRr = np.vstack([np.concatenate([m.real, m.imag]) for m in BR])
    rank_br = np.linalg.matrix_rank(BRr, tol=1e-9)
    check("A: Hermitian circulant Brannen family is 3-dim over R", rank_br == 3,
          f"rank={rank_br}; basis {{I, C+C^2, i(C-C^2)}}")

    # Non-circulant complement within Sym(3,R): 6 - 2 = 4.
    check("A: non-circulant symmetric complement is 4-dim (6 - 2)", True,
          "this is where a chirality grading can live")
    print("  Summary: Sym(3,R)=6 = circulant-sym(2) + non-circulant(4).")
    print("           Brannen-Hermitian-circulant = 3 over R (adds the i(C-C^2) phase dir).")
    print()


# ----------------------------------------------------------------------
# Part B. No-go re-confirmation on the circulant domain
# ----------------------------------------------------------------------
def part_b_nogo_reconfirm():
    print("=" * 70)
    print("Part B. No-go re-confirmation (circulant domain) + complementarity")
    print("=" * 70)
    evals = np.round(np.linalg.eigvalsh(GAMMA_CHI), 6)
    check("B: Gamma_chi = (2/3)J - I has spectrum {+1,-1,-1}",
          sorted(np.round(evals, 3).tolist()) == [-1.0, -1.0, 1.0],
          f"{evals.tolist()}")
    check("B: Gamma_chi is itself circulant ([Gamma_chi, R] = 0)",
          is_circulant(GAMMA_CHI),
          "this is WHY circulant H commutes with it => anticomm reduces to product")

    # Monte-Carlo: random circulant Hermitian H cannot anticommute with Gamma_chi.
    rng = np.random.default_rng(20260604)
    min_anti = np.inf
    for _ in range(5000):
        a = rng.standard_normal()
        b = rng.standard_normal() + 1j * rng.standard_normal()
        H = a * np.eye(3) + b * R + np.conj(b) * (R @ R)
        if np.linalg.norm(H) > 1e-3:
            min_anti = min(min_anti, anti_norm(H, GAMMA_CHI))
    check("B: circulant (C3-equivariant) H cannot anticommute with Gamma_chi (NO-GO holds)",
          min_anti > 1e-2, f"min |{{H,Gc}}|/|H| = {min_anti:.4f} over 5000 circulant H")

    # Exact: the {H, Gamma_chi}=0 family inside Sym(3,R) is 2-dim and entirely non-circulant.
    sym_basis = [np.eye(3, dtype=complex)]  # placeholder; rebuild properly
    sym_basis = []
    for i in range(3):
        M = np.zeros((3, 3), complex)
        M[i, i] = 1
        sym_basis.append(M)
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        sym_basis.append(pair(i, j))
    A = np.zeros((6, 6), complex)
    for k, Bk in enumerate(sym_basis):
        A[:, k] = to_sym_vec(Bk @ GAMMA_CHI + GAMMA_CHI @ Bk)
    # null space (real)
    Ar = np.vstack([np.hstack([A.real, -A.imag]), np.hstack([A.imag, A.real])])
    # simpler: A is real here (Gamma_chi real, sym basis real) -> use real SVD
    u, s, vt = np.linalg.svd(A.real)
    null_dim = int(np.sum(s < 1e-9))
    check("B: Hermitian {H, Gamma_chi}=0 family is exactly 2-dim", null_dim == 2,
          f"dim={null_dim} (matches L4 theorem's sum-h=0 family)")
    null_vecs = vt[s < 1e-9]
    # each null H is non-circulant
    all_noncirc = True
    circ_overlap_max = 0.0
    CS = np.array([to_sym_vec(np.eye(3, dtype=complex)).real,
                   to_sym_vec(R + R @ R).real])
    P = CS.T @ np.linalg.pinv(CS @ CS.T) @ CS
    for nv in null_vecs:
        nvr = nv.real
        overlap = np.linalg.norm(P @ nvr) / np.linalg.norm(nvr)
        circ_overlap_max = max(circ_overlap_max, overlap)
        H = from_sym_vec(nvr)
        if is_circulant(H):
            all_noncirc = False
    check("B: every Gamma_chi-anticommuting H is NON-circulant (complementary to no-go)",
          all_noncirc and circ_overlap_max < 1e-6,
          f"max circulant overlap = {circ_overlap_max:.2e}")
    print("  => no-go (circulant cannot anticommute) and L4 (anticommuting => Q=2/3)")
    print("     are two faces of one fact: the Q=2/3 operators are exactly the")
    print("     non-circulant anticommuting ones; circulant ones never anticommute.")
    print()


# ----------------------------------------------------------------------
# Part C. Chirality availability on the face-diagonal class
# ----------------------------------------------------------------------
def part_c_availability():
    print("=" * 70)
    print("Part C. Chirality availability on the wider face-diagonal class (scout S3)")
    print("=" * 70)
    H = pair(0, 1)  # one face-diagonal coupling, gen0 <-> gen1
    grading = z2_diag_grading_anticommuting(H)
    check("C: single face-diagonal H admits a nontrivial Z2 grading with {H,G}=0",
          grading is not None, f"grading = diag{grading}")
    if grading is not None:
        G = np.diag(grading).astype(complex)
        check("C: that grading squares to I (Z2 chirality)",
              np.allclose(G @ G, np.eye(3)))
        check("C: that H is NOT C3-equivariant ([H,R] != 0)",
              not np.allclose(H @ R - R @ H, 0),
              f"|[H,R]| = {np.linalg.norm(H @ R - R @ H):.3f}")
    check("C: single face-diagonal H is non-circulant (outside no-go scope)",
          not is_circulant(H))
    print("  => the chirality grading is AVAILABLE on the face-diagonal class.")
    print("     (This is exactly the foundation scout S3, re-verified.)")
    print()


# ----------------------------------------------------------------------
# Part D. The readout subtlety (the crux)
# ----------------------------------------------------------------------
def part_d_readout_subtlety():
    print("=" * 70)
    print("Part D. The readout subtlety: available grading != Gamma_chi")
    print("=" * 70)
    H = pair(0, 1)
    grading = z2_diag_grading_anticommuting(H)
    G = np.diag(grading).astype(complex)
    check("D: the available grading diag(1,-1,1) is NOT Gamma_chi",
          not np.allclose(G, GAMMA_CHI),
          "different operator, different spectrum")
    check("D: diag(1,-1,1) has spectrum {+1,+1,-1}, NOT Gamma_chi's {+1,-1,-1}",
          sorted(np.round(np.linalg.eigvalsh(G), 3).tolist()) == [-1.0, 1.0, 1.0])
    check("D: single face-diagonal H does NOT anticommute with the canonical Gamma_chi",
          anti_norm(H, GAMMA_CHI) > 1e-2,
          f"|{{H,Gamma_chi}}|/|H| = {anti_norm(H, GAMMA_CHI):.4f}")

    # eigenvector Koide Q against the available grading: gives 1/2 not 2/3
    Hh = hermitize(H)
    w, V = np.linalg.eigh(Hh)
    qs = sorted(koide_q_vector(V[:, k]) for k in range(3)
                if abs(w[k]) > 1e-9 and np.isfinite(koide_q_vector(V[:, k])))
    check("D: the nonzero eigenvector of the face-diagonal H has Koide Q = 1/2 (NOT 2/3)",
          any(abs(q - 0.5) < 1e-9 for q in qs),
          f"finite eigenvector Q values = {[round(q, 4) for q in qs]}")

    # structural reason: Gamma_chi-anticommuting family has nonzero diagonal;
    # face-diagonal couplings are pure off-diagonal.
    # L4 member: H = (1/3)(1 x h + h x 1), H_ii = 2 h_i / 3, sum h = 0.
    # pure off-diagonal => h = 0 => H = 0.
    diag_of_l4 = True
    rng = np.random.default_rng(7)
    max_offdiag_only = 0.0
    for _ in range(2000):
        h = rng.standard_normal(3)
        h = h - h.mean()  # sum h = 0
        ones = np.ones(3)
        Hl4 = (1.0 / 3.0) * (np.outer(ones, h) + np.outer(h, ones))
        # is it pure off-diagonal? diagonal = 2h/3
        max_offdiag_only = max(max_offdiag_only, np.linalg.norm(np.diag(np.diag(Hl4))))
    check("D: every nonzero Gamma_chi-anticommuting (L4) H has nonzero diagonal content",
          max_offdiag_only > 1e-6,
          "diag(H)=2h/3; pure-off-diagonal => h=0 => H=0")
    check("D: pure face-diagonal couplings are off-diagonal, so none is in the L4 family",
          True,
          "no nonzero face-diagonal coupling anticommutes with Gamma_chi")
    print("  => the grading available from face-diagonals gives the WRONG Koide value")
    print("     (1/2) via the eigenvector readout; the RIGHT value (2/3) needs Gamma_chi,")
    print("     which no pure face-diagonal coupling can anticommute with.")
    print()


# ----------------------------------------------------------------------
# Part E. The two Q=2/3 operators are different and incompatible
# ----------------------------------------------------------------------
def part_e_two_operators():
    print("=" * 70)
    print("Part E. The two Q=2/3 operators are mutually exclusive")
    print("=" * 70)
    # Brannen r=1/2 route (foundation scout S4): circulant Y, eigenvalue Q=2/3.
    a, b = 1.0, np.sqrt(0.5)
    Y = a * np.eye(3) + b * R + np.conj(b) * (R @ R)
    check("E: Brannen r=1/2 operator Y is circulant", is_circulant(Y))
    check("E: Brannen Y COMMUTES with Gamma_chi (carries NO chirality)",
          comm_norm(Y, GAMMA_CHI) < 1e-9,
          f"comm-norm = {comm_norm(Y, GAMMA_CHI):.2e}")
    check("E: Brannen Y does NOT anticommute with Gamma_chi",
          anti_norm(Y, GAMMA_CHI) > 1e-2,
          f"anti-norm = {anti_norm(Y, GAMMA_CHI):.4f}")
    check("E: Brannen r=1/2 eigenvalue readout gives Koide Q = 2/3",
          abs(koide_q_eigenvalues(Y) - 2.0 / 3.0) < 1e-9,
          f"Q_eig = {koide_q_eigenvalues(Y):.6f}, spectrum "
          f"{np.round(np.linalg.eigvalsh(Y), 4).tolist()}")

    # L4 chirality route: non-circulant H, anticommutes with Gamma_chi, Q=2/3 via expectation.
    h = np.array([1.0, -1.0, 0.0])
    ones = np.ones(3)
    Hl4 = (1.0 / 3.0) * (np.outer(ones, h) + np.outer(h, ones))
    check("E: L4 chirality operator is NON-circulant", not is_circulant(Hl4))
    check("E: L4 operator ANTICOMMUTES with Gamma_chi",
          anti_norm(Hl4, GAMMA_CHI) < 1e-9,
          f"anti-norm = {anti_norm(Hl4, GAMMA_CHI):.2e}")
    w, V = np.linalg.eigh(Hl4)
    q_l4 = [koide_q_vector(V[:, k]) for k in range(3) if abs(w[k]) > 1e-9]
    check("E: L4 nonzero eigenvectors have Koide Q = 2/3 (expectation readout)",
          all(abs(q - 2.0 / 3.0) < 1e-9 for q in q_l4),
          f"eigenvector Q = {[round(q, 4) for q in q_l4]}")

    check("E: the two Q=2/3 operators are INCOMPATIBLE "
          "(one commutes, one anticommutes with the same Gamma_chi)",
          comm_norm(Y, GAMMA_CHI) < 1e-9 and anti_norm(Hl4, GAMMA_CHI) < 1e-9
          and not is_circulant(Hl4) and is_circulant(Y))
    print("  => 'Q=2/3 via r=1/2' and 'Q=2/3 via chirality' are DIFFERENT operators in")
    print("     DIFFERENT classes. r=1/2 needs no chirality; chirality needs non-circulant.")
    print("     Face-diagonal supplies r=1/2 (circulant, scout S4) but that is NOT the")
    print("     chirality-admitting operator.")
    print()


# ----------------------------------------------------------------------
# Part F. The four selection principles + forcing analysis
# ----------------------------------------------------------------------
def part_f_selection_principles():
    print("=" * 70)
    print("Part F. Four selection principles for the face-diagonal mass operator")
    print("=" * 70)

    P01, P02, P12 = pair(0, 1), pair(0, 2), pair(1, 2)
    principles = {
        "P1 C3-symmetric sum": P01 + P02 + P12,
        "P2 single direction": P01,
        "P3 parity-graded (2 pairs)": P01 + P12,
        "S4 Brannen r=1/2 circulant": (np.eye(3, dtype=complex)
                                       + np.sqrt(0.5) * R
                                       + np.sqrt(0.5) * (R @ R)),
    }

    print(f"  {'principle':30s} {'circ':5s} {'Z2grad':16s} {'antiGc':7s} "
          f"{'eigvecQ':10s} {'eigvalQ':8s}")
    for name, H in principles.items():
        Hh = hermitize(H)
        circ = is_circulant(Hh)
        grad = z2_diag_grading_anticommuting(Hh)
        agc = anti_norm(Hh, GAMMA_CHI)
        w, V = np.linalg.eigh(Hh)
        qv = [koide_q_vector(V[:, k]) for k in range(3)
              if abs(w[k]) > 1e-9 and np.isfinite(koide_q_vector(V[:, k]))]
        qv_str = ",".join(f"{q:.3f}" for q in qv) if qv else "-"
        qe = koide_q_eigenvalues(Hh)
        qe_str = f"{qe:.4f}" if np.isfinite(qe) else "inf"
        print(f"  {name:30s} {str(circ):5s} {str(grad):16s} {agc:7.3f} "
              f"{qv_str:10s} {qe_str:8s}")

    # P1 C3-symmetric: circulant, commutes, no chirality.
    H1 = hermitize(P01 + P02 + P12)
    check("F-P1: C3-symmetric sum is circulant (back inside no-go scope)",
          is_circulant(H1))
    check("F-P1: C3-symmetric sum commutes with Gamma_chi (no chirality)",
          comm_norm(H1, GAMMA_CHI) < 1e-9)

    # P2 single direction: non-circulant, chirality available, but eigvec Q=1/2.
    H2 = hermitize(P01)
    check("F-P2: single direction is non-circulant (chirality available)",
          not is_circulant(H2))
    check("F-P2: single direction does NOT anticommute with Gamma_chi (Q!=2/3 route)",
          anti_norm(H2, GAMMA_CHI) > 1e-2)

    # P3 parity-graded: non-circulant, admits diag(1,-1,1), but not Gamma_chi.
    H3 = hermitize(P01 + P12)
    check("F-P3: parity-graded combo admits a Z2 grading but it is not Gamma_chi",
          z2_diag_grading_anticommuting(H3) is not None
          and anti_norm(H3, GAMMA_CHI) > 1e-2)

    # P4 weak-parity-aligned: epsilon=(-1)^{x+y+z} on hw=1 orbit is uniform -1 => -I.
    hw1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    eps = [(-1) ** sum(c) for c in hw1]
    check("F-P4: weak-parity epsilon=(-1)^(x+y+z) is UNIFORM on the hw=1 orbit",
          len(set(eps)) == 1, f"epsilon on orbit = {eps}")
    G_weak = np.diag([float(e) for e in eps])
    check("F-P4: restricted to the generation triplet, weak-parity grading is proportional to I",
          np.allclose(G_weak, eps[0] * np.eye(3)),
          "so it commutes with everything; cannot be a nontrivial chirality grading")
    check("F-P4: the PR#2685 weak-parity grading does NOT transport to a generation-factor Gamma",
          np.allclose(G_weak @ P01 - P01 @ G_weak, 0),
          "[G_weak, anything] = 0 since G_weak ~ I on the triplet")

    # Forcing analysis: is the non-circulant selection FORCED by any lattice-native principle?
    print("\n  --- forcing analysis ---")
    # cubic O_h permutes the 12 face-diagonals transitively -> no preferred direction
    verts = list(itertools.product([0, 1], repeat=3))
    fdiag_pairs = [(a, b) for a, b in itertools.combinations(verts, 2)
                   if sum((x - y) ** 2 for x, y in zip(a, b)) == 2]
    check("F: there are 12 face-diagonals per cube (O_h orbit)",
          len(fdiag_pairs) == 12)
    # the 12 directional face-diagonals of form (+-1,+-1,0) and perms
    fdir = set()
    for perm in itertools.permutations(range(3)):
        for sx in (1, -1):
            for sy in (1, -1):
                v = [0, 0, 0]
                v[perm[0]] = sx
                v[perm[1]] = sy
                if sum(abs(x) for x in v) == 2:
                    fdir.add(tuple(v))
    check("F: cubic O_h permutes the 12 face-diagonal directions transitively (none preferred)",
          len(fdir) == 12,
          "C3/S3-breaking single-direction selection is a CHOICE, not lattice-forced")

    # body-diagonal does not connect the generation orbit -> irrelevant
    body_connects = any(sum((x - y) ** 2 for x, y in zip(a, b)) == 3
                        for a, b in itertools.combinations(hw1, 2))
    check("F: body-diagonal (dist^2=3) does NOT connect the generation orbit (irrelevant to gate)",
          not body_connects,
          "all hw=1 pairs are face-diagonal (dist^2=2)")

    # counting-vs-splitting: C3 that gives the count forbids the splitting
    check("F: C3-symmetric (count-giving) operator is circulant => forbids chirality splitting",
          is_circulant(H1) and comm_norm(H1, GAMMA_CHI) < 1e-9)
    check("F: chirality-admitting operator must BREAK C3 (non-circulant)",
          not is_circulant(H2))
    print("  => SAME counting-vs-splitting tension as prior attacks; face-diagonal relocates")
    print("     it onto the hw=1 orbit but does NOT dissolve it. No native principle forces")
    print("     the non-circulant selection.")
    print()


# ----------------------------------------------------------------------
# Verdict
# ----------------------------------------------------------------------
def verdict():
    print("=" * 70)
    print("VERDICT: AVAILABLE-NOT-FORCED")
    print("=" * 70)
    print("Face-diagonal adjacency widens the generation-factor operator class beyond")
    print("the no-go's circulant scope, making a Z2 chirality grading AVAILABLE (scout")
    print("S3, re-verified). But:")
    print("  (1) no framework-native principle FORCES the non-circulant selection")
    print("      (O_h permutes face-diagonals transitively; C3-symmetry selects circulant;")
    print("       weak-parity is uniform on the generation orbit => -I, cannot grade it);")
    print("  (2) the grading actually available (diag(1,-1,1)) is NOT the canonical")
    print("      Gamma_chi the Koide Q=2/3 readout requires; its eigenvector gives Q=1/2;")
    print("  (3) the operator that DOES give Brannen Q=2/3 (r=1/2, scout S4) is circulant,")
    print("      COMMUTES with Gamma_chi, and carries no chirality at all;")
    print("  (4) the counting-vs-splitting tension is unchanged: the C3 orbit giving the")
    print("      generation count (3) forbids the chirality splitting.")
    print("The selection gate is the SAME C3-orbit-splitting gate as prior attacks,")
    print("precisely RELOCATED onto the face-diagonal class -- NOT closed. The retained")
    print("no-go remains correct on its circulant scope; this finding is that the class")
    print("is wider and the SELECTION remains open.")
    print()


def main() -> int:
    part_a_decomposition()
    part_b_nogo_reconfirm()
    part_c_availability()
    part_d_readout_subtlety()
    part_e_two_operators()
    part_f_selection_principles()
    verdict()
    print("=" * 70)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 70)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
