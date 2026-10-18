# Focused rational spectral-enclosure review

Disposition: PASS. The polar-unitary bound and factor336 perturbation estimate are valid under the stated Hermiticity and complex-entry modulus assumptions. No correction required. Read-only review; no formal audit or repository edits.

I read the complete script/result and replayed an exact copy with both declared data files in a relocated temporary directory. Exit0; exact output JSON matches byte-for-byte. The four eigenvalue enclosure radii are 5.652897555719089e-14, 5.122689888690378e-14, 4.685185450194465e-14 and 4.71871112725185e-14. The exact rational separation lower bound is positive, with displayed value8.241208801051598e-7. Dividing the exact bound by336 gives displayed entry radius2.45274071459869e-9.

## Independent bound check

The function bound(X) bounds the operator2-norm: replacing each complex modulus by |Re|+|Im| upper-bounds both induced row/column norms, and ||X||2 <= sqrt(||X||1 ||X||infinity) <= their maximum.

Let delta bound ||U^dagger U-I||2 and delta<1. In the polar decomposition U=Q S, Q is unitary and singular values of U lie in [sqrt(1-delta),sqrt(1+delta)]. Therefore

    ||U-Q||2 <= max(1-sqrt(1-delta),sqrt(1+delta)-1) <= delta.

Writing R=A U-U D gives

    A Q-Q D = R + A(Q-U) - (Q-U)D,

so ||A-Q D Q^dagger||2 <= r+(||A||2+||D||2)delta. The script's rational row/column bounds and max absolute diagonal D supply valid upper bounds for these quantities. Since A is checked exactly Hermitian and D is real, Weyl's inequality matches ordered eigenvalues with the stated uniform error. Numerical diagonalization need not itself be exact: the decimalized U and D are merely candidate witnesses, and the residual/orthogonality calculations are exact rational arithmetic.

Each Liouvillian transition is a difference of two one-particle eigenvalues, giving error err_h+err_hq. Subtracting the sum of both pointwise transition errors from the minimum approximate cross-point separation is therefore valid. All phase triples were independently validated in the previous no-flat review; the staggered phase in this script also correctly implements k+Q.

For entrywise complex modulus perturbations |delta B_s,ij|<=epsilon in each of seven12x12 blocks, ||delta B_s||2<=12epsilon. Unit-modulus Bloch phases then imply ||delta h(k)||2<=84epsilon at either momentum and its Q partner. A transition can move by at most168epsilon; cross-point transition separation can shrink by at most336epsilon. Hence strict epsilon<lower/336 preserves disjointness, provided the perturbed block family remains exactly Hermitian on the real torus. If separate real and imaginary component errors are bounded by epsilon instead, an additional sqrt(2) conversion is needed; the stated radius is for the complex modulus.

## Scope

This establishes a nonzero robustness neighborhood of the stored seven-block model at the two fixed momenta. It does not prove that an unrounded upstream symbolic model lies in that neighborhood; such a claim needs its actual coefficient error bound. It does not cover additional unconstrained hopping blocks, arbitrary q, loss of Hermiticity, or new interactions. The exact rational inequalities are authoritative; decimal displays are summaries, not outward-rounded standalone certificates.

## SHA-256 identities

```text
b4c2bc8c25dafa7c529a96f3109331924eb428d2b363ec765f66fd1efc1e0588  /private/tmp/scalar-environment-20261017/data/collective_corner_response/candidate.json
fc3551317dd9cf09e0530acabd06a0f033e26ec247c6f218ce1c3227d41dc6f6  /private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/probes/exact_no_flat_transition.json
5d282427db93dd3cc574df4b0a92ed5bfa2b7a06df64d903d03539414ecf63e9  /private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/probes/rational_spectral_enclosure.py
e883f704b8bfd43aa0a8244636771b8d2069e1304e3303837e3f8df050cffc13  /private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/probes/rational_spectral_enclosure.json
```
