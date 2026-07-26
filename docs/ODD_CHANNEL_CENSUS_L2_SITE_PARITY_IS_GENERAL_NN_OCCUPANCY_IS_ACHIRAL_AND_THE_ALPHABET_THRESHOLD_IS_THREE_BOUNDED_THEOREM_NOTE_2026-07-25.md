# Odd-Channel Census by Quotient, Range and Alphabet: the L = 2 Parity Protection Is General, Nearest-Neighbour Occupancy Carries No Orientation at Any Quotient, and the Condition Alphabet Must Reach Three Before It Can (Bounded Theorem)

**Date:** 2026-07-25
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact integer character counts, each
cross-checked by an independent combinatorial method; two general proofs with
the census as witness).
**Status authority:** none. Audit: unset. Constitutional effect: none. This
note edits no axiom, foundation, Qualification, primitive, registry, policy,
queue, audit-status, or PR-control surface. **It introduces no axiom and no
primitive, adopts no rule, and does not determine whether the framework's
fixed rule is chiral.**
**Primary runner:**
[`scripts/physical_odd_channel_quotient_threshold_census_cycle706_2026_07_25.py`](../scripts/physical_odd_channel_quotient_threshold_census_cycle706_2026_07_25.py)
(9 PASS / 0 FAIL, exit 0; exact integer arithmetic, no sampling, no floating
point, no repository imports).

## The residual this addresses

> "**Quotient-size thresholds**: the `L = 2` parity protection suggests a
> graded family — which odd channels first fire at which lattice quotients — a
> possible tool for bounding rule chirality by locality range."
> — [`BOOTSTRAP_CONTINUATION_..._2026-07-04`](BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md),
> Residual 2

The landed input is a single data point: the specific channel
`J2 = sum det(d, e, c(e))` vanishes identically on the `L = 2` torus, so
"direction-sensitive rule chirality needs `L >= 3`". This note replaces the
data point with a census, and finds that two of the three gradings are sharp
enough to state as theorems.

## Method

An **odd channel** is a function of the local configuration transforming by
the determinant character of the full cubic group — the unique character that
separates a configuration from its improper image. The number of independent
odd channels is that character's multiplicity in the permutation
representation on configurations,

```text
mult(det) = (1/48) * sum over g of det(g) * Fix(g),
```

with `Fix(g)` the number of configurations `g` leaves alone. Equivalently — and
this is used as an independent check, not as a restatement — `mult(det)` counts
the full-group orbits whose point stabilizer contains **no** improper element.
Both routes are computed and agree.

## Answer

**Theorem 1 (the `L = 2` protection is general, and is site-parity).** On
`(Z/2)^3` we have `-x = x` for every site, so **inversion acts trivially on
sites**, and every improper element acts exactly as its proper partner. The
det-weighted character sum therefore cancels term by term, and **every odd
channel built from site data vanishes identically on `L = 2` — at every range
and at every alphabet richness.** This strictly generalizes the landed
statement, which covered one channel at one range.

The protection is specific to `L = 2` and is **not** an even-`L` effect: at
`L = 4`, `-1 != 1 (mod 4)`, inversion acts nontrivially, and the cancellation
fails (row K3).

What survives at `L = 2` is exactly what the group still moves: contents. With
inert labels of any richness the count is zero at every range; with
polar-vector contents it is not (13 channels at range 1, 12289 at range 2).
**At `L = 2`, orientation can only be content-carried** (row K8).

**Theorem 2 (nearest-neighbour occupancy carries no orientation, at any
quotient).** On the seven-site star — a site and its six neighbours —
`mult(det) = 0` for binary occupancy. The mechanism is verified directly and
independently of the character sum: **all 128 occupancy patterns of the star
have an improper symmetry** (row K7). Since the star and its group action are
identical for every `L >= 3`, and `L = 2` is covered by Theorem 1, this holds
at every quotient.

**Consequence, stated at the width it actually has.** Let `A(k)` be the
availability set the rule assigns to a nearest-neighbour occupancy condition
`k`. Every such `k` has an improper stabilizer `m0`. For any improper `m`,
write `m = g m0` with `g = m m0^{-1}` proper; then `m k = g k`, so proper
covariance alone gives

```text
A(m k) = A(g k) = g A(k).
```

So the **condition side carries no orientation**: the improper image of a
nearest-neighbour occupancy condition is always reachable from it by a proper
rotation. This does **not** make the rule achiral. Achirality additionally
requires `A(m k) = m A(k)`, which by the display above holds iff `A(k)` is
`m0`-invariant — and availability sets may be chiral. **The correct conclusion
is that any chirality of a rule reading only nearest-neighbour occupancy must
be carried entirely by the availability sets it outputs, never by the
conditions it reads.**

**Theorem 3 (the alphabet threshold is three).** On the same star, with sites
carrying empty or one of `k` distinguishable labels:

