#!/usr/bin/env python3
"""
axiom_first_spin_statistics_check.py
------------------------------------

Runner for the RE-SCOPED (2026-06-10) note

  docs/AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md

The note no longer claims that anticommutation is *forced* by the
baseline.  Its load-bearing claim is the free-boson / CCR exclusion
(S2'), plus Grassmann-calculus consequences (S1)/(S3)/(S4) that are
conditional on the declared Grassmann frame choice.  The hard-core-boson
vs Grassmann/CAR selection is OUT of this note's scope (owned by the
GL(F) predicate, see the 2026-06-10 conditional discriminator note).

Check groups (each line tagged, PASS/FAIL; final line
`TOTAL: PASS=n FAIL=0`):

  [S2]   CCR exclusion certificate.
         (a) Trace obstruction: in ANY finite-dimensional Hilbert
             space tr([a, a^+]) = 0, while the canonical CCR
             [a, a^+] = I demands tr = dim > 0.  Verified on the
             truncated bosonic ladder at several cutoffs K; the
             truncation defect ||[a,a^+] - I||_max = K is also
             reported (no finite truncation repairs the CCR).
         (b) Per-site finiteness readout: both Cl(3) chirality
             irreps rho_+/-(gamma_i) = +/- sigma_i satisfy the
             Clifford relations and have complex dimension 2
             (recomputing the cited cl3 note's U2/U4 dimensional
             conclusion used here).
         (c) Certificate: CCR => no finite-dim per-site space;
             substep-1 per-site space is dim 2 (finite) => the
             free-boson (CCR) realization is EXCLUDED.

  [FALS] Falsification / scope-boundary leg.  The hard-core-boson
         ladder a = sigma_+ VIOLATES the CCR hypothesis on-site:
         [a, a^+] = 1 - 2n != I, defect norm exactly 2, while having
         per-site dimension 2 and cross-site commutation.  Hence the
         hard-core frame is NOT excluded by this note's hypothesis:
         the exclusion reaches exactly the CCR branch and no further.
         (This makes the note's scope boundary runner-visible and
         reproduces the 2026-05-25 no-forcing note's third candidate.)

  [S1]   The note's displayed Grassmann relations (eq. (3)): realized
         EXACTLY by left exterior (wedge) multiplication of the 2N
         generators (chi_x, chibar_x) on the 2^{2N}-dimensional
         Grassmann algebra Lambda_{2N} itself -- ALL anticommutators
         zero, including every chibar/chi cross pair, all generators
         nilpotent, and the realization is faithful (left regular
         representation, rank 2^{2N}).
  [S1-CAR] SEPARATELY LABELED operator realization: the Jordan-Wigner
         construction on the 2^N-dim Fock space satisfies the CAR
         {c_i, c^+_j} = delta_ij I -- a NONZERO mixed anticommutator,
         hence a different algebra that is NOT a realization of
         eq. (3).  A refutation-shaped [S1] contrast line computes the
         difference (exterior cross anticommutators exactly 0 vs CAR
         mixed anticommutator exactly I) rather than asserting it.

  [S3]   Berezin determinant identity: |det(M)| = |Pf(A)| for the
         antisymmetrised quadratic form of the canonical staggered
         Dirac-Wilson matrix (exhibit instance; the identity is
         generic in M).

  [S4]   Identical-fermion two-point antisymmetry exhibit
         <c_x c_y> = -<c_y c_x> in a state where both sides are
         individually non-zero.

  [CTX]  Honesty context: H(M) = (M+M^+)/2 on the canonical mass +
         Wilson surface is positive definite, so the bosonic GAUSSIAN
         INTEGRAL converges there -- the exclusion is at the
         operator/Hilbert-space level, not Gaussian convergence.

Deterministic, no randomness, finishes in seconds.  Exits non-zero on
any FAIL.
"""

from __future__ import annotations

import sys
import math
from itertools import combinations, product

import numpy as np
from numpy.linalg import det, eigvalsh

RESULTS = []


def check(tag, ok, msg):
    verdict = "PASS" if ok else "FAIL"
    print(f"[{tag}] {verdict}: {msg}")
    RESULTS.append(bool(ok))
    return bool(ok)


