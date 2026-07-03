# Time's Axis Is the History Index: the Record-Monotone Stack Direction

**Date:** 2026-07-03
**Type:** bounded_theorem (T1-T2) + bounded observation (T3) + bounded_support (T4-T5)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome; audit verdict and effective status are set only by
the independent audit lane. No status is claimed, moved, or promoted here.
**Runner:** [`scripts/frontier_time_axis_is_history_index_2026_07_03.py`](../scripts/frontier_time_axis_is_history_index_2026_07_03.py)
**Runner output:** [`outputs/frontier_time_axis_is_history_index_2026_07_03.txt`](../outputs/frontier_time_axis_is_history_index_2026_07_03.txt)
(`TOTAL: PASS=36 FAIL=0`; exact arithmetic — int/tuple/set/frozenset/dict only,
no floats, no fitted or observed inputs, deterministic, nonzero exit on any FAIL).

## Firewall (read first)

- **Permanence is LANDED (commit `50f0db6187`).** Record-nesting (T2) depends on
  the permanence clause `records are permanent`, which the review loop LANDED on
  main as commit `50f0db6187` (drafted as PR #4874, review-loop-closed — not in
  flight, not conditional). This worktree branched off older main, so its axiom
  copy still states only that the locked possibility `is invariant under repeated
  readout`; the landed form is authoritative and the runner's Record-clause guard
  is TRANSITIONAL, passing on either wording (T4 guard [30]). Every nesting claim
  below is grounded on the landed permanence sentence.
- **The theorem is quantifier-scoped, not universal.** The index direction nests
  for **every** realized history (universal, T2(i)); spatial nesting **fails for
  some** event-bearing history along **each** spatial axis (existential, T2(ii));
  per-history uniqueness of the index as the record-monotone direction holds
  **only outside** two named degeneracy classes (T2(iii)). A universally phrased
  "index is the unique record-monotone direction for every event-bearing
  history" is FALSE and is not claimed: event-bearing but spatially symmetric
  histories nest along a spatial axis too.
- **The single spatial-comparability criterion is a named CONVENTION.** Spatial
  directions are compared under one fixed rule — translation-identified
  comparability with empty-slice comparability included (`emptyset` is comparable
  to every slice). All spatial claims below use this one criterion; the note does
  not switch to a same-site-only criterion anywhere.
- **The representation bridge is OPEN; this note does not close B-AXIS.** The
  open item this note creates is the *representation-faithfulness bridge*: that
  the operator-layer stack consumed by the transfer/anomaly constructions is
  built from a realized history with transfer direction = history index, **and**
  that the periodic operator block `(Z/L_τ Z) × (Z/L_s Z)^3` (cyclic fourth
  coordinate) is the compactification of that linearly ordered history index
  `{0..T}`. Both legs — realized-history origin and periodic compactification —
  are named OPEN. Not proved here.
- **Rate / unit / clock content untouched.** No time metric, clock rate, blocked
  step, or spacing is derived; B-AXIS.1a/1b stay as supplied, walled by the
  count-not-rate firewalls (unaudited post-reset).
- **Realized-sector conditioning.** The marking theorem covers event-bearing
  histories only; the static (event-free) history is a declared degeneracy
  (class D0).
- **Nothing adopted; audit lane owns statuses.** No axiom, primitive, fit, or
  observation is introduced; the realized-history definition (a sequence) and the
  event-ordering by strict record-inclusion are flagged note-level imports.

## Purpose

Answer *which of the four stack directions is time* at the **record layer**, not
the operator layer. The honest answer is quantifier-scoped: the history index is
the direction that nests for every history, and for a spatially *generic*
event-bearing history it is the *unique* record-monotone stack direction — time's
direction is then read off record content alone. Where the record content is
spatially symmetric, the record layer cannot single the axis out either; this
does not contradict the single-clock note's exchange certificate, it *resonates*
with it.

## Supplied surface (quoted)

### Record axiom, PRE-restoration wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`)

> "When present, a record locks exactly one local possibility from the subset
> available at that site under Admissibility; the locked possibility is
> invariant under repeated readout."

> "Only records are readable. A readout value is determined by record content
> alone."

> "A state is a configuration of records."

