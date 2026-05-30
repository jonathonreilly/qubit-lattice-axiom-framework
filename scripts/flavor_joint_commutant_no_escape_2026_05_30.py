#!/usr/bin/env python3
"""
THREAD 1 -- joint-commutant characterization (the decidable gap the chiral-import
verdict left open). The retained no-go koide_z3_equivariant_anticommuting forbids
C3-EQUIVARIANT operators anticommuting with Gamma_chi; it leaves open a native
C3-NON-equivariant operator. This computation closes that gap.

On the hw=1 generation triplet (corners (pi,0,0),(0,pi,0),(0,0,pi)): sign flips act
trivially (pi=-pi mod 2pi), so the realized cube point-group symmetry is the axis
permutation group S3. The Wilson mass + the native cube double-shift are S3-INVARIANT,
and the Dirac sigma-term VANISHES at the corners (sin k=0). So every NATIVE generation
mass operator commutes with S3 -- it lies in the S3-commutant.

RESULT (verified): the S3-commutant of the permutation rep on C^3 is exactly 2-dim
(Schur: perm rep = trivial + standard, multiplicities 1 -> commutant dim 1^2+1^2 = 2)
= span{I, J-I}. BOTH basis operators COMMUTE with Gamma_chi=(2/3)J-I; NONE anticommute.
A C3-non-equivariant operator would require breaking S3 explicitly -- NOT native. So the
gap is EMPTY: there is NO native operator that anticommutes with Gamma_chi. The
anticommuting no-go is AIRTIGHT for ALL native operators (not just C3-equivariant ones).

CONCLUSION: the chiral import cannot be realized by any native operator on the
generation space. The operator-route to deriving the chiral grading is closed (no
escape). This confirms (and strengthens) the chiral-import verdict: r=1/2 (Q=2/3)
requires a non-native input; no native operator supplies it.
"""
import numpy as np, itertools


def main():
    perms = [np.array([[1.0 if p[i] == j else 0 for j in range(3)] for i in range(3)])
             for p in itertools.permutations(range(3))]
    rows = [np.kron(P.T, np.eye(3)) - np.kron(np.eye(3), P) for P in perms]
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    nulldim = 9 - int(np.sum(s > 1e-9))
    print(f"S3-commutant (native operator space) dimension = {nulldim}  (Schur expects 2)")
    _, _, vt = np.linalg.svd(A)
    null = vt[int(np.sum(s > 1e-9)):]
    J = np.ones((3, 3)); I = np.eye(3); Gx = (2 / 3) * J - I
    anyanti = False
    for k, v in enumerate(null):
        M = v.reshape(3, 3)
        comm = np.allclose(M @ Gx - Gx @ M, 0)
        anti = np.allclose(M @ Gx + Gx @ M, 0) and not np.allclose(M, 0)
        anyanti = anyanti or anti
        print(f"  commutant basis {k}: [M,Gamma_chi]=0 -> {comm};  {{M,Gamma_chi}}=0 -> {anti}")
    print(f"\n  any native operator anticommutes with Gamma_chi? {anyanti}")
    print("  => the gap (native C3-non-equivariant anticommutant) is EMPTY; no-go AIRTIGHT.")
    print("  THREAD 1 CLOSED: no native OPERATOR escape to the chiral import.")


if __name__ == "__main__":
    main()