# ---------------------------------------------------------------------------
# Shared constructions
# ---------------------------------------------------------------------------

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SP = np.array([[0, 1], [0, 0]], dtype=complex)   # sigma_+ (annihilation conv.)
SM = np.array([[0, 0], [1, 0]], dtype=complex)   # sigma_-


def kron_chain(ops):
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def site_op(op, i, N):
    return kron_chain([op if j == i else I2 for j in range(N)])


def jw_modes(N):
    """Jordan-Wigner fermion modes c_i on (C^2)^{tensor N}."""
    c_list = []
    for i in range(N):
        chain = [SZ] * i + [SP] + [I2] * (N - i - 1)
        c_list.append(kron_chain(chain))
    return c_list, [c.conj().T for c in c_list]


def exterior_left_mult(n_gen):
    """Left (wedge) multiplication operators L_i for the generators
    theta_1..theta_{n_gen} of the finite Grassmann algebra Lambda_{n_gen},
    acting on the 2^{n_gen}-dimensional algebra itself.  Basis = ordered
    monomials encoded as bitmasks; moving theta_i past the occupied
    generators below i gives the sign (-1)^{#occupied j < i}.  Entries are
    exactly 0/+-1, so all anticommutator checks below are exact."""
    dim = 2 ** n_gen
    ops = []
    for i in range(n_gen):
        L = np.zeros((dim, dim))
        for S in range(dim):
            if S & (1 << i):
                continue          # theta_i wedge (monomial containing theta_i) = 0
            sign = (-1) ** bin(S & ((1 << i) - 1)).count("1")
            L[S | (1 << i), S] = sign
        ops.append(L)
    return ops


def anticomm(A, B):
    return A @ B + B @ A


def comm(A, B):
    return A @ B - B @ A


def staggered_eta(x, mu):
    if mu == 0:
        return 1.0
    return float((-1) ** sum(x[:mu]))


def build_staggered_dirac_wilson(L, mass=0.3, r_wilson=1.0, dim=3):
    """Canonical staggered Dirac-Wilson matrix on a periodic L^dim block
    (package-standard exhibit instance; the S3 identity is generic in M)."""
    sites = list(product(range(L), repeat=dim))
    idx = {x: i for i, x in enumerate(sites)}
    N = len(sites)
    M = np.zeros((N, N), dtype=complex)
    for x in sites:
        i = idx[x]
        M[i, i] += mass
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
            xm = tuple((x[k] - ehat[k]) % L for k in range(dim))
            eta = staggered_eta(x, mu)
            M[i, idx[xp]] += 0.5 * eta - 0.5 * r_wilson
            M[i, idx[xm]] += -0.5 * eta - 0.5 * r_wilson
            M[i, i] += r_wilson
    return M


def pfaffian(A):
    """Pfaffian by Laplace expansion (fine for the tiny exhibits here)."""
    A = np.array(A, dtype=complex)
    n = A.shape[0]
    if n == 0:
        return 1.0 + 0j
    if n % 2 != 0:
        return 0.0 + 0j
    if n == 2:
        return A[0, 1]
    pf = 0.0 + 0j
    for k in range(1, n):
        if A[0, k] == 0:
            continue
        idx = [i for i in range(n) if i not in (0, k)]
        pf += ((-1) ** (k - 1)) * A[0, k] * pfaffian(A[np.ix_(idx, idx)])
    return pf


def antisymmetrize_for_pf(M):
    n = M.shape[0]
    A = np.zeros((2 * n, 2 * n), dtype=complex)
    A[:n, n:] = M
    A[n:, :n] = -M.T
    return A


# ---------------------------------------------------------------------------
# [S2] CCR exclusion certificate
# ---------------------------------------------------------------------------

