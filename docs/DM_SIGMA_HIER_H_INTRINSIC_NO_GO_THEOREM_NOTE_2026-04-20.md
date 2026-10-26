# Conditional fixed-H and row-swap invariance

**Date:** 2026-04-20
**Type:** bounded_theorem
**Status:** conditional invariance identities with finite supplied-pin illustrations;
physical source and row selection remain open
**Primary runner:** `scripts/frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py`

The historical no-go filename is retained for recovery. The current owner is
only the conditional invariance argument below; it does not exhaust physical
selector routes or establish a globally complete pair of alternatives.

## Premises and statement

Fix a Hermitian 3×3 matrix H and a chosen unitary eigenbasis V, with a fixed
column ordering. A simple spectrum suffices for the ascending-column labeling
used by the numerical illustration; the invariance itself only requires the
same chosen V in both comparisons. Define

```text
P_minus = V[[2,1,0],:]
P_plus  = V[[2,0,1],:]
S = [[1,0,0],[0,0,1],[0,1,0]].
```

Then P_plus = S P_minus. This fixes the electron row and swaps the muon and
tau rows, not the eigenmode columns. H itself is identical in both constructions.

For any well-defined function f of H alone, the two constructions have the
same value f(H). For any function F of the row-labeled matrix that satisfies
F(SP)=F(P) on the compared matrices, F(P_plus)=F(P_minus). These are equal-input
and stipulated symmetry identities. They do not establish that an arbitrary
physical selector has either restriction. A selector with extra label data
is outside these hypotheses.

## Proof and limits

Direct indexing gives P_plus = S P_minus. Since H is held fixed, applying the
same function f gives the same value. Substitution of P=P_minus in the assumed
identity F(SP)=F(P) gives the second equality. No chamber-completeness,
observational-fit, threshold, asymptotic or physical-source premise is needed.

The labeled modulus matrices are row-permuted and need not be equal. Their
unordered row multisets agree. Thus this statement must not be extended to
all functions of the labeled modulus matrix.

With the Jarlskog convention
J(P)=Im(P_e1 conj(P_e2) conj(P_mu1) P_mu2), unitarity gives
J(SP)=-J(P). Indeed, writing z_r=P_r1 conj(P_r2), column orthogonality gives
z_e+z_mu+z_tau=0, and Im(z_e conj(z_tau))=-Im(z_e conj(z_mu)).
A nonzero J therefore has opposite signs under the swap. A corresponding
sin(delta_CP) sign statement additionally requires the same angle convention
with positive nonzero normalization s12*c12*s23*c23*s13*c13²; degenerate
angle boundaries do not define such a phase. These premises and identity
match the independently checked conditional row-swap argument of the finite
[upper-octant diagnostic](DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md).
No physical preference for either row labeling follows.

## Actual finite illustration

The unchanged numerical functions import the supplied matrix and rounded pin
(m,delta,q)=(0.657061,0.933806,0.715042), magnitude bands, and phase convention
from `scripts/frontier_sigma_hier_uniqueness_theorem.py`. The target bands and
pin are supplied data, not a physical derivation. The runner checks the two
specified row permutations against all nine bands; it does not enumerate all
six permutations or prove that no other source/label fits. It compares the row
swap, fixed-H trace/spectrum/determinant identities, unordered row moduli,
distinct labeled moduli, and computed phase values near ±0.9873607592.
All eleven predicates, tolerances and supplied constants are unchanged.
Several fixed-input equalities are self-comparisons: their PASS is an
illustration, not an independent proof of the general statement above.

The old physical-pin/global-selector/no-go interpretation is withdrawn from
this owner. I12, physical source provenance, flavor labeling and complete
alternative-route coverage remain open. This withdrawal does not refute
unverified upstream proofs.

## Recovery and context

The complete old argument, dependency section, runner and cache remain
recoverable at `4a12013c6f4bfe6b71a07fe8c557d34fb3f17e9a` and in repair evidence.
The [chamber diagnostic](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20.md)
and [parity diagnostic](DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md)
are context only; no complete chamber census or physical selector is imported.
The historical hygiene snapshot is not a current receipt or verdict authority.

## Reproduction

Run `PYTHONPATH=scripts python3 scripts/frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py`
under its declared 120-second bound. Fresh execution is pending source review;
no old cache is represented as current after this repair.
