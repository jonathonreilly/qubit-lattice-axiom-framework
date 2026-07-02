# Record Count Bounds the Composition Word: a Finite, Exactly Enumerable Dial Set

**Date:** 2026-07-02
**Type:** bounded theorem (named-premise-family bound + exact finite enumeration)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note does not set,
predict, or estimate any audit verdict, and it edits no audit-lane-owned registry
or audit data file.
**Actual current surface status:** open. No wall is closed and nothing is
adjudicated. The moduli / word-supplier lane stays live, now carrying a named,
un-adopted premise family instead of an open densification.
**Primary runner:** `scripts/frontier_record_count_bounds_composition_words_2026_07_02.py`
**Runner output:** `outputs/frontier_record_count_bounds_composition_words_2026_07_02.txt`

## FIREWALL

- The bound rests on a **premise family** -- **P1** (letter = event, pure words),
  **P2** (production), **P3** (persistence), **P4** (collection scoping) --
  together with **CHART-MIX** (per-step dictionary supply for mixed words). Every
  one is **NAMED**, **not derived**, and **not adopted**; none is promoted to an
  axiom or admission here.
- P2 and P3 are dynamics-shaped: the memo disclaims any "record-production
  process" and lists "physical persistence dynamics" among the gates outside the
  axioms. P4 is a scoping premise: the axiom set **does not bound** a
  configuration's record total. CHART-MIX is inherited from review-pending
  block12's word class, where the occupancy note's open dictionary binary enters.