def checks_S2(tol=1e-12):
    # (a) trace obstruction at finite cutoffs
    all_tr_zero = True
    for K in (2, 3, 5, 8, 16):
        a = np.diag(np.sqrt(np.arange(1, K, dtype=float)), 1)
        adag = a.conj().T
        c = comm(a, adag)
        tr = float(np.trace(c).real)
        defect = float(np.max(np.abs(c - np.eye(K))))
        ok_tr = abs(tr) < 1e-10
        ok_def = abs(defect - K) < 1e-10
        all_tr_zero = all_tr_zero and ok_tr
        check("S2", ok_tr and ok_def,
              f"cutoff K={K}: tr([a,a^+]) = {tr:+.1f} (must be 0) vs tr(I) = {K}; "
              f"truncation defect ||[a,a^+]-I||_max = {defect:.1f} = K (no finite truncation satisfies the CCR)")
    check("S2", all_tr_zero,
          "trace obstruction: tr([a,a^+]) = 0 in every finite dimension while CCR demands tr(I) = dim > 0 "
          "=> the canonical CCR [a,a^+] = I has NO finite-dimensional realization")

    # (b) per-site finiteness readout: both Cl(3) chirality irreps are dim 2
    for sign, name in ((+1, "rho_+"), (-1, "rho_-")):
        g = [sign * SX, sign * SY, sign * SZ]
        cliff_ok = all(
            np.max(np.abs(anticomm(g[i], g[j]) - 2.0 * (1.0 if i == j else 0.0) * I2)) < tol
            for i in range(3) for j in range(3)
        )
        check("S2", cliff_ok and g[0].shape == (2, 2),
              f"Cl(3) chirality irrep {name}(gamma_i) = {'+' if sign > 0 else '-'}sigma_i satisfies "
              f"{{gamma_i,gamma_j}} = 2 delta_ij on a complex space of dimension 2 "
              "(recomputes the cited cl3 note's chirality-independent dim-2 readout)")

    # (c) the certificate
    check("S2", all_tr_zero,
          "exclusion certificate: CCR => infinite-dimensional per-site space; the substep-1 per-site "
          "matter space is a dim-2 Cl(3) module (finite) => the free-boson (CCR) realization is EXCLUDED "
          "on the substep-1 surface")


# ---------------------------------------------------------------------------
# [FALS] falsification / scope-boundary leg
# ---------------------------------------------------------------------------

def checks_FALS(tol=1e-12):
    a = SP
    adag = SM
    n_op = adag @ a
    c = comm(a, adag)
    target = I2 - 2.0 * n_op            # 1 - 2n
    ok_form = np.max(np.abs(c - target)) < tol
    defect = float(np.max(np.abs(c - I2)))
    check("FALS", ok_form and abs(defect - 2.0) < tol,
          "hard-core ladders VIOLATE the CCR hypothesis on-site: [a, a^+] = 1 - 2n != I "
          f"(defect norm = {defect:.0f}) => the hard-core boson is OUTSIDE the class this note excludes")

    # the surviving alternative is genuinely finite-dim and cross-site commuting
    nilp = np.max(np.abs(a @ a)) < tol
    check("FALS", nilp,
          "hard-core per-site space is dim 2 (sigma_+^2 = 0): the dimensional readout does NOT exclude it")
    N = 3
    sp0 = site_op(SP, 0, N)
    sp1 = site_op(SP, 1, N)
    cross_comm = np.max(np.abs(comm(sp0, sp1))) < tol
    cross_anti = np.max(np.abs(anticomm(sp0, sp1))) > 0.5
    check("FALS", cross_comm and cross_anti,
          "hard-core fields COMMUTE across distinct sites ({sigma_+^(x), sigma_+^(y)} != 0): "
          "an ungraded dim-2 alternative survives; old Fact 2.3's binary was false")
    # every datum this note's hypothesis uses is CONSTANT across the two
    # tied frames, so the note provably cannot decide between them
    c1, c1dag = jw_modes(1)
    jw_onsite = comm(c1[0], c1dag[0])
    hc_onsite = comm(SP, SM)
    same_onsite = np.max(np.abs(jw_onsite - hc_onsite)) < tol
    jw_nilp = np.max(np.abs(c1[0] @ c1[0])) < tol
    check("FALS", same_onsite and jw_nilp and abs(float(np.max(np.abs(jw_onsite - I2))) - 2.0) < tol,
          "scope boundary is computed, not asserted: hard-core AND Grassmann/JW frames have identical "
          "on-site data ([a,a^+] = 1-2n, per-site dim 2) and BOTH sit outside the CCR hypothesis class, "
          "so this note's hypothesis cannot decide between them (the selection is the GL(F) predicate, "
          "owned by the 2026-06-10 conditional discriminator note; 2026-05-25 no-forcing note reproduced, not contradicted)")