On current main the review loop LANDED the permanence restoration (commit
`50f0db6187`, drafted as PR #4874, review-loop-closed): the locking clause above
now ends "records are permanent." That landed sentence is the authoritative
permanence grounding for this note; the pre-restoration wording quoted above is
this worktree's older copy, honored only by the transitional Record-clause guard
[30].

That file lists, as content **outside** the axioms, "arrow, record-production
dynamics, physical persistence dynamics, time metric, and local observability of
records." A time metric and an arrow are not axiom content; this note supplies
neither.

### Supervisor-supplied context (quoted as supervisor-supplied)

- **PR #4874 (LANDED as commit `50f0db6187`, review-loop-closed):** the Record
  clause now ends "records are permanent." Permanence-dependent claims are
  grounded on this landed sentence, not conditionally.
- **Sibling PR #4882 (recut of closed #4873; review-pending, branch-only):** derives the
  record-inclusion event-ordering from permanence plus "A state is a
  configuration of records"; the realized history is a note-level definition ("a
  sequence of states") and an event is a strict record-inclusion step — both
  imports, flagged; non-triviality is contingent realized data per owner ruling
  (condition on the realized sector).
- **Operator-layer non-vacuity:** S3' exhibits a mathematically realizable
  two-clock comparator, so B-AXIS.3 is non-vacuous at the operator layer.

### B-AXIS premise (quoted from the single-clock note, 2026-05-03)

> "**(B-AXIS)** — **declared premise of this bounded theorem** (not derived, not
> an axiom):
> - (B-AXIS.1) one supplied blocked time step `2a_τ` (= N2), now split by
>   (S-N2-SPLIT): the internal denominator `2a_tau` for the supplied `T_hat^2`
>   transfer is source-supported, while the absolute physical clock unit/time
>   metric represented by `a_tau` remains a supplied/open clock-rate boundary;
> - (B-AXIS.2) one declared evolution axis carrying one RP/transfer
>   construction, namely the `(T̂², 2a_τ)` supply of (R-RP2)/(R-SC2) (= N4);
> - (B-AXIS.3) no independent commuting transfer factor is admitted as a second
>   physical clock (= N5)."

The single-clock note also fixes the operator block it lives on:

> "The staggered Dirac + Wilson surface `Λ = (Z/L_τ Z) × (Z/L_s Z)^3` enters only
> through the retained_bounded RP/SC supplier rows".

Its fourth (temporal) coordinate is therefore **cyclic** (`Z/L_τ Z`), whereas the
realized-history index of the stack below is a **linear** finite order `{0..T}`.
Closing the representation bridge requires the compactification `{0..T} →
Z/L_τ Z`, so the bridge carries a periodic-compactification leg (T4, residue 4).

### S3' exchange-symmetry certificate (quoted from the single-clock note)

> "`W M_KS W^T = M_KS ,   W := P_{τ↔1} ∘ diag( (-1)^{x_τ x_1} )`" and
> "`W M_τ-hop W^T = M_1-hop ,   W M_1-hop W^T = M_τ-hop`"

> "(Runner block [C-EX]: residuals are exactly `0`; the plain permutation
> without the sign field fails by a nonzero margin, so the identity is
> non-trivial.) Consequently the staggered phase structure does **not**
> distinguish the temporal axis: any reflection/transfer construction about the
> `τ` axis conjugates by the unitary `W` into the identical construction about
> the `x_1` axis ..."

> "Therefore the single-clock conclusion cannot be derived from RP-admissibility
> of the action; it holds conditional on (B-AXIS) ... A two-clock comparator
> exists mathematically (two commuting tensor-factor transfers with a
> 2-dimensional generator span; runner block [C-2CLK]) and is excluded only by
> (B-AXIS.3) — the premise excludes something realizable, so it is non-vacuous
> and load-bearing."

## T1 — The stacked representation (definition-level; no physics claim) [checks 01-04]

Given a realized history `(h_0, ..., h_T)` of configurations of `Z^3` (finite
windows in the runner), the STACK is the 4D array `S` on
`(window of Z^3) × {0..T}` with `S[x, t] = h_t at x`. By construction the 4th
direction **is** the history index. This is a representation definition, not a
derivation. The operator-layer lattice-QFT constructions of the single-clock note
are built on 4D arrays **of this general shape** — a spatial `Z^3` product with
one distinguished fourth coordinate — but whether the specific operator block is
built from a realized history with transfer direction = history index is exactly
the OPEN representation bridge, not asserted here. The runner exact-checks stack
construction with no phantom cells [01], slice extraction [02], full round-trip
`reconstruct(S) == (h_0,...,h_T)` [03], and that the 4th-axis coordinate set is
exactly `{0..T}` [04]. No physics claim is made here.

## T2 — Record nesting marks the index direction [checks 05-21]

Bounded theorem, grounded on the landed permanence clause (commit `50f0db6187`)
and conditional on the realized sector.

