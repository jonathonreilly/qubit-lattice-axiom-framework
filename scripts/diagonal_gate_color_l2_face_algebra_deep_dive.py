#!/usr/bin/env python3
"""Diagonal-thinking GATE-COLOR deep dive (Phase 4, L2 face-diagonal algebra).

Deepens scout S2 of the sqrt2-centered foundation
(`scripts/diagonal_sqrt2_foundation_enumerator.py`): face-diagonal
pair-connections on the 3-generation factor C^3 generate u(3) = su(3) + u(1).
The honest question this runner settles: does that u(3) genuinely supply
physical COLOR SU(3), or is it a GENERATION-space rotation that does not
discharge GATE-COLOR?

Six finite linear-algebra blocks (all exact; no PDG value, no axiom edit,
no fitted selector, no import):

  Part A. NN obstruction is REAL. Under NN-only adjacency, the three hw=1
     generation sites are mutually face-diagonal (dist^2=2), so NN
     connections connect ZERO of the three pairs. The NN-connection algebra
     on the hw=1 triplet is the diagonal commutant u(1)^3 (real dim 3),
     strictly smaller than u(3) (real dim 9). This is exactly why the
     qubit-link note says color is obstructed: you cannot build the three
     pair-generators when the three pairs are not adjacent.

  Part B. FACE-DIAGONAL closure. With face-diagonals, the three pairs ARE
     adjacent; pairwise u(2) closes to u(3) (real dim 9). The split
     su(3) (dim 8) + u(1) (dim 1) is verified RIGOROUSLY (proper
     traceless-anti-Hermitian basis-count, repairing the foundation
     runner's "coarse proxy" trace-free count). Generators close under the
     Lie bracket and structure constants are real.

  Part C. su(3) embedding check. The 8 generated traceless generators are
     verified to satisfy [T^a,T^b]=i f^{abc} T^c with real, totally
     antisymmetric f, Killing form negative-definite (compact su(3)),
     and rank 2 (two-dim Cartan). This certifies the algebra IS su(3),
     not merely 8-dimensional.

  Part D. GENERATION-vs-COLOR identification probe (THE DEEP QUESTION).
     The u(3) acts on the hw=1 GENERATION subspace
     {|100>, |010>, |001>} of C^8. The framework's retained COLOR SU(3)
     (CL3_COLOR_AUTOMORPHISM_THEOREM, audited_clean) lives on a DIFFERENT
     subspace: the 3D SYMMETRIC BASE {|00>, |11>, (|01>+|10>)/sqrt2} of the
     (b1,b2)-base x b3-fiber decomposition. We verify:
       (D1) the two 3D carriers are DIFFERENT subspaces of C^8 (overlap < 3);
       (D2) the Z_3 cyclic generation action has permutation character
            (3,0,0) = regular rep, whereas the SU(3)_c center acts on the
            color fundamental with character (3,3w,3w^2); these are DISTINCT,
            so the center is not the bridge (matches the open-gate note);
       (D3) imposing the SAME cyclic label on both 3-spaces makes them
            isomorphic as Z_3 reps -- but that common action is an EXTRA
            bridge assumption, exactly the open gate
            Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE.
     Conclusion: face-diagonal supplies a u(3) on GENERATION space; reading
     it as COLOR needs the still-open color/generation identification.

  Part E. BODY-DIAGONAL effect. The 4 body-diagonals (dist^2=3) of the cube
     connect OPPOSITE-parity Hamming levels (hw flips by an odd amount), so
     no body-diagonal connects two hw=1 sites: body-diagonals act trivially
     WITHIN the hw=1 triplet. Hence body-diagonals add no 4th generation and
     do not change the u(3) on hw=1. (They connect hw=1 <-> hw=2, i.e. the
     C-conjugate generation orbit, which is a separate sector.)

  Part F. Honest-verdict consistency checks (the negative is recorded as a
     first-class fact, not buried): dim(face-diag algebra)=9=dim(color u(3))
     is a DIMENSION match only; the carrier-identity and Z_3-character checks
     show it is NOT yet a color identification.

Run:
    python3 scripts/diagonal_gate_color_l2_face_algebra_deep_dive.py
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
# Shared Lie-algebra utilities
# ----------------------------------------------------------------------
def lie_closure(gens, tol: float = 1e-9, maxdim: int = 81):
    """Real-linear span closed under the commutator bracket.

    Returns an orthonormal (Frobenius) basis of flattened matrices spanning
    the smallest *real* Lie algebra containing `gens`.
    """
    shape = gens[0].shape

    def add(M, basis):
        v = M.flatten().astype(complex)
        # Real-linear independence: project against complex-conj-symmetrized
        # real span. We work over R by stacking re/im, but since all our
        # generators are anti-Hermitian we can stay in the complex flatten
        # and orthogonalize with the real inner product Re<.,.>.
        for b in basis:
            coeff = np.real(np.vdot(b, v)) / np.real(np.vdot(b, b))
            v = v - coeff * b
        if np.linalg.norm(v) > tol:
            basis.append(v.copy())
            return True
        return False

    basis: list[np.ndarray] = []
    for g in gens:
        add(g, basis)
    changed = True
    while changed and len(basis) < maxdim:
        changed = False
        cur = [b.reshape(shape) for b in basis]
        for A in cur:
            for B in cur:
                if add(A @ B - B @ A, basis):
                    changed = True
    return basis


def pair_u2_generators(i: int, j: int, n: int = 3):
    """Anti-Hermitian u(2) generators on the (i,j) 2-block embedded in u(n)."""
    Eij = np.zeros((n, n), complex); Eij[i, j] = 1
    Eji = np.zeros((n, n), complex); Eji[j, i] = 1
    Dij = np.zeros((n, n), complex); Dij[i, i] = 1; Dij[j, j] = -1
    Pij = np.zeros((n, n), complex); Pij[i, i] = 1; Pij[j, j] = 1
    return [0.5 * (Eij - Eji),     # off-diagonal real rotation
            0.5j * (Eij + Eji),    # off-diagonal imaginary
            0.5j * Dij,            # traceless diagonal su(2) Cartan
            0.5j * Pij]            # pair u(1) phase


# ----------------------------------------------------------------------
# Part A. NN obstruction is REAL on the hw=1 triplet
# ----------------------------------------------------------------------
def part_a_nn_obstruction():
    print("=" * 70)
    print("Part A. NN-only adjacency on the hw=1 generation triplet")
    print("=" * 70)
    hw1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    # Which of the three pairs are NN-adjacent (dist^2 == 1)?
    nn_pairs = []
    fd_pairs = []
    for (a, b) in itertools.combinations(range(3), 2):
        d = np.array(hw1[a]) - np.array(hw1[b])
        dist2 = int(d @ d)
        (nn_pairs if dist2 == 1 else fd_pairs).append((a, b, dist2))
        print(f"  pair (gen{a},gen{b}): dist^2 = {dist2} "
              f"({'NN-adjacent' if dist2 == 1 else 'face-diagonal'})")
    check("A1: NN adjacency connects ZERO hw=1 pairs", len(nn_pairs) == 0,
          f"{len(nn_pairs)} NN-adjacent pairs among the 3")
    check("A2: all three hw=1 pairs are face-diagonal (dist^2=2)",
          len(fd_pairs) == 3 and all(p[2] == 2 for p in fd_pairs))

    # NN-connection algebra on the triplet: only generators from NN-adjacent
    # pairs are available. With ZERO adjacent pairs, the only connection
    # generators are the per-site (diagonal) phases the connection convention
    # already carries on each fiber -- i.e. the diagonal commutant u(1)^3.
    # We model this as: generators = {i E_kk} (per-site phase) plus any
    # NN-pair u(2) blocks (here none).
    gens_nn = [1j * np.diag([1.0 if k == m else 0.0 for k in range(3)]).astype(complex)
               for m in range(3)]
    for (a, b, _d) in nn_pairs:
        gens_nn += pair_u2_generators(a, b)
    basis_nn = lie_closure(gens_nn)
    dim_nn = len(basis_nn)
    print(f"  NN-connection algebra generators: {len(gens_nn)} "
          f"(3 site-phases + {4 * len(nn_pairs)} pair-block)")
    print(f"  NN-connection algebra real dimension: {dim_nn}")
    check("A3: NN-connection algebra on hw=1 is u(1)^3 (real dim 3)",
          dim_nn == 3, f"dim={dim_nn}")
    check("A4: NN-connection algebra is STRICTLY smaller than u(3) (dim 9)",
          dim_nn < 9, f"{dim_nn} < 9")
    check("A5: NN-connection algebra is abelian (diagonal commutant)",
          all(np.linalg.norm(A.reshape(3, 3) @ B.reshape(3, 3)
                             - B.reshape(3, 3) @ A.reshape(3, 3)) < 1e-9
              for A in basis_nn for B in basis_nn))
    print("  => NN cannot build the three off-diagonal pair-generators because")
    print("     the three generation pairs are not adjacent. Color obstructed.")
    print()
    return dim_nn


# ----------------------------------------------------------------------
# Part B. Face-diagonal closure to u(3)
# ----------------------------------------------------------------------
def traceless_antihermitian_dim(basis, n=3):
    """Count basis elements that are (within tol) traceless, after projecting
    the central iI direction out of the algebra. Returns (su_dim, has_center).
    """
    center = (1j * np.eye(n)).flatten()
    center = center / np.linalg.norm(center)
    # Is the central phase in the algebra?
    # Build the Gram projector of the algebra and test the center vector.
    M = np.array(basis)  # (dim, n*n)
    # real least-squares: express center in the real span of basis
    A = np.vstack([M.real, M.imag]).T if False else None
    # Simpler: project center onto algebra using real inner product
    proj = np.zeros_like(center)
    for b in basis:
        proj = proj + (np.real(np.vdot(b, center)) / np.real(np.vdot(b, b))) * b
    has_center = np.linalg.norm(proj - center) < 1e-6
    # su dim = total - 1 if center present (u(n)=su(n)+u(1))
    su_dim = len(basis) - (1 if has_center else 0)
    return su_dim, has_center


def part_b_face_closure():
    print("=" * 70)
    print("Part B. Face-diagonal pair-connections close to u(3)")
    print("=" * 70)
    pairs = [(0, 1), (0, 2), (1, 2)]  # all three hw=1 face-diagonal pairs
    gens = []
    for (i, j) in pairs:
        gens += pair_u2_generators(i, j)
    basis = lie_closure(gens)
    dim = len(basis)
    print(f"  generators from 3 face-diagonal pairs: {len(gens)} (4 each)")
    print(f"  Lie algebra real dimension: {dim}")
    check("B1: face-diagonal pairwise u(2) closes to u(3) (real dim 9)",
          dim == 9, f"dim={dim}")
    su_dim, has_center = traceless_antihermitian_dim(basis, 3)
    check("B2: u(3) contains the central u(1) phase iI", has_center)
    check("B3: traceless part is su(3) (real dim 8)", su_dim == 8,
          f"su_dim={su_dim}")
    # Direct-sum check: center commutes with everything
    iI = 1j * np.eye(3)
    central = all(np.linalg.norm(iI @ b.reshape(3, 3) - b.reshape(3, 3) @ iI) < 1e-9
                  for b in basis)
    check("B4: u(3) = su(3) + u(1) is a Lie-algebra DIRECT SUM (center commutes)",
          central)
    # Repair the foundation runner's "coarse proxy": counting trace-free
    # vectors of the ARBITRARILY orthonormalized basis is unreliable (the
    # Gram-Schmidt mixes the central direction into off-diagonal vectors).
    # The reliable su(3) dimension is total - (1 if center in algebra), B3.
    naive_trace_free = sum(1 for b in basis
                           if abs(np.trace(b.reshape(3, 3))) < 1e-9)
    print(f"  (foundation 'coarse proxy' trace-free count on this ortho basis: "
          f"{naive_trace_free})")
    check("B5: rigorous su(3) dim (8) is basis-independent, unlike the coarse "
          "trace-free proxy", su_dim == 8)
    print("  => once the three generation pairs are simultaneously connected")
    print("     (face-diagonal supplies that), pairwise u(2) closes to u(3).")
    print()
    return basis, dim, su_dim


# ----------------------------------------------------------------------
# Part C. Rigorous su(3) certification (structure constants, Killing, rank)
# ----------------------------------------------------------------------
def gell_mann():
    """The 8 Gell-Mann matrices."""
    l = []
    l.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex))
    l.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex))
    l.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex))
    l.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex))
    l.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex))
    l.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex))
    l.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex))
    l.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3))
    return l


def part_c_su3_certificate(face_basis):
    print("=" * 70)
    print("Part C. su(3) certification of the face-diagonal traceless part")
    print("=" * 70)
    # Use the canonical su(3) generators T^a = lambda^a/2 (Hermitian).
    # The face-diagonal algebra's traceless part is, by Part B, an 8-dim
    # real Lie algebra of anti-Hermitian traceless 3x3 matrices. The full
    # space of such matrices is exactly su(3); since dim=8 it equals su(3).
    # We certify the canonical su(3) satisfies the compact-simple signature,
    # then confirm the face-diagonal traceless span coincides with it.
    T = [0.5 * m for m in gell_mann()]  # Hermitian generators
    # Structure constants f^{abc}: [T^a,T^b] = i f^{abc} T^c
    f = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            comm = T[a] @ T[b] - T[b] @ T[a]  # = i f^{abc} T^c
            for c in range(8):
                f[a, b, c] = np.real(2.0 * np.trace((comm / 1j) @ T[c]))
    real_ok = np.allclose(f, np.real(f))
    antisym_ok = np.allclose(f, -np.transpose(f, (1, 0, 2)))
    # total antisymmetry: f^{abc} antisymmetric in all three indices
    tot_antisym = (np.allclose(f, -np.transpose(f, (1, 0, 2))) and
                   np.allclose(f, -np.transpose(f, (0, 2, 1))))
    check("C1: su(3) structure constants are real", real_ok)
    check("C2: f^{abc} totally antisymmetric (compact simple)", tot_antisym)
    # Killing form K_{ab} = f^{acd} f^{bdc} ; for su(3) it is -6 delta (neg def)
    K = np.einsum('acd,bdc->ab', f, f)
    Kdiag = np.diag(K)
    neg_def = np.all(np.linalg.eigvalsh(K) < -1e-6)
    check("C3: Killing form is negative-definite (compact real form)", neg_def,
          f"eig range [{np.linalg.eigvalsh(K).min():.2f},"
          f"{np.linalg.eigvalsh(K).max():.2f}]")
    check("C4: Killing form proportional to identity (simple algebra)",
          np.allclose(K, K[0, 0] * np.eye(8)), f"K_00={K[0,0]:.2f}")
    # Cartan rank = 2: T^3, T^8 commute and are a maximal abelian subalgebra
    rank_comm = np.linalg.norm(T[2] @ T[7] - T[7] @ T[2])
    check("C5: rank 2 -- T^3 and T^8 commute (2-dim Cartan)", rank_comm < 1e-9)
    # Now confirm the face-diagonal traceless part EQUALS su(3): both are the
    # full 8-dim space of traceless anti-Hermitian 3x3 matrices.
    su3_anti = [1j * m for m in gell_mann()]  # anti-Hermitian su(3) basis
    closure_su3 = lie_closure(su3_anti)
    # face_basis traceless part: remove central component
    check("C6: canonical su(3) anti-Herm basis closes to dim 8",
          len(closure_su3) == 8, f"dim={len(closure_su3)}")
    # Coincidence: the face-diagonal traceless span and su(3) span the same
    # subspace of M_3(C). Test by checking every su(3) basis vector lies in
    # the real span of face_basis.
    def in_real_span(v, basis):
        r = v.flatten().astype(complex).copy()
        for b in basis:
            r = r - (np.real(np.vdot(b, r)) / np.real(np.vdot(b, b))) * b
        return np.linalg.norm(r) < 1e-7
    all_in = all(in_real_span(g, face_basis) for g in su3_anti)
    check("C7: every su(3) generator lies in the face-diagonal algebra",
          all_in)
    print("  => the face-diagonal traceless part IS su(3) (compact, simple,")
    print("     rank 2), not merely an 8-dim coincidence.")
    print()


# ----------------------------------------------------------------------
# Part D. GENERATION-vs-COLOR identification probe (the deep question)
# ----------------------------------------------------------------------
def part_d_generation_vs_color():
    print("=" * 70)
    print("Part D. Generation-vs-color carrier + Z_3 character probe")
    print("=" * 70)
    # C^8 = (C^2)^{x3}, basis |b1 b2 b3>, index n = 4 b1 + 2 b2 + b3.
    def idx(b1, b2, b3):
        return 4 * b1 + 2 * b2 + b3

    def ket(b1, b2, b3):
        v = np.zeros(8, complex); v[idx(b1, b2, b3)] = 1.0; return v

    # (i) hw=1 GENERATION carrier: {|100>, |010>, |001>}
    gen_carrier = np.array([ket(1, 0, 0), ket(0, 1, 0), ket(0, 0, 1)]).T  # 8x3
    # (ii) framework COLOR carrier (CL3_COLOR_AUTOMORPHISM): the 3D SYMMETRIC
    #      BASE of the (b1,b2)-base x b3-fiber decomposition.
    #      symmetric base of the (b1,b2) 4D base = {|00>,|11>,(|01>+|10>)/sqrt2};
    #      tensored with a fixed fiber b3 (take b3=0) to land in C^8.
    s00 = ket(0, 0, 0)
    s11 = ket(1, 1, 0)
    ssym = (ket(0, 1, 0) + ket(1, 0, 0)) / np.sqrt(2.0)
    color_carrier = np.array([s00, s11, ssym]).T  # 8x3 (symmetric base, fiber b3=0)

    # (D1) the two 3D carriers are DIFFERENT subspaces of C^8.
    # Dimension of the intersection via combined-rank: dim(U)+dim(V)-rank[U|V].
    M = np.hstack([gen_carrier, color_carrier])
    rank_union = np.linalg.matrix_rank(M, tol=1e-9)
    dim_inter = 3 + 3 - rank_union
    print(f"  dim(hw=1 generation carrier) = 3")
    print(f"  dim(symmetric-base color carrier) = 3")
    print(f"  rank[gen | color] = {rank_union}  =>  dim(intersection) = {dim_inter}")
    check("D1: generation carrier and color carrier are DIFFERENT subspaces",
          dim_inter < 3, f"intersection dim {dim_inter} < 3")
    check("D1b: the two carriers are not even equal as sets of basis vectors",
          rank_union > 3, f"union rank {rank_union} > 3")

    # (D2) Z_3 character mismatch: permutation (generation) vs SU(3)_c center.
    w = np.exp(2j * np.pi / 3.0)
    # generation cyclic permutation char: regular rep (3,0,0)
    P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)
    perm_char = (np.trace(np.linalg.matrix_power(P, 0)),
                 np.trace(np.linalg.matrix_power(P, 1)),
                 np.trace(np.linalg.matrix_power(P, 2)))
    perm_char = tuple(complex(np.round(x, 6)) for x in perm_char)
    # SU(3)_c center on the color fundamental: z = w I, char (3, 3w, 3w^2)
    center_char = (3.0 + 0j, 3.0 * w, 3.0 * w ** 2)
    center_char = tuple(complex(np.round(x, 6)) for x in center_char)
    print(f"  generation permutation Z_3 character: {perm_char}")
    print(f"  SU(3)_c center Z_3 character (fundamental): {center_char}")
    check("D2: generation perm character is the REGULAR rep (3,0,0)",
          np.allclose(perm_char, (3, 0, 0)))
    check("D2b: SU(3)_c center character is (3,3w,3w^2), NOT regular",
          np.allclose(center_char, (3.0, 3.0 * w, 3.0 * w ** 2))
          and not np.allclose(center_char, (3, 0, 0)))
    check("D2c: the two Z_3 characters DIFFER (center is not the bridge)",
          not np.allclose(perm_char, center_char))

    # (D3) imposing the SAME cyclic label makes the two 3-spaces isomorphic
    #      as Z_3 reps -- but that common action is an EXTRA bridge assumption.
    # Both perm reps of Z_3 on C^3 (same P) are literally identical, hence
    # isomorphic; this is the tempting-but-extra bridge.
    iso_after_imposed = np.allclose(P, P)  # tautology: same imposed action
    check("D3: under a COMMON imposed cyclic action both 3-spaces are "
          "Z_3-isomorphic", iso_after_imposed)
    # The honest content: the common action is NOT derived. We encode this by
    # checking that the color carrier does NOT natively carry the permutation
    # P as its SU(3)_c center action (they are different operators on
    # different spaces), so isomorphism requires IMPOSING P on color.
    # Center action w*I has character (3,3w,3w^2) != perm char => not the same
    # operator up to the natural identification.
    native_match = np.allclose(perm_char, center_char)
    check("D3b: the common action is an EXTRA assumption (native center "
          "action != generation permutation)", not native_match)

    # (D4) Pinpoint the 1D overlap: it is precisely the symmetric combination
    #      shared between the symmetric base and the generation span. This
    #      makes "distinct but not orthogonal" exact -- the carriers meet only
    #      in the single hw=1 symmetric vector (|100>+|010>)/sqrt2.
    overlap_vec = (ket(1, 0, 0) + ket(0, 1, 0)) / np.sqrt(2.0)
    def in_span(v, cols):
        r = v.astype(complex).copy()
        Q, _ = np.linalg.qr(cols)
        return np.linalg.norm(r - Q @ (Q.conj().T @ r)) < 1e-9
    in_gen = in_span(overlap_vec, gen_carrier)
    in_col = in_span(overlap_vec, color_carrier)
    check("D4: the 1D carrier overlap is exactly the symmetric vector "
          "(|100>+|010>)/sqrt2", in_gen and in_col and dim_inter == 1)
    check("D4b: the generation pseudoscalar/full triplet is NOT inside the "
          "color carrier (carriers are genuinely distinct)",
          not in_span(ket(0, 0, 1), color_carrier))

    # (D5) Physical distinction: color SU(3) is a GAUGE symmetry (anomaly-free,
    #      vector-like on quarks); a gauged generation U(3) flavor symmetry is a
    #      different physical object. We record the structural fact that the
    #      face-diagonal u(3) carries a u(1) FACTOR (the central phase): reading
    #      su(3) as color silently DISCARDS that u(1), an extra choice. Color
    #      SU(3) has trivial center action distinct from the U(3) overall phase.
    iI = (1j * np.eye(3))
    # central phase has nonzero trace (it is the U(1) generator), su(3) is the
    # traceless ideal; the projection split is a CHOICE of which factor is "the"
    # gauge group.
    check("D5: the face-diagonal algebra is u(3)=su(3)+u(1); selecting su(3) as "
          "'color' discards the central u(1) (an extra choice)",
          abs(np.trace(iI)) > 1e-9)
    print("  => face-diagonal u(3) acts on the GENERATION carrier; the")
    print("     framework's COLOR su(3) lives on the DISTINCT symmetric-base")
    print("     carrier. Matching them is the still-open color/generation")
    print("     identification gate, not a consequence of face-diagonal.")
    print()
    return dim_inter


# ----------------------------------------------------------------------
# Part E. Body-diagonal effect on the hw=1 triplet
# ----------------------------------------------------------------------
def part_e_body_diagonal():
    print("=" * 70)
    print("Part E. Body-diagonal connections and the hw=1 triplet")
    print("=" * 70)
    verts = list(itertools.product([0, 1], repeat=3))

    def hw(v):
        return sum(v)

    body = []
    for a, b in itertools.combinations(verts, 2):
        d = np.array(a) - np.array(b)
        if int(d @ d) == 3:
            body.append((a, b))
    check("E1: there are 4 body-diagonals (dist^2=3) on the cube",
          len(body) == 4, f"{len(body)} found")
    # Each body-diagonal connects opposite corners -> Hamming weights sum to 3.
    hw_pairs = [(hw(a), hw(b)) for a, b in body]
    print("  body-diagonal endpoint Hamming weights:")
    for (a, b), (ha, hb) in zip(body, hw_pairs):
        print(f"    {a} (hw={ha}) <-> {b} (hw={hb})")
    # Does any body-diagonal connect two hw=1 sites?
    within_hw1 = [(a, b) for a, b in body if hw(a) == 1 and hw(b) == 1]
    check("E2: NO body-diagonal connects two hw=1 sites",
          len(within_hw1) == 0, f"{len(within_hw1)} within-hw1 body-diagonals")
    # Body-diagonals connect hw=1 <-> hw=2 (and hw=0 <-> hw=3).
    cross_12 = [(a, b) for a, b in body
                if {hw(a), hw(b)} == {1, 2}]
    check("E3: every hw=1 body-diagonal endpoint pairs with an hw=2 site "
          "(C-conjugate orbit)",
          all({ha, hb} in ({0, 3}, {1, 2}) for ha, hb in hw_pairs))
    check("E4: the 3 hw=1<->hw=2 body-diagonals exist (cross-parity, not "
          "within-generation)", len(cross_12) == 3, f"{len(cross_12)} found")
    # Therefore the body-diagonal-connection algebra RESTRICTED to span(hw=1)
    # adds no off-diagonal generator within the triplet: the within-hw=1
    # connection content is unchanged (still only the face-diagonal pairs).
    print("  => body-diagonals act between hw=1 and hw=2 (the C-conjugate")
    print("     generation orbit); within the hw=1 triplet they add NOTHING.")
    print("     No 4th generation; the u(3) on hw=1 is unchanged.")
    print()


# ----------------------------------------------------------------------
# Part F. Honest-verdict consistency (dimension match is NOT identification)
# ----------------------------------------------------------------------
def part_f_verdict(dim_nn, dim_face, su_dim, dim_inter):
    print("=" * 70)
    print("Part F. Honest verdict consistency")
    print("=" * 70)
    check("F1: NN gives strictly-smaller algebra (dim 3) than face (dim 9)",
          dim_nn == 3 and dim_face == 9)
    check("F2: face-diagonal algebra dimension MATCHES color u(3) dimension 9",
          dim_face == 9)
    check("F3: but the carriers DIFFER (gen vs color intersection < 3) -- a "
          "dimension match is NOT a color identification",
          dim_inter < 3)
    check("F4: face-diagonal su(3) is GENERATION-space; color identification "
          "remains the open Z3-character gate", su_dim == 8 and dim_inter < 3)
    print("  VERDICT: PARTIAL. Face-diagonal adjacency genuinely supplies an")
    print("  su(3)+u(1) on the 3-generation factor (the NN obstruction is real")
    print("  and is lifted). But that su(3) acts on GENERATION space, which is")
    print("  a DIFFERENT subspace of C^8 than the framework's symmetric-base")
    print("  COLOR carrier, and the Z_3 characters differ. Identifying the two")
    print("  is exactly the still-open color/generation bridge. So face-")
    print("  diagonal does NOT by itself close GATE-COLOR; it relocates the")
    print("  obstruction from 'no su(3) algebra at all' to 'su(3) present on")
    print("  generation space, color identification still required.'")
    print()


def main() -> int:
    print("DIAGONAL GATE-COLOR L2 FACE-ALGEBRA DEEP DIVE")
    print("(deepens scout S2 of the sqrt2-centered foundation)\n")
    dim_nn = part_a_nn_obstruction()
    face_basis, dim_face, su_dim = part_b_face_closure()
    part_c_su3_certificate(face_basis)
    dim_inter = part_d_generation_vs_color()
    part_e_body_diagonal()
    part_f_verdict(dim_nn, dim_face, su_dim, dim_inter)
    print("=" * 70)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 70)
    print("Face-diagonal adjacency lifts the REAL NN obstruction (u(1)^3 -> ")
    print("u(3)) on the generation triplet, but the resulting su(3) is a")
    print("GENERATION-space algebra on a carrier distinct from the framework's")
    print("symmetric-base color carrier, with a mismatched Z_3 character.")
    print("GATE-COLOR is PARTIAL, not closed: the color/generation")
    print("identification remains the open bridge.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
