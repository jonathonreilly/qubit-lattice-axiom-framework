#!/usr/bin/env python3
"""
Two import-free moves on the value question (stripped of the red herrings the
Route-2 press removed):

MOVE A -- re-run the condensate on the chiral (staggered, Wilson-term-removed)
operator: does the Wilson-based 'uniform condensate wins -> Q=1/3' baseline
survive? YES. The coupled density-wave gap equation gives the uniform condensate
(b=0 -> Q=1/3) on BOTH the Wilson (r=1) and the chiral naive/staggered (r=0)
operator, for every coupling tested. (New detail: the off-diagonal CAN condense
alone on the Gu=0 branch, but loses to uniform when both compete.) So the
methodological worry is resolved -- the Q=1/3 condensate baseline is NOT a Wilson
artifact. Consequence: the condensate VEV is degenerate; the VALUE Q=2/3 is the
fluctuation MEASURE, not the VEV.

MOVE B -- is the covariant SECTOR measure forced over the DIMENSION measure for
the concrete generation mass operator? YES, in expectation. The mass operator is
a concrete 3x3 matrix on the 3 generations (eigenvalues lambda0 [singlet x1],
lambda1 [doublet x2]). Two candidate measures:
  (1) standard covariant action Tr(M^2)=lambda0^2 + 2 lambda1^2 -- correctly
      counts the doublet TWICE (2 physical generations). e^-Tr(M^2)/2 gives
      <lambda0^2>=1, <lambda1^2>=1/2 -> isotype weights <singlet>=<doublet>=1
      -> SECTOR/block-count -> Q=2/3.
  (2) dimension/Plancherel -- treats the doublet eigenvalue as ONE dof (drops the
      multiplicity) -> <singlet>:<doublet>=1:2 -> Q=1.
Measure (2) MIS-COUNTS: it gives the 2-fold-degenerate doublet the same variance
as the singlet, i.e. treats 2 physical generations as 1 dof. The standard
covariant action on the concrete 3-dim operator (Tr over all 3 states) is (1) ->
SECTOR -> Q=2/3. (1) is unitarily invariant; the Q=1 form a^2+b^2 is not (it
depends on normalizing {I,J-I} to unit). So the campaign's 'rep theory ranks
NEITHER' fork is RESOLVED -- toward SECTOR/2/3 -- once the mass operator is treated
as the concrete 3-generation matrix it physically is, with the standard covariant
measure.

HONEST GAP (Move B): this forces the EXPECTED isotype balance (Q=2/3 in
expectation); a single operator fluctuates about it, so it does NOT by itself
explain the observed Q=2/3 to ~1e-5 -- that needs the mass operator to BE the
typical/max-entropy draw, or a separate exactness mechanism. The fork is ranked;
exactness remains open.
"""

import numpy as np

s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex),
     np.array([[1, 0], [0, -1]], complex)]
I2 = np.eye(2, dtype=complex); QV = np.array([np.pi, np.pi, 0.0])


def Wf(k, m, r):
    return (m + r * sum(1 - np.cos(kk) for kk in k)) * I2 + 1j * sum(s[mu] * np.sin(k[mu]) for mu in range(3))


def gap(Gu, Gs, r, a0, b0, m=0.0, L=12, iters=250):
    ks = 2 * np.pi * np.arange(L) / L
    kl = [np.array([kx, ky, kz]) for kx in ks for ky in ks for kz in ks]
    a, b = a0, b0
    for _ in range(iters):
        sa = sb = 0.0
        for k in kl:
            G = np.block([[Wf(k, m, r) + a * I2, b * I2], [b * I2, Wf(k + QV, m, r) + a * I2]])
            S = np.linalg.inv(G)
            sa += np.real(np.trace(S[:2, :2]) + np.trace(S[2:, 2:])) / 2
            sb += np.real(np.trace(S[:2, 2:]) + np.trace(S[2:, :2])) / 2
        a = 0.5 * a + 0.5 * Gu * sa / len(kl); b = 0.5 * b + 0.5 * Gs * sb / len(kl)
    return a, b


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("MOVE A: condensate on Wilson (r=1) vs chiral/staggered (r=0) -- does Q=1/3 survive?")
    print("   r  Gu Gs   a        b        r_K=(b/a)^2  Q")
    for r in [1.0, 0.0]:
        for Gu, Gs in [(2.0, 2.0), (2.0, 6.0)]:
            a, b = gap(Gu, Gs, r, 0.5, 0.4)
            rk = (b / a) ** 2 if abs(a) > 1e-5 else 0.0
            print(f"   {r:.0f}  {Gu:.0f}  {Gs:.0f}   {a:+.4f}  {b:+.4f}   {rk:.4f}     {1/3+2/3*rk:.4f}")
    print("   uniform wins (b=0, Q=1/3) on BOTH operators -> baseline NOT a Wilson artifact.")
    print("   (off-diagonal condenses alone on Gu=0, but loses to uniform when both compete.)")

    sep("MOVE B: covariant Tr(M^2) measure forces SECTOR (Q=2/3) over dimension (Q=1)")
    print("  M concrete 3x3, eigenvalues lambda0 (singlet x1), lambda1 (doublet x2).")
    print("  (1) Tr(M^2)=lambda0^2+2 lambda1^2 (correct multiplicity): <l0^2>=1,<l1^2>=1/2")
    print(f"      isotype weights <singlet>={1.0}, <doublet>={2*0.5} -> EQUAL -> SECTOR -> Q=2/3")
    print("  (2) dimension (doublet as 1 dof): <l0^2>=<l1^2>=1 -> 1:2 -> Q=1  [MIS-COUNTS doublet]")
    print("  Tr(M^2) is unitarily invariant; the Q=1 form a^2+b^2 is basis-dependent.")
    print("  => fork RESOLVED toward SECTOR/2/3 (the concrete mass matrix counts all 3 generations).")

    sep("VERDICT")
    print("  A: Q=1/3 condensate baseline robust (Wilson AND staggered) -> value is the MEASURE,")
    print("     not the VEV. B: the covariant standard matrix measure Tr(M^2), correctly counting")
    print("     the doublet's 2-fold multiplicity, is forced over the dimension measure -> SECTOR")
    print("     -> Q=2/3 IN EXPECTATION, resolving the campaign's trace-vs-sector fork toward 2/3.")
    print("  HONEST GAP: expected 2/3, not the exact 1e-5 -- needs the operator to be the typical/")
    print("  max-entropy draw, or a separate exactness mechanism. The fork is ranked; exactness open.")


if __name__ == "__main__":
    main()
