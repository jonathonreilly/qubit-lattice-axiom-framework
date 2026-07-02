# Gauge Factor-Local Selector Normalizer Theorem

**Date:** 2026-06-18
**Claim type:** bounded_theorem / exact-support boundary.
**Status authority:** independent audit lane only. This source note does not
update or predict any audit verdict.
**Primary runner:**
[`scripts/gauge_factor_local_selector_normalizer_2026_06_18.py`](../scripts/gauge_factor_local_selector_normalizer_2026_06_18.py)
**Cached runner output:**
[`logs/runner-cache/gauge_factor_local_selector_normalizer_2026_06_18.txt`](../logs/runner-cache/gauge_factor_local_selector_normalizer_2026_06_18.txt)

## Targeted blocker

This note targets a finite-algebra part of the audited conditional blocker for
the parent trace target
`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md`:

```text
missing_bridge_theorem: derive or explicitly admit a retained MR_color/factorwise
carrier-locality and gauging-selection bridge, including chiral su(2)_L.
```

The result here does **not** supply that physical bridge. It proves the exact
finite statement that, once a factor-algebra preservation rule is supplied on
the same `C^3(base) x C^2(fiber)` carrier, the algebraic normalizer is uniquely
the factorwise `su(3) + su(2) + u(1)` surface rather than full `u(6)`.

## Minimal premise set

Allowed:

- the supplied carrier used by the parent row, `H = C^3(base) x C^2(fiber)`;
- finite-dimensional matrix algebra on `End(H)`;
- the candidate factor observable algebras
  `A_base = End(C^3) x I_2` and `A_fiber = I_3 x End(C^2)`.

Forbidden as proof inputs:

- physical-color matter realization `MR_color`;
- a derivation of the supplied tensor split from Lattice, Quantum, or Record;
- a dynamical gauge-action principle;
- chiral `su(2)_L`;
- observed Standard Model matter content, fitted couplings, or PDG values.

## Exact theorem

Let `X` be a Hermitian infinitesimal carrier generator on
`H = C^3 x C^2`. Say that `X` preserves the supplied factor observable
algebras if its commutator derivation maps each factor algebra back into
itself:

```text
i[X, End(C^3) x I_2] subset End(C^3) x I_2,
i[X, I_3 x End(C^2)] subset I_3 x End(C^2).
```

Then the full real solution space is exactly

```text
u(3) x I_2  +  I_3 x u(2),
```

with the shared identity counted once. Its dimension is

```text
dim u(3) + dim u(2) - dim u(1) = 9 + 4 - 1 = 12.
```

Equivalently, it decomposes as

```text
su(3) x I_2  +  I_3 x su(2)  +  u(1) I_6.
```

The remaining `24` Hermitian tensors

```text
su(3) x su(2)
```

are exactly the cross-factor complement: together with the 12-dimensional
factor-preserving algebra they span full `u(6)`, but each nonzero cross tensor
fails the factor-algebra preservation condition.

## What this proves for the parent gauge row

The parent row already checks that the factorwise algebra is closed and that
full `u(6)` is the unrestricted carrier algebra. This note adds the missing
finite-algebra normalizer statement:

```text
supplied C^3 x C^2 carrier
+ supplied rule "gauged generators preserve the base/fiber observable
  algebras separately"
  => unique maximal infinitesimal algebra is su(3) + su(2) + u(1).
```

Thus, under that rule, there is no additional matrix-algebra ambiguity between
the dim-12 factorwise algebra and the dim-36 full carrier algebra. The `u(6)`
ambiguity has been localized: it is exactly the absence of a retained source
for the factor-algebra preservation rule, `MR_color`, and the chiral weak
coupling surface.

## What remains open

- Derive or explicitly admit `MR_color`: quark matter occupies the symmetric
  base fundamental, physical color-singlet records are the relevant record
  algebra, and link/connection variables route the base-`SU(3)` index.
- Derive or explicitly admit the physical factor-algebra preservation rule.
  This note proves its consequence; it does not make that rule an axiom or a
  retained primitive.
- Derive or explicitly admit chiral `su(2)_L`. The finite normalizer theorem is
  blind to vector versus left-handed weak coupling.
- Supply gauge dynamics, action, couplings, anomaly-complete matter content,
  and electroweak matching.

## Relation to the conjugation-independence no-go

[`GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md`](GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md)
proved that conjugation-invariant carrier data and scalar-commutant
irreducibility cannot select the factorwise embedding. This note is the
positive companion on the surviving route: a non-conjugation-invariant
factor-observable preservation rule does select it, and the runner verifies
that selection exactly.

The two statements are consistent:

- invariant carrier data cannot select the factorwise embedding;
- preserving the supplied factor observable algebras can select it;
- therefore the load-bearing missing bridge is the physical source of that
  factor-observable preservation rule, not another hidden finite-matrix
  computation.

## What this note does not claim

- It does not derive physical `SU(3)_c`, `MR_color`, or quark matter
  assignment.
- It does not derive the supplied `C^3 x C^2` carrier split from the axioms.
- It does not derive why gauge generators must preserve the factor observable
  algebras; that is the rule whose physical source remains open.
- It does not derive chiral `su(2)_L` or distinguish left-handed, right-handed,
  or vector weak coupling.
- It does not update audit ledgers, apply audit verdicts, or claim retained
  status.

## Runner certificate

The runner verifies:

1. the linear normalizer constraints have nullity `12` inside Hermitian `u(6)`;
2. the local span `su(3) x I_2 + I_3 x su(2) + u(1)I_6` has dimension `12`;
3. every local generator preserves both factor observable algebras;
4. the 24 `su(3) x su(2)` cross tensors span the complement and, one by one,
   fail factor-algebra preservation;
5. local plus cross spans all Hermitian `u(6)`;
6. the local span is Lie-closed;
7. the source note keeps `MR_color`, the physical factor-locality source,
   chiral `su(2)_L`, and audit status out of scope.

Expected output:

```text
SCORECARD PASS=14 FAIL=0
```
