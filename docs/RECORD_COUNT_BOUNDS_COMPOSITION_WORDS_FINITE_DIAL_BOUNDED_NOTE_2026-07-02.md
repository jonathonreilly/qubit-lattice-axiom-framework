# Record Count Bounds the Composition Word: a Finite, Exactly Enumerable Dial Set

**Date:** 2026-07-02
**Type:** bounded theorem (premise-named bound + exact finite enumeration)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note does not set,
predict, or estimate any audit verdict, and it edits no audit-lane-owned
registry or audit data file.
**Actual current surface status:** open. No wall is closed and nothing is
adjudicated. The moduli / word-supplier lane stays live, now carrying one
named, un-adopted premise instead of an open densification.
**Primary runner:** `scripts/frontier_record_count_bounds_composition_words_2026_07_02.py`
**Runner output:** `outputs/frontier_record_count_bounds_composition_words_2026_07_02.txt`

## FIREWALL

- The registration premise **REG>=1** is NAMED. It is **not derived** and it is
  **not adopted**. It is dynamics-shaped: the landed axiom memo states the
  axioms do not "provide a record-production process", so no flow step's
  production of a record is supplied by the axioms. REG>=1 is grounded only in
  landed monotonicity and counting text (below); it is not promoted to an axiom
  or to an admission here.
- No selector is proposed. No empirical modulus is imported. No value of `r` is
  fixed by this note.
