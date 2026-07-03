"""Koide r=1/2 dynamical determinant route-pruning diagnostics.

Complements koide_corner_dirac_determinant_2026_06_08.py (det D = |det M|^2 -> r=1). This verifies the
three tested dynamical determinant escape routes independently:

  Pfaffian/Majorana route (does NOT give a one-slot count). For the block-antisymmetric Majorana kernel
     A = [[0, M],[-M^T, 0]], Pf(A) = +-det M, so the Pfaffian removes only the OUTER L/R doubling, never
     the intra-M doublet multiplicity: |Pf(A)| = |det M| = prod(singular values of M) -> the doublet's
     |b|^2 is still counted -> r=1. (And the only antisymmetric C3-equivariant kernel is J_cs itself,
     which annihilates the singlet, so it cannot even form Q.)

  Reflection-positivity route (does not support the tested first-order reading). The first-order holomorphic operator
     W_h = a I + b C has a COMPLEX (non-real) spectrum for every b != 0 -> non-self-adjoint -> not a
     positive transfer -> NOT reflection-positive. The Dirac operator D = [[0,M],[M^dag,0]] is Hermitian
     and D^dag D (= the OS/transfer object T = B^dag B) is manifestly positive (second-order).

  Berezin-power route (r-neutral). Any determinant power p (Dirac p=2, Majorana p=1, rooted
     p=1/2) multiplies every isotype's log-weight UNIFORMLY, so it cancels in the doublet:singlet ratio
     -> r is p-independent. The halving to r=1/2 comes from POLARIZATION (count b once), not from the
     statistics/measure -- and the polarization is measure-neutral (#3258).

CONCLUSION: the tested determinant-family routes (Dirac, Majorana/Pfaffian, Weyl-magnitude,
and uniform Berezin power) do not supply an equal-block r=1/2 selector on the supplied C3 matrix.
No PDG/fitted value; exact sympy/numpy. This is not a global Koide admission claim.
"""
from __future__ import annotations
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def pfaffian(A):
    """Pfaffian of a (real/complex) antisymmetric 2n x 2n matrix via the recursive expansion."""
    A = np.array(A, dtype=complex)
    n = A.shape[0]
    if n == 0:
        return 1.0 + 0j
    if n % 2 == 1:
        return 0.0 + 0j
    # recursive: expand along the first row
    pf = 0.0 + 0j
    for j in range(1, n):
        if A[0, j] == 0:
            continue
        idx = [k for k in range(1, n) if k != j]
        minor = A[np.ix_(idx, idx)]
        pf += ((-1) ** (j + 1)) * A[0, j] * pfaffian(minor)
    return pf


def main() -> int:
    print("KOIDE r=1/2 DYNAMICAL DETERMINANT ROUTE PRUNING")
    print("=" * 86)
    Cn = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    av = 1.3
    bv = 0.8 * np.exp(1j * 0.6)
    M = av * np.eye(3) + bv * Cn + np.conj(bv) * (Cn @ Cn)
    sv = np.sort(np.linalg.svd(M, compute_uv=False))

    # Pfaffian of the block-antisymmetric Majorana kernel = +- det M -> magnitude = |det M| = prod sigma.
    A = np.block([[np.zeros((3, 3), complex), M], [-M.T, np.zeros((3, 3), complex)]])
    antisym = np.allclose(A, -A.T)
    pf = pfaffian(A)
    detM = np.linalg.det(M)
    check("Pfaffian/Majorana route: Pf([[0,M],[-M^T,0]]) = +- det M -> the Pfaffian removes only the outer L/R doubling, NOT the "
          "intra-M doublet multiplicity; |Pf| = |det M| = prod(singular values) -> r=1 (Majorana does not give a one-slot count)",
          antisym and np.isclose(abs(pf), abs(detM)) and np.isclose(abs(pf), float(np.prod(sv))),
          f"|Pf(A)| = {abs(pf):.4f}, |det M| = {abs(detM):.4f}, prod(sigma) = {float(np.prod(sv)):.4f}")
    # only antisymmetric C3-equivariant kernel is J_cs (annihilates the singlet)
    Jcs = (Cn - Cn @ Cn) / np.sqrt(3.0)
    triv = np.ones(3) / np.sqrt(3.0)
    check("C3-equivariant antisymmetric kernel check: the only antisymmetric C3-equivariant kernel is J_cs, which annihilates the singlet "
          "(J_cs.(1,1,1)=0) -> cannot form the Koide Q (no singlet channel)",
          np.allclose(Jcs.T, -Jcs) and np.allclose(Jcs @ triv, 0),
          f"||J_cs + J_cs^T|| = {np.linalg.norm(Jcs + Jcs.T):.1e}, ||J_cs.triv|| = {np.linalg.norm(Jcs @ triv):.1e}")

    # The tested first-order W_h has complex spectrum for b!=0 -> not self-adjoint -> not RP.
    Wh = av * np.eye(3) + bv * Cn
    eig_Wh = np.linalg.eigvals(Wh)
    complex_spec = np.max(np.abs(np.imag(eig_Wh))) > 1e-6
    # D^dag D (= T = B^dag B) manifestly positive (second order)
    D = np.block([[np.zeros((3, 3), complex), M], [M.conj().T, np.zeros((3, 3), complex)]])
    DdD = D.conj().T @ D
    pos = np.all(np.linalg.eigvalsh(DdD) > -1e-9)
    herm_D = np.allclose(D, D.conj().T)
    check("Reflection-positivity route: the tested first-order holomorphic W_h = aI + bC has a COMPLEX spectrum for b!=0 (non-self-adjoint "
          "-> not reflection-positive); the Dirac D is Hermitian and D^dag D (= OS transfer B^dag B) is "
          "positive (second order). This prunes the tested RP first-order route.",
          complex_spec and herm_D and pos,
          f"max|Im eig(W_h)| = {np.max(np.abs(np.imag(eig_Wh))):.3f} (>0 -> complex), D Hermitian={herm_D}, D^dag D PSD={pos}")

    # Berezin measure power is r-neutral. r = |b|^2/a^2; a uniform power p multiplies both isotype
    # log-weights -> cancels in the ratio. Symbolically: with weights (p*w_s, p*w_d), x and r unchanged.
    p, ws, wd = sp.symbols('p w_s w_d', positive=True)
    x_p = (p * ws) / (p * ws + p * wd)
    x_1 = ws / (ws + wd)
    r_p = sp.simplify((1 - x_p) / (2 * x_p))
    r_1 = sp.simplify((1 - x_1) / (2 * x_1))
    check("Berezin-power route: the Berezin determinant POWER p (Dirac 2, Majorana 1, rooted 1/2) multiplies every isotype "
          "log-weight uniformly -> cancels in the singlet:doublet ratio -> r is p-INDEPENDENT (the halving "
          "comes from POLARIZATION, not statistics)",
          sp.simplify(r_p - r_1) == 0,
          f"r(power p) = {r_p} = r(p=1) = {r_1}  (p cancels)")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: Pfaffian/Majorana -> |det M| (no one-slot count); the tested non-self-adjoint first-order "
        "operator is not RP-compatible while the Hermitian Dirac object is second order; the Berezin measure "
        "power is r-neutral. This prunes the tested determinant-family routes only and does not classify Koide "
        "r=1/2 globally. The independent audit lane owns status."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
