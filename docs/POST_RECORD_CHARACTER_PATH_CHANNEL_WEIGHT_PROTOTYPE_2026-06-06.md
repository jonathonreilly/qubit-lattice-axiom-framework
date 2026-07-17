# Exact Finite Weight Normalization and Path-Product Theorem

**Date:** 2026-06-06
**Type:** positive_theorem
**Claim type:** positive_theorem
**Primary runner:**
[`scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py`](../scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.txt)
**Dependencies:** none. The finite carriers and rational weights below are
universally quantified mathematical arguments, not framework-supplied premises.

## 1. Exact normalization theorem

Let `I` be a nonempty finite set and let

```text
w : I -> Q_{>=0},                 W = sum_{i in I} w_i > 0.
```

Define `p_i = w_i/W`. Then, exactly in `Q`,

```text
p_i >= 0,                           sum_{i in I} p_i = 1.
```

Indeed, `W` is positive, so division preserves nonnegativity, and

```text
sum_i p_i = (sum_i w_i)/W = W/W = 1.
```

This is a positive theorem about every finite rational packet satisfying the
displayed hypotheses. The carrier and weights are variables of the theorem;
no physical carrier or weight rule is asserted.

The executable representation is an ordered finite tuple of `(label, weight)`
pairs. Labels must be unique, every weight must be an actual `Fraction`, and
the tuple must be nonempty. Zero entries are allowed, but a zero total is not.
Floats, integers masquerading as exact weights, duplicate labels, negative
weights, empty carriers, and nonpositive totals are rejected rather than
coerced. Labels and edge identifiers are compared by exact string equality:
case folding and Unicode normalization are not implicit, so distinct strings
remain distinct while an exact repeated string is a duplicate.

For example,

```text
(4, 1)       -> (4/5, 1/5),
(6, 3, 1)    -> (3/5, 3/10, 1/10).
```

## 2. Row-stochastic corollary

Let `R` and `C` be nonempty finite row and column carriers. For every `r in R`,
let `w_(r,c) in Q_{>=0}` have positive row total
`W_r = sum_c w_(r,c)`. Applying the theorem separately to each row gives

```text
P_(r,c) = w_(r,c)/W_r >= 0,          sum_{c in C} P_(r,c) = 1.
```

Thus `P` is row-stochastic in the exact algebraic sense. Every row uses the
same explicitly supplied column-label set. Column order is representation only:
the executable canonicalizes every row to the first row's order, while a
missing or extra column is rejected. For the two-row example

```text
A: (3, 1) -> (3/4, 1/4),
B: (1, 1) -> (1/2, 1/2).
```

both row sums are exactly one. Calling this array row-stochastic adds no claim
that it is a physical transition kernel.

## 3. Supplied-edge path-product theorem

Let `E` be a finite collection of directed edges with unique edge identifiers,
explicit source and target vertices, and exact nonnegative rational weights
`a_e`. A path is an ordered word of edge identifiers with a supplied start
vertex. It is valid only when each edge exists and its source is the current
vertex. Define

```text
A(empty path at v) = 1,
A(e_1 ... e_n)     = product_{k=1}^n a_(e_k).
```

Repeated traversal is counted once per occurrence; edge definitions themselves
must be unique. If `P` ends where `Q` starts, concatenation is defined and

```text
A(P Q) = A(P) A(Q).
```

This follows from associativity of finite rational multiplication: the factors
on the left are exactly the factors of `P` followed by those of `Q`. Missing
edges, duplicate edge definitions, inexact or negative edge weights, broken
incidence, and noncomposable concatenations are rejected.

For edges of weights `2` from `s` to `m`, `3` from `m` to `t`, and `1`
directly from `s` to `t`, the two path products are `6` and `1`. Normalizing
that explicitly supplied two-path carrier gives `(6/7, 1/7)`. A loop of weight
`2/3` traversed twice has weight `4/9`, not `2/3`; this fixes duplicate-traversal
semantics.

## 4. Exact scope boundary

The theorem proves only finite rational normalization, rowwise stochasticity,
and multiplicative composition under the definitions above. It does not derive
or select

- a carrier of paths, characters, channels, rows, columns, vertices, or edges;
- any local weight, measure, prior, character coefficient, channel rule, path
  rule, or probability law;
- a physical selector, Born rule, source law, production kernel, Hamiltonian,
  instrument, clock, rate, or arrow;
- a directional parameter, Wilson surface, generation/Koide dial, or any
  physical interpretation of a normalized packet; or
- any of those data from Record, the minimal axioms, or the approved
  primitives.

In particular, normalization cannot choose its own inputs. A later physical
claim must separately derive or explicitly premise the relevant carrier,
weights, interpretation, and selector. None is a dependency of this formal
theorem because none is used in its proof.

The theorem has no audit-census, ledger, queue, export, or row-count premise.
Those mutable repository inventories are not mathematical evidence and are not
part of this certificate.

## 5. Falsification and reproducibility

The runner uses only standard-library exact `Fraction` arithmetic. Its normal
mode checks the theorem, both displayed normalizations, multiple stochastic
rows, empty-path identity, repeated traversal, path concatenation, and the
`6:1` path normalization. Its independent mode reconstructs normalization via
common-denominator integer counts and path products via separate numerator and
denominator products.

Hostile mode verifies rejection of empty and zero-total carriers, negative and
inexact weights, strict rejection rather than coercion of booleans and type
subclasses, malformed entries, duplicate labels, rows, and edge definitions,
and mismatched row carriers. It also checks order-independent common-carrier
semantics, exact Unicode-identifier equality, an empty edge set with the empty
path, zero-weight edges, missing and incidence-broken edges, noncomposable
paths, wrong-total normalization, additive path weights, dropped repeated
traversals, and an in-memory source mutation that asserts unsupported physical
selection. Individually selectable intentional-failure fixtures promote each
of the 17 named hostile mutations to a claimed success; every individual
fixture and their aggregate must exit nonzero.

Run:

```bash
python3 scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py
python3 scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py --independent
python3 scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py --hostile
python3 scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py --mode intentional-failure --fixture all
```

The cached log records the default normal run.

## 6. Consumer boundary

The fresh citation graph has no direct claim consumer of this note. Repository
exports that merely record its path or runner are inventory snapshots, not
scientific consumers. Any future consumer may use only the three exact
algebraic conclusions above and must keep every physical input and
interpretation explicit.