| alphabet (incl. empty) | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|
| odd channels | **0** | **3** | 80 | 600 | 2730 | 9310 |

Binary occupancy carries nothing; **three values — empty plus two contents —
is the smallest condition alphabet at which the nearest-neighbour star carries
an orientation, and it carries exactly three channels.** The value 3 is
computed twice, by the character sum and by direct orbit-stabilizer counting
over all `3^7` configurations, with agreement (row K9).

**The occupancy census (row K4).** Odd occupancy channels by quotient and
range:

| `L` \ `r` | 1 | 2 | 3 |
|---|---:|---:|---:|
| 2 | 0 | 0 | 0 |
| 3 | 0 | 9776 | 2753216 |
| 4 | 0 | 79088 | 91488443648 |
| 5 | 0 | 662192 | 3002363501982720 |

The first firing is at `(L, r) = (3, 2)`. **The three zeros in the `r = 1`
column are one computation, not three independent confirmations** — for every
`L >= 3` the range-one window is the same seven-site star. The cell
`(L, r) = (5, 2)` is the only tabulated cell whose window is unwrapped
(`|W| = 25`, the full taxicab ball); every other `r >= 2` cell wraps.

## A refuted hypothesis, recorded

An earlier design of this cycle asserted that **inert** labels cannot carry
oddness, on the reasoning that with the group blind to the labels only
position is left to carry it. **That is false, and the runner refuted it:**
inert labels at `L = 3, r = 1` give 9310 odd channels while binary occupancy
on the same window gives zero. Distinguishability alone breaks improper
symmetries — label the neighbours `+e1, +e2, +e3` with distinct labels and the
mirror exchanging `e1` and `e2` no longer fixes the configuration.

The refutation is what produced Theorem 3: the graded parameter is **alphabet
richness**, not whether contents transform. The false hypothesis survives in
the runner only as the docstring of `make_fix_inert`, which records it.

## What this does not do

- It does **not** determine whether the framework's fixed rule is chiral, and
  supplies no rule.
- It does **not** show that a nearest-neighbour rule is achiral. The scoped
  consequence under Theorem 2 is the whole of what follows, and the note
  states the gap explicitly rather than closing it.
- It does not bound rule chirality by locality range in the sense Residual 2
  hoped for. What it delivers is the census that such a bound would have to be
  read off, plus two thresholds that are sharp.
- The polar-vector content model is carried from the landed empty-state
  bootstrap as a **named model**, not as axiom content; the content-carrying
  rows depend on it. The occupancy and inert-label rows do not.
- Counts are for the full function space on configurations; no claim is made
  that any particular channel is realized by the framework's rule, nor that
  low-degree or physically simple channels exist among them.
- No lane, row, or obligation status is changed, and no N1–N8 verdict is
  awarded.

## Controls and cross-checks

- **Burnside (row K6).** The trivial-character multiplicity equals the orbit
  count, computed by direct enumeration, at three separate `(L, r)` cells.
  This validates the `Fix(g)` bookkeeping that every other count uses.
- **Two methods for the threshold (row K9).** Character sum and direct
  orbit-stabilizer counting both give 3.
- **Two methods for the range-one zero (rows K4, K7).** Character sum gives 0;
  direct search exhibits an improper stabilizer element for each of the 128
  patterns.
- **A negative control on the mechanism (row K3).** `L = 4` breaks the `L = 2`
  cancellation, so Theorem 1 is not an even-`L` artifact.
- **Window well-definedness.** The torus taxicab metric is signed-permutation
  invariant, so every window is a union of group orbits; the runner asserts
  closure under the action rather than assuming it.
- Every character sum asserts divisibility by 48 before dividing, so a
  malformed count fails loudly instead of silently rounding.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the Admissibility
covariance sentence (proper rotations only) and the nearest-neighbour clause.
The residual, the `L = 2` parity-protection data point, the `J2` channel, and
the proper/improper covariance bookkeeping are from
[`BOOTSTRAP_CONTINUATION_..._2026-07-04`](BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md).
The content-as-polar-vector model and the orbit dichotomy are from
[`EMPTY_STATE_BOOTSTRAP_..._2026-07-04`](EMPTY_STATE_BOOTSTRAP_ALL_OPEN_AVAILABILITY_ORBIT_DICHOTOMY_DEGREE_NINE_CHIRALITY_WALL_BOUNDED_THEOREM_NOTE_2026-07-04.md).
The ten-orbit classification of the 64 nearest-neighbour occupancy patterns is
landed in
[`INFORMATIVE_FRACTION_..._2026-07-02`](INFORMATIVE_FRACTION_COVARIANT_RULE_QUANTIZATION_OCCUPANCY_RESIDUAL_THEOREM_NOTE_2026-07-02.md);
this note's Theorem 2 concerns the improper symmetries of those patterns,
which that note does not treat. All pieces the runner needs are re-earned
inside it.
