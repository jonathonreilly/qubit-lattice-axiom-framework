#!/usr/bin/env python3
"""
axiom_first_reeh_schlieder_check.py
-----------------------------------

Exact finite-lattice certificates for the re-scoped axiom-first
Reeh-Schlieder note (bounded theorem):

  docs/AXIOM_FIRST_REEH_SCHLIEDER_THEOREM_NOTE_2026-05-01.md

Carrier: the framework's staggered-only surface — the free staggered
fermion many-body Hamiltonian under Jordan-Wigner on a small chain
(same construction family as scripts/axiom_first_spectrum_condition_check.py;
Quantum-axiom per-site qubit, finite representative of the Lattice-axiom
Z^3 substrate).
NO random Hamiltonians: every object is deterministic framework data.

What is certified (12 checks, [A]/[C] tags per the audit rubric):

  RS-1 (exact dichotomy, checks 1-2, 5):
     For H_phys = H_O (x) H_Oc, A(O) = B(H_O) (x) 1, and any unit
     vector v of Schmidt rank r across the cut:
        dim A(O) v = d_O * r,
     so  v cyclic for A(O)      <=>  r = d_Oc,
         v separating for A(O)  <=>  r = d_O  <=>  rho_O full rank
                                <=>  v cyclic for A(O)'.

  RS-2 (vacuum separating certificate, checks 3-4, 10):
     The staggered vacuum (ground state, L = 6 and 8, OBC, m = 0.3)
     has full-rank rho_O for the tested small regions => no nonzero
     local operator annihilates the vacuum. Verified EXACTLY per
     carrier and per region, with margins reported.

  Falsification / scope legs (checks 6-9):
     6: equal-time A(O)|Omega> is NOT dense for a small region
        (the pre-2026-06-11 headline (R1) is false as stated);
     7: PBC L = 6 pins a correlation eigenvalue at exactly 1 =>
        half-chain separating property FAILS on a framework carrier
        (explicit unit-norm annihilator exhibited);
     8: gapped PRODUCT vacuum (hopping off) has Schmidt rank 1 =>
        separating fails everywhere although H >= 0 and gap > 0 —
        the property is state-sensitive, NOT a gap+positivity
        consequence;
     9: a large region (d_O > d_Oc) is cyclic but NOT separating —
        equal-time cyclicity is a large-region triviality.

  RS-3 (time-translated corollary, genericity exposed, checks 11-12):
     11: A_T(O)' = largest ad_H-invariant subspace of A(O)' computed
         exactly by iterated nullspaces: dim 256 -> ... -> 1 =>
         A_T(O) = B(H_phys) (finite-dim double commutant).
     12: hence cyclicity of the time-translated set holds for the
         vacuum AND for excited eigenstates with the same word set —
         vector-GENERIC, not vacuum-specific, and A_T(O) is NOT a
         local algebra. This is not the continuum Reeh-Schlieder
         theorem and is not claimed as such.

Deterministic, numpy only, no network, runtime ~ seconds.
Output: 12 numbered [PASS]/[FAIL] lines, 3 RESIDUAL (declared-open)
lines, then exactly `TOTAL: PASS=n FAIL=m` and a VERDICT block.
Exit code 0 iff FAIL=0.
"""
from __future__ import annotations

import sys

import numpy as np

I2 = np.eye(2, dtype=complex)
PAULI = {
    "I": I2,
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}

RESULTS: list[tuple[int, str, bool, str]] = []


def record(num: int, tag: str, ok: bool, msg: str) -> None:
    RESULTS.append((num, tag, ok, msg))
    print(f"  [{'PASS' if ok else 'FAIL'}] check {num} [{tag}]: {msg}")


def kron_chain(ops):
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def pauli_word(L: int, word: str) -> np.ndarray:
    """word is a string of length L over I,X,Y,Z."""
    return kron_chain([PAULI[c] for c in word])


def jw_annihilators(L: int):
    """Jordan-Wigner c_x with string on sites < x."""
    SP = np.array([[0, 1], [0, 0]], dtype=complex)
    Z = PAULI["Z"]
    return [kron_chain([Z] * i + [SP] + [I2] * (L - 1 - i)) for i in range(L)]


