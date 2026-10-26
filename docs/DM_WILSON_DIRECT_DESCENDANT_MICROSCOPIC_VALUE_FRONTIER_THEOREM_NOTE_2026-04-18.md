# Conditional direct-descendant Schur response diagnostic

**Type:** bounded_theorem
**Primary runner:** [runner](../scripts/frontier_dm_wilson_direct_descendant_microscopic_value_frontier_theorem_2026_04_18.py)

Supply a charged-support split E_-=E_e⊕E_r and a block matrix D_-=[[A,B],[C,F]], with F and L_e=A-B F^-1 C invertible. For a Hermitian source X=X* supported on E_e and real t sufficiently near zero, det(D_-+t I_e X I_e*)=det(F) det(L_e+tX). Differentiating log absolute determinant at zero gives Re Tr(L_e^-1 X). Thus the Hermitian response is represented by Herm(L_e^-1) on this supplied support. Equal L_e gives the same response law; this is conditional algebra, not a Wilson-native value law or support derivation.

The restriction X=X* is essential to representation by Herm(L_e^-1): for the scalar L_e=i and X=i, Re(L_e^-1 X)=1 while Herm(L_e^-1)=0. With Hermitian X, Re Tr(L_e^-1 X)=Tr(Herm(L_e^-1)X), which determines the response representative uniquely under the real trace pairing.

For the downstream packet, additionally supply a fixed coordinate basis, a simple spectrum for H_e, ascending eigenvalue labels, and the same eigenvector conventions. Column phases cancel in squared magnitudes. Use the same finite transport inputs and functional, and select the first ascending-label maximizer when values tie. Degenerate eigenspaces require a separately supplied basis; this statement does not derive one.

The runner preserves its supplied reconstruction example, packet sums, transport value, two ambient completions and finite-difference thresholds. These computations do not fix a physical source or exclude alternative constructions. The generic Wilson keyword inventory supplies no absence theorem. Therefore no claim is made that the unique remaining frontier must be D_-/L_e, that generic source-family search is invalid, or that every alternative is exhausted.

Deriving source values, support provenance and physical matching remains open. A note assuming them does not itself derive them; this local fact is different from a claim that no derivation exists anywhere. Historical global-frontier claims are withdrawn, with original recovery preserved.
