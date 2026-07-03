# Time's Axis Is the History Index: the Record-Monotone Stack Direction

**Date:** 2026-07-03
**Type:** bounded_theorem (T1-T3) + bounded_support (T4-T5)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome; audit verdict and effective status are set only by
the independent audit lane. No status is claimed, moved, or promoted here.
**Runner:** [`scripts/frontier_time_axis_is_history_index_2026_07_03.py`](../scripts/frontier_time_axis_is_history_index_2026_07_03.py)
**Runner output:** [`outputs/frontier_time_axis_is_history_index_2026_07_03.txt`](../outputs/frontier_time_axis_is_history_index_2026_07_03.txt)
(`TOTAL: PASS=27 FAIL=0`; exact arithmetic — int/tuple/set/dict only, no floats,
no fitted or observed inputs, deterministic, nonzero exit on any FAIL).

## Firewall (read first)

- **Conditional on PR #4874.** Record-nesting (T2a) depends on the permanence
  clause `records are permanent`, in flight as PR #4874 (owner-approved, not
  landed); the current axiom file states only that the locked possibility `is
  invariant under repeated readout`. Every nesting claim below is conditional on
  #4874 landing and is flagged in the runner.
- **The representation bridge is OPEN; this note does not close B-AXIS.** The
  open item this note creates is the *representation-faithfulness bridge*: that
  the operator-layer stack consumed by the transfer/anomaly constructions is
  built from a realized history with transfer direction = history index. Not
  proved here.
- **Rate / unit / clock content untouched.** No time metric, clock rate, blocked
  step, or spacing is derived; B-AXIS.1a/1b stay as supplied, walled by the
  count-not-rate firewalls (unaudited post-reset).
- **Realized-sector conditioning.** The marking theorem covers event-bearing
  histories only; the static history is a declared degeneracy.
- **Nothing adopted; audit lane owns statuses.** No axiom, primitive, fit, or
  observation is introduced; the realized-history definition (a sequence) is a
  flagged note-level import.

## Purpose

Answer *which of the four stack directions is time* at the **record layer**, not
the operator layer: for event-bearing realized histories the history index is
the unique stack direction whose slices sit on the same site set and whose
record content nests at every step. Time's direction is read off record content
alone. This reconciles — not contradicts — the single-clock note's exchange
certificate, which shows the *operator* layer cannot see the axis.

## Supplied surface (quoted)

### Record axiom, PRE-restoration wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`)

> "When present, a record locks exactly one local possibility from the subset
> available at that site under Admissibility; the locked possibility is
> invariant under repeated readout."

> "Only records are readable. A readout value is determined by record content
> alone."

> "A state is a configuration of records."

That file lists, as content **outside** the axioms, "arrow, record-production
dynamics, physical persistence dynamics, time metric, and local observability of
records." A time metric and an arrow are not axiom content; this note supplies
neither.

### Supervisor-supplied context (quoted as supervisor-supplied)

- **PR #4874 (in flight, owner-approved):** the Record clause becomes "records
  are permanent." Permanence-dependent claims are grounded conditionally on it.
- **Sibling PR #4873 (review-pending, branch-only):** derives the
  record-inclusion event-ordering from permanence plus "A state is a
  configuration of records"; the realized history is a note-level definition ("a
  sequence of states") — an import, flagged; non-triviality is contingent
  realized data per owner ruling (condition on the realized sector).
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
derivation; the operator-layer lattice-QFT constructions live on such stacks.
The runner exact-checks stack construction with no phantom cells [01], slice
extraction [02], full round-trip `reconstruct(S) == (h_0,...,h_T)` [03], and
that the 4th-axis coordinate set is exactly `{0..T}` [04]. No physics claim is
made here.

## T2 — Record nesting marks the index direction [checks 05-15]

Bounded theorem, conditional on PR #4874 and the realized sector.

- **(a) Along the index direction**, slices sit on the **same site set**
  (identification native, [05]); permanence gives nesting `rec(h_t) ⊆
  rec(h_{t+1})` for all `t` [06], strict at least once for the event-bearing
  witness [07]. Carrying records as `(site, value)` pairs, nesting also enforces
  value-invariance: a value-flip history is rejected [08].
- **(b) Along any spatial direction**, slices live on **disjoint site sets**
  [09]; the raw record sets are disjoint, so containment is undefined without a
  translation identification [10]. Under that identification, nesting fails — the
  runner exhibits an event-bearing history whose spatial-slice record sets are
  pairwise incomparable in every spatial axis `x1, x2, x3` [11-13] while
  index-nesting holds at every stage.
- **(c) Degeneracy stated honestly.** For the static (event-free) history every
  stack direction is trivially monotone (all four), so the marking is not unique
  [14]. This is the realized-sector conditioning: per the owner ruling above,
  "non-triviality is contingent realized data ... condition on the realized
  sector."

**Theorem (record layer).** For event-bearing realized histories, the history
index is the unique stack direction carrying same-site identification plus
record nesting at every step [15]. Time's direction is read off record content
alone; no operator structure is consulted.

## T3 — The second-clock exclusion is type-level [checks 16-20]

Bounded observation. A realized history is a **sequence** (the sibling's
note-level definition, imported and flagged): one index. A second independent
record-layer clock would be a **2D grid** of configurations with two independent
nesting directions — a different **type** of object, not a history. The runner
builds one, shows independent nesting along `i` [16] and `j` [17], both
non-degenerate [18], and that two off-diagonal cells are incomparable, so the
record-inclusion order is not total and the grid does not embed as a single
sequence with one record-monotone direction [19]; if one direction is degenerate
the grid collapses to a single chain — one clock remains [20]. So at the record
layer single-clock is definitional-plus-realized-sector, not a premise.