# ---------------------------------------------------------------------------
# [S1] displayed Grassmann relations: exterior realization (conditional on the
#      declared Grassmann frame), the separately labeled CAR/Jordan-Wigner
#      operator realization, and the refutation-shaped contrast between them
# ---------------------------------------------------------------------------

def checks_S1(N=4, tol=1e-12):
    # (a) eq. (3) of the note, realized exactly: 2N generators
    # (chi_x = L[x], chibar_x = L[N+x]) acting by left exterior (wedge)
    # multiplication on the 2^{2N}-dimensional Grassmann algebra itself
    n_gen = 2 * N
    dim = 2 ** n_gen
    L = exterior_left_mult(n_gen)
    chi = L[:N]
    chibar = L[N:]
    max_all = max(float(np.max(np.abs(anticomm(L[i], L[j]))))
                  for i in range(n_gen) for j in range(n_gen))
    max_cross = max(float(np.max(np.abs(anticomm(chibar[x], chi[y]))))
                    for x in range(N) for y in range(N))
    max_nilp = max(float(np.max(np.abs(L[i] @ L[i]))) for i in range(n_gen))
    check("S1", max_all == 0.0 and max_cross == 0.0 and max_nilp == 0.0,
          f"displayed relations (3) realized by left exterior (wedge) multiplication on the "
          f"Grassmann algebra Lambda_{{2N}}, N={N} modes (algebra dim 2^{{2N}} = {dim}): "
          f"max |{{theta_i,theta_j}}| over ALL {n_gen}x{n_gen} generator pairs = {max_all:.1f}, "
          f"max |{{chibar_x,chi_y}}| incl. x=y = {max_cross:.1f}, all generators nilpotent "
          f"(max |theta^2| = {max_nilp:.1f}); every anticommutator ZERO, cross terms included")

    # (b) the exterior realization is faithful at the right algebra dimension:
    # the monomial images of the unit span all of Lambda_{2N}
    unit = np.zeros(dim)
    unit[0] = 1.0
    vecs = []
    for k in range(n_gen + 1):
        for subset in combinations(range(n_gen), k):
            v = unit.copy()
            for i in reversed(subset):
                v = L[i] @ v
            vecs.append(v)
    rank = int(np.linalg.matrix_rank(np.array(vecs)))
    check("S1", rank == dim,
          f"exterior realization is FAITHFUL at the right dimension: the 2^{{2N}} = {dim} monomial "
          f"images of the unit have rank {rank} (left regular representation, L_a 1 = a)")

    # (c) SEPARATELY LABELED operator realization: CAR/Jordan-Wigner on the
    # 2^N-dim Fock space -- nonzero mixed anticommutator, a different algebra
    car_single = np.max(np.abs(anticomm(SP, SM) - I2)) < tol
    nilp = np.max(np.abs(SP @ SP)) < tol
    c, cdag = jw_modes(N)
    eye = np.eye(2 ** N, dtype=complex)
    max_off = 0.0
    max_diag = 0.0
    for i in range(N):
        for j in range(N):
            max_off = max(max_off, float(np.max(np.abs(anticomm(c[i], c[j])))))
            max_off = max(max_off, float(np.max(np.abs(anticomm(cdag[i], cdag[j])))))
            ac = anticomm(c[i], cdag[j])
            if i == j:
                max_diag = max(max_diag, float(np.max(np.abs(ac - eye))))
            else:
                max_off = max(max_off, float(np.max(np.abs(ac))))
    check("S1-CAR", car_single and nilp and max_off < tol and max_diag < tol,
          f"SEPARATE CAR/Jordan-Wigner OPERATOR realization on the 2^N-dim Fock space "
          f"(N={N}, Hilbert dim {2**N}): pairwise CAR {{c_i,c_j}} = 0, {{c_i,c^+_j}} = delta_ij I "
          f"(max dev {max(max_off, max_diag):.1e}); on-site {{c,c^+}} = I, c^2 = 0 matches the "
          f"dim-2 Cl(3) spinor module; the mixed anticommutator is NOT zero, so this realizes "
          f"the CAR algebra, not eq. (3)")

    # (d) refutation-shaped contrast: the two realizations differ exactly on
    # the cross anticommutator, and eq. (3) pins the exterior one
    car_mixed = max(float(np.max(np.abs(anticomm(c[i], cdag[i])))) for i in range(N))
    check("S1", max_cross == 0.0 and abs(car_mixed - 1.0) < tol,
          f"refutation-shaped contrast: exterior cross anticommutators are ZERO exactly "
          f"(max = {max_cross:.1f}) while the CAR mixed anticommutator is NOT "
          f"({{c_x,c^+_x}} = I, max |.| = {car_mixed:.1f}) => the displayed relations (3) are "
          f"realized on the 2^{{2N}}-dim exterior algebra, NOT by the CAR operators on the "
          f"2^N-dim Fock space")


