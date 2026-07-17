# Exact Finite Rational Normalization and Radon–Nikodym Theorem

**Date:** 2026-06-06
**Type:** positive_theorem
**Claim type:** positive_theorem
**Primary runner:**
[`scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py`](../scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.txt)
**Dependencies:** none. Every carrier, weight, and observable below is a
universally quantified mathematical argument, not a framework premise.

## 1. Exact finite normalization

Let `I` be a nonempty finite set. For exact rational weights

```text
u : I -> Q_{>=0},                   U = sum_i u_i > 0,
v : I -> Q_{>=0},                   V = sum_i v_i > 0,
```

define

```text
P_i = u_i/U,                        R_i = v_i/V.
```

Then `P_i,R_i >= 0` and `sum_i P_i = sum_i R_i = 1`. This follows
immediately from positivity of `U,V` and exact finite distributivity:
`sum_i u_i/U = U/U = 1`, and similarly for `R`.

The executable representation is an ordered tuple of `(label, Fraction)`
pairs. Labels are unique. Every number must have exact runtime type `Fraction`;
integers, booleans, floats, subclasses, and coercion are rejected. Input order
is preserved for display, but carrier compatibility means equality of label
sets. All algebra aligns entries by label, never by tuple position.

## 2. Finite Radon–Nikodym density and expectation identity

Say that `P` is absolutely continuous with respect to `R`, written `P << R`,
when

```text
R_i = 0  implies  P_i = 0.
```

Define the finite density label by label by

```text
                P_i/R_i,   if R_i > 0,
(dP/dR)_i  =
                0,         if R_i = 0.
```

The second branch is a declared `0/0 := 0` convention. It is used only after
`P << R` has established that the numerator is also zero. Thus the density is
nonnegative and

```text
sum_i R_i (dP/dR)_i = sum_{R_i>0} P_i = sum_i P_i = 1.
```

For every exact rational observable `f : I -> Q`, including signed values,

```text
sum_i P_i f_i = sum_i R_i (dP/dR)_i f_i.
```

On indices with `R_i>0`, the right summand reduces to `P_i f_i`. On indices
with `R_i=0`, absolute continuity makes both sides zero. This proves the
identity without a positivity assumption on `f`.

Example: raw reference weights `(1,1,0)` and raw source weights `(1,3,0)`
normalize to

```text
R = (1/2, 1/2, 0),
P = (1/4, 3/4, 0),
dP/dR = (1/2, 3/2, 0).
```

For `f=(-1,1,7)`, both expectation formulas equal `1/2`; the value at the
zero-reference label contributes zero.

## 3. Exact density cocycle, including zeros

Let `P,Q,R` be probability packets on the same finite label carrier and assume

```text
P << Q,                             Q << R.
```

Then `P << R`, and with the same zero-denominator convention,

```text
dP/dR = (dP/dQ)(dQ/dR)
```

pointwise on every label. There are three exhaustive cases:

1. If `R_i>0` and `Q_i>0`, ordinary cancellation gives
   `(P_i/Q_i)(Q_i/R_i)=P_i/R_i`.
2. If `R_i>0` and `Q_i=0`, then `P_i=0`; both sides are zero.
3. If `R_i=0`, then `Q_i=P_i=0`; every density in the displayed identity is
   zero by convention.

This proves the cocycle on the full carrier, not merely on its common positive
support.

## 4. Ordering and permutation semantics

Normalization preserves the order of its input tuple. A density is emitted in
the numerator packet's order. Expectations and cocycles compare label maps, so
independent permutations of compatible input tuples do not change any scalar
identity or label-to-density assignment. A positional zip of differently
ordered packets is not an allowed implementation and is tested as a hostile
counterexample.

## 5. Exact scope

This theorem is finite rational algebra only. The words “source,” “reference,”
“measure,” “probability,” “trace/reference,” and “density” name the displayed
finite arrays and sums. Its conclusion consists exactly of normalization,
absolute continuity, the expectation identity, and the density cocycle.

The carrier, both weight packets, and the observable are supplied theorem
arguments. A physical application therefore carries separate premises for
its interpretation and for any physical measure, matrix trace, tracial
functional, trace state, reference state, prior, source law, Born rule,
character/channel/path rule, selector, generation or Koide dial, source unit,
production kernel, Hamiltonian, instrument, dynamics, clock, rate, or arrow.
Record and any physical framework enter only through such a separately stated
application, rather than through the finite algebra proved here.

Audit censuses, ledgers, queues, exports, helper runners, and row counts are
repository metadata outside the theorem arguments. The statement and proof
are invariant under changes to those inventories.

## 6. Falsification and reproducibility

The standard-library runner supplies:

- a normal exact derivation with reference zeros, zero source entries, signed
  observables, label permutations, and both positive-support and zero-support
  cocycle examples;
- an independent normalization through common-denominator integer counts and
  independently coded density, expectation, and cocycle calculations; and
- hostile controls for malformed carriers/types/support, false densities,
  unsafe zero conventions, positional alignment, false expectations, broken
  cocycles, and unsupported physical selection.

Selectable intentional-failure fixtures promote each hostile mutation to a
claimed success. Every individual fixture and the aggregate must exit nonzero.

Run:

```bash
python3 scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py
python3 scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py --independent
python3 scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py --hostile
python3 scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py --mode intentional-failure --fixture all
```

The cached log records the default normal run.

## 7. Consumer boundary

The fresh citation graph has no direct claim consumer of this note. A future
consumer may use only the exact finite identities above and must keep every
physical input and interpretation explicit.
