#!/usr/bin/env python3
"""Corner Dirac determinant route-pruning diagnostic.

For the supplied C3 circulant mass matrix, the implemented Hermitian corner
Dirac operator gives det D = |det M|^2 up to sign. This prunes the specific
Dirac-determinant route to an equal-block r=1/2 readout; it does not classify
Koide r=1/2 globally or set any Tier-A admission status.

SETUP: C3 generation triplet, circulant mass M = a I + b C + b-bar C^2 (a real singlet coeff; b complex
doublet coeff). The Dirac operator coupling left/right generation copies is the Hermitian off-diagonal
  D = [[0, M], [M^dag, 0]]   (6x6: 3 L-modes (+) 3 R-modes).
Koide: r = |b|^2/a^2, Q = 1/3 + (2/3) r; the doublet energy E_d = 6|b|^2, singlet E_s = 3a^2.

VERIFIES:
  Dirac determinant identity. det D = (-1)^3 det(M M^dag) = -|det M|^2 -> the Dirac determinant is the MODULUS-SQUARED
      (second order). Both chiral blocks each contribute |det M|; only a single-block (Weyl) operator
      would give det M. So the tested Dirac determinant reading counts the SINGULAR values of M.
  Singular-value pairing. The Dirac eigenvalues are +- the singular values of M (paired), so |det D| = (prod sigma_k)^2 =
      |det M|^2; the effective action Tr log(D^dag D) = 2 Tr log(M^dag M) -> the rank-2 modulus -> r=1.
  Weyl determinant magnitude. First-order WEYL half det M is COMPLEX: |det M| (its MAGNITUDE) equals the modulus -> r=1; its
      PHASE arg(det M) is a phase channel, not an equal-block magnitude selector.
  Complex-structure invariance. The native complex structure J_cs = (C - C^2)/sqrt(3) commutes with M and preserves
      |det M| and the singular values, so this diagnostic does not select a holomorphic
      one-slot count.

CONCLUSION: the tested corner-Dirac determinant route reads the modulus and does not supply
an equal-block r=1/2 selector. No PDG/fitted value; exact sympy/numpy.
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


def main() -> int:
    print("THE CORNER DIRAC DETERMINANT: det D = |det M|^2 (second order) -> r=1")
    print("=" * 70)

    # symbolic circulant M = a I + b C + conj(b) C^2 over C3
    a, br, bi = sp.symbols('a b_r b_i', real=True)
    b = br + sp.I * bi
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    M = a * sp.eye(3) + b * C + sp.conjugate(b) * (C * C)
    Mdag = M.conjugate().T

    # Dirac determinant identity for D = [[0,M],[Mdag,0]].
    Z = sp.zeros(3, 3)
    D = sp.Matrix(sp.BlockMatrix([[Z, M], [Mdag, Z]]))
    detD = sp.simplify(D.det())
    detM = sp.simplify(M.det())
    detMMdag = sp.simplify((M * Mdag).det())
    target = sp.simplify((-1)**3 * detMMdag)
    check("Dirac determinant identity: det D = (-1)^3 det(M M^dag) = -|det M|^2  (Dirac determinant is the MODULUS-squared, "
          "second order; both chiral blocks contribute |det M|)",
          sp.simplify(detD - target) == 0,
          f"det D = {detD}  ;  -det(M M^dag) = {target}")
    check("Dirac modulus identity: |det D| = |det M|^2  (and det(M M^dag) = |det M|^2 is real-nonneg)",
          sp.simplify(detMMdag - sp.Abs(detM)**2) == 0 or sp.simplify(detMMdag - (sp.re(detM)**2 + sp.im(detM)**2)) == 0,
          f"det(M M^dag) = {detMMdag}")

    # Dirac eigenvalues are +- singular values of M; effective action = 2 Tr log(M^dag M).
    rng = np.random.default_rng(0)
    av = 1.3
    bv = 0.8 * np.exp(1j * 0.6)
    Cn = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    Mn = av * np.eye(3) + bv * Cn + np.conj(bv) * (Cn @ Cn)
    Dn = np.block([[np.zeros((3, 3), complex), Mn], [Mn.conj().T, np.zeros((3, 3), complex)]])
    eigD = np.sort(np.real(np.linalg.eigvals(Dn)))   # Hermitian -> real, paired +-sigma
    sv = np.sort(np.linalg.svd(Mn, compute_uv=False))
    paired = np.allclose(np.sort(np.abs(eigD)), np.sort(np.concatenate([sv, sv])))
    check("Singular-value pairing: the Dirac operator's eigenvalues are +- the singular values of M (paired) -> the tested "
          "determinant reading counts SINGULAR values (modulus), Tr log(D^dag D) = 2 Tr log(M^dag M)",
          paired, f"|eig D| sorted = {np.round(np.sort(np.abs(eigD)),4)}, singular values = {np.round(sv,4)} (each x2)")

    # the doublet energy is the modulus 6|b|^2 with rank-2 Hessian over (Re b, Im b) -> r=1
    Ed = 6 * (br**2 + bi**2)
    H = sp.Matrix([[sp.diff(Ed, v1, v2) for v2 in (br, bi)] for v1 in (br, bi)])
    check("Doublet modulus rank: doublet energy E_d = 6|b|^2 (the second-order modulus) has rank-2 Hessian over (Re b,Im b) "
          "-> two real modes -> weighting (1,2) -> r=1",
          H.rank() == 2 and H == sp.Matrix([[12, 0], [0, 12]]),
          f"Hessian(E_d) = {H.tolist()}, rank = {H.rank()}")

    # First-order Weyl half det M is complex; |det M| = modulus (r=1), arg = delta (phase).
    detMn = np.linalg.det(Mn)
    mag = abs(detMn)
    # the magnitude reading reproduces the modulus (product of singular values); phase is the delta channel
    check("Weyl determinant magnitude: first-order Weyl determinant det M is COMPLEX; its MAGNITUDE |det M| = prod(singular values) "
          "= the modulus, while its PHASE arg(det M) is not an equal-block magnitude selector",
          np.isclose(mag, float(np.prod(sv))),
          f"|det M| = {mag:.4f} = prod(sigma) = {float(np.prod(sv)):.4f}; arg(det M) = {np.angle(detMn):.4f} (delta channel)")

    # J_cs preserves the modulus/singular values, so this diagnostic does not select a holomorphic one-slot count.
    Jcs = (Cn - Cn @ Cn) / np.sqrt(3.0)
    commutes = np.allclose(Jcs @ Mn - Mn @ Jcs, 0)
    # SO(2) flow preserves |det M| (magnitude) and E_d
    def expm_np(A, n=60):
        out = np.eye(A.shape[0], dtype=complex); term = np.eye(A.shape[0], dtype=complex)
        for k in range(1, n):
            term = term @ A / k; out = out + term
        return out
    inv = True
    for th in [0.4, 1.1, 2.2]:
        R = expm_np(th * Jcs)
        Mth = R @ Mn @ R.T
        inv = inv and np.isclose(abs(np.linalg.det(Mth)), mag) and np.allclose(np.sort(np.linalg.svd(Mth, compute_uv=False)), sv)
    check("Complex-structure invariance: the holomorphic one-slot count is not selected by the native J_cs=(C-C^2)/sqrt3 diagnostic; J_cs "
          "commutes with M and its SO(2) flow preserves |det M| and the singular values -> measure-neutral, "
          "so this determinant diagnostic does not SELECT that count.",
          commutes and inv, f"[J_cs,M]=0: {commutes}; |det M| & singular values J_cs-invariant: {inv}")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the tested C3 generation Dirac operator D=[[0,M],[M^dag,0]] has det D = -|det M|^2 "
        "(SECOND order) and eigenvalues +- the singular values of M -> the tested determinant reading counts the "
        "modulus -> r=1. A first-order Weyl half det M is complex, but its MAGNITUDE is still the modulus "
        "and its phase is not a magnitude selector; the native complex-structure diagnostic preserves |det M| "
        "and singular values. This prunes the tested corner-Dirac determinant route only; it does not classify "
        "Koide r=1/2 globally. The independent audit lane owns status."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
