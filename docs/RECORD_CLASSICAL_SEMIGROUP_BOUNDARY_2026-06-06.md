# Record Classical Semigroup Boundary

**Date:** 2026-06-06
**Claim type:** exact-support / negative-route-pruning boundary
**Status:** branch-local source note awaiting independent audit handling.
**Primary runner:**
[`scripts/frontier_record_classical_semigroup_boundary_2026_06_06.py`](../scripts/frontier_record_classical_semigroup_boundary_2026_06_06.py)
with cached output
[`logs/runner-cache/frontier_record_classical_semigroup_boundary_2026_06_06.txt`](../logs/runner-cache/frontier_record_classical_semigroup_boundary_2026_06_06.txt).

## Result

For a supplied finite post-record alphabet `O`, the post-record event algebra is
the finite commutative algebra of functions on `O`, equivalently `C^O` after a
basis choice. Its atom basis is the set of realized one-hot record labels.

This finite algebra has a sharp dynamics boundary:

1. Reversible algebra automorphisms are exactly permutations of record atoms.
2. Every derivation of `C^O` is zero. Therefore there is no nontrivial
   connected reversible Hamiltonian-like flow on the finite post-record algebra
   itself.
3. Append/count dynamics on histories `O*` and counts `N^O` is an irreversible
   monoid action/translation: it preserves old records as prefixes and
   increments counts, but nonzero append translations are not automorphisms of
   `N^O`.
4. Nontrivial continuous Markov semigroups live on the probability/ensemble
   layer. They require supplied transition rates or a supplied generator.
5. Stable dial locations are properties of the supplied generator/functional.
   The same two-record alphabet permits an equal-letter stationary point, a
   dimension-weighted stationary point, or other stationary points under
   different valid generators.

Thus the post-record object is information, not probability, in a stronger
dynamics sense: the realized atom/count layer has exact append/coarse-grain
algebra, while rates, stochastic relaxation, and dial attraction are additional
dynamics inputs.

## Why this moves dynamics

The existing record stack gives the typed sequence:

```text
pre-record quantum state / ensemble
  -> record instrument / realized atom
  -> post-record word/count dynamics
```

This note adds the algebraic boundary on the last arrow. Once a record is in
the finite classical alphabet, the only reversible symmetries of that alphabet
are discrete relabelings. There is no hidden continuous post-record unitary
dynamics inside the finite record algebra.

Consequently, any route that needs a continuous rate, convergence law, thermal
relaxation, entropy-gradient flow, or stable dial attractor must supply that
dynamics explicitly. Record can host the resulting realized tokens and counts;
Record alone does not generate the rate law.

## Proof Sketch

Let `A = C^O` with pointwise multiplication and unit `1`.

Every function `phi: O -> O` induces a unital algebra endomorphism

```text
T_phi(f) = f o phi.
```

`T_phi` is invertible exactly when `phi` is a bijection. Therefore

```text
Aut(A) = Sym(O).
```

The group is finite and discrete. A continuous one-parameter path in `Aut(A)`
starting at the identity cannot leave the identity component, because the
identity is isolated from every nonidentity permutation.

Equivalently at the infinitesimal level, if `D` is a derivation of `A`, then for
each atom idempotent `e_i`:

```text
D(e_i) = D(e_i^2) = 2 e_i D(e_i),
```

and for `i != j`:

```text
0 = D(e_i e_j) = e_j D(e_i) + e_i D(e_j).
```

These equations force every component of every `D(e_i)` to vanish, so
`Der(A)=0`.

Append/count dynamics is different. For a finite suffix `v in O*`,

```text
R_v(w) = wv,
count(wv) = count(w) + count(v).
```

If `count(v) != 0`, translation by `count(v)` is not onto `N^O`; for example
the zero count has no preimage. This is exactly the post-record arrow:
durable information accumulates, rather than reversibly flowing inside a fixed
finite atom algebra.

Continuous Markov dynamics can be supplied on the ensemble layer. For a
two-state generator

```text
Q = [[-a, b],
     [ a,-b]]
```

the stationary vector is

```text
pi = (b/(a+b), a/(a+b)).
```

Changing the supplied rates changes the stable point. With `(a,b)=(1,1)` the
stationary vector is `(1/2,1/2)`. With `(a,b)=(2,1)` it is `(1/3,2/3)`. Both are
valid supplied dynamics on the same two-letter alphabet. The finite record
algebra does not select between them.

## Dynamics Implication

This is the clean implication of the user's pre/post split:

- Pre-record qubit states can carry amplitudes and predictive probabilities.
- Record events select/write a realized atom when an instrument and outcome are
  supplied.
- Post-record sites carry information tokens and count/history updates.
- A continuous post-record rate law is a supplied Markov/ensemble model, not a
  consequence of the finite record alphabet.

For the generation/Koide dial, this supports the stable-setting language
without forcing the dial. A dial location can be a stable fixed point of a
named generator or entropy functional. It is not selected by Record unless the
generator/partition/arrow is also supplied or derived elsewhere.

## Unlocks

- Audit rows that only need post-record append/count behavior can cite the
  exact information-dynamics layer.
- Audit rows that claim rates, convergence, relaxation, or stable dial
  attraction must expose the supplied generator/functional.
- Attempts to hide a continuous reversible dynamics inside the finite
  post-record alphabet are pruned.
- The dynamics program can separate three questions:
  record storage, record production, and supplied ensemble/rate evolution.

## Boundaries

- Does not derive record-production dynamics.
- Does not derive Born probabilities, IID trials, transition rates, or a clock
  metric.
- Does not derive a measurement/decoherence model.
- Does not select a Koide/generation dial location.
- Does not force a nontrivial Markov generator.
- Does not turn branch-local source status into repo-wide authority.

## Runner Summary

The runner verifies:

- all functions `O -> O` induce finite-algebra endomorphisms;
- automorphisms are exactly bijections/permutations;
- non-bijective coarse-graining endomorphisms are not reversible;
- derivations of `C^3` have zero-dimensional solution space;
- nonidentity permutations are separated from the identity, so no connected
  reversible flow leaves identity;
- append/count translations compose but are not surjective on `N^O`;
- a supplied Markov semigroup step is stochastic but not a realized atom write;
- its inverse is not stochastic;
- different supplied two-state generators stabilize `(1/2,1/2)`,
  `(1/3,2/3)`, and `(2/3,1/3)` on the same alphabet.

Expected scorecard:

```text
PASS=21 FAIL=0
```
