# Record-Composition Bridge: Semigroup + Positivity Selection Reduces the Action Wall to One Dynamics-Shaped Premise (Bounded Note)

**Date:** 2026-07-02
**Type:** bounded theorem (bridge decomposition + exact selection facts)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note does **not** set or
predict any audit outcome; it records a decomposition and a set of exact facts.
**Actual current surface status:** the action-selection question remains the
*well-posed open physical question* of the parent relocation note. Nothing here
closes it. The one non-axiom premise it isolates (C-add) is **not adopted**.
**Primary runner:**
[`scripts/frontier_record_composition_bridge_positivity_2026_07_02.py`](../scripts/frontier_record_composition_bridge_positivity_2026_07_02.py)
**Runner output:**
[`outputs/frontier_record_composition_bridge_positivity_2026_07_02.txt`](../outputs/frontier_record_composition_bridge_positivity_2026_07_02.txt)

## FIREWALL (read first)

- **C-add is NAMED, GROUNDED, and NOT derived or adopted here.** It is the premise
  that a supplied one-step record-growth process composes so the two-step
  class-weight kernel is the *convolution* of the one-step kernels. Its readout half
  is axiom-supplied; its kernel half is **dynamics-shaped content the four axioms
  explicitly do not supply** (check 03). C-add is a conditional premise only.
- **No action is adopted or adjudicated** (Wilson, HK, Manton, exact-Q-gen).
- **The T3 selection is family-level**, among the *named* candidate family
  {Wilson, HK / wrapped-Gaussian, Manton, exact-Q-gen}. A hostile *unnamed*
  positive convolution-semigroup member is **not** generically excluded.
- **The parent relocation note is unaudited; its caveat is inherited.** All
  action-lane campaign citations are **review-pending** (see Dependencies).
- **Nothing here edits axioms, policy, primitives, or registries; this note sets
  no audit status.** The independent audit lane owns all statuses.

## Purpose

The parent relocation note (2026-06-08) converted action-selection from a foreclosed
no-go into a *well-posed open physical question* on the physical-lattice baseline.
This note **decomposes** that question into (a) exact, floats-free arithmetic facts
that hold outright, plus (b) a single named non-axiom premise, **C-add**, carrying
all remaining dynamics weight; it then **maps** — without taking — the candidate
homes for C-add and flags the residual for the owner. It is a bridge-decomposition
note, not a selection result.

## Supplied Surface (landed text, quoted) `[checks 1-4]`

From `docs/MINIMAL_AXIOMS_2026-06-29.md`:

- Objects: *"A state is a configuration of records."*
- Readout additivity (the axiom-supplied half of C-add): *"For any finite
  collection of pairwise-disjoint records, scalar readout `I` is additive, with
  `I(empty)=0`."*
