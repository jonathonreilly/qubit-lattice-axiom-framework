# Canonical-to-local fourth-order gauge transfer

Disposition: PASS in the explicitly specified zero-block local homological convention. The long slow-channel fourth-order matrix, including its vacuum-subtracted bulk symbol 109/96, transfers from the energy-E8 canonical construction. No generic gauge independence is claimed.

## Algebra

Work first in a finite volume, coefficientwise in lambda, with P the FULL H0 eigenspace of energy E0=8, Q=1-P. The local convention has U_L H U_L† block diagonal in every H0 eigenspace through the retained order, with each sequential generator L_j having zero diagonal H0 blocks. The canonical convention U_C H U_C† decouples P from Q and is the direct/polar canonical rotation; its logarithmic generators A_j have zero PP and QQ blocks. Its effective P Hamiltonian is the Hermitian canonical SW matrix used by the displayed K4 formula.

The first P-Q homological equation is unique because E0-H0 is invertible on Q. Hence

 L1=A+B,   A=A1,   B=Q B Q,

where A is off diagonal relative to P,Q. In particular PBP=PB=BP=0. Also P L2 P=P A2 P=0. The local product ordering does not matter at order two:

 U_L=I+lambda L1+lambda²(L2+L1²/2)+O(lambda³),
 U_C†=I-lambda A+lambda²(-A2+A²/2)+O(lambda³).

Let W=U_L U_C†. Then

 P W1 P=0,
 P W2 P=P[L2-A2+(A+B)²/2+A²/2-(A+B)A]P=0.

Indeed the square terms each reduce to PA²P; all B-containing terms vanish after this PP compression. Thus the extra first-order QQ rotation cannot induce a second-order PP gauge rotation. This explicitly establishes the cancellation rather than assuming it.

Both transformations identify the same formal spectral subspace issuing from the full E0 eigenspace. Uniqueness follows recursively by solving the off-diagonal homological equation with nonzero H0 energy denominators. Therefore W has zero P-Q blocks to the needed formal order. Its PP block is consequently unitary coefficientwise and

 W_P=I+lambda³ G3+O(lambda4),  G3†=-G3.

Writing H_C,P=E0 P+lambda K1+lambda²K2+lambda³K3+lambda4K4+…, conjugation gives

 D1=K1, D2=K2, D3=K3,
 D4=K4+[G3,K1].

The sign displayed uses H_L=W H_C W†; reversing the relative-unitary convention reverses both G3 and the written commutator, without changing the conclusion.

For any a,b with K1|a>=K1|b>=0,

 <b|(D4-K4)|a>=0.

Both external conditions matter. This does not establish equality of arbitrary slow-to-fast matrix elements.

## Application to the long slow kernel

The axial-distance-two common-interval states at ell>=2 are annihilated by the full K1: a single native transverse edge cannot move both non-neighboring columns' endpoints, and cannot move an entire occupied column at ell>=2. In particular all external states used for the long ell>=5 diagonal and endpoint-hop coefficients satisfy the required condition. The formula therefore transfers the entire projected long-slow K4 kernel, including the ell/8 tension, diagonal endpoint constant 29/192, endpoint steps 19/64 and -13/256, and the cancellation of separated-end moves. Summing the two endpoints gives symbol

 29/192+(19/16)cos k-(13/64)cos 2k,

whose k=0 value is 109/96.

The analogous comparison for the full zero-wall H0 block has K1=0 in the nonwrapping local setting: one transverse bond creates longitudinal walls, rather than mapping an aligned configuration to another aligned configuration. Its fourth-order canonical and local scalar vacuum shifts therefore agree as well. Vacuum subtraction does not undo the result.

This finite-volume formal identity passes to the coefficientwise bulk limit used for the long kernel. No uniform-in-volume convergence radius of global spectral perturbation theory is needed: only equality of each finite algebraic coefficient followed by the separately established connected local coefficient limit. Proper local supports exclude whole-column wrapping terms. The canonical P must include all states at E8, not merely the chosen slow subset; otherwise the presumed invertible Q denominators and projector uniqueness would fail.

## Boundaries and provenance

The proof uses the actual homological choice P_E L_j P_E=0 at every order. An additional freely chosen PP rotation at order lambda² would introduce [G2,K2] at fourth order and is not covered. The proposed weaker Toeplitz-commutation argument is unnecessary here. Likewise this argument does not identify transformed observables between gauges, nor transfer a pole of a truncated coefficient Hamiltonian to the exact microscopic dynamics.

Read docs/NATIVE_SLOW_COMPOSITE_CONTROL_NOTE_2026-10-18.md, especially its canonical external-K1-zero kernel, and native/INDEPENDENT_LOCAL_NORMALFORM.md, including its sign and sequential zero-block homological construction. This is an independent algebraic gauge comparison; no repository edits or formal audit performed.