# ---------------------------------------------------------------------------
# [S3] Berezin determinant identity (exhibit instance)
# ---------------------------------------------------------------------------

def checks_S3(tol=1e-9):
    M = build_staggered_dirac_wilson(L=4, mass=0.3, r_wilson=1.0, dim=1)
    detM = det(M)
    pf = pfaffian(antisymmetrize_for_pf(M))
    rel = abs(abs(pf) - abs(detM)) / max(abs(detM), 1e-30)
    check("S3", rel < tol,
          f"Berezin identity |det(M)| = |Pf(A)| on the canonical staggered Dirac-Wilson exhibit "
          f"(N=4): det = {detM.real:+.6e}, Pf = {pf.real:+.6e}, rel dev = {rel:.1e}")


# ---------------------------------------------------------------------------
# [S4] two-point antisymmetry exhibit
# ---------------------------------------------------------------------------

def checks_S4(tol=1e-12):
    N = 2
    c, cdag = jw_modes(N)
    dim = 2 ** N
    vac = np.zeros(dim, dtype=complex)
    vac[0] = 1.0
    psi = (cdag[0] @ cdag[1] @ vac + vac) / math.sqrt(2.0)
    v_xy = psi.conj() @ (c[0] @ c[1] @ psi)
    v_yx = psi.conj() @ (c[1] @ c[0] @ psi)
    ok = abs(v_xy + v_yx) < tol and abs(v_xy) > 0.1
    check("S4", ok,
          f"<psi|c_x c_y|psi> = {v_xy.real:+.3f}, <psi|c_y c_x|psi> = {v_yx.real:+.3f}: "
          "equal magnitude, opposite sign, sum exactly 0 (both sides individually non-zero)")


# ---------------------------------------------------------------------------
# [CTX] honesty context
# ---------------------------------------------------------------------------

def checks_CTX():
    M = build_staggered_dirac_wilson(L=2, mass=0.3, r_wilson=1.0, dim=3)
    H = 0.5 * (M + M.conj().T)
    evals = eigvalsh(H)
    pos_def = bool(evals.min() > 1e-10)
    check("CTX", pos_def,
          f"H(M) = (M+M^+)/2 positive definite on the canonical mass+Wilson surface "
          f"(min eig {evals.min():+.4f}): the bosonic GAUSSIAN integral converges there, so the "
          "exclusion is at the operator/Hilbert-space level, not Gaussian convergence")


# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print(" axiom_first_spin_statistics_check.py  (re-scoped 2026-06-10)")
    print(" Claim: free-boson (CCR) exclusion on the substep-1 surface;")
    print(" Grassmann-calculus consequences conditional on the declared Grassmann frame.")
    print(" NOT claimed: hard-core vs CAR selection (GL(F), out of scope).")
    print("=" * 72)
    checks_S2()
    checks_FALS()
    checks_S1()
    checks_S3()
    checks_S4()
    checks_CTX()
    n_pass = sum(RESULTS)
    n_fail = len(RESULTS) - n_pass
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
