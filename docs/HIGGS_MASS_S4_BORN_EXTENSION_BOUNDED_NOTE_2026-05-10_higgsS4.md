# Finite trace and curvature controls for the Higgs readout question

**Date:** 2026-05-10; correction 2026-10-21
**Type:** bounded_theorem
**Status:** finite supplied algebra; physical mass matching remains open
**Primary runner:** `scripts/cl3_higgs_mass_s4_born_extension_2026_05_10_higgsS4.py`

## Corrected claim

For a finite density matrix rho and a supplied Hermitian operator O, the expectation convention is Tr(rho O). For rho=psi psi†, matrix multiplication gives Tr(rho O)=psi†O psi. This identity does not choose rho or O, identify a physical Higgs mass observable, or equate a vacuum expectation with a single-particle mass readout. Such physical identifications require separate hypotheses and matching; none is proved here.

The former runner mixed genuine finite matrix calculations with literal-True assertions and documentary checks. The claim that all its checks were tautologies was too broad, but those assertions were not independent evidence for physical identification or scientific closure. They no longer count as passed tests. Historical sources and failures remain recoverable in Git.

## Supplied finite examples

1. On a four-dimensional space, normalize psi=(.6,.5,.4,.3). The supplied observables are two coordinate projectors, diag(0,1,2,3), and the periodic four-cycle Laplacian L with diagonal2 and neighboring entries−1. Direct contractions agree with the pure-state trace expression. L has spectrum0,2,2,4, rank3, and is not idempotent, whereas a coordinate projector has rank1 and is idempotent. These particular operators are distinct; their different expectations do not identify L with a physical potential Hessian or establish a universal rank statement about mass operators.
2. Supply the scalar potential V(phi)=−a phi²+b phi⁴ with a,b>0. Differentiation gives V''(0)=−2a and V''(sqrt(a/(2b)))=4a. The runner evaluates a=1,b=.1, then compares b=.1 and .4: the same origin curvature has different minima. This is a two-model demonstration that the origin curvature alone does not determine the minimum in this supplied family. It is not a construction of either framework vacuum.
3. The historical supplied values140.3GeV and125.25GeV differ by15.05GeV, or301/2505 (about12.016%) relative to the second. Neither value is derived by this runner. The discrepancy alone does not establish that a particular mean-field, state-selection or operator approximation caused it; a common-input error analysis remains absent.

No state/operator selection, post-EWSB matching, physical mass prediction or closure of the historical S4/S7 research obligations follows from these examples. The finite expectation identity survives independently of the unresolved physical interpretation.

## Reproduction and recovery

Run `python3 scripts/cl3_higgs_mass_s4_born_extension_2026_05_10_higgsS4.py`. Its numerical assertions compare independently evaluated finite expressions at their declared tolerances; they are not a general proof certificate. The runner uses NumPy and supplied constants, with no documentary file reads.

Original654-line note and682-line runner are recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under the same paths. Historical context, without inherited authority:

- [Original lattice matching question](LATTICE_PHYSICAL_MATCHING_THEOREM_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_match.md)
- [Historical Higgs tree-level construction](HIGGS_MASS_FROM_AXIOM_NOTE.md)
- [Historical Born-map extension](G_NEWTON_BORN_AS_SOURCE_POSITIVE_THEOREM_NOTE_2026-05-10_gnewtonG2.md)
