# Complete Classification of Frame-Blind Averaging Sets for the Reassembled Static Operator — Cycle 716

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

Cycle `physical_source_stabilizer_coset_collapse_k_sign_law_cycle707` and its
successor `physical_frame_group_factorization_cycle715` measured the stabilizer
sextet `S = [1, 4, 9, 15, 18, 23]` — the six frames with `Q_g = Q` at tolerance
`1.0e-09` — and established that `g -> Q_g` is constant on the right cosets
`S.g`, so the reassembled operator is a function on four cosets rather than on
24 frames.

The sextet `S` is **measured, not derived**, from the assembled operator. Every
group-layer statement below is derived from `S` by the coset argument and then
matched against a complete scan; nothing in the group layer is fitted.

## The question this cycle answers

Cycle 715 classified which *subgroups* of the rotation group average the frame
dependence away. An averaging prescription need not be a subgroup. In general it
is an arbitrary nonempty collection `A` of frames, defining a pulled source and a
reassembled response

    b_A = sum over a in A of P_a^T b,     v_A(g) = (b_A / |b_A|)^T Q_g^{-1} (b_A / |b_A|).

Call `A` **frame-blind** for `b` when `g -> v_A(g)` is constant. There are
16777215 nonempty collections. This cycle classifies all of them.

## Theorem I — sufficiency, valid for every source

Let `L(A) = { t : t.A = A }` be the left stabilizer of `A`. It is a subgroup, and
`A` is a union of right cosets of `L(A)`, so the order of `L(A)` divides the size
of `A`. Because `a -> P_a` reverses products (`P_a P_b = P_{ba}`), the pulled
source transforms as `P_t^T b_A = b_{t.A}`; hence `b_A` is fixed by every
`t` in `L(A)`. If the sextet and the left stabilizer together fill the rotation
group, `S.L(A) = G`, then every frame is reached from a stabilizer frame by an
element that fixes `b_A`, and `v_A` is constant.

Equivalently: **`A` is blind for every source exactly when `A` is a union of
right cosets of a covering subgroup** — a subgroup `H` with `S.H = G`.

This direction is one of the cycle's **computational identities**: it does not
depend on the source. Measured over all 231 members of the predicted family
against five distinct sources (two generic draws, two single-slot sources, and
the all-ones source), the worst spread is `7.0e-12` at `L = 3` and `1.6e-10` at
`L = 4`, with smallest normalizing norm `2.0e+00`.

## Theorem II — the converse, over the complete powerset

Scanning all 16777215 nonempty collections, at two independent generic sources
and at both box sizes, the measured blind family is exactly the predicted family
of 231 members, with no member missing and none extra:

| box | source | blind | family match | worst blind | best non-blind | ratio | smallest norm |
|-----|--------|-------|--------------|-------------|----------------|-------|----------------|
| `L = 3` | generic seed 7160 | 231 | yes | `5.8e-12` | `6.8e-06` | `1.2e+06` | `1.1e+01` |
| `L = 3` | generic seed 7161 | 231 | yes | `7.0e-12` | `4.7e-05` | `6.6e+06` | `9.7e+00` |
| `L = 4` | generic seed 7160 | 231 | yes | `1.6e-10` | `6.6e-05` | `4.2e+05` | `1.6e+01` |
| `L = 4` | generic seed 7161 | 231 | yes | `1.1e-10` | `3.4e-04` | `3.1e+06` | `1.6e+01` |

The blind and non-blind populations are separated by at least five orders of
magnitude in every column, so the classification is not a tolerance artefact.

The size ladder is identical in all four scans: sizes 4, 8, 12, 16, 20 and 24
carry 24, 51, 80, 51, 24 and 1 blind collections respectively, and **every one of
the other eighteen sizes carries none**. No collection of size 1, 2 or 3 is blind
for a generic source.

The complete scan is made feasible by the cycle-715 coset collapse: the frame
functional takes at most four distinct values, so four representatives suffice.
That reduction is validated inside this cycle rather than assumed — over all 2324
collections of size at most three, the four-representative and 24-frame spreads
agree to `6.2e-12` at `L = 3` and `3.0e-10` at `L = 4`.