- The dynamics disclaimer (why C-add's kernel half is **not** supplied), from the
  "Relation To Dynamics And Kinetic Branch Selection" section — Admissibility
  *"does not choose a Hamiltonian or transfer operator, supply transition
  probabilities or weights, select a scalar or nonzero kinetic branch, assert a
  Dirac-square carrier, define a time metric, or provide a record-production
  process."*
- Law shape: *"A law privileges no states. Its domain is a supplied condition, and
  at every state where the condition holds it gives exactly one answer."*

The runner guards each sentence (whitespace-normalized) against drift.

## T1 — the composition premise C-add, named and grounded (NOT derived) `[checks 5-8]`

**Definition (note-level).** *C-add:* for the supplied one-step record-growth
process on a class-weight surface, two successive admissible steps compose by
**disjoint union of the new records**, and the two-step class-weight kernel is the
**convolution** of the one-step kernels.

*"A state is a configuration of records"* supplies the objects, and the Record
additivity sentence makes the **readout** additive over the disjoint union — this
half holds outright (check 05). That the two-step **kernel is the convolution** is
process content: the memo's dynamics section states Admissibility does not
*"provide a record-production process"*, so the convolution clause is not an axiom
consequence.

**C-add has independent content (exact toy).** On `Z_3` with one-step kernel
`p = (1/2, 1/4, 1/4)`: *independent* composition gives two-step kernel
`p * p = (3/8, 5/16, 5/16)` (check 06); a *correlated* process (second increment
equals the first) has **identical one-step marginals for both steps** (check 07)
and identical readout additivity, yet two-step kernel `(1/2, 1/4, 1/4) ≠ p * p`
(check 08). Readout additivity plus marginals do **not** force convolution — the
convolution clause is genuine, dynamics-shaped, extra content. **C-add is named and
flagged; it is not adopted here.**

## T2 — under C-add, the semigroup CLASS is selected (and only the class) `[checks 9-12]`

Under C-add the one-step kernel embeds in a convolution semigroup on the class
group; on the Fourier side this is exactly multiplicativity
`c_n(t+s) = c_n(t) c_n(s)`. For the wrapped-Gaussian family `c_n(t) = q^(n^2)` the
runner checks this exactly in rationals: multiplicativity with `q_t=1/2`,
`q_s=1/3`, `q_{t+s}=1/6` for all `n` in `Z_5` (check 09); doubling
`c_n(2t)=c_n(t)^2` under `q → q^2` (check 10); and family closure
`q^(n^2)·r^(n^2)=(qr)^(n^2)` (check 11).

But C-add selects the **class, not a member**. A rational vector
`w=(1, 1/2, 1/2, 1/2, 1/2)` violates the `n^2`-law (`w_2 = 1/2 ≠ w_1^4 = 1/16`)
while a genuine member obeys it exactly (check 12): the finite jump witness lives in
the convolution-closed class but off the continuous `q^(n^2)` curve. Among the three
*named* actions only HK's class weight is a convolution semigroup — the
**review-pending** block04 (#4819) `U(1)`-character discriminator plus block09
(#4824) class-only refinement; **Wilson/Manton exclusion is stated as those
results, not re-derived here.**

## T3 — within the class, positivity + locality select the wrapped Gaussian among all NAMED candidates `[checks 13-20]`

All legs are exact in `Q[sqrt(5)]` (Fraction pairs `a + b·sqrt(5)`), with
`cos(2π/5) = (sqrt(5)-1)/4`, `cos(4π/5) = -(sqrt(5)+1)/4`. Extension sanity:
`cos(2π/5)` satisfies `4c^2+2c-1=0` (check 13); `2cos(2π/5)+2cos(4π/5) = -1`
(check 14); `sum_{n=0}^{4} cos(2πn/5) = 0` (check 15).

**(i) The exact quadratic generator is not positivity-preserving (Metzler
violation).** With `L_{0,d} = -(1/5) · sum_n n^2 · cos(2π·n·d/5)` over balanced
labels `n ∈ {-2,-1,0,1,2}`: `L_{0,1} = 1/2 + (3/10)sqrt(5) > 0` (check 16) but
`L_{0,2} = (5 - 3·sqrt(5))/10 < 0` **strictly** (check 17). A generator gives an
entrywise-nonnegative semigroup iff it is Metzler (off-diagonals `≥ 0`); strict
negativity at `j=2` breaks that, so `exp(tL)` develops a negative entry for some
`t>0` — block14 (#4829)/block13 (#4828), recomputed independently, review-pending.

**(ii) Wrapped-Gaussian positivity (certified corrections).** With
`K_t(j) = sum_{m ∈ Z} q^((j+5m)^2)` truncated at `|m| ≤ M=3` under an **exact
geometric tail bound**, every term is positive and the `m=0` term `q^(j^2)` alone
certifies `K_t(j) ≥ S_M(j) > 0` for all `j ∈ Z_5`, for `q = 1/2` (check 18) and
`q = 1/3` (check 19); the wrapping terms are the certified non-quadratic corrections
(block13 pattern), the tail bound a faithful proxy for the infinite kernel.

**Locality leg.** The single-step locality deficit at `N=5` is
`4 sin^2(π/5) = 4·(5 - sqrt(5))/8 = (5 - sqrt(5))/2 ≠ 0` (check 20) — block10's
(#4825) single-step exclusion of the exact `Q-gen`, recomputed. Full-step `Z_N`
matching then needs signed weights (block10's trichotomy: extended steps /
small-step limit in tension with the physical-`a` baseline / no record-composition
bridge), review-pending.

**Honest family boundary.** The selection is **within the named candidate family**
{Wilson, HK / wrapped-Gaussian, Manton, exact-Q-gen}: a hostile *unnamed* positive
convolution-semigroup member is **not** generically excluded — this narrows the
named field, it does not prove global uniqueness.

## T4 — the bridge residual is one dynamics-shaped premise; governance hand-off (MORNING LIST) `[checks 21-23]`

The action-selection question now reduces to **C-add plus the exact facts above**,
with everything dynamics-shaped concentrated in C-add. Its candidate homes are
**recorded without adoption**, for the owner:

1. **A narrow record-composition primitive** — a registered framework primitive on
   the owner surface, if the convolution clause is to be admitted as structure.
2. **The banked Dynamics-axiom proposal (PR #4843, docs-only, review-pending)** —
   whose law + realized-branch content would *supply* C-add; provenance only.
3. **Remain a named conditional premise** — carry C-add as "if C-add, then ...".

Choosing among (1)–(3) is an **owner decision**, not a worker or audit call. This
note maps the three homes, takes none, and flags them for the owner's **morning**
review.

## T5 — action-wall end-state (flagged, not closed) `[checks 21-23]`

Under C-add + positivity + the locality trichotomy, the selected action among all
**named** candidates is HK / the wrapped Gaussian. The relocation note's
*"well-posed open physical question"* thereby acquires an exact shape:

> `{C-add}` → convolution-semigroup **class** → positivity (Metzler) + locality →
> **wrapped Gaussian** (among named candidates).

**No wall is closed.** The negative no-go is not retired; the relocation note's
unaudited caveat is inherited; every campaign citation is review-pending; and the
sole remaining lever, C-add, is **not adopted**. The end-state is a sharpened
conditional flagged for governance — nothing is adjudicated.

## Consequence (governance map)

The practical output is the map, not a verdict: the whole action-lane campaign now
hangs on **one** premise with **three** candidate homes (T4), while every other
moving part is an axiom-supplied or exact recomputed fact. Placed on the **morning**
list as an **owner decision** — the worker records and does not decide.

## Does NOT

- Does **not** derive, adopt, or register C-add; does not claim the axioms supply a
  record-production process or a two-step convolution kernel.
- Does **not** select or adjudicate any action or claim uniqueness beyond the named
  family; does **not** close, retire, or contradict any no-go — **no wall is closed**.
- Does **not** re-derive the block04/09/10/13/14 results — it cites them as
  review-pending and recomputes only the isolated exact instances stated.
- Does **not** edit axioms, policy, primitives, or registries, and sets **no** audit
  status.

## Dependencies

- Supplied surface: `docs/MINIMAL_AXIOMS_2026-06-29.md` (Record additivity; state
  definition; dynamics-section disclaimer; law sentence).
- Parent (unaudited, caveat inherited):
  `docs/ACTION_FORM_NO_GO_EQUIVALENCE_PREMISE_CONTINUUM_REMOVAL_SCOPED_RELOCATION_NOTE_2026-06-08.md`.
- Campaign context (all **review-pending**, cited by number, not read here):
  #4819 (block04), #4824 (block09), #4825 (block10), #4828 (block13),
  #4829 (block14), and the docs-only banked proposal PR #4843 (no status).

## No-Promotion Statement

This note promotes nothing. C-add is a named, unadopted, dynamics-shaped premise;
the selection is family-level among named candidates; the parent's caveat is
inherited; all campaign citations are review-pending; and the audit lane alone sets
status. The residual is handed to the owner as a **morning**-list **owner
decision**.

---

### Summary

- Action-selection decomposes into exact arithmetic facts **plus one** dynamics-
  shaped premise, **C-add** (record-composition → kernel convolution).
- C-add's readout half is axiom-supplied; its convolution half is **not** — an exact
  `Z_3` toy shows readout additivity + marginals do not force convolution.
- Under C-add the convolution-semigroup **class** is selected (exact `q^(n^2)`
  multiplicativity), but only the class (jump witness violates the `n^2`-law).
- Exact `Q[sqrt(5)]` facts — Metzler `L_{0,2}<0`, wrapped positivity, nonzero deficit
  `(5-sqrt5)/2` — pick the wrapped Gaussian **among named candidates only**.
- C-add has three candidate homes; the choice is an **owner decision** on the
  **morning** list. **No wall is closed**; nothing adopted; citations review-pending.