- The block07 selector-constraint map, the block12 moduli-word results
  (including the boundary fact), the block20 action-lane premise `C-add`, and
  the banked Dynamics-axiom proposal (PR #4843) are all **review-pending** and
  are cited as context only. This note reads no branch.
- Residues are conserved and enumerated in full (see T5): REG>=1 (a
  dynamics-family premise), the realized record history (content), and the
  sibling review-pending audits. Nothing is adjudicated; **no wall** is closed.

## Purpose

Block12 (review-pending) showed that with the composition word unbounded, the
positive fixed points densify and selection loses discriminating power inside
`[1/2, 1]`. This note isolates the structure that removes the densification: a
bound on word length. It names one dynamics-shaped premise, REG>=1, grounds it
in landed text without deriving it, shows it makes the record count bound the
word length, and enumerates the resulting dial set exactly at fixed record
count. The word-supplier residual is not resolved; it is sharpened into an
owner-facing governance question and mapped.

## The Supplied Surface

Landed axiom text (`docs/MINIMAL_AXIOMS_2026-06-29.md`), quoted:

> A state is a configuration of records.

> When present, a record locks exactly one local possibility from the subset
> available at that site under Admissibility; the locked possibility is
> invariant under repeated readout.

> For any finite collection of pairwise-disjoint records, scalar readout `I` is
> additive, with `I(empty)=0`.

> [Admissibility] does not choose a Hamiltonian or transfer operator, supply
> transition probabilities or weights, select a scalar or nonzero kinetic
> branch, assert a Dirac-square carrier, define a time metric, or provide a
> record-production process.

Landed occupancy note
(`docs/OCCUPANCY_ATOM_..._BOUNDED_NOTE_2026-06-12.md`), quoted:

> The agreement-conditioned double-registration update squares registered
> weights and renormalizes ...

with the two dictionary charts `x = 2r` giving `r -> 2r^2` and `x = r` giving
`r -> r^2`. Write `f(r) = 2r^2` and `g(r) = r^2`. The word class is the set of
finite compositions of `f` and `g` (block12).

Review-pending block12 supplied verbatim (context only):

> [every] target in `[1/2, 1]` [is reachable] by choosing an appropriate binary
> word. Therefore fixed-point selection has no discriminating power inside
> `[1/2, 1]` unless the composition word itself is supplied or bounded. ... Every
> positive fixed point of every word in this class satisfies `r*_w >= 1/2`.

## T1 -- the registration premise REG>=1: named and grounded, not derived `[checks 1-7]`

Each application of `f` or `g` is one agreement-conditioned double-REGISTRATION
step of the occupancy note's flow -- the step whose "double-registration update
squares registered weights and renormalizes". **REG>=1** is the premise that
every such flow step registers at least one new record.

Grounding from landed text, without derivation: records, once present, are fixed
-- "the locked possibility is invariant under repeated readout", so registration
is monotone and nothing un-registers; and "A state is a configuration of
records" supplies the counted objects. What is **not** supplied is that a flow
step *produces* a record: the axiom memo's dynamics section disclaims any
"record-production process". REG>=1 therefore names a dynamics-shaped premise; it
is not adopted here.

REG>=1 has independent content: a toy monotone registration sequence in which
each step adds `>= 1` record satisfies it, while a degenerate step that adds none
keeps the record count non-decreasing (monotone) yet fails REG>=1. Monotonicity
alone does not give REG>=1 `[checks 6-7]`.

## T2 -- under REG>=1 the record count bounds the word: k <= N_rec `[checks 8-10]`

By monotone induction, after `k` registration steps at least `k` records exist.
The realized configuration has a finite record count `N_rec` -- finite by the
Record additivity sentence, whose scope is any finite collection of
pairwise-disjoint records on a readout collection. Hence `k <= N_rec`.

The bound is content-carried: `N_rec` is a record-content quantity (the count is
the additive scalar readout with unit weights, expressible from the landed
additivity sentence), so it is motion-closed and needs no anchor. The runner
exhibits the induction witness, a tight sequence achieving `k = N_rec`, and a
witness with `k > N_rec` that forces a REG>=1 violation -- so the bound is
violated only by violating REG>=1 `[checks 8-10]`.

## T3 -- bounded words give a finite, exactly enumerable dial set `[checks 11-21]`

For word length `<= k` over `{f, g}` the number of words is exactly
`2^(k+1) - 2` (`k = 1..4`: `2, 6, 14, 30`) `[check 11]`. Each word `w` of length
`m` has fixed-point polynomial `p_w(r) = w(r) - r` of degree `2^m`, so for
bounded `k` the dial set is contained in the roots of finitely many polynomials
and is finite, with cardinality at most the sum of degrees (an exact integer;
`20` for `k <= 2`) `[check 12]`.

Exact small-word enumeration at the polynomial level (no numerics, no floats):

- `f`: `2r^2 - r = r(2r - 1)` -- positive fixed point `r = 1/2` `[checks 13-14]`.
- `g`: `r^2 - r = r(r - 1)` -- positive fixed point `r = 1` `[checks 15-16]`.
- `f.g` (`= f(g(r))`): `f(g(r)) - r = 2r^4 - r = r(2r^3 - 1)` -- the positive
  fixed point is the root of `2r^3 - 1`, i.e. the campaign's `2^(-1/3)` dial
  point, stated as an exact polynomial identity and never evaluated numerically
  `[check 17]`.
- `g.f` (`= g(f(r))`): `g(f(r)) - r = 4r^4 - r = r(4r^3 - 1)` -- root of
  `4r^3 - 1`, i.e. `2^(-2/3)` `[check 18]`.

Distinctness of the four length-`<=2` dial points, by exact polynomial algebra:
`gcd(2r^3 - 1, 4r^3 - 1)` is a nonzero constant (the Euclidean remainder is a
nonzero constant), so the two cubics are coprime and share no root; equivalently
a common root would need `r^3 = 1/2` and `r^3 = 1/4` at once, which is impossible
`[check 19]`. And `r = 1/2` and `r = 1` are not roots of either cubic by exact
evaluation, and `1/2 != 1`, so all four dial points are pairwise distinct
`[check 20]`.

Block12's boundary fact (every positive fixed point `>= 1/2`) is cited
review-pending and spot-checked on the enumerated points: `1/2` and `1` are
`>= 1/2` exactly; for the cubic roots, `2*(1/2)^3 - 1 = -3/4 < 0` and
`4*(1/2)^3 - 1 = -1/2 < 0` with positive leading coefficients, so each real root
exceeds `1/2` by exact sign arithmetic `[check 21]`.

Consequence: with `k` bounded by `N_rec`, the dial set is finite and discrete.
Fixed-point selection **regains** discriminating power at any fixed record count;
block12's densification deflation applies only to UNBOUNDED words.

## T4 -- the word-supplier residual updates; governance hand-off (morning list) `[check 22]`

The word-supplier question reduces: the word length is bounded by the record
count (content) under one dynamics-shaped premise, REG>=1. REG>=1's candidate
homes are recorded here **without adoption**:

1. a narrow record-production / registration-step primitive;
2. the banked Dynamics-axiom proposal (PR #4843, review-pending) -- and note
   that the action lane's composition premise `C-add` (review-pending block20)
   is the **same family**: one Dynamics decision would supply both lanes;
3. remain a named conditional premise.

This is an **owner decision**; the note only maps it, and marks it for the
owner's **morning** review list. What is **not** reduced is which word, within
the bound, is realized -- that is the realized state's record history, content
and not premise.

## T5 -- moduli-lane end-state (flagged, not closed) `[check 22]`

Under REG>=1: the dial sets are finite at fixed `N_rec`; the boundary `1/2`
stands (block12, review-pending); the `2^(-1/3)` and `2^(-2/3)` points are the
exact length-2 mixed-word fixed points (polynomial identities); and the block07
selector constraints (review-pending) are unchanged.

The lane's residue, enumerated completely and conserved:

1. **REG>=1** -- a dynamics-family premise (morning list; owner decision;
   not adopted).
2. **The realized record history** -- which word within the bound is realized
   (content, not premise).
3. **The sibling review-pending audits** -- block07 (selector-constraint map),
   block12 (moduli words / boundary `1/2`), block20 (action-lane `C-add`, the
   same family as REG>=1), and PR #4843 (banked Dynamics-axiom proposal).

No wall is closed; nothing is adjudicated; no empirical modulus is imported; no
selector is proposed.

## Does NOT

- Does not derive or adopt REG>=1; REG>=1 stays a named, un-adopted,
  dynamics-shaped premise.
- Does not supply, select, or fix which word is realized within the bound.
- Does not propose a selector, fix `r`, or import an empirical modulus.
- Does not close any wall, adjudicate anything, or set any audit status.
- Does not read or rely on any review-pending branch; block07 / block12 /
  block20 / #4843 are context only.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) -- Record,
  state definition, finite additivity, and the record-production disclaimer.
- [`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md)
  -- the double-registration flow and the two dictionary charts giving
  `f(r)=2r^2`, `g(r)=r^2`.

Context only, review-pending (not read here): block12 moduli-words (PR #4827),
block07 selector-constraint map (PR #4822), block20 action-lane `C-add`, and the
banked Dynamics-axiom proposal (PR #4843).

## No-Promotion Statement

This note does not promote, demote, or set the audit status of any dependency or
sibling block. The independent audit lane is the only status authority. REG>=1
is named and not adopted; its adoption, if any, is an owner decision.