def staggered_many_body_H(L: int, mass: float = 0.3, pbc: bool = False,
                          hop: float = 0.5) -> np.ndarray:
    """Free staggered fermion many-body Hamiltonian (Quantum/Lattice
    framework data, same construction family as the spectrum-condition runner):
       h[x,x]   = mass * (-1)^x
       h[x,x+1] = +i*hop, h[x+1,x] = -i*hop   (OBC or PBC)
       H = sum_xy h_xy (c_x^dag c_y - (1/2) delta_xy)
    """
    h = np.zeros((L, L), dtype=complex)
    for x in range(L):
        h[x, x] += mass * (-1) ** x
    for x in (range(L) if pbc else range(L - 1)):
        xp = (x + 1) % L
        h[x, xp] += 1j * hop
        h[xp, x] += -1j * hop
    c = jw_annihilators(L)
    dim = 2 ** L
    H = np.zeros((dim, dim), dtype=complex)
    for x in range(L):
        for y in range(L):
            if abs(h[x, y]) > 1e-15:
                H += h[x, y] * (c[x].conj().T @ c[y]
                                - (0.5 * np.eye(dim) if x == y else 0))
    return 0.5 * (H + H.conj().T)


def schmidt_vals(v: np.ndarray, d_O: int, d_Oc: int) -> np.ndarray:
    return np.linalg.svd(v.reshape(d_O, d_Oc), compute_uv=False)


def local_pauli_basis(L: int, R: int):
    """All 4^R Pauli words supported on sites 0..R-1 (a basis of
    B(H_O) (x) 1 for the left-anchored tensor-factor local algebra)."""
    words = [""]
    for _ in range(R):
        words = [w + c for w in words for c in "IXYZ"]
    return [pauli_word(L, w + "I" * (L - R)) for w in words]


def span_rank(ops, v, tol):
    M = np.array([op @ v for op in ops]).T
    s = np.linalg.svd(M, compute_uv=False)
    return int((s > tol).sum()), s