- No selector is proposed, no empirical modulus imported, no `r` fixed. block07
  (selector-constraint map), block12 (moduli words / boundary `1/2` /
  word class), block20 (action-lane `C-add`), and the banked Dynamics-axiom
  proposal (PR #4843) are all **review-pending**, context only. This note reads no
  branch; the "`C-add` is the **same family**" reading is **supervisor-supplied**
  cross-block context. Residues are conserved and enumerated in full (T5');
  nothing is adjudicated; **no wall** is closed.

## Purpose

Under ANY single supplied dictionary the composition-word dial set is exactly
`{1/2}` (component chart) or `{1}` (slot chart) for **all** word lengths:
`f^m(r) = 2^(2^m - 1) r^(2^m)` has unique positive fixed point `1/2`, and
`g^m(r) = r^(2^m)` has unique positive fixed point `1`. **No densification ever
arises physically** -- densification needs mixed words, and a mixed word is not
an iterate of any single supplied flow. This is the block's sharpest statement.

Block12 (review-pending) showed that with the word unbounded and the dictionary
allowed to change per step, positive fixed points densify inside `[1/2, 1]`. This
note names the premise family that removes it, grounds each premise in landed text
without deriving it, bounds the word length by the record count, and enumerates
the length-`<=2` dial set completely and exactly.

## The Supplied Surface -- landed-text guards `[checks 1-7]`

Landed axiom text (`docs/MINIMAL_AXIOMS_2026-06-29.md`): "A state is a
configuration of records", and the additivity conditional --

> For any finite collection of pairwise-disjoint records, scalar readout `I` is
> additive, with `I(empty)=0`.

Landed occupancy note: the flow is "the agreement-conditioned double-registration
update squares registered weights and renormalizes", with charts `x = 2r` giving
`r -> 2r^2` and `x = r` giving `r -> r^2`. Write `f(r) = 2r^2` (component),
`g(r) = r^2` (slot). The note is explicit that `f`, `g` are two CHARTS of one
binary -- its tri-guise theorem: the descriptions "form the same binary, not
three independent binaries". The word class is block12's formal set of finite
compositions of `f` and `g`.

## The premise family (all named; none derived; none adopted)

**P1 -- letter = event (pure words); CHART-MIX for mixed words `[checks 8-9]`.**
Each letter of a realized SINGLE-CHART word is one agreement-conditioned
double-registration event of the occupancy flow read in that chart -- its own
flow definition restricted to ONE supplied dictionary: under the component chart
every step is `f` (word `f^m`), under slot every step is `g` (`g^m`). Since `f`,
`g` are two charts of the *same binary*, a MIXED word is **not** an iterate of any
single flow -- `f.f = 8r^4`, `g.g = r^4`, while `f.g = 2r^4`, `g.f = 4r^4` match
neither -- so it needs **CHART-MIX** (per-step dictionary supply), inherited from
review-pending block12's word class, where the occupancy note's open dictionary
binary enters, carried as an existing campaign surface, not created here.

**P2 -- production `[check 10]`.** Each event registers at least one new record.
Dynamics-shaped; the memo disclaims it:

> [Admissibility] ... does not ... provide a record-production process.

Independent content: a history can advance event by event while registering
nothing, so production is not supplied by the letters alone. Named, not adopted.

**P3 -- persistence `[check 11]`.** Records persist across events. Dynamics-shaped;
the memo's Open Gates list it outside the axioms:

> arrow, record-production dynamics, physical persistence dynamics, time metric,
> and local observability of records ...

Correction (a prior draft's category error, rejected by the refutation pass): the
Record sentence "the locked possibility is invariant under repeated readout"
grounds only WITHIN-readout stability of an already-present record; it is **not**
persistence across events, which is its own premise. Independent content: a
produce-then-vanish history registers records that later vanish, and the count
then ceases to bound the event total. Named, not adopted.

**P4 -- collection scoping / FIN `[check 12]`.** A supplied finite readout
collection contains the realized history's registered records, and `N_rec` is
that collection's count. Plainly: the axiom set **does not bound** a
configuration's record total -- an all-sites-recorded configuration on `Z^3`
satisfies every quoted sentence, since "For any finite collection ..." is a
conditional, not a bound. Finiteness enters only through the supplied collection;
`N_rec` is configuration data relative to it. No unit-weight readout gloss is used.

## T2' -- under P1(pure) + P2 + P3 + P4: k <= N_rec `[checks 13-17]`

By monotone induction on a pure single-chart word: P2 gives `>= 1` new record per
event, P3 keeps every registered record, and P4 places them in the supplied
counted collection, so after `k` events `N_rec >= k`. Exact and tight: a unit,
persistent, contained history achieves `k = N_rec` `[checks 13-14]`. `N_rec` is
content relative to the supplied collection (motion-closed; no anchor). Each
premise is load-bearing, with a per-premise violation witness `[checks 15-17]`:

- drop **P2** -> unbounded words with no new records: `k` advances while the
  record count stays fixed, so `k > N_rec`;
- drop **P3** -> records vanish and the count ceases to bound `k`;
- drop **P4** containment -> registrations land outside the counted collection,
  so `N_rec < k`.

## T3' -- the length-`<=2` dial set is finite, exact, and COMPLETE `[checks 18-28]`

For length `<= k` over `{f, g}` the word count is exactly `2^(k+1) - 2`
(`k = 1..4`: `2, 6, 14, 30`) `[check 18]`. A length-`m` word has fixed-point
polynomial `p_w(r) = w(r) - r` of degree `2^m`, so the dial set is a finite set of
roots, cardinality bounded by the sum of degrees (`20` for `k <= 2`) `[check 19]`.
Exact enumeration at the polynomial level (no numerics):

- `f`: `2r^2 - r = r(2r-1)` -- fixed point `1/2` `[check 20]`.
- `g`: `r^2 - r = r(r-1)` -- fixed point `1` `[check 21]`.
- `f.g`: `2r^4 - r = r(2r^3-1)` -- root of `2r^3-1` `= 2^(-1/3)`; MIXED,
  conditional on CHART-MIX `[check 22]`.
- `g.f`: `4r^4 - r = r(4r^3-1)` -- root of `4r^3-1` `= 2^(-2/3)`; MIXED,
  conditional on CHART-MIX `[check 23]`.
- `f.f`: `8r^4 - r = r(2r-1)(4r^2+2r+1)`; cofactor discriminant `4-16 = -12 < 0`,
  positive leading coeff, positive-definite -- adds **no** new positive root, only
  `1/2` `[check 24]`.
- `g.g`: `r^4 - r = r(r-1)(r^2+r+1)`; cofactor discriminant `1-4 = -3 < 0`,
  positive-definite -- adds only `1` `[check 25]`.

Since `f.f`, `g.g` add nothing, the length-`<=2` dial set is **complete**:
`{1/2, 1}` unconditionally (pure words) plus `{2^(-1/3), 2^(-2/3)}` conditional on
CHART-MIX (mixed words). The four points are pairwise distinct:
`gcd(2r^3-1, 4r^3-1)` is a nonzero constant (coprime cubics) and `1/2, 1` are
roots of neither `[check 26]`.

The boundary `>= 1/2` (block12, review-pending) is fixed via strict monotonicity,
not the earlier invalid "negative at `1/2` + positive leading coeff => root
exceeds `1/2`" cubic inference: `a r^3 - 1` strictly increases on `r > 0` because
`a(r2^3 - r1^3) = a(r2 - r1)(r2^2 + r2 r1 + r1^2) > 0` for `0 < r1 < r2`
`[check 27]`. With `(2r^3-1)@(1/2) = -3/4` and `(4r^3-1)@(1/2) = -1/2` both `< 0`,
each unique positive root exceeds `1/2`; and `1/2, 1 >= 1/2` `[check 28]`.

## Pure-word corollary -- the headline `[checks 29-31]`

For every `m >= 1`, by coefficient-level induction: `f^m(r) = 2^(2^m - 1) r^(2^m)`,
so `f^m(r) - r = r(2^(2^m-1) r^(2^m-1) - 1)` with the cofactor a strictly
increasing monomial-minus-`1` -- unique positive fixed point `r = 1/2` for every
`m` `[check 29]`; and `g^m(r) = r^(2^m)`, unique positive fixed point `r = 1` for
every `m` `[check 30]`. Hence under any single supplied dictionary the dial set is
exactly `{1/2}` (component) or `{1}` (slot) for ALL word lengths: no densification
ever arises physically, and the mixed dial points `2^(-1/3), 2^(-2/3)` are
CHART-MIX artifacts, not pure-word fixed points `[check 31]`.

## T4' -- word-supplier residual; governance hand-off (morning list) `[checks 32-33]`

The residual is sharpened, not resolved: the word length is bounded by the record
count (content), and the remaining supply questions are handed off without
adoption as an **owner decision** on the owner's **morning** review list, mapped
in full in T5'.

## T5' -- moduli-lane end-state (flagged, not closed) `[checks 32-33]`

The lane's residue, enumerated completely and conserved:

1. **The dynamics family** -- P2 (production) and P3 (persistence); the action
   lane's `C-add` is the **same family** per **supervisor-supplied** cross-block
   context (morning list; owner decision; not adopted).
2. **The supplied-context scoping** -- P4: the supplied finite readout collection
   (the axiom set **does not bound** a configuration's total).
3. **CHART-MIX and the dictionary binary** -- per-step dictionary supply and the
   occupancy note's open dictionary binary (existing campaign surface, carried).
4. **The realized history** -- which word within the bound is realized, and the
   realized step count (content, not premise).
5. **The sibling review-pending audits** -- block07 (selector-constraint map),
   block12 (moduli words / boundary `1/2` / word class), block20 (action-lane
   `C-add`), and PR #4843 (banked Dynamics-axiom proposal).

No wall is closed; nothing is adjudicated; no empirical modulus is imported; no
selector is proposed.

## Does NOT

- Does not derive or adopt P1, P2, P3, P4, or CHART-MIX; each stays named and not
  adopted.
- Does not supply/select which word is realized, propose a selector, fix `r`, or
  import an empirical modulus.
- Does not close any wall, adjudicate anything, or set any audit status.
- Does not read any review-pending branch; block07 / block12 / block20 / #4843 are
  context only, and the `C-add` same-family reading is supervisor-supplied.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) -- Record, state
  definition, the finite-additivity conditional, the record-production disclaimer,
  the "physical persistence dynamics" open gate.
- [`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md)
  -- the ONE double-registration flow, the two charts `f(r)=2r^2`, `g(r)=r^2`, the
  tri-guise "same binary" identity.

Context only, review-pending: block12 (PR #4827), block07 (PR #4822), block20
`C-add`, PR #4843.

## No-Promotion Statement

This note does not promote, demote, or set the audit status of any dependency or
sibling block. The independent audit lane is the only status authority. P1-P4 and
CHART-MIX are named and not adopted; their adoption, if any, is an owner decision.

## Summary

- **Checks:** 33, all PASS (`outputs/frontier_record_count_bounds_composition_words_2026_07_02.txt`).
- **Headline:** under any single supplied dictionary the dial set is exactly
  `{1/2}` (component) or `{1}` (slot) for all lengths -- `f^m = 2^(2^m-1) r^(2^m)`
  fixes `1/2`, `g^m = r^(2^m)` fixes `1`; no physical densification, and the mixed
  points `2^(-1/3), 2^(-2/3)` are CHART-MIX artifacts.
- **Bound:** P1(pure)+P2+P3+P4 give `k <= N_rec`, exact and tight, with a
  per-premise violation witness for each of P2, P3, P4.
- **Residue (complete):** the dynamics family (P2/P3 and, per supervisor-supplied
  context, `C-add`); the supplied-context scoping (P4); CHART-MIX + the dictionary
  binary; the realized history / step count; the sibling review-pending audits.
