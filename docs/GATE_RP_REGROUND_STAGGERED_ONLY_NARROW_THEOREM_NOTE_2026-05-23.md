# Staggered determinant positivity; reflection-positivity bridge remains open

**Date:** 2026-05-23; source correction 2026-10-21.
**Claim type:** bounded_theorem (finite determinant statement only).
**Status authority:** independent audit lane only; no ledger verdict is changed.
**Runner:** [`scripts/frontier_gate_rp_reground_staggered_only_discriminator.py`](../scripts/frontier_gate_rp_reground_staggered_only_discriminator.py).

## Corrected conclusion

The former note inferred that staggered determinant positivity discharged the gate's reflection-positivity dependency. That inference is withdrawn. The cited [Case A note](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md) explicitly excludes reflection positivity of the full action; its theorem supplies a determinant input only. Historical audit labels cannot strengthen its mathematical conclusion. The original source is recoverable at f24d17d97d372df977476e4a69674577f31af575.

## Finite determinant theorem

Use an even-side-length periodic lattice, unitary links, the nearest-neighbor massless staggered operator M, and epsilon(x)=(-1)^(sum x). The bipartite periodic boundary condition matters: an arbitrary odd periodic side does not preserve the grading across its boundary. Opposite hopping blocks are adjoint negatives, so M^dagger=-M; every hop flips parity, so {epsilon,M}=0.

In the balanced parity basis (including color multiplicities),

```text
M = [[0,K],[-K^dagger,0]],   K square.
det(m I+M)=det(m² I+K^dagger K)=product_j(m²+sigma_j²)>0, m>0.
```

This follows by the Schur complement with invertible m I, or by singular-value decomposition of K. Include zero singular values: each contributes m². It holds for every link configuration satisfying the structural hypotheses. Random SU(3) tests illustrate those identities, not universal quantification by sampling.

## Why determinant positivity is insufficient

Reflection positivity asks for <(Theta F) F> >= 0 for all observables F supported on the chosen positive-time side, with a specified reflection, measure and observable algebra. A positive density alone does not ensure it. On two reflected spins s_-,s_+ in {−1,1}, take weight 1 when they agree and 2 when they differ. All four weights are strictly positive, and the measure is reflection invariant. For F=s_+ and Theta F=s_-,

```text
<(Theta F)F>=(1+1-2-2)/(1+1+2+2)=-1/3.
```

Thus even a reflection-invariant positive weight may fail reflection positivity. This counterexample refutes the implication, not reflection positivity of a particular staggered action. Establishing that action's RP still needs the actual time-reflection factorization or transfer construction, including fermionic variables/boundaries. No new RP impossibility claim is made.

## Scope and reproduction

Run `python3 scripts/frontier_gate_rp_reground_staggered_only_discriminator.py`. It checks staggered finite-matrix identities, the singular-value determinant formula including a zero-mode fixture, and the reflection-positive-weight counterexample. It does not close a gate, repair a broad RP theorem, certify an audit status, or derive a full fermionic transfer operator.

The [gate synthesis](STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md) is context, not evidence that the missing RP implication holds. The [broad RP source](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md) is also context; this correction makes no adjudication of its other arguments. Stable file and claim identifiers are preserved.
