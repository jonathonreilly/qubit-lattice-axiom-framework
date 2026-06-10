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

  [S1]   Grassmann/CAR consequences conditional on the declared Grassmann
         frame: {c,c^+} = I, c^2 = 0 on the 2-dim Fock space, and
         full pairwise CAR for N Jordan-Wigner modes.

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
from itertools import product

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
# [S1] Grassmann/CAR consequences (conditional on the declared Grassmann frame)
# ---------------------------------------------------------------------------

def checks_S1(N=4, tol=1e-12):
    car_single = np.max(np.abs(anticomm(SP, SM) - I2)) < tol
    nilp = np.max(np.abs(SP @ SP)) < tol
    check("S1", car_single and nilp,
          "Grassmann CAR realized on the 2-dim per-site Fock space: {c, c^+} = I, c^2 = 0 "
          "(matches the dim-2 Cl(3) spinor module)")

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
    check("S1", max_off < tol and max_diag < tol,
          f"pairwise CAR for N={N} modes (Hilbert dim {2**N}): "
          f"max off-diag anticommutator {max_off:.1e}, max |{{c_i,c_i^+}} - I| {max_diag:.1e}")


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