**Convention (translation-identified comparability, one criterion).** The index
direction needs no identification: its slices sit natively on one shared `Z^3`
site set, so `rec(h_t)` and `rec(h_{t+1})` are compared directly [05]. A spatial
direction has slices on **disjoint** site sets [05, 09]; its two opposite slices
are compared only after the natural translation identification — drop the sliced
coordinate, index by the remaining two spatial coordinates and the history index
[10] — and, by convention, an empty slice is comparable to every slice
(`emptyset ⊆ anything`). Every spatial claim below uses this **one** criterion.

- **(a) Same-site along the index direction.** Index slices share one `Z^3` site
  set (identity identification, native); the opposite spatial slices along an
  axis occupy disjoint site supports that partition that set [05]. Permanence — landed as commit `50f0db6187` —
  gives nesting `rec(h_t) ⊆ rec(h_{t+1})` for all `t` [06], strict at least once
  for the event-bearing witness [07]. Carrying records as `(site, value)` pairs,
  nesting also enforces value-invariance: a value-flip history is rejected [08].
- **(b) Disjoint along any spatial direction.** Raw spatial-slice record sets are
  disjoint [09-10], so containment is undefined without the translation
  identification named above.

**Theorem (record layer), three quantifier-scoped parts.**

- **(i) UNIVERSAL index nesting.** For **every** realized history — event-bearing,
  degenerate, or static — the history index nests: `rec(h_t) ⊆ rec(h_{t+1})` at
  every step [11] (permanence-derived; permanence landed as commit `50f0db6187`).
  Event-bearing
  histories nest strictly at least once [07].
- **(ii) EXISTENTIAL spatial failure.** For **each** spatial axis direction there
  **exist** event-bearing histories whose translation-identified opposite slices
  are incomparable, so nesting fails along that axis. A spatially generic witness
  fails on all three spatial axes `x1, x2, x3` [12-14]; an independent second
  witness fails along `x2` while its index still nests [15].
- **(iii) PER-HISTORY uniqueness outside the degeneracy classes.** For an
  event-bearing history whose record layout is spatially generic — breaking
  translation symmetry along every spatial axis — the history index is the
  **unique** record-monotone stack direction [16]. Uniqueness **fails** on two
  named degeneracy classes:
  - **class D0 — the static (event-free) history**: every stack direction is
    trivially monotone (all four) [21], the realized-sector conditioning;
  - **class D1 — the translation-degenerate event-bearing class**: histories
    whose content is spatially symmetric enough to nest along a spatial axis.
    Four members are exhibited as CHECKS, each with its own mechanism —
    single-record (opposite slices empty) [17], uniform-burst
    (translation-identified slices EQUAL) [18], translation-invariant growth
    (slices equal at every step) [19], and face-confined (records confined to one
    face, the opposite slice empty) [20]. On each, more than one direction is
    record-monotone.

**Physics, stated honestly.** Time's direction is readable from record content
alone exactly when the content is spatially generic enough to break translation
symmetry; symmetric worlds do not wear their time on their sleeve. This resonates
with the operator layer's own exchange symmetry (S3'): where the record content
is translation-symmetric, the record layer is as axis-blind as the operator
layer, so the reconciliation with S3' gets stronger, not weaker.

## T3 — The second-clock exclusion is type-level [checks 22-27]

Bounded observation. A realized history is a **sequence** (the sibling's
note-level definition, imported and flagged): one index. A second independent
record-layer clock would be a **2D grid** of configurations with two independent
nesting directions — a different **type** of object, not a history. The runner
builds one, shows independent nesting along `i` [22] and `j` [23], both
non-degenerate [24], then completes the dichotomy on the grid's record-inclusion
order:

- **horn A — order not total.** Two off-diagonal cells are incomparable, so the
  record-inclusion order is not total and the grid does not embed as a single
  sequence with one record-monotone direction [25]; and if one direction is
  degenerate the grid collapses to a single chain — one clock remains [26].
- **horn B — order total.** If instead the grid's record order is TOTAL (witness:
  cells whose record content depends only on `i + j`), it serializes into a
  single inclusion chain — again one clock remains [27].

Either horn yields no second independent record-clock. So at the record layer
single-clock is definitional-plus-realized-sector, not a premise.

**Honesty.** This does **not** retire the operator-layer B-AXIS.3: as quoted, "A
two-clock comparator exists mathematically ... excluded only by (B-AXIS.3) — the
premise excludes something realizable, so it is non-vacuous and load-bearing."
T3 shows only that the record layer never needed the premise; the operator-layer
comparator exclusion is left exactly where the single-clock note left it.

