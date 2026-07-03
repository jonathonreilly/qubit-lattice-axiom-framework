# Observable-Principle T1-d Positive-Diagonal Readout Classifier

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Source-side status:** bounded-support source theorem; independent audit lane owns any effective status.
**Trace class:** upstream_support
**Target blocker:** `observable_principle_from_axiom_note` is currently blocked
on T1-d: the determinant-only scalar readout quotient on `R_{>0}` and the
source-blocks-to-records clause are declared bridge inputs rather than derived
from Record plus determinant algebra.
**Primary runner:**
[`scripts/observable_principle_t1d_positive_diagonal_readout_classifier_2026_06_18.py`](../scripts/observable_principle_t1d_positive_diagonal_readout_classifier_2026_06_18.py)

## Result

This note classifies the exact finite positive diagonal readout freedom left by
the 2026-06-16 T1-d no-go. It does not derive T1-d from Record, does not add a
new axiom or primitive, and does not assert a physical readout context. It
proves the local mathematical shape of the missing bridge:

1. On finite positive diagonal source blocks, every continuous scalar readout
   family that is additive under block direct sums has the form
   `W_n(x_1,...,x_n) = sum_i phi(x_i)` for a continuous one-site function
   `phi : R_{>0} -> R`.
2. Such a family is a single determinant-only readout across dimensions iff
   `phi(x) = c log x`.
3. If fixed block dimension is allowed as extra readout data, the larger family
   `phi(x) = c log x + k` is determinant-only only after the dimension label
   `n` is supplied separately: `W_n = c log(prod_i x_i) + k n`.
4. Therefore the T1-d determinant-only bridge is exactly the quotient that
   erases all non-logarithmic one-site invariants and any global dimension
   label. The separate source-blocks-to-records clause remains a separate
   bridge: this classifier starts after a source-block additive readout family
   has been supplied.

The retained no-go witness
`W_epsilon(S) = log det(S) + epsilon Tr(S)` is not an isolated trick. It is
the classifier member with `phi(x) = log x + epsilon x`, so it is one point in
the full family of continuous direct-sum additive positive-diagonal source
readouts that Record-style additivity cannot exclude.

## Proof-surface dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  -- Record supplies finite scalar additivity only and does not supply the
  source/action or physical-observable identification used by T1-d.
- [`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md`](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md)
  -- existing independence wall showing that determinant-only readout and
  source-block-to-record disjointness are not consequences of Record plus
  determinant algebra.

## Theorem 1: direct-sum additive diagonal readouts are one-site sums

Let `D_n = (R_{>0})^n`, with direct sum given by tuple concatenation. Let

```text
W_n : D_n -> R,       n >= 1
```

be a family of continuous scalar readouts satisfying block additivity:

```text
W_{m+n}(x_1,...,x_m,y_1,...,y_n)
  = W_m(x_1,...,x_m) + W_n(y_1,...,y_n).
```

Set `phi(t) = W_1(t)`. Then for every `n`,

```text
W_n(x_1,...,x_n) = phi(x_1) + ... + phi(x_n).
```

Proof: repeatedly split off the first coordinate by the block-additivity law.
The case `n=1` is the definition of `phi`; the induction step is

```text
W_{n+1}(x_1,...,x_n,x_{n+1})
  = W_n(x_1,...,x_n) + W_1(x_{n+1})
  = sum_{i=1}^{n+1} phi(x_i).
```

Permutation invariance is automatic for the sum form; if the direct-sum
surface treats ordered blocks as mere representatives of unordered diagonal
blocks, this is the required symmetric representative.

## Theorem 2: determinant-only is the logarithmic quotient

Assume in addition that one scalar function `F : R_{>0} -> R` makes the family
determinant-only across block dimensions:

```text
W_n(x_1,...,x_n) = F(prod_i x_i)       for all n >= 1.
```

For `n=1`, `F(t)=phi(t)`. For `n=2`,

```text
phi(x) + phi(y) = W_2(x,y) = F(xy) = phi(xy).
```

Thus `phi` is a continuous homomorphism from the multiplicative positive reals
to the additive reals. With `u = log x`, the function
`g(u)=phi(exp u)` is continuous and additive on `R`, so `g(u)=c u`. Hence

```text
phi(x) = c log x,      W_n(x_1,...,x_n)=c log(prod_i x_i).
```

Conversely, every `c log(prod_i x_i)` is continuous, direct-sum additive, and
determinant-only.

If a separate dimension label is allowed, then
`phi(x)=c log x + k` gives

```text
W_n(x_1,...,x_n)=c log(prod_i x_i)+k n.
```

This is determinant-only on a fixed `n`, but not as a single function of
`prod_i x_i` across all dimensions unless `k=0`; for example `diag(4)` and
`diag(2,2)` have the same determinant and different `n`.

## Implication for T1-d

The parent Observable Principle note needs two independent pieces:

1. a source-to-record disjointness bridge, supplied by a readout-context
   theorem, that makes disjoint independent source blocks register as disjoint
   records, so Record additivity applies to the supplied source blocks; and
2. a determinant quotient selecting the logarithmic one-site function and
   erasing all other continuous one-site invariants and global dimension
   labels.

The 2026-06-16 no-go proves these pieces are not consequences of the current
Record/minimal axioms plus determinant algebra. This classifier shows what the
positive bridge must actually prove on the finite positive diagonal surface.
It is source-side support for a future readout-context theorem; it is not that
theorem.

## No-Go And Overclaim Guardrails

- This note does not treat T1-d as Record-derived.
- This note does not add a new axiom, primitive, Tier-A admission, physical
  readout context, source/action map, or measurement rule.
- This note does not close the parent `observable_principle_from_axiom_note`
  audit row. It supplies bounded support that makes the remaining bridge
  mathematically explicit.
- This note does not claim that trace-sensitive readouts are physically right;
  it shows they remain mathematically live until the determinant quotient is
  supplied.
- The source-to-record disjointness wall is not solved here. A non-injective
  source-to-record assignment is still possible unless a readout-context
  theorem rules it out.

## Verification

The runner checks:

- exact recursive decomposition of direct-sum additive diagonal readouts into
  one-site sums;
- exact additivity for several continuous one-site functions, including
  `log x + epsilon x`;
- determinant-only iff the one-site function is logarithmic, with the dimension
  constant exposed as non-global determinant data;
- the same determinant witnesses `diag(4,1)`/`diag(2,2)` and
  `diag(4)`/`diag(2,2)`;
- source-note guardrails: the parent still declares T1-d as a Boundary, cites
  this classifier and the 2026-06-16 no-go, and does not claim the classifier
  derives T1-d from Record.

Expected runner result: `TOTAL: PASS=33 FAIL=0`.