**Honesty.** This does **not** retire the operator-layer B-AXIS.3: as quoted, "A
two-clock comparator exists mathematically ... excluded only by (B-AXIS.3) — the
premise excludes something realizable, so it is non-vacuous and load-bearing."
T3 shows only that the record layer never needed the premise; the operator-layer
comparator exclusion is left exactly where the single-clock note left it.

## T4 — Reconciliation with the exchange-symmetry certificate + B-AXIS decomposition [checks 21-24]

Bounded support. S3' (quoted above): `W` swaps the temporal and `x_1` hop
sectors with residual `0`, and "the single-clock conclusion cannot be derived
from RP-admissibility of the action."

**Reconciliation.** The certificate is about the **bare operator array**, which
by T1 is representation scaffolding. The runner models the combinatorial analog:
nearest-neighbor adjacency on a symmetric 4-cube is exactly invariant under the
axis-swap `sigma` exchanging time and a spatial axis [21] (the residual-0 analog
— the operator layer cannot distinguish the axis), while the **record content**
on the same cube is not `sigma`-invariant [22]: nesting holds along the time
axis and fails along the swapped spatial axis, and the two coexist with no
contradiction [23]. The operator layer was never going to see time, because time
is not operator geometry — it is record structure, so the certificate becomes
the **expected** statement (not re-derived here; quoted).

**B-AXIS decomposition** (covered, none dropped [24]):

| B-AXIS clause | disposition at the record layer |
|---|---|
| (B-AXIS.2) axis selection | **derived** at the record layer for event-bearing histories (T2), **CONDITIONAL** on the representation-faithfulness bridge — **named OPEN**: this note does not prove the operator-layer stack must be built from a realized history with transfer direction = history index |
| (B-AXIS.3) single clock | **type-level** at the record layer (T3); operator-layer comparator exclusion **unchanged** |
| (B-AXIS.1a) internal denominator | **not touched** — supplied; walled by the count-not-rate firewalls (unaudited post-reset) |
| (B-AXIS.1b) absolute clock unit | **not touched** — supplied/open rate-class boundary |

What this retires: the "which direction is time" question **at the record
layer**. What it does not retire: B-AXIS.1 (rate class), the single-clock note's
supplied transfer data, the anomaly chain's other premises (ABJ external, P-REC,
etc.), the representation bridge.

## T5 — Consequence + complete residues [checks 25-27]

The campaign's #1 refutation failure mode is dropped residues, so the runner
enumerates the complete list and exact-checks it as a set with the expected
count [25-26] and the load-bearing flags [27]:

1. PR #4874 in-flight conditionality (permanence not landed);
2. realized-sector conditioning (event-bearing histories only);
3. the realized-history import (sequence definition, note-level, flagged);
4. the representation-faithfulness bridge — **named OPEN**, the main open item
   this note creates;
5. B-AXIS.1a/1b untouched (rate class);
6. operator-layer B-AXIS.3 comparator exclusion untouched;
7. the single-clock note's own premise stack and unaudited-post-reset status;
8. sibling PR #4873 review-pending;
9. no rate / metric / clock content anywhere in this note;
10. nothing adopted (no axiom, primitive, fit, or observation);
11. the audit lane owns all statuses.

## Consequence

Conditional on #4874 and the realized sector, the record layer answers the axis
question by itself: the history index is the unique record-monotone, same-site
stack direction for event-bearing histories. The operator-layer exchange
certificate is exactly what one should expect — axis-blind scaffolding, with the
axis living in the record content stacked onto it.

## What this note does NOT do

- Does not close B-AXIS: the representation-faithfulness bridge is left OPEN.
- Does not touch B-AXIS.1 (rate / spacing / clock unit), the single-clock note's
  supplied transfer data, or the operator-layer B-AXIS.3 comparator exclusion.
- Does not derive an arrow, time metric, record-production, or persistence
  dynamics; does not re-derive the S3' certificate (it quotes it).
- Introduces no axiom, primitive, fitted parameter, or observed value.

## Dependencies

- Record axiom PRE-restoration wording — `docs/MINIMAL_AXIOMS_2026-06-29.md`
  (quoted).
- B-AXIS premise + S3' certificate — single-clock codimension-1 evolution note,
  2026-05-03 (quoted; not re-derived).
- Permanence clause — PR #4874 (in flight); record-inclusion event-ordering and
  "history = a sequence" — sibling PR #4873 (review-pending), imported/flagged.
- Owner ruling: non-triviality is contingent realized data (condition on the
  realized sector).

## No-Promotion

Source-note proposal. It claims no status and predicts no audit outcome. Nothing
is promoted to axiom or primitive. The independent audit lane is the only
authority for effective status; the count-not-rate firewalls and the
single-clock note's status are cited as unaudited post-reset.

## Summary

- Record layer: time's direction is the history index — the unique same-site,
  record-nesting stack direction for event-bearing histories (T2, checks 05-15).
- The stack is representation scaffolding (T1); a second record-layer clock is a
  2D grid, a different type — single-clock is definitional there (T3, 16-20).
- S3' is reconciled, not contradicted: operator geometry is axis-blind; the axis
  is record structure (T4, checks 21-24).
- Conditional on PR #4874; representation-faithfulness bridge is OPEN; B-AXIS.1
  and operator-layer B-AXIS.3 untouched; all residues enumerated (T5, 25-27).
- Runner `TOTAL: PASS=27 FAIL=0`; nothing adopted; the audit lane owns statuses.