## T4 — Reconciliation with the exchange-symmetry certificate + B-AXIS decomposition [checks 28-33]

Bounded support. The reconciliation is a **statement-level** claim about a
certificate this note quotes and does not re-derive, so the runner asserts the
quoted sentences live in their source files rather than modelling a combinatorial
analog. (An earlier draft used a symmetric-cube adjacency analog; that analog
inverted S3', because on a symmetric cube the plain axis-swap already succeeds,
whereas in S3' the plain permutation FAILS and the sign field
`diag((-1)^{x_τ x_1})` carries the content. The analog is dropped.)

**Live quote guards.** The runner reads the single-clock note and asserts the S3'
certificate `W M_KS W^T = M_KS` [28] and its non-triviality — "the plain
permutation without the sign field fails by a nonzero margin" [29]. It reads the
axioms file and applies a TRANSITIONAL Record-clause guard [30]: it passes if the
file carries EITHER the landed permanence clause "records are permanent"
(authoritative — commit `50f0db6187`, drafted as PR #4874, review-loop-closed) OR
the pre-restoration locking clause "the locked possibility is invariant under
repeated readout" (accepted only for pre-restoration checkouts such as this
worktree). The landed form is authoritative; honoring the old form makes the
guard pass both on this worktree's older axiom copy and on current main after
this block merges, so no live guard keyed to the old clause fails on merge. It
reads this note and asserts its own reconciliation/resonance sentence [31].

**Reconciliation.** S3' is about the **bare operator array**: `W` swaps the
temporal and `x_1` hop sectors with residual `0`, and "the single-clock
conclusion cannot be derived from RP-admissibility of the action." The record
content is a different object. On the real translation-identified criterion a
spatially generic history singles out the index (`mono == {index}`), so the
record layer sees an axis the operator certificate cannot; a translation-symmetric
history does not (`mono ⊋ {index}`), so there the record layer is as axis-blind as
the operator layer [32]. The two coexist with no contradiction: the operator
layer was never going to see time, because time is not operator geometry — it is
record structure, and only spatially generic record structure at that.

**B-AXIS decomposition** (covered, none dropped [33]):

| B-AXIS clause | disposition at the record layer |
|---|---|
| (B-AXIS.2) axis selection | **record-layer axis structure** for spatially generic event-bearing histories (T2), **CONDITIONAL** on the representation-faithfulness bridge — **named OPEN**, covering BOTH the realized-history origin of the stack AND the periodic compactification `{0..T} → Z/L_τ Z`; this note does not prove the operator block is built from a realized history with transfer direction = history index, nor that its cyclic fourth coordinate is that history index compactified |
| (B-AXIS.3) single clock | **type-level** at the record layer (T3); operator-layer comparator exclusion **unchanged** |
| (B-AXIS.1a) internal denominator | **not touched** — supplied; walled by the count-not-rate firewalls (unaudited post-reset) |
| (B-AXIS.1b) absolute clock unit | **not touched** — supplied/open rate-class boundary |

What this addresses: the "which direction is time" question **at the record
layer**, in the quantifier-scoped form of T2. What it does not retire: B-AXIS.1
(rate class), the single-clock note's supplied transfer data, the anomaly chain's
other premises (ABJ external, P-REC, etc.), the representation bridge (both legs).

## T5 — Consequence + complete residues [checks 34-36]

The campaign's #1 refutation failure mode is dropped residues, so the runner
PARSES this note's residue list below (single source of truth) and exact-checks
its count [34] and the required load-bearing keys [35], including the four
residues added by this repair [36]:

1. permanence grounding: the permanence clause `records are permanent` is LANDED
   (commit `50f0db6187`; drafted as PR #4874, review-loop-closed), and the
   runner's Record-clause guard is transitional (accepts the landed form or, for
   pre-restoration checkouts, the old locking clause);
2. realized-sector conditioning (event-bearing histories only; static is D0);
3. the realized-history import (sequence definition, note-level, flagged);
4. the representation-faithfulness bridge — **named OPEN** — covering BOTH the
   realized-history origin of the stack AND the periodic compactification
   `{0..T} → Z/L_τ Z` of the operator block's cyclic fourth coordinate;
5. B-AXIS.1a/1b untouched (rate class);
6. operator-layer B-AXIS.3 comparator exclusion untouched;
7. the single-clock note's own premise stack and unaudited-post-reset status;
8. sibling PR #4882 (recut of closed #4873) review-pending;
9. no rate / metric / clock content anywhere in this note;
10. nothing adopted (no axiom, primitive, fit, or observation);
11. the audit lane owns all statuses;
12. the translation-identification convention — a named, load-bearing choice;
    spatial comparability is defined only relative to it, and empty-slice
    comparability is part of the convention;