## Theorem III — the structure of the blind family

Independently of any source, from the sextet alone:

- The rotation group has a 30-member subgroup lattice. Exactly nine subgroups are
  covering, of orders 4, 4, 4, 4, 8, 8, 8, 12 and 24.
- The four order-4 covering subgroups meet the sextet in the identity alone; they
  are complements of `S`. Every covering subgroup contains a complement.
- Their right cosets give 24 minimal blind collections, each of size four. The
  left-coset family is the same 24 sets.
- Every one of the 231 members is a union of minimal blind collections.
- The family is nonetheless **not union-closed**: of the 168 disjoint pairs of
  minimal collections, 108 have a union that is not blind. The 24 minimal
  collections overlap partially — they do not partition the rotation group.
- A left stabilizer computed over the complete powerset always lands in the
  30-member lattice, taking 30 distinct values; the covering criterion
  `S.L(A) = G` selects exactly 231 of the 16777215 collections; and on all 231
  the order of `L(A)` divides the size of `A`, with minimum order four.

The minimum blind size of four is therefore derived, not observed: a covering
subgroup must have order at least four, and the order of `L(A)` divides `|A|`.

## Rejectors

Every gate carries an explicit wrong-set rejector, so a mistaken family would
fail rather than pass silently. At the generic source:

| rejector | `L = 3` spread | `L = 4` spread |
|----------|----------------|----------------|
| the sextet `S` itself (order 6, not covering) | `2.0e-02` | `1.4e+00` |
| the non-subgroup 4-subset `[1, 4, 9, 23]` of the sextet | `3.3e-02` | `1.1e+00` |
| least over the 72 cosets of the three non-covering order-4 subgroups | `5.4e-03` | `2.3e-01` |

The three non-covering order-4 subgroups meet the sextet twice and reach 12 of
the 24 frames; being the same size as a complement is not enough.

## Boundary — the converse is a generic-source statement

Sufficiency holds for every source, but the converse does not. Structured sources
blind strictly more. Over the 1271625 collections of size at most eight at
`L = 3`, where the predicted family contributes 75 members:

- a single-slot source at slot 0 blinds 153 collections, all at sizes four and
  eight;
- a single-slot source at slot 7 blinds 723 collections, and 24 of them have size
  **two** — below the generic minimum of four;
- the all-ones source has a one-point frame orbit (orbit diameter `0.0e+00`,
  since the permutations fix it) and is blind on all 1271625 collections.

So the size-four floor is a generic-source floor, not a universal one, and the
231-member family is the *smallest* blind family, attained by generic sources.
This is stated as a limit of the theorem, not as a residual to be repaired.

## What this cycle claims and does not claim

Claimed: for the reassembled static operator of the cycle-696 compiler on an
unwrapped box, at `L = 3` and `L = 4`, an averaging prescription is frame-blind
for a generic source exactly when it is a union of right cosets of a covering
subgroup, and blind for *every* source whenever it is; the family has 231
members with the ladder above; the minimum blind size is four; and the family is
generated by, but not closed under unions of, its 24 minimal members.

Not claimed: any statement about a continuum limit, about wrapped boundaries,
about box sizes beyond those measured, or about the audit status of this or any
other row. No new axiom, primitive, or import is proposed. The sextet and the
degree-of-freedom counts are inputs measured from the compiler, and the note
carries no closed form for them.

## Physics reading

The reassembled static operator carries a genuine four-valued frame functional,
and this cycle shows how hard it is to erase. No collection of one, two or three
frames erases it. Of the 16777215 averaging prescriptions available, 231 do, and
they are exactly the coset-aligned ones. Frame-blindness is a rare structural
alignment between the averaging set and the stabilizer sextet, not something a
generic averaging prescription achieves — and this removes the subgroup
hypothesis that the cycle-715 classification carried, replacing it with a
statement over arbitrary averaging sets.

## Reproduction

Runner:
[physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02.py](../scripts/physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02.py)

Cold stdout and the machine-readable receipt are landed under `outputs/`. The
runner prints one line per gate and ends with a `TOTAL: PASS=` line; every
floating-point value quoted above is printed by the runner itself.
