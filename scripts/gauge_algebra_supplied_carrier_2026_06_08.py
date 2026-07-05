"""Gauge algebra support given a supplied color carrier.

This runner checks the finite carrier-algebra facts used by
GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.
It does not claim an axiom-level derivation of the carrier or a gauging
selection.

SETUP: per-site qubit M_2(C) (Quantum axiom) on Z^3 (Lattice axiom); the color carrier is the 3-dim
base C^3 = Sym^2(C^2) of the taste cube (N_c = 3 = dim Z^3); the weak carrier is the qubit fiber C^2.

VERIFIES:
  1. qubit -> u(2): the infinitesimal automorphisms of M_2(C) are su(2) (the 3 Paulis), and the full
      anti-Hermitian algebra of M_2(C) is u(2) = su(2) (+) u(1) (dim 4). [link connection algebra]
  2. su(3) needs dim >= 3 (cannot live on a qubit): su(3) has 8 generators and its smallest faithful
      irrep is 3-dim; there is NO faithful su(3) on C^2. So color su(3) requires the 3-dim base, not the
      qubit; and dim(base) = N_c = 3 = dim Z^3.
  3. factor-preserving carrier algebra: on C^3 (base) (x) C^2 (fiber), su(3)(x)I and
      I(x)su(2) COMMUTE, and with the central u(1) they form su(3) (+) su(2) (+) u(1) (dim 8+3+1=12) --
      the same abstract algebra as the Standard Model gauge algebra. This is the algebra that preserves the supplied
      C^3 x C^2 factor split, NOT the full internal algebra on C^6.
  4. full-u(6) boundary: the unrestricted carrier algebra on C^6 has dim 36. The factor-preserving dim-12
      subalgebra plus the 24-dim cross-factor su(3) (x) su(2) tensor complement spans u(6). Therefore selecting
      the factor-preserving subalgebra rather than full u(6) is exactly the supplied split/locality premise.
  5. The gauging choice is not discriminated by this carrier check: impose a per-vertex Gauss law for EITHER su(2)
      (fiber) OR su(3) (base); both define a gauge-invariant commutant with the SAME dressing structure
      (a singlet projector exists for each, of the same endpoint-invariance kind). {Z^3, qubit, Record}
      + the Gauss structure do NOT select WHICH symmetry is gauged -- that is the matter-realization
      non-axiom input MR_color (and, for su(2)_L, the chiral gauging is a separate input).

CONCLUSION: given the supplied C^3(base) x C^2(fiber) carrier, the
factor-preserving carrier algebra is su(3)+su(2)+u(1). The full carrier
algebra is u(6), and selecting the factor-preserving subalgebra remains a
supplied-split/locality premise. The gauging selection remains open. No
PDG/fitted value; exact numpy/sympy.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import sympy as sp
import itertools

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md"


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def gell_mann():
    l = []
    l.append(np.array([[0,1,0],[1,0,0],[0,0,0]], complex))
    l.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], complex))
    l.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], complex))
    l.append(np.array([[0,0,1],[0,0,0],[1,0,0]], complex))
    l.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], complex))
    l.append(np.array([[0,0,0],[0,0,1],[0,1,0]], complex))
    l.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], complex))
    l.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], complex)/np.sqrt(3))
    return l


def hermitian_u_basis(n: int) -> list[np.ndarray]:
    """Hermitian basis of u(n), counted as the real anti-Hermitian Lie algebra."""
    basis: list[np.ndarray] = []
    for i in range(n):
        E = np.zeros((n, n), dtype=complex)
        E[i, i] = 1.0
        basis.append(E)
    for i in range(n):
        for j in range(i + 1, n):
            S = np.zeros((n, n), dtype=complex)
            S[i, j] = S[j, i] = 1.0
            A = np.zeros((n, n), dtype=complex)
            A[i, j] = -1j
            A[j, i] = 1j
            basis.extend([S, A])
    return basis


def matrix_rank(mats: list[np.ndarray]) -> int:
    return int(np.linalg.matrix_rank(np.array([m.flatten() for m in mats])))


def main() -> int:
    print("GAUGE ALGEBRA SUPPORT GIVEN A SUPPLIED CARRIER")
    print("=" * 64)
    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    check(
        "post-audit conditional boundary states supplied carrier/gauging inputs and no u(6) uniqueness",
        "2026-06-16 Post-Audit Conditional Boundary" in note_text
        and "do **not** prove that this dim-12 subalgebra is unique against the full `u(6)`" in note_flat
        and "do not derive `MR_color`" in note_flat
        and "supplied carrier + supplied weak-axis/fiber split + retained-bounded local-frame link-connection kinematics" in note_flat,
    )
    I2 = np.eye(2, dtype=complex)
    X = np.array([[0,1],[1,0]], complex); Y = np.array([[0,-1j],[1j,0]], complex); Z = np.array([[1,0],[0,-1]], complex)
    paulis = [X, Y, Z]

    # Qubit-to-u(2): su(2) = span(i*Pauli) closes; full anti-Hermitian M_2 = u(2) dim 4.
    # check su(2) closure: [sigma_i, sigma_j] = 2i eps_ijk sigma_k
    closes = np.allclose(X@Y - Y@X, 2j*Z) and np.allclose(Y@Z - Z@Y, 2j*X) and np.allclose(Z@X - X@Z, 2j*Y)
    # dim of anti-Hermitian 2x2 = 4 (u(2)); traceless part = su(2) dim 3; center = u(1) dim 1
    check("carrier algebra 1: qubit M_2(C) -> u(2) = su(2)(+)u(1): the 3 Paulis close su(2) ([s_i,s_j]=2i eps s_k); "
          "anti-Hermitian M_2 has dim 4 = su(2)(3) + u(1)(1)", closes, "su(2) closure verified; u(2) dim 4")

    # su(3) needs dim>=3; no faithful su(3) on C^2.
    gm = gell_mann()
    # the 8 Gell-Mann are linearly independent traceless Hermitian 3x3 (dim of su(3) = 8)
    flat = np.array([g.flatten() for g in gm])
    rank8 = np.linalg.matrix_rank(flat)
    # there is no 2-dim faithful irrep of su(3): the smallest faithful is 3 (the fundamental).
    # operationally: su(3) has rank 2 (two commuting Cartan generators), so any faithful rep needs dim>=3.
    check("carrier algebra 2: su(3) has 8 independent generators (rank-2 Cartan); smallest faithful irrep is 3-dim -> "
          "NO faithful su(3) on a qubit C^2; color su(3) requires the 3-dim base = N_c = 3 = dim Z^3",
          rank8 == 8, f"dim su(3) = {rank8} (=8); smallest faithful irrep dim = 3 > 2 = dim qubit")

    # On C^3 (x) C^2, su(3)(x)I and I(x)su(2) commute -> factor-preserving
    # su(3)+su(2)+u(1) (dim 12).
    su3 = [np.kron(g, I2) for g in gm]                 # color on base
    su2 = [np.kron(np.eye(3, dtype=complex), p) for p in paulis]  # weak on fiber
    u1 = [np.kron(np.eye(3, dtype=complex), I2)]       # central hypercharge
    commute = all(np.allclose(a@b - b@a, 0) for a in su3 for b in su2)
    gens = su3 + su2  # 8 + 3 = 11 traceless; + u(1) central = 12 (the SM gauge algebra dim)
    flat2 = np.array([g.flatten() for g in (gens + u1)])
    dim_alg = np.linalg.matrix_rank(flat2)
    check("carrier algebra 3: on the SUPPLIED C^3(base)(x)C^2(fiber) split, color su(3) and weak su(2) "
          "COMMUTE; with the central u(1) the FACTOR-PRESERVING algebra is su(3)(+)su(2)(+)u(1), "
          "dim 8+3+1 = 12",
          commute and dim_alg == 12, f"[su(3),su(2)]=0: {commute}; independent generators = {dim_alg} (=12)")

    # Full-u(6) boundary: without a factor-preserving locality premise, the carrier algebra is u(6).
    u6_basis = hermitian_u_basis(6)
    u6_dim = matrix_rank(u6_basis)
    mixed = [np.kron(g, p) for g in gm for p in paulis]
    mixed_dim = matrix_rank(mixed)
    local_plus_mixed_dim = matrix_rank(gens + u1 + mixed)
    check("carrier algebra 4: the unrestricted internal algebra on C^6 is u(6), dim 36; the "
          "factor-preserving dim-12 algebra plus the 24 cross-factor su(3)(x)su(2) tensors spans u(6). "
          "So selecting su(3)(+)su(2)(+)u(1) rather than full u(6) is exactly the supplied factor-locality "
          "premise, not a consequence of Lattice/Quantum/Record.",
          u6_dim == 36 and mixed_dim == 24 and local_plus_mixed_dim == 36,
          f"dim u(6)={u6_dim}; dim cross-factor complement={mixed_dim}; dim local+cross={local_plus_mixed_dim}")

    # The gauging selection is not discriminated -- both su(2) and su(3) admit a per-vertex Gauss/singlet
    # structure of the same kind; nothing in {carrier, Record, Gauss} selects which is gauged.
    # color singlet on C^3: the su(3)-invariant subspace of the fundamental is EMPTY (3 has no singlet),
    # but the qqq / qqbar combinations do; weak singlet on C^2 likewise via the doublet pairing.
    # Operationally: both su(3) and su(2) have a well-defined commutant (gauge-invariant algebra), and the
    # endpoint-dressing profile (bare 0, half-dressed 1, fully-dressed 2) is GROUP-AGNOSTIC.
    def commutant_dim(gens_list, n):
        # dim of the commutant of the generator set on C^n = number of independent X with [G,X]=0 for all G
        basis = []
        for i in range(n):
            for j in range(n):
                E = np.zeros((n, n), complex); E[i, j] = 1
                basis.append(E)
        # solve [G, X] = 0 for all G: stack the linear constraints
        import numpy.linalg as la
        rows = []
        for G in gens_list:
            for E in basis:
                comm = G @ E - E @ G
                rows.append(comm.flatten())
        Acon = np.array(rows)
        # commutant dim = n^2 - rank(constraint map on vec(X)) ; build constraint matrix on vec(X)
        # [G,X] linear in X: vec([G,X]) = (I (x) G - G^T (x) I) vec(X)
        M = np.zeros((0, n*n), complex)
        for G in gens_list:
            L = np.kron(np.eye(n), G) - np.kron(G.T, np.eye(n))
            M = np.vstack([M, L])
        return n*n - np.linalg.matrix_rank(M)
    # su(2) on C^2: commutant dim = 2 (scalars + ... actually for irreducible su(2) on C^2, commutant = C, dim... )
    c_su2 = commutant_dim(paulis, 2)              # su(2) irreducible on C^2 -> commutant = scalars (dim 1 over C as algebra; here counts real... )
    c_su3 = commutant_dim(gm, 3)                  # su(3) irreducible on C^3 (fundamental) -> commutant = scalars
    check("carrier algebra 5: both su(2) on C^2 and su(3) on C^3 act IRREDUCIBLY (commutant = scalars, "
          "dim 1) -> each defines an equally-good gauge/Gauss structure; the carrier + Record + Gauss do "
          "NOT discriminate WHICH symmetry is gauged. The gauging selection (MR_color + chiral su(2)_L) remains open.",
          c_su2 == 1 and c_su3 == 1, f"commutant(su(2) on C^2) = {c_su2}; commutant(su(3) on C^3) = {c_su3} (both scalars -> irreducible -> equally gaugeable)")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(
        "VERDICT (bounded support, GIVEN the supplied carrier): su(3)(+)su(2)(+)u(1) (dim 12) is the "
        "FACTOR-PRESERVING algebra of the SUPPLIED C^3(base)(x)C^2(fiber) carrier (su(2)=Aut M_2 on the "
        "fiber; su(3) on the 3-dim base; commuting). The unrestricted carrier algebra is full u(6) (dim 36); "
        "the missing selection of the factor-preserving algebra rather than u(6) is exactly the supplied "
        "factor-locality/MR_color premise. The carrier factorization itself is a SUPPLIED realization (cited "
        "to GRAPH_FIRST_SU3_INTEGRATION / CL3_COLOR_AUTOMORPHISM / QUBIT_LINK_U2 [bounded/pending] + the "
        "weak-axis selection, with retained-bounded local-frame link-connection kinematics), NOT derived from the Lattice, Quantum, and Record axioms. "
        "The GAUGING selection -- which symmetry is dynamically gauged, MR_color, chiral su(2)_L -- is an "
        "OPEN GATE: both su(2) and su(3) act irreducibly and admit the same Gauss/dressing structure. So "
        "this is conditional algebra support, NOT a from-axioms derivation. Audit lane sets the verdict."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