13. witness-class / finite-window scoping — every witness is a finite `Z^3`
    window and a finite history; the theorem is stated on that class, not a
    thermodynamic or infinite-lattice limit;
14. four-axis-direction scoping — only the four stack axis-directions are
    considered; diagonal or composite directions are excluded by framing;
15. the event-definition import — an event is a strict record-inclusion step,
    from review-pending PR #4882 (recut of closed #4873).

## Consequence

Grounded on the landed permanence clause (commit `50f0db6187`) and conditional on
the realized sector **and** the OPEN representation-faithfulness bridge (both legs — realized-history origin and the
periodic compactification `{0..T} → Z/L_τ Z`), the record layer answers the axis
question in quantifier-scoped form: the history index nests for every history and,
for spatially generic event-bearing histories, is the unique record-monotone,
same-site stack direction. The operator-layer exchange certificate is exactly what
one should expect — axis-blind scaffolding, with the axis living in the spatially
generic record content stacked onto it; symmetric content leaves both layers
axis-blind.

## What this note does NOT do

- Does not close B-AXIS: the representation-faithfulness bridge is left OPEN, in
  both its realized-history-origin and periodic-compactification legs.
- Does not claim a universal per-history uniqueness: event-bearing but spatially
  symmetric histories (class D1) nest along a spatial axis too.
- Does not touch B-AXIS.1 (rate / spacing / clock unit), the single-clock note's
  supplied transfer data, or the operator-layer B-AXIS.3 comparator exclusion.
- Does not derive an arrow, time metric, record-production, or persistence
  dynamics; does not re-derive the S3' certificate (it quotes it).
- Introduces no axiom, primitive, fitted parameter, or observed value.

## Dependencies

- Record axiom — `docs/MINIMAL_AXIOMS_2026-06-29.md` (quoted). The landed
  permanence clause `records are permanent` (commit `50f0db6187`) is
  authoritative; this worktree's copy still shows the pre-restoration wording, so
  the runner's Record-clause guard is transitional (passes on either wording).
- B-AXIS premise + S3' certificate + the operator block `Λ = (Z/L_τ Z) ×
  (Z/L_s Z)^3` — single-clock codimension-1 evolution note, 2026-05-03 (quoted;
  not re-derived; the runner live-guards the certificate).
- Permanence clause — LANDED as commit `50f0db6187` (drafted as PR #4874,
  review-loop-closed); record-inclusion event-ordering, "history = a sequence",
  and "event = strict record-inclusion step" — sibling PR #4882 (recut of closed #4873; review-pending),
  imported/flagged.
- Owner ruling: non-triviality is contingent realized data (condition on the
  realized sector).

## No-Promotion

Source-note proposal. It claims no status and predicts no audit outcome. Nothing
is promoted to axiom or primitive. The independent audit lane is the only
authority for effective status; the count-not-rate firewalls and the
single-clock note's status are cited as unaudited post-reset.

## Summary

- Record layer, quantifier-scoped (T2, checks 05-21): the history index nests for
  EVERY history (universal); spatial nesting FAILS for some event-bearing history
  on EACH spatial axis (existential); the index is the UNIQUE record-monotone
  direction only OUTSIDE two degeneracy classes — D0 static and D1
  translation-degenerate (single-record, uniform-burst, translation-invariant,
  face-confined).
- Time is readable from record content alone exactly when the content is
  spatially generic; symmetric worlds do not wear their time on their sleeve.
- The stack is a representation of that general shape (T1); a second record-layer
  clock is a 2D grid, a different type, and the record-order dichotomy (total →
  single chain; not total → not a sequence) leaves one clock either way (T3,
  22-27).
- S3' is reconciled, not contradicted: operator geometry is axis-blind; the axis
  is spatially generic record structure (T4, checks 28-33; live quote guards on
  both source files).
- Permanence is LANDED (commit `50f0db6187`; drafted as PR #4874,
  review-loop-closed), so record nesting is grounded, not conditional; the
  representation-faithfulness bridge is OPEN in both the realized-history-origin
  and periodic-compactification `{0..T} → Z/L_τ Z` legs; B-AXIS.1 and
  operator-layer B-AXIS.3 untouched; all 15 residues enumerated and parsed from
  the note (T5, 34-36).
- Runner `TOTAL: PASS=36 FAIL=0`; nothing adopted; the audit lane owns statuses.