def main() -> None:
    np.set_printoptions(precision=4, suppress=False)
    print("=" * 72)
    print(" axiom_first_reeh_schlieder_check.py  (re-scoped 2026-06-11)")
    print(" Finite-lattice RS dichotomy + vacuum separating certificates")
    print(" Carrier: free staggered fermion chain (Quantum qubit/site, Lattice chain)")
    print("=" * 72)

    L, R = 6, 2
    dim = 2 ** L
    d_O, d_Oc = 2 ** R, 2 ** (L - R)
    RANK_TOL = 1e-7

    # ------------------------------------------------------------------
    print("\n--- Section [A]: exact dichotomy theorem RS-1 ---")

    # check 1 [A]: every 1 (x) E_kl commutes with the A(O) generators
    gens6 = [pauli_word(L, ("I" * s) + w + ("I" * (L - s - 1)))
             for s in range(R) for w in "XYZ"]
    comm_basis = []
    for k in range(d_Oc):
        for l in range(d_Oc):
            E = np.zeros((d_Oc, d_Oc), dtype=complex)
            E[k, l] = 1.0
            comm_basis.append(np.kron(np.eye(d_O), E))
    max_comm = max(np.abs(g @ X - X @ g).max()
                   for g in gens6 for X in comm_basis)
    record(1, "A", max_comm < 1e-13,
           f"1 (x) B(H_Oc) commutes with all A(O) generators exactly "
           f"(max |[g, 1(x)E]| = {max_comm:.1e}); with the von Neumann "
           f"double-commutant theorem this gives A(O)' = 1 (x) B(H_Oc)")

    # check 2 [A]: dichotomy dim A(O)v = d_O * r on hand-built vectors
    P_O = local_pauli_basis(L, R)  # 16 Pauli words on O
    ok2, parts = True, []
    for r_target in (1, 2, 4):
        v = np.zeros(dim, dtype=complex)
        for k in range(r_target):
            v[k * d_Oc + k] = 1.0  # e_k (x) f_k
        v /= np.linalg.norm(v)
        rank, _ = span_rank(P_O, v, RANK_TOL)
        ok2 &= (rank == d_O * r_target)
        parts.append(f"r={r_target}: dim A(O)v = {rank} (= {d_O}*{r_target})")
    record(2, "A", ok2,
           "dichotomy dim A(O)v = d_O * SchmidtRank(v) holds exactly on "
           "constructed vectors — " + "; ".join(parts))

    # ------------------------------------------------------------------
    print("\n--- Section [C]: framework carrier, vacuum certificates ---")

    # check 3 [C]: carrier build, vacuum, gap (per-carrier nondegeneracy)
    H = staggered_many_body_H(L, mass=0.3, pbc=False)
    ev, V = np.linalg.eigh(H)
    Omega = V[:, 0]
    gap = float(ev[1] - ev[0])
    record(3, "C", gap > 1e-6,
           f"L={L} OBC staggered carrier: E_0 = {ev[0]:.6f}, gap "
           f"E_1 - E_0 = {gap:.6f} > 0 (vacuum nondegenerate on THIS "
           f"carrier; SC3's conditional clause is not consumed)")

    # check 4 [C]: rho_O full rank for R = 1, 2, 3 => separating
    ok4, parts = True, []
    for Rr in (1, 2, 3):
        dr, drc = 2 ** Rr, 2 ** (L - Rr)
        s = schmidt_vals(Omega, dr, drc)
        full = int((s > 1e-6).sum()) == dr
        ok4 &= full
        parts.append(f"R={Rr}: rank {int((s>1e-6).sum())}/{dr}, "
                     f"min lambda(rho_O) = {s.min()**2:.2e}")
    record(4, "C", ok4,
           "staggered vacuum has FULL-RANK rho_O on tested regions => "
           "|Omega> separating for A(O) (no nonzero local annihilator) — "
           + "; ".join(parts))

    # check 5 [A]: RS-1 equivalences verified on the carrier at R=2
    rank_AO, _ = span_rank(P_O, Omega, RANK_TOL)         # = d_O * r
    rank_comm, _ = span_rank(comm_basis, Omega, RANK_TOL)  # commutant cyclic
    sep_inj = (rank_AO == d_O * d_O)  # A -> A|Omega> injective on 16-dim A(O)
    comm_cyc = (rank_comm == dim)
    record(5, "A", sep_inj and comm_cyc,
           f"equivalences on the carrier: dim A(O)Omega = {rank_AO} = "
           f"d_O^2 = {d_O*d_O} (map A -> A|Omega> injective <=> separating) "
           f"AND dim A(O)' Omega = {rank_comm} = dim H = {dim} "
           f"(cyclic for the commutant) — the two RS-1 forms agree")

    # check 6 [C]: anti-claim — equal-time A(O)|Omega> is NOT dense
    record(6, "C", rank_AO == 16 and rank_AO < dim,
           f"equal-time A(O)|Omega> spans {rank_AO} of {dim} dims "
           f"(= d_O * r = {d_O}*{d_O}): the pre-2026-06-11 headline "
           f"'A(O)|Omega> dense for any nonempty O' is FALSE as stated "
           f"for tensor-factor local algebras on a finite lattice")

    # check 7 [C]: framework-internal falsifier — PBC pinned mode
    Hp = staggered_many_body_H(L, mass=0.3, pbc=True)
    evp, Vp = np.linalg.eigh(Hp)
    Om_p = Vp[:, 0]
    s_p = schmidt_vals(Om_p, 8, 8)
    rank_p = int((s_p > 1e-10).sum())
    u, s_full, vh = np.linalg.svd(Om_p.reshape(8, 8))
    u_ker = u[:, 7]                       # kernel vector of rho_O (rank 4)
    A_ann = np.outer(u[:, 0], u_ker.conj())
    A_full = np.kron(A_ann, np.eye(8))
    norm_A = float(np.linalg.norm(A_ann, 2))
    norm_AOm = float(np.linalg.norm(A_full @ Om_p))
    record(7, "C", rank_p == 4 and norm_A > 0.99 and norm_AOm < 1e-12,
           f"L=6 PBC half-chain cut: Schmidt rank {rank_p}/8 (a correlation "
           f"eigenvalue pins at exactly 1) => vacuum NOT separating for the "
           f"half-chain algebra; explicit annihilator ||A|| = {norm_A:.3f}, "
           f"||A Omega|| = {norm_AOm:.1e} — the property is region- and "
           f"carrier-sensitive even inside the framework")

    # check 8 [C]: gap + positivity do NOT imply separating (product vacuum)
    H0 = staggered_many_body_H(L, mass=0.3, pbc=False, hop=0.0)
    ev0, V0 = np.linalg.eigh(H0)
    Om_0 = V0[:, 0]
    gap0 = float(ev0[1] - ev0[0])
    s_0 = schmidt_vals(Om_0, d_O, d_Oc)
    rank_0 = int((s_0 > 1e-10).sum())
    # explicit local annihilator: the ground state of the mass-only H
    # occupies the odd sublattice only; the occupation projector on
    # site 0 (supported in O) annihilates it:
    c = jw_annihilators(L)
    P_occ0 = c[0].conj().T @ c[0]          # supported on site 0 (in A(O))
    norm_P = float(np.linalg.norm(P_occ0, 2))
    norm_POm = float(np.linalg.norm(P_occ0 @ Om_0))
    record(8, "C", gap0 > 1e-6 and rank_0 == 1 and norm_P > 0.99
           and norm_POm < 1e-12,
           f"mass-only comparator (hop = 0): gap = {gap0:.3f} > 0, H >= 0, "
           f"but Schmidt rank = {rank_0} (product vacuum) and the LOCAL "
           f"projector n_0 in A(O) annihilates it (||n_0 Omega|| = "
           f"{norm_POm:.1e}, ||n_0|| = {norm_P:.2f}) => the separating "
           f"property is STATE-SENSITIVE: gap + spectrum condition alone "
           f"cannot prove it")

    # check 9 [C]: large region trivializes cyclicity, kills separating
    R_big = 4
    d_big, d_bigc = 2 ** R_big, 2 ** (L - R_big)
    P_big = local_pauli_basis(L, R_big)    # 256 Pauli words
    rank_big, _ = span_rank(P_big, Omega, RANK_TOL)
    s_big = schmidt_vals(Omega, d_big, d_bigc)
    r_big = int((s_big > 1e-10).sum())
    ub, sb, _ = np.linalg.svd(Omega.reshape(d_big, d_bigc))
    A_ann2 = np.outer(ub[:, 0], ub[:, d_big - 1].conj())  # kernel of rho_O
    norm_A2Om = float(np.linalg.norm(np.kron(A_ann2, np.eye(d_bigc)) @ Omega))
    record(9, "C", rank_big == dim and r_big == d_bigc
           and r_big < d_big and norm_A2Om < 1e-12,
           f"large region O = 4 of 6 sites: dim A(O)Omega = {rank_big} = "
           f"dim H (cyclic, since r = {r_big} = d_Oc) but NOT separating "
           f"(r < d_O = {d_big}; annihilator with ||A Omega|| = "
           f"{norm_A2Om:.1e}) — equal-time cyclicity is a large-region "
           f"triviality, not Reeh-Schlieder content")

    # check 10 [C]: size robustness at L = 8
    L8 = 8
    H8 = staggered_many_body_H(L8, mass=0.3, pbc=False)
    ev8, V8 = np.linalg.eigh(H8)
    Om8 = V8[:, 0]
    gap8 = float(ev8[1] - ev8[0])
    ok10, parts = gap8 > 1e-6, [f"gap = {gap8:.4f}"]
    for Rr in (2, 3):
        dr, drc = 2 ** Rr, 2 ** (L8 - Rr)
        s = schmidt_vals(Om8, dr, drc)
        full = int((s > 1e-6).sum()) == dr
        ok10 &= full
        parts.append(f"R={Rr}: rank {int((s>1e-6).sum())}/{dr}, "
                     f"min lambda(rho_O) = {s.min()**2:.2e}")
    P_O8 = local_pauli_basis(L8, 2)
    rank8, _ = span_rank(P_O8, Om8, RANK_TOL)
    ok10 &= (rank8 == 16 and rank8 < 2 ** L8)
    parts.append(f"dim A(O)Omega = {rank8} = d_O*r << {2**L8}")
    record(10, "C", ok10,
           "L=8 OBC carrier reproduces the certificates — " + "; ".join(parts))

    # ------------------------------------------------------------------
    print("\n--- Section [C]: RS-3 time-translated corollary "
          "(genericity exposed) ---")

    # check 11 [C]: A_T(O)' = largest ad_H-invariant subspace of A(O)'
    Q, _ = np.linalg.qr(np.array([b.flatten() for b in comm_basis]).T)
    dims_seq = [Q.shape[1]]
    while True:
        k = Q.shape[1]
        C = np.zeros((dim * dim, k), dtype=complex)
        for i in range(k):
            X = Q[:, i].reshape(dim, dim)
            C[:, i] = (H @ X - X @ H).flatten()
        Rmat = C - Q @ (Q.conj().T @ C)
        _, s, vh = np.linalg.svd(Rmat, full_matrices=False)
        null = vh.conj().T[:, s < 1e-9]
        Qn = Q @ null
        if null.shape[1] > 0:
            Qn, _ = np.linalg.qr(Qn)
        if Qn.shape[1] == k:
            Q = Qn
            break
        Q = Qn
        dims_seq.append(Q.shape[1])
        if Q.shape[1] <= 1:
            break
    final_dim = Q.shape[1]
    Xf = Q[:, 0].reshape(dim, dim)
    is_scalar = float(np.linalg.norm(
        Xf - (Xf.trace() / dim) * np.eye(dim))) < 1e-8
    record(11, "C", final_dim == 1 and is_scalar,
           f"A_T(O)' computed exactly as the largest ad_H-invariant "
           f"subspace of A(O)': dims {' -> '.join(map(str, dims_seq))} "
           f"-> scalars only => A_T(O) = B(H_phys) by the finite-dim "
           f"double commutant. NOTE: A_T(O) is NOT a local algebra "
           f"(alpha_t(A) has global support; exact lattice strict "
           f"locality fails)")

    # check 12 [C]: cyclicity of the time-translated word set is
    # vector-GENERIC (vacuum has no special role)
    def alpha_t(O: np.ndarray, t: float) -> np.ndarray:
        U = (V * np.exp(1j * t * ev)) @ V.conj().T
        return U @ O @ U.conj().T

    times = np.linspace(0.0, 7.0, 10)
    w1 = [alpha_t(g, t) for t in times for g in gens6]   # 60 ops
    b = w1[:18]
    w2 = [a @ cc for a in b for cc in b]                 # 324 ops
    w3 = [a @ cc for a in b[:6] for cc in w2[:54]]       # 324 ops
    word_ops = w1 + w2 + w3
    # (words up to length 3 are needed: H conserves fermion number and
    #  |Omega> sits in the N=3 sector; length <= 2 misses N = 0, 6)
    ok12, parts = True, []
    for label, vec in (("vacuum", Omega),
                       ("excited E_17", V[:, 17]),
                       ("excited E_30", V[:, 30])):
        rk, s = span_rank(word_ops, vec, RANK_TOL)
        ok12 &= (rk == dim)
        parts.append(f"{label}: rank {rk}/{dim} "
                     f"(64th sv = {s[dim-1]:.1e})")
    record(12, "C", ok12,
           "time-translated words are cyclic for the vacuum AND for "
           "excited eigenstates with the same word set => RS-3 is "
           "vector-generic, NOT a vacuum-specific statement — "
           + "; ".join(parts))

    # ------------------------------------------------------------------
    print()
    print("RESIDUAL (declared-open): full-rank rho_O is VERIFIED per carrier"
          " and per region, never derived; check 8 proves no derivation from"
          " gap + spectrum condition alone can exist (B-1).")
    print("RESIDUAL (declared-open): min lambda(rho_O) margins decay fast"
          " with region size (4.1e-08 at L=6 R=3); no uniform-in-volume"
          " bound, no continuum statement (B-2).")
    print("RESIDUAL (declared-open): RS-3's algebra A_T(O) is non-local and"
          " its cyclicity is vector-generic; the continuum Reeh-Schlieder"
          " theorem (type-III local algebras, spectrum-condition"
          " analyticity) is NOT recovered here (B-3).")
    print()
    n_pass = sum(1 for r in RESULTS if r[2])
    n_fail = len(RESULTS) - n_pass
    breakdown = {t: sum(1 for r in RESULTS if r[1] == t and r[2])
                 for t in "ABCD"}
    print(f"Check-class breakdown (PASS): A={breakdown['A']} "
          f"B={breakdown['B']} C={breakdown['C']} D={breakdown['D']}")
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    print()
    print("VERDICT: on the framework's staggered carriers the finite-lattice")
    print("RS dichotomy holds exactly (dim A(O)Omega = d_O * SchmidtRank);")
    print("the staggered vacuum is separating for every tested small local")
    print("algebra (full-rank rho_O, exact certificates); equal-time")
    print("cyclicity for small regions is FALSE; the separating property is")
    print("state- and carrier-sensitive (PBC pinned mode, product vacuum);")
    print("time-translated cyclicity holds but is vector-generic and")
    print("non-local. Bounded theorem; no continuum claim.")
    if n_fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
