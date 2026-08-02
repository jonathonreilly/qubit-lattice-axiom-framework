# The Body-Diagonal Law for the Reassembled Static Operator, and the Transversal Refinement — Cycle 717

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

## Setting

The open-coframe static Hessian `Q(L)` is assembled by the cycle-696 compiler
[physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
on an `L x L x L` box with a free (unwrapped) boundary. The 24 proper rotations
of the cube act on the static variable index by relabelling; write `P_a` for the
permutation carried by frame `a`, and `Q_g = P_g Q P_g^T` for the operator
reassembled in frame `g`. The measured degree-of-freedom counts are `n = 98` at
`L = 3` and `n = 279` at `L = 4`, at scale `2.9e+01`.

Cycle `physical_source_stabilizer_coset_collapse_k_sign_law_cycle707` measured
the stabilizer sextet `S = [1, 4, 9, 15, 18, 23]` — the six frames with
`Q_g = Q` at tolerance `1.0e-09`. Cycle
`physical_frame_group_factorization_cycle715` showed the reassembled operator is
constant on the right cosets `S.g`, and cycle
`physical_complete_averaging_set_frame_blindness_classification_cycle716`
classified the frame-blind averaging sets over the complete powerset, finding a
231-member family with the size ladder 24, 51, 80, 51, 24, 1.

Those cycles carried the sextet and the counts as measured facts. The sextet is
still **measured, not derived**, from the assembled operator here. What this
cycle adds is the geometric name of the invariant, and the derivation of the
counts from that name.

## The question this cycle answers

What *is* the four-valued invariant that the reassembled operator depends on,
and why is the census exactly 231 with exactly that ladder?

## Theorem A — the invariant is a body diagonal

The cube has four body diagonals, taken up to sign:

    d0 = (1, 1, 1),  d1 = (1, 1, -1),  d2 = (1, -1, 1),  d3 = (-1, 1, 1).

A body diagonal here is an **axis of the rotation group**, not an adjacency. The
lattice stencil is untouched throughout this cycle and remains nearest-neighbour.

The 24 proper rotations permute these four axes. The action is faithful and onto:
the 24 frames realise all 24 permutations of the four diagonals, one each. The
stabilizer of `d0` under this action is exactly the measured sextet
`[1, 4, 9, 15, 18, 23]`, and the stabilizers of the other three diagonals are
different sixes. Define

    delta(g) = the body diagonal that frame g carries onto d0.

Then the four fibres of `delta` have six frames each and are exactly the right
cosets of the sextet. So the coset structure measured in cycle 715 is the
diagonal-fibre structure, and the four-valued frame functional is the choice of
body diagonal.

This is checked at the operator level, not only through a source. Over all 276
unordered frame pairs, the entrywise deviation between `Q_g` and `Q_h` is at most
`1.2e-10` when `delta(g) = delta(h)`, and at least `4.0e+00` when they differ — a
ratio of `3.2e+10`. The same three numbers are obtained at `L = 3` and at
`L = 4`. The reassembled operator is therefore a function of the body diagonal
alone, to ten orders of magnitude.

## Theorem B — covering is transitivity, and the floor of four is forced

Call a subgroup `H` *covering* when `S.H` is the whole rotation group; cycle 716
measured that the blind averaging sets are exactly the unions of right cosets of
covering subgroups. Under Theorem A this condition has a one-line reading:

    S.H = whole group  <=>  H is transitive on the four body diagonals.

The complete subgroup lattice has 30 members. Exactly 9 of them are transitive on
the diagonals, of orders 4, 4, 4, 4, 8, 8, 8, 12, 24 — precisely the 9 covering
subgroups. The four minimal ones act *simply* transitively (regular): order four,
one element carrying `d0` to each diagonal. The three order-four subgroups that
are not covering have diagonal orbits of size two, two, two, two; being the right
size is not enough, the orbits must be single.

The floor now has a reason. No subgroup of order 1, 2, 3 or 6 can be transitive
on a four-element set, since a transitive action needs order divisible by four.
So the minimum blind size of four is forced by the diagonal action, not fitted to
the scan. Every transitive subgroup contains a regular one, so every blind
averaging set contains a minimal one.

## Theorem C — the family is complement-closed

Complementation in the 24-frame group is an involution on the 230 proper members
of the family; the whole group is the single member whose complement is empty.
Consequently the size ladder reads the same in both directions on sizes below 24:
24, 51, 80, 51, 24.

This is confirmed physically, not only combinatorially. At `L = 3` with a generic
source, the complements of the 24 blind transversals are blind at `8.5e-12`,
while the complements of the other 1272 spread by at least `6.7e-04`; with a
second independent generic source the same two numbers are `3.9e-13` and
`3.9e-04`. At `L = 4` they are `2.3e-11` against `1.8e-02`, and `1.1e-10`
against `1.6e-02`.

## Theorem D — the census 231 is derived

The four regular subgroups are the minimal covering subgroups. Each has six right
cosets, so each contributes `2^6 - 1 = 63` nonempty unions of its own cosets.
Inclusion and exclusion over the four requires the joins, which are recomputed
rather than assumed: the six pairwise joins have orders `[8, 8, 8, 24, 24, 24]`,
the four triple joins all have order 24, and the join of all four has order 24.
A join of order 8 has three cosets and contributes `2^3 - 1 = 7` unions; a join
of order 24 has one coset and contributes 1. Hence

    4*63 - (3*7 + 3*1) + 4*1 - 1 = 252 - 24 + 4 - 1 = 231.

The three terms subtracted, added and subtracted again are the pair, triple and
quadruple overlaps in that order. The result matches an independent construction
that enumerates the coset unions of all 9 covering subgroups and deduplicates:
both constructions give the same 231 members, with the ladder
`[(4, 24), (8, 51), (12, 80), (16, 51), (20, 24), (24, 1)]`. Size eight resolves
into 9 unions that are single cosets of an order-eight covering subgroup and 42
that are unions of two minimal cosets.

These are **computational identities** over a 24-element group: they carry no
statement about the continuum.

## The physical refinement — transversality is necessary, not sufficient

Theorem A suggests an averaging prescription that hits each body diagonal once.
There are `6^4 = 1296` such transversals. Exactly 24 of them are blind, and they
are precisely the right cosets of the four regular subgroups.

Measured at both box sizes and with two independent generic sources:

| box | source | blind | least pulled norm | worst blind | best non-blind | ratio |
|-----|--------|-------|-------------------|-------------|----------------|-------|
| `L = 3` | first  | 24 of 1296 | `1.6e+01` | `1.4e-11` | `4.4e-03` | `3.2e+08` |
| `L = 3` | second | 24 of 1296 | `1.8e+01` | `8.8e-13` | `3.7e-03` | `4.2e+09` |
| `L = 4` | first  | 24 of 1296 | `3.1e+01` | `9.7e-11` | `6.0e-02` | `6.2e+08` |
| `L = 4` | second | 24 of 1296 | `3.3e+01` | `1.0e-10` | `9.5e-02` | `9.3e+08` |

So spreading an averaging prescription evenly over the four diagonals — which is
what the diagonal law would naively recommend — buys nothing on its own. Only 24
of the 1296 even spreads are blind, and the alignment of the six-element fibres
with a regular subgroup is what distinguishes them. Blindness is a group-theoretic
alignment, not a counting balance.

## Rejectors

Each rejector is a set that satisfies a nearby condition and is still not blind,
measured rather than argued.

- One whole fibre — the sextet itself — lies inside a single body diagonal and
  spreads `1.8e-02` at `L = 3`, `2.0e-01` at `L = 4`.
- The 18 distinct right cosets of the three intransitive order-four subgroups
  have least spread `4.8e-03` at `L = 3` and `3.0e-01` at `L = 4`, and none of
  them lies in the predicted family.
- The transversal `[0, 1, 3, 5]` meets each diagonal exactly once and still
  spreads `2.3e-02` at `L = 3` and `4.7e-01` at `L = 4`.

## Boundary — the transversal count is source-robust, degenerate orbits aside

Cycle 716 recorded that structured sources blind strictly more collections than
generic ones. Inside the transversal family, that widening does not occur. A
single-slot source at slot 0 and a single-slot source at slot 7 each have frame
orbit diameter `1.0e+00`, and each blinds exactly the same 24 transversals as the
generic sources, at both `L = 3` and `L = 4`. The extra structured blindness
found in cycle 716 lies entirely off the transversal family.

The one source that does break the count is degenerate: the all-ones source has
frame orbit diameter `0.0e+00` — the permutations fix it, so there is only one
point to compare — and it is blind on all 1296 transversals. A one-point frame
orbit carries no frame information at all, so this is a statement about the
source, not about the operator.

## What this cycle claims and does not claim

Claimed: for the reassembled static operator of the cycle-696 compiler on an
unwrapped box, at `L = 3` and `L = 4`, the four-valued frame functional is the
body diagonal that the frame carries onto `(1, 1, 1)`; the measured stabilizer
sextet is exactly the stabilizer of that diagonal; a subgroup averages the frame
dependence away exactly when it is transitive on the four diagonals; the minimum
blind size of four follows from that transitivity; the 231-member census and its
ladder follow by inclusion and exclusion over the four regular subgroups; the
family is complement-closed on its proper members; and of the 1296 diagonal
transversals exactly 24 are blind.

Not claimed: any statement about a continuum limit, about wrapped boundaries,
about box sizes beyond those measured, or about the audit status of this or any
other row. No new axiom, primitive, or import is proposed. The sextet and the
degree-of-freedom counts remain inputs measured from the compiler.

## Physics reading

The frame dependence of the reassembled static operator is not a diffuse
24-valued nuisance. It is a single geometric datum: which body diagonal of the
cube the frame selects. Everything cycle 716 counted follows from that one fact —
the size-four floor, the 9 covering subgroups, the 231-member family, the
palindromic ladder. And the refinement cuts the other way from the naive reading:
of the 1296 prescriptions that treat the four diagonals evenly, all but 24 still
see the frame. The nearest structure to a frame-blind average is a regular
subgroup of the rotation group acting on a cube diagonal, and the operator holds
at that structure rather than at any balance of counts.

## Reproduction

Runner:
[physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.py](../scripts/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.py)

Cold stdout and the machine-readable receipt are landed under `outputs/`. The
runner prints one line per gate and ends with a `TOTAL: PASS=` line; every
floating-point value quoted above is printed by the runner itself.
