# Exact Finite Deterministic Pushforward and Product-Kernel Transport Theorem

**Date:** 2026-06-06
**Type:** positive_theorem
**Claim type:** positive_theorem
**Primary runner:**
[`scripts/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.py`](../scripts/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.txt)
**Dependencies:** none. The carriers, probability packet, deterministic map,
observable, and pair kernel below are universally quantified mathematical
arguments.

## 1. Exact finite pushforward

Let `X` and `Y` be nonempty finite sets. Supply an exact rational probability
packet on `X` and a total deterministic map:

```text
P : X -> Q_{>=0},                   sum_{x in X} P(x) = 1,
F : X -> Y.
```

Define the pushforward packet on every target label, including unused labels,
by

```text
Q(y) = sum_{x in X : F(x)=y} P(x).
```

Every summand is nonnegative, so `Q(y)>=0`. Because totality assigns each
source label to exactly one target fiber, the fibers partition `X`; hence

```text
sum_{y in Y} Q(y)
  = sum_{y in Y} sum_{x:F(x)=y} P(x)
  = sum_{x in X} P(x)
  = 1.
```

This proves that deterministic pushforward preserves exact normalization.
Surjectivity is unnecessary: an unused target has its empty-fiber value zero.

## 2. Observable pullback identity

For every exact rational observable `h : Y -> Q`, including signed values,
finite rearrangement gives

```text
sum_{y in Y} Q(y) h(y)
  = sum_{y in Y} sum_{x:F(x)=y} P(x) h(y)
  = sum_{x in X} P(x) h(F(x)).
```

Thus expectation after pushforward equals expectation of the pulled-back
observable before pushforward.

## 3. Product-kernel transport identity

Supply any exact rational pair observable

```text
K : Y x Y -> Q.
```

It may be signed, asymmetric, unbounded relative to `[0,1]`, or different from
one on the diagonal. Those are optional properties of particular supplied
kernels, rather than hypotheses of the transport identity. Expanding both
target fibers proves

```text
sum_{y,y' in Y} Q(y) Q(y') K(y,y')
  = sum_{x,x' in X} P(x) P(x') K(F(x),F(x')).
```

Indeed, the coefficient of each `K(y,y')` on the right is

```text
(sum_{x:F(x)=y} P(x)) (sum_{x':F(x')=y'} P(x')) = Q(y)Q(y').
```

The multiplication `P(x)P(x')` is essential: the identity concerns the
product packet `P x P`, not an additive or single-sample surrogate.

## 4. Executable domain and ordering semantics

The runner represents:

- `X` by the unique string labels in an ordered probability tuple;
- `Y` by a nonempty ordered tuple of unique string labels;
- `F` by one `(source_label, target_label)` tuple entry per source label;
- `h` by one `(target_label, Fraction)` entry per target label; and
- `K` by one `(left_target, right_target, Fraction)` entry per ordered pair in
  `Y x Y`.

Every numeric value has exact runtime type `Fraction`. Integers, booleans,
floats, subclasses, and coercion are rejected. Identifiers have exact runtime
type `str` and are nonempty. Duplicate labels or pairs are rejected.

The order of `Y` fixes pushforward display order. All algebra aligns values by
labels. Independent permutations of the probability, map, observable, or
kernel tuples preserve every label assignment and scalar identity. The map
must be total on `X`; its image may be a proper subset of `Y`.

## 5. Defined word/count example

The following is one finite combinatorial instance, not a physical model.
Take source labels `LL, LR, RL, RR` with

```text
P = (1/2, 1/4, 1/8, 1/8).
```

Define `F` by counting `L` and `R` in each two-letter word and retaining its
first letter:

```text
LL -> 2:0:L,   LR -> 1:1:L,   RL -> 1:1:R,   RR -> 0:2:R.
```

On these four target labels, define

```text
K(a,b) = 1 / (1 + (L_a-L_b)^2 + (R_a-R_b)^2 + [first_a != first_b]).
```

This particular supplied kernel is symmetric, takes values in `(0,1]`, and is
one on the diagonal. Exact enumeration of `Q x Q` gives

```text
sum_{a,b} Q(a)Q(b)K(a,b) = 169/320.
```

The associated capped count update

```text
(l,r,m) --L--> (min(2,l+1), r,       L if m=none else m),
(l,r,m) --R--> (l,       min(2,r+1), R if m=none else m)
```

has a direct combinatorial monotonicity lemma: both counts are nondecreasing,
and a marker different from `none` stays unchanged. This lemma concerns the
displayed defined update only.

## 6. Exact scope

The theorem conclusion consists exactly of finite pushforward normalization,
observable pullback, and product-kernel transport. Its probability packet,
map, observable, and kernel are supplied theorem arguments.

Any application involving physical records, formation, production,
persistence, transition laws, priors, Born weights, instruments, dynamics,
Hamiltonians, clocks, rates, arrows, selectors, or dial interpretations
carries separate model premises. The legacy path name is an identifier and
adds none of those meanings to the theorem.

Audit censuses, ledgers, queues, row maps, exports, helper runners, hashes, and
row counts are repository metadata outside the theorem arguments. The proof is
invariant under changes to those inventories.

## 7. Falsification and reproducibility

The standard-library runner provides:

- a normal exact derivation, including unused targets, collisions, signed
  observables, an arbitrary signed asymmetric kernel, and the `169/320`
  combinatorial example;
- an independent common-denominator implementation exercised across many
  finite carriers, maps, laws, observables, and kernels; and
- hostile controls for malformed domains and false pushforward, expectation,
  collision, product-probability, optional-kernel-property, permutation, and
  physical-selection claims.

Selectable intentional-failure fixtures promote each hostile mutation to a
claimed success. Every individual fixture and the aggregate must exit nonzero.

Run:

```bash
python3 scripts/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.py
python3 scripts/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.py --independent
python3 scripts/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.py --hostile
python3 scripts/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.py --mode intentional-failure --fixture all
```

The cached log records the default normal run. The fresh citation graph has no
direct claim consumer of this theorem. Any future consumer must preserve the
supplied-input boundary above.
