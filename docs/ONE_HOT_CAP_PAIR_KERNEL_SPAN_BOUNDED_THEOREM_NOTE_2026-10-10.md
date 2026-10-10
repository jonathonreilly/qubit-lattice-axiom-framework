---
claim_id: one_hot_cap_pair_kernel_span_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), fix a sign and a modulus m in {1, 2, 3}. The soldered bond-symmetric kernels supported on the bonds a·d = (sign) m and b·d = -(sign) m, with every slice sum equal to 0, form a 3-dimensional space. Six such patterns are disjoint and give dimension 18. Each pattern is spanned by the cap line and the matched and swapped transverse crosses on that pair of caps. The six crosses on the positive caps lie outside the six cap lines and the six crosses on the negative caps. Each positive-cap basis kernel is strictly positive for absolute parameter below 1 and has product mean 1, so the 2026-09-22 converse makes it order-blind. The sum of the positive matched crosses at heights 1 and 2 has two-neighbour moment 23/24. No parameter is selected. Kernels with two live directions are not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/one_hot_cap_pair_kernel_span_2026_10_10.py
---

# One-hot cap-pair kernels are spanned by three lines

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/one_hot_cap_pair_kernel_span_2026_10_10.py`](../scripts/one_hot_cap_pair_kernel_span_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Each equivariant one-cap-pair support has kernel dimension 3, spanned by the cap line and two transverse crosses."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a soldered order-blind kernel with two live directions on this orbit remains outside the eighteen cap-pair kernels. Search first. A negative answer must name the ansatz."
conditional_surface_status: "one proper orbit of (1, 2, 3); one cap-pair support a·d = (sign) m and b·d = -(sign) m; uniform average; absolute parameter below 1 on the positive-cap basis"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Quoted premises

Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site."

Admissibility: "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations."

Reading note (2), interpretive: "Read with Record, the distribution
concerns which possibility a forming record locks, conditional on
formation at that site; it does not supply the formation site,
probability, or rate."

The parent note's converse: "Conversely every family with these
properties is order-blind on every window." It leaves the sentence
"Other generic orbits and higher-rank bond spaces are not classified."

## Theorem

**Target.** Inside the ansatz of soldered bond-symmetric kernels on the
proper orbit of `(1, 2, 3)` that are supported on one pair of opposite
caps, decide whether any kernel remains outside the cap line and the
transverse crosses.

**Ansatz.** Fix a sign `σ` in `{+1, -1}` and a modulus `m` in
`{1, 2, 3}`. A kernel in this pattern may be nonzero only on bonds
`(d, a, b)` with `a·d = σ m` and `b·d = -σ m`. It is unchanged by bond
reversal, it transforms by the soldered proper action, and every slice
sums to 0.

**Conclusion.** Each record meets `a·d = σ m` for exactly one direction
`d`. Proper rotations preserve the pattern. Bond orbits on the pattern
number 4, and the slice-sum rows have rank 1, so the kernel dimension
is 3. The six patterns are disjoint as sets of bonds and the sum of the
dimensions is 18.

The cap sign at level `k` is the sign of the product of the two
coordinates transverse to `d` when `a·d = k`, and 0 otherwise. The cap
line is the product of that sign on the left record with the sign on
the right record at `-d`. For records `a = (x, y, z)` and
`b = (x', y', z')`, the matched cross is

`sign(x y' - y x')`

when `z = σ m`, `z' = -σ m`, `|x| = |x'|` and `|y| = |y'|`, and 0
otherwise. The swapped cross is nonzero when `z = σ m`, `z' = -σ m`,
`|x| = |y'|` and `|y| = |x'|`. Its value is `sign(x y' - y x')` for
`σ = +1`, and `sign(y x' - x y')` for `σ = -1`. Transport by a proper
rotation `g` with `g e_z = d` gives the kernel in direction `d`, and
the value does not depend on `g`. These three kernels span the
3-dimensional pattern. The eighteen kernels, six caps and twelve
crosses, are linearly independent, so they are a basis of the ansatz.
No further kernel exists inside this ansatz.

The six crosses with `σ = +1` each lie outside the span of the six cap
lines and the six crosses with `σ = -1`. Their values lie in
`{-1, 0, 1}`. Each record activates one direction and every slice sums
to 0, so

`phi_d(a, b) = 1 + t L_d(a, b)`

has neighbour-product mean 1. For `|t| < 1` every factor is positive.
The parent converse makes each such family order-blind on every window.

The witnesses, each equal to `-1`, are the positive matched bonds

`((-3, 2, 1), (3, 2, -1))`, `((-3, -1, 2), (-3, 1, -2))`,
`((-2, 1, 3), (2, 1, -3))`

and the positive swapped bonds

`((-3, 2, 1), (-2, 3, -1))`, `((-3, -1, 2), (1, 3, -2))`,
`((-2, 1, 3), (-1, 2, -3))`,

all in direction `e_z`. The sum of the positive matched crosses at
heights 1 and 2 has

`E[(1 + M_{-e_x}(., (1, -2, -3))) (1 + M_{-e_y}(., (-1, 2, -3)))] = 23/24`.

**Proof.** The runner enumerates the 24 proper rotations and the orbit.
It counts bond orbits by the soldered action and bond reversal, then
row-reduces the slice sums. Four orbits and slice rank 1 give dimension
3 on each pattern. The three explicit kernels are constant on each bond
orbit, vanish off the pattern, and their orbit coordinates have rank 3,
so they span the pattern. Row reduction of all eighteen bond vectors
has rank 18. The twelve vectors with the cap lines and the negative
crosses have rank 12, and each positive cross raises that rank to 13.
The product-mean argument is the one-live-direction cancellation already
used for a single cross: the product equals `1 + t L_d(a, b_d)` at the
single live direction, and the slice sum is 0. The two-neighbour moment
is the uniform average of the displayed product.

**Obligations.** Proved here: the pattern count, the spanning basis, the
positive-cap witnesses, positivity at half the parameter, and the
mixture moment. Cited from the parent, and not re-proved: the converse.
The strongest missing lemma is whether a soldered order-blind kernel
with two live directions remains outside this basis. This note does not
classify that larger set.

## What this does not do

- It does not select `t`.
- It does not claim that every soldered order-blind kernel on the orbit
  lies in this 18-dimensional ansatz.
- It does not claim that a sum of two patterns is order-blind. The
  moment `23/24` says that two-neighbour normalisation fails for the
  displayed sum.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/one_hot_cap_pair_kernel_span_2026_10_10.py` repeats the group,
the orbit, the pattern count, the spanning check, and the moment.

## Imports

No formation site, probability, rate, or selected parameter is imported.
The proper rotations, the cap signs, and the cross values are enumerated
here. Order-blindness of a family that already meets the product-mean
conditions is the parent converse, quoted above.
